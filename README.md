# CT2MNI152 

This repository implement the affine and deformation transformation in order to register the CT scan to the MNI152 1mm space

The input CT scan MUST be in .nii.gz file format.

- For data format converting tool, you are able to use [c3d](http://www.itksnap.org/pmwiki/pmwiki.php?n=Downloads.C3D) from ITK

- For converting DICOM to NIFTI, you are able to use [dcm2nii](http://www.cabiatl.com/mricro/mricron/dcm2nii.html)

- You can also use [ITK-SNAP](http://www.itksnap.org/pmwiki/pmwiki.php) to covert a series of DICOM scans to a single .nii.gz scan

- Please cite the following reference paper and this repository if it helps your research. 

## Dependencies

Python 2.7

## 1. You have to install [FSL](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) in your local machine. 

```
$ sudo apt-get install fsl
```
## 2. You have to install [elastix](http://elastix.isi.uu.nl/) in your local machine as well.
```
$ sudo apt-get install elastix
```
## 3. You have to install SimpleITK package in python
```
$ pip install SimpleITK
```

## You can apply the affine transformation on a given ct scan with nifti format by 
```
$ python CT2MNI152Affine.py <location_of_ct_scan>
```

## Reference paper: 

Kuijf, Hugo J., et al. "[Registration of brain CT images to an MRI template for the purpose of lesion-symptom mapping.](https://link.springer.com/content/pdf/10.1007%2F978-3-319-02126-3_12.pdf)" International Workshop on Multimodal Brain Image Analysis. Springer, Cham, 2013.

## How to cite this reposisoty

```
@misc{kao2019ct,
    author       = {Po-Yu Kao},
    title        = {{CT2MNI152: First release of the CT to MNI 152 space registration tool}},
    month        = December,
    year         = 2019,
    doi          = {10.5281/zenodo.3572912},
    version      = {1.0.0},
    publisher    = {Zenodo},
    url          = {https://doi.org/10.5281/zenodo.3572912}
    }
```

# LICENSE

MIT LICENSE

# Author

[pykao](https://github.com/pykao/), December 2017.
