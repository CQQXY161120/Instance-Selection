# Instance Selection: A Bayesian Decision Theory Perspective

## Introduction:

This is the code repository to reproduce the experiments in the paper **[Instance Selection: A Bayesian Decision Theory Perspective](http://jiyeliang.net/Cms_Data/Contents/SXU_JYL/Folders/JournalPapers/~contents/20223301.pdf)**. This repository is based on [faiss](https://github.com/facebookresearch/faiss), and [Sklearn](https://scikit-learn.org/stable/).

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
