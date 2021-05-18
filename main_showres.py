# This code shows the result of noiseprint_blind output
#    python main_blind.py input.png output.mat
#    python main_showres.py input.png reference.png output.mat
#
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#
# Copyright (c) 2019 Image Processing Research Group of University Federico II of Naples ('GRIP-UNINA').
# All rights reserved.
# This work should only be used for nonprofit purposes.
#
# By downloading and/or using any of these files, you implicitly agree to all the
# terms of the license, as specified in the document LICENSE.txt
# (included in this package) and online at
# http://www.grip.unina.it/download/LICENSE_OPEN.txt
#

# erodeKernSize  = 15
# dilateKernSize = 11

import sys
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from sys import argv


# imgfilename = start_screen.x
# reffilename = "output-heat.png"
# outfilename = "map"
imgfilename = argv[1]
reffilename = argv[2]
outfilename = argv[3]

print(' %s' % imgfilename)
from noiseprint.utility.utilityRead import imread2f, computeMCC
from noiseprint.noiseprint_blind import genMappFloat
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.filters import minimum_filter
from sklearn import metrics


img, mode = imread2f(imgfilename, channel = 3)
gt = imread2f(reffilename, channel = 1)[0]>0.5
print('size : ', img.shape)
assert(img.shape[0]==gt.shape[0])
assert(img.shape[1]==gt.shape[1])

# gt1 = minimum_filter(gt, erodeKernSize)
# gt0 = np.logical_not(maximum_filter(gt, dilateKernSize))
# gtV = np.logical_or(gt0, gt1)
    
if outfilename[-4:] == '.mat':
    import scipy.io as sio
    dat = sio.loadmat(outfilename)
else:
    dat = np.load(outfilename)

time = dat['time'].flatten()
qf   = dat['QF'].flatten()

print('time : %g' % time)
print('qf   : %g' % qf)

valid   = dat['valid']
range0  = dat['range0'].flatten()
range1  = dat['range1'].flatten()
imgsize = dat['imgsize'].flatten()
mapp    = genMappFloat(dat['map'], valid, range0,range1, imgsize)

plt.figure(figsize=(3,3))
grid = gridspec.GridSpec(1,1, wspace=0.1, hspace=0.1,)

# plt.subplot(grid[0,0])
# plt.imshow(gt, clim=[0,1], cmap='gray')
# plt.title('Ground truth')
plt.subplot(grid[0,0])
plt.imshow(mapp, clim=[np.nanmin(mapp),np.nanmax(mapp)], cmap='jet')
plt.title('Heatmap')
plt.savefig("heatmap.png")


