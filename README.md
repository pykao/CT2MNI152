# CT2MNI152
This repository implement the affine and deformation transformation in order to register the CT scan to the MNI152 1mm sapce

Reference Paper: 

Kuijf, Hugo J., et al. "Registration of brain CT images to an MRI template for the purpose of lesion-symptom mapping." International Workshop on Multimodal Brain Image Analysis. Springer, Cham, 2013.

1. You have to install FSL(https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) in your local machine. 

$ sudo apt-get install fsl

2. You have to install elastix(http://elastix.isi.uu.nl/) in your local machine as well.

$ sudo apt-get install elastix

3. You have to install SimpleITK package in python

$ pip install SimpleITK
