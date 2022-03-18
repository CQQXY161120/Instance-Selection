# Instance Selection: A Bayesian Decision Theory Perspective

## Introduction:

This is the code repository to reproduce the experiments in the paper **[Instance Selection: A Bayesian Decision Theory Perspective](http://jiyeliang.net/Cms_Data/Contents/SXU_JYL/Folders/JournalPapers/~contents/20223301.pdf)**. This repository is based on [faiss](https://github.com/facebookresearch/faiss), numpy, and [Sklearn](https://scikit-learn.org/stable/).

## Prerequisite

we implement our methods by Python 3.8. The environment is as bellow:

- Anaconda 3  
- Linux operating system or Windows operating system  
- Sklearn, numpy, matplotlib  
- [faiss](https://github.com/facebookresearch/faiss)

```
Install faiss (CPU):  
conda install -c pytorch faiss-cpu  
conda install -c pytorch/label/nightly faiss-cpu  
```

```
Install faiss (CPU): 
conda install -c pytorch faiss-gpu
conda install -c pytorch/label/nightly faiss-gpu
```
## Run Demo

### Synthetic Data Set 
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/circles.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/moons.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Gaussian.png" width='30%' height='30%'/>
</p>

### Homogeneous clusters  
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/circles_hc.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/moons_hc.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Gaussian_hc.png" width='30%' height='30%'/>
</p>

### Reduced Data Set  
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/circles_reduced.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/moons_reduced.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Gaussian_reduced.png" width='30%' height='30%'/>
</p>

## Technical Details and Citations:  
You can find more details in the paper:  
[Instance Selection: A Bayesian Decision Theory Perspective](http://jiyeliang.net/Cms_Data/Contents/SXU_JYL/Folders/JournalPapers/~contents/20223301.pdf)

If you're using this repo in your research or applications, please cite using this BibTeX:

@inproceedings{chen2022IS,  
  title={Instance Selection: A Bayesian Decision Theory Perspective},  
  author={Qingqiang Chen, Fuyuan Cao, Ying Xing, Jiye Liang},  
  booktitle={AAAI},  
  year={2022}  
}
