# Instance Selection: A Bayesian Decision Theory Perspective

## Introduction:

This is the code repository to reproduce the experiments in the paper **[Instance Selection: A Bayesian Decision Theory Perspective](http://jiyeliang.net/Cms_Data/Contents/SXU_JYL/Folders/JournalPapers/~contents/20223301.pdf)**. This repository is based on [faiss](https://github.com/facebookresearch/faiss), numpy, and [Sklearn](https://scikit-learn.org/stable/).

## Prerequisite

We implement our methods by Python 3.8. The environment is as bellow:

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
Install faiss (GPU): 
conda install -c pytorch faiss-gpu
conda install -c pytorch/label/nightly faiss-gpu
```
## Run demo

### Synthetic Data Set 
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/circles.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/moons.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/Gaussian.png" width='30%' height='30%'/>
</p>

### Homogeneous clusters  
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/circles_hc.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/moons_hc.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/Gaussian_hc.png" width='30%' height='30%'/>
</p>

### Reduced Data Set  
<p align="center">
  <img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/circles_reduced.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/moons_reduced.png" width='30%' height='30%'/><img src="https://github.com/CQQXY161120/Instance-Selection/blob/main/Experimental%20Results/Gaussian_reduced.png" width='30%' height='30%'/>
</p>

## Technical Details and Citations:  
You can find more details in the paper:  
[Instance Selection: A Bayesian Decision Theory Perspective](http://jiyeliang.net/Cms_Data/Contents/SXU_JYL/Folders/JournalPapers/~contents/20223301.pdf)

If you're using this repo in your research or applications, please cite this BibTeX:

@inproceedings{Chen_Cao_Xing_Liang_2022, 
title={Instance Selection: A Bayesian Decision Theory Perspective}, 
volume={36}, 
url={https://ojs.aaai.org/index.php/AAAI/article/view/20578}, 
DOI={10.1609/aaai.v36i6.20578},
number={6}, 
journal={Proceedings of the AAAI Conference on Artificial Intelligence}, 
author={Chen, Qingqiang and Cao, Fuyuan and Xing, Ying and Liang, Jiye}, 
year={2022}, 
month={Jun.}, 
pages={6287-6294} 
}
