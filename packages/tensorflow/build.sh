#!/usr/bin/env bash
# TensorFlow builder for Jetson (architecture: ARM64, CUDA support)
set -ex

# Variables
TENSORFLOW_VERSION=${TENSORFLOW_BUILD_VERSION}

# Install LLVM/Clang 18
./llvm.sh 18 all

echo "Building TensorFlow for Jetson"

# Clone the TensorFlow repository
git clone --branch "v${TENSORFLOW_VERSION}" --depth=1 https://github.com/tensorflow/tensorflow.git /opt/tensorflow || \
git clone --depth=1 https://github.com/tensorflow/tensorflow.git /opt/tensorflow 

cd /opt/tensorflow

# Set up environment variables for the configure script
export PYTHON_BIN_PATH="$(which python3)"
export PYTHON_LIB_PATH="$(python3 -c 'import site; print(site.getsitepackages()[0])')"
export TF_NEED_CUDA=1
export TF_CUDA_CLANG=1
# Set Clang path for CUDA
export CLANG_CUDA_COMPILER_PATH=/usr/local/llvm/bin/clang
# Set Clang path for CPU
export CLANG_COMPILER_PATH=/usr/local/llvm/bin/clang
export HERMETIC_CUDA_VERSION=12.6.0
export HERMETIC_CUDNN_VERSION=9.3.0 
export HERMETIC_CUDA_COMPUTE_CAPABILITIES=8.7


# Build the TensorFlow pip package
bazel build //tensorflow/tools/pip_package:wheel --repo_env=WHEEL_NAME=tensorflow --config=cuda --config=cuda_wheel --copt=-Wno-gnu-offsetof-extensions

# Upload the wheels to mirror
twine upload --verbose /opt/tensorflow/bazel-bin/tensorflow/tools/pip_package/wheel_house/tensorflow*.whl || echo "failed to upload wheel to ${TWINE_REPOSITORY_URL}"

# Install them into the container
pip3 install --verbose --no-cache-dir /opt/tensorflow/bazel-bin/tensorflow/tools/pip_package/wheel_house/tensorflow*.whl

# Verify the installation
python3 -c "import tensorflow as tf; print(tf.__version__)"