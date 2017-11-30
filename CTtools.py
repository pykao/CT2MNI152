#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 15:49:08 2017

@author: pkao
"""

import SimpleITK as sitk
import numpy as np
from skimage.filters import threshold_otsu
from skimage import measure
from scipy import ndimage

def bone_extracted(ct_img_path):
    
    print 'The CT scan you want to implement bone extraction: ', ct_img_path


    ct_img = sitk.ReadImage(ct_img_path)

    bone_mask_img = sitk.Image(ct_img.GetWidth(), ct_img.GetHeight(), ct_img.GetDepth(), sitk.sitkFloat32)

    output_ct_img = sitk.Image(ct_img.GetWidth(), ct_img.GetHeight(), ct_img.GetDepth(), sitk.sitkFloat32)

    #print 'The size of CT scan:', ct_img.GetSize()

    ct_nda = sitk.GetArrayFromImage(ct_img)

    bone_mask_nda = sitk.GetArrayFromImage(bone_mask_img)

    output_ct_nda = sitk.GetArrayFromImage(output_ct_img)

    #print 'The minimum value of CT scan: ', np.amin(ct_nda)

    #print 'The maximum value of CT scan: ', np.amax(ct_nda)

    #print 'The pixel ID type of CT scan: ', ct_img.GetPixelIDTypeAsString()

    #m = 1.0

    #b = -1024.0

    #bone_HU = 500.0

    #bone_pixel = (bone_HU-b)/m
    
    bone_pixel = 500

    for z in range(ct_nda.shape[0]):
        for x in range(ct_nda.shape[1]):
            for y in range(ct_nda.shape[2]):
                if ct_nda[z, x, y] >= bone_pixel:
                    output_ct_nda[z, x, y] = ct_nda[z, x, y]
                    bone_mask_nda[z, x, y] = 1.0;

    output_ct_image = sitk.GetImageFromArray(output_ct_nda)

    bone_mask_image = sitk.GetImageFromArray(bone_mask_nda)

    output_ct_image_name = ct_img_path[:ct_img_path.find('.nii.gz')]+'_skull.nii.gz'

    bone_mask_image_name = ct_img_path[:ct_img_path.find('.nii.gz')]+'_skullMask.nii.gz'
    
    output_ct_image.CopyInformation(ct_img)
    
    bone_mask_image.CopyInformation(ct_img)

    #print 'The name of the output skull image: ', output_ct_image_name

    #print 'The name of the output skull mask image: ', bone_mask_image_name

    sitk.WriteImage(output_ct_image, output_ct_image_name)

    #sitk.WriteImage(bone_mask_image, bone_mask_image_name)

    return output_ct_image_name
    #return output_ct_image_name, bone_mask_image_name

def getMaximum3DRegion(binary):
    
    all_labels = measure.label(binary, background = 0)
    
    props = measure.regionprops(all_labels)
    
    areas = [prop.area for prop in props]
    
    maxArea_label = 1+np.argmax(areas)
    
    max_binary = np.float32(all_labels == maxArea_label)
    
    return max_binary


   

def normalizeCTscan(ct_nda):
    
    if np.amin(ct_nda) < 0:
        ct_normalized_nda = ct_nda - np.amin(ct_nda)
        
    ct_normalized_nda = ct_normalized_nda/np.amax(ct_normalized_nda)
    
    return ct_normalized_nda


def otsuThreshoulding(ct_normalized_nda):
    
    thresh = threshold_otsu(ct_normalized_nda)
    
    binary = (ct_normalized_nda > thresh)*1
    
    return binary.astype(np.float32)
    
def get2Maximum2DRegions(max_binary):
    
    xy_two_largest_binary = np.zeros(max_binary.shape, dtype = np.float32 )
    
    largest_area = np.zeros(max_binary.shape[0])
    
    second_largest_area = np.zeros(max_binary.shape[0])
    
    for i in range(max_binary.shape[0]):
        xy_binary = max_binary[i, :, :]
        xy_labels = measure.label(xy_binary, background = 0)
        xy_props = measure.regionprops(xy_labels)
        xy_areas = [prop.area for prop in xy_props]
        #print xy_areas
        
        if xy_areas == []:
            continue
        
        elif len(xy_areas) == 1:
            largest_area[i] = xy_areas[0]
            second_largest_area[i] = 0.0
            largest_label = xy_areas.index(largest_area[i]) + 1 
            xy_two_largest_binary[i, :, :] = xy_labels == largest_label
            
        else:
            xy_areas_sorted = sorted(xy_areas)
            largest_area[i] = xy_areas_sorted[-1]
            second_largest_area[i] = xy_areas_sorted[-2]
            largest_label = xy_areas.index(largest_area[i]) + 1 
            second_largest_label = xy_areas.index(second_largest_area[i])+1
            xy_largest_binary = xy_labels == largest_label
            xy_second_largest_binary = xy_labels == second_largest_label
            xy_two_largest_binary[i, :, :] = np.float32(np.logical_or(xy_largest_binary, xy_second_largest_binary))
            
    return xy_two_largest_binary

def get1Maximum2DRegion(max_second_binary):
    
    new_binary = np.zeros(max_second_binary.shape, dtype = np.float32)
    for i in range(max_second_binary.shape[0]):
        xy_binary = max_second_binary[i,:,:]
        xy_labels = measure.label(xy_binary)
        xy_props = measure.regionprops(xy_labels)
        xy_areas = [prop.area for prop in xy_props]
        #print i, xy_areas_1
        if xy_areas == []:
            continue
        else:
            max_area_label = 1 + np.argmax(xy_areas)
            new_binary[i,:,:] = np.float32(xy_labels == max_area_label)
            
    return new_binary


def imageOpening2D(max_second_binary, structure=np.ones((15, 15))):
    
    new_max_second_binary = np.zeros(max_second_binary.shape, dtype = np.float32)
    
    for i in range(max_second_binary.shape[0]):
        
        new_max_second_binary[i,:,:] = ndimage.binary_opening(max_second_binary[i,:,:].astype(int), structure=structure).astype(np.float32)
        
    return new_max_second_binary

def removeCTscandevice(ct_img_path):

    ct_img = sitk.ReadImage(ct_img_path)
    
    ct_nda = sitk.GetArrayFromImage(ct_img)

    print 'The CT scan you want to implement CT scan device removal:', ct_img_path

    #print 'The minimum value of CT scan: ', np.amin(ct_nda)

    #print 'The maximum value of CT scan: ', np.amax(ct_nda)

    #print 'The pixel ID type of CT scan: ', ct_img.GetPixelIDTypeAsString()
    
   
    ct_normalized_nda = normalizeCTscan(ct_nda)
    
    binary = otsuThreshoulding(ct_normalized_nda)
    
    max_binary = getMaximum3DRegion(binary)
    
    xy_two_largest_binary = get2Maximum2DRegions(max_binary)
    
    max_second_binary = getMaximum3DRegion(xy_two_largest_binary)
    
    new_binary = get1Maximum2DRegion(max_second_binary)
    
    new_max_second_bindary = imageOpening2D(new_binary)
    
    new_max_binary = getMaximum3DRegion(new_max_second_bindary)
    
    woCTscan_mask_image = sitk.GetImageFromArray(new_max_binary)
    
    woCTscan_mask_image.CopyInformation(ct_img)
    
    woCTscan_mask_image_name = ct_img_path[:ct_img_path.find('.nii.gz')]+'_woCTscanMask.nii.gz'
    
    output_ct_image = sitk.GetImageFromArray(ct_nda * new_max_binary)
    
    output_ct_image.CopyInformation(ct_img)
    
    output_ct_image_name = ct_img_path[:ct_img_path.find('.nii.gz')]+'_woCTscan.nii.gz'
    
    
    #sitk.WriteImage(woCTscan_mask_image, woCTscan_mask_image_name)
    
    sitk.WriteImage(output_ct_image, output_ct_image_name)
    
    #return output_ct_image_name, woCTscan_mask_image_name

    return output_ct_image_name
