import os
import sys
# TODO: this is quite nasty; it would be nice to reorganise file structure later so top level folder is always in path
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
if rootDir not in sys.path:  # add parent dir to paths
    sys.path.append(rootDir)

import numpy as np
import Demos.geometry as geometry
import Test_data.data_loader as data_loader
import scipy.io
import copy
import time
from _Ax import Ax
from matplotlib import pyplot as plt
TIGRE_parameters = geometry.TIGREParameters(high_quality=False)
timestamp=time.asctime()

source_img = data_loader.load_head_phantom(number_of_voxels=TIGRE_parameters.nVoxel)
angles = np.linspace(0, 2*np.pi, 100, dtype=np.float32)

ray_voxel = Ax(source_img, TIGRE_parameters, angles, 'ray-voxel')
interpolated = Ax(source_img, TIGRE_parameters, angles, 'interpolated')
np.save('compile_test/compdata/'+timestamp,interpolated)
plt.matshow(interpolated[:,:,1])
plt.show()
