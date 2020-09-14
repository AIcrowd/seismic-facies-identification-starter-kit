# learning-to-smell-starter-kit
![AIcrowd-Logo](https://raw.githubusercontent.com/AIcrowd/AIcrowd/master/app/assets/images/misc/aicrowd-horizontal.png)

Starter kit for getting started in the [Seismic Facies Identification Challenge](https://www.aicrowd.com/challenges/seismic-facies-identification-challenge).

# Installation

```
git clone https://github.com/AIcrowd/seismic-facies-identification-starter-kit
cd seismic-facies-identification-starter-kit
pip install -r requirements.txt
```

# Data download
Download all the files from the [AIcrowd Resources page](https://www.aicrowd.com/challenges/seismic-facies-identification-challenge/dataset_files),
and put them in the `data/` folder. This should give you a folder structure similar to : 

```
data/
├── data_test.npz
├── data_train.npz
└── labels_train.npz
```


**NOTE**: If you have not accepted the challenge rules (by clicking on the `Participate` button), you will be asked to agree to the Rules of the competition at this point.

# Basic Usage

## Generate Random Predictions
```
python random_predict.py 
```

This should generate a `prediction.npz` file, which you can upload by clicking on `Create Submission` on the challenge page.

## Starter Notebooks
**Coming Soon**

# Author
S.P. Mohanty <mohanty@aicrowd.com>