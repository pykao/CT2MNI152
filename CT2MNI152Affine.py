#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:02:52 2017

@author: pkao
"""

import os
import CTtools
from subprocess import call
import sys


#ct_scan_path = '/home/pkao/CT2MNI152/example/example.nii.gz'

ct_scan_path = sys.argv[1]

MNI_152_bone = os.path.join(os.getcwd(),'MNI152_T1_1mm_bone.nii.gz')

MNI_152 = os.path.join(os.getcwd(),'MNI152_T1_1mm.nii.gz')

nameOfAffineMatrix = ct_scan_path[:ct_scan_path.find('.nii.gz')]+'_affine.mat'

print 'The location of MNI152 bone:' , MNI_152_bone

ct_scan_wodevice = CTtools.removeCTscandevice(ct_scan_path)

ct_scan_wodevice_bone = CTtools.bone_extracted(ct_scan_wodevice)

call(['flirt', '-in', ct_scan_wodevice_bone, '-ref', MNI_152_bone, '-omat', nameOfAffineMatrix])

call(['flirt', '-in', ct_scan_wodevice, '-ref', MNI_152, '-applyxfm', '-init', nameOfAffineMatrix, '-out', ct_scan_wodevice[:ct_scan_wodevice.find('.nii.gz')]+'_MNI152.nii.gz'])
