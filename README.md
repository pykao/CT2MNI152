# CT2MNI152
This repository implement the affine and deformation transformation in order to register the CT scan to the MNI152 1mm sapce

The input CT scan MUST be in .nii.gz file format.

[Reference Paper](https://link.springer.com/content/pdf/10.1007%2F978-3-319-02126-3_12.pdf): 

Kuijf, Hugo J., et al. "Registration of brain CT images to an MRI template for the purpose of lesion-symptom mapping." International Workshop on Multimodal Brain Image Analysis. Springer, Cham, 2013.

1. You have to install FSL(https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) in your local machine. 

$ sudo apt-get install fsl

2. You have to install elastix(http://elastix.isi.uu.nl/) in your local machine as well.

$ sudo apt-get install elastix

3. You have to install SimpleITK package in python

$ pip install SimpleITK

You can apply the affine transformation on a given ct scan with nifti format by 

$ python CT2MNI152Affine.py <location_of_ct_scan>


For data format converting tool, you are able to use c3d from ITK through http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.C3D

For converting DICOM to NIFTI, you are able to use dcm2nii through http://www.cabiatl.com/mricro/mricron/dcm2nii.html
