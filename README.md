# Seismic Facies Identification - Starter Kit

![Seismic-Facies-Challenge](https://i.imgur.com/8rBSM1Z.jpeg)


- 💪 &nbsp;Challenge Page: https://www.aicrowd.com/challenges/seismic-facies-identification-challenge
- 🗣️ &nbsp;Discussion Forum: https://www.aicrowd.com/challenges/seismic-facies-identification-challenge/discussion
- 🏆 &nbsp;Leaderboard: https://www.aicrowd.com/challenges/seismic-facies-identification-challenge/leaderboards

<p align="center">
 <a href="https://discord.gg/RC9d7cJ"><img src="https://img.shields.io/discord/657211973435392011?style=for-the-badge" alt="chat on Discord"></a>
</p>

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
├── data_test_1.npz
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

**NOTE** The submitted `npz` is expected to contain a `prediction` key storing a ndarray of the same shape as that of the `data_test.npz`.  Please refer [here](https://github.com/AIcrowd/seismic-facies-identification-starter-kit/blob/master/random_predict.py#L34) for an example.

## Starter Notebooks
**Coming Soon**

# Author
S.P. Mohanty <mohanty@aicrowd.com>
