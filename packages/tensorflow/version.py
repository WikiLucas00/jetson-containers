# version.py
# Este archivo define la versión de TensorFlow y mantiene los enlaces (URLs) y nombres de los archivos wheel.
# Otros paquetes pueden importar variables desde este archivo.

from jetson_containers import L4T_VERSION, CUDA_VERSION
from packaging.version import Version

import os

# Determinar la versión de TensorFlow
if 'TENSORFLOW_VERSION' in os.environ and len(os.environ['TENSORFLOW_VERSION']) > 0:
    TENSORFLOW_VERSION = Version(os.environ['TENSORFLOW_VERSION'])
else:
    if L4T_VERSION.major >= 36:
        if CUDA_VERSION >= Version('12.4'):
            TENSORFLOW_VERSION = Version('2.18.0')
        else:
            TENSORFLOW_VERSION = Version('2.16.1')
    elif L4T_VERSION.major == 35:
        TENSORFLOW_VERSION = Version('2.12.0')
    elif L4T_VERSION.major == 34:
        TENSORFLOW_VERSION = Version('2.8.0')
    elif L4T_VERSION.major == 32:
        TENSORFLOW_VERSION = Version('2.7.0')
    else:
        TENSORFLOW_VERSION = Version('2.18.0')

# Definir los enlaces y nombres de archivos wheel para TensorFlow 1 y 2
if L4T_VERSION.major >= 36:    # JetPack 6.0
    TENSORFLOW1_URL = None
    TENSORFLOW1_WHL = None
    if TENSORFLOW_VERSION == Version('2.16.1'):
        TENSORFLOW2_URL = 'https://developer.download.nvidia.com/compute/redist/jp/v60/tensorflow/tensorflow-2.16.1+nv24.07-cp310-cp310-linux_aarch64.whl'
        TENSORFLOW2_WHL = 'tensorflow-2.16.1+nv24.07-cp310-cp310-linux_aarch64.whl'
    else:
        TENSORFLOW2_URL = None
        TENSORFLOW2_WHL = None
elif L4T_VERSION.major == 35:  # JetPack 5.1.x
    TENSORFLOW1_URL = None
    TENSORFLOW1_WHL = None
    if TENSORFLOW_VERSION == Version('2.11.0'):
        TENSORFLOW2_URL = 'https://developer.download.nvidia.com/compute/redist/jp/v512/tensorflow/tensorflow-2.12.0+nv23.06-cp38-cp38-linux_aarch64.whl'
        TENSORFLOW2_WHL = 'tensorflow-2.12.0+nv23.06-cp38-cp38-linux_aarch64.whl'
    else:
        TENSORFLOW2_URL = None
        TENSORFLOW2_WHL = None
elif L4T_VERSION.major == 34:  # JetPack 5.0 / 5.0.1
    TENSORFLOW1_URL = 'https://developer.download.nvidia.com/compute/redist/jp/v50/tensorflow/tensorflow-1.15.5+nv22.4-cp38-cp38-linux_aarch64.whl'
    TENSORFLOW1_WHL = 'tensorflow-1.15.5+nv22.4-cp38-cp38-linux_aarch64.whl'
    if TENSORFLOW_VERSION == Version('2.8.0'):
        TENSORFLOW2_URL = 'https://developer.download.nvidia.com/compute/redist/jp/v50/tensorflow/tensorflow-2.8.0+nv22.4-cp38-cp38-linux_aarch64.whl'
        TENSORFLOW2_WHL = 'tensorflow-2.8.0+nv22.4-cp38-cp38-linux_aarch64.whl'
    else:
        TENSORFLOW2_URL = None
        TENSORFLOW2_WHL = None
elif L4T_VERSION.major == 32:  # JetPack 4.x
    TENSORFLOW1_URL = 'https://developer.download.nvidia.com/compute/redist/jp/v461/tensorflow/tensorflow-1.15.5+nv22.1-cp36-cp36m-linux_aarch64.whl'
    TENSORFLOW1_WHL = 'tensorflow-1.15.5+nv22.1-cp36-cp36m-linux_aarch64.whl'
    if TENSORFLOW_VERSION == Version('2.7.0'):
        TENSORFLOW2_URL = 'https://developer.download.nvidia.com/compute/redist/jp/v461/tensorflow/tensorflow-2.7.0+nv22.1-cp36-cp36m-linux_aarch64.whl'
        TENSORFLOW2_WHL = 'tensorflow-2.7.0+nv22.1-cp36-cp36m-linux_aarch64.whl'
    else:
        TENSORFLOW2_URL = None
        TENSORFLOW2_WHL = None
else:
    TENSORFLOW1_URL = None
    TENSORFLOW1_WHL = None
    TENSORFLOW2_URL = None
    TENSORFLOW2_WHL = None