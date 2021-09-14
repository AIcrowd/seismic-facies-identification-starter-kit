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
├── data_test_2.npz
├── data_train.npz
└── labels_train.npz
```


**NOTE**: If you have not accepted the challenge rules (by clicking on the `Participate` button), you will be asked to agree to the Rules of the competition at this point.

**NOTE**: For Round-2, you will have to submit predictions using `data_test_2.npz` and for Round-1 you should submit predictions using `data_test_1.npz`.

# Basic Usage

## Generate Random Predictions
```
python random_predict.py 
```

This should generate a `prediction.npz` file, which you can upload by clicking on `Create Submission` on the challenge page.

**NOTE** The submitted `npz` is expected to contain a `prediction` key storing a ndarray of the same shape as that of the `data_test.npz`.  Please refer [here](https://github.com/AIcrowd/seismic-facies-identification-starter-kit/blob/master/random_predict.py#L34) for an example.

## Compute Score locally 

Please refer to [compute_score.py](compute_score.py) for the code that is used to compute the scores on the leaderboard. If there are any optimizations you would want to suggest, or any bugs you find, please consider sending across a pull request.

## Notebooks by Community

* [Just a simple Video-Notebook - Starter Pack](www.aicrowd.com/showcase/explainer-just-a-simple-video-notebook-starter-pack)
* [Introduction and General Approach Final Pack!](www.aicrowd.com/showcase/explainer-introduction-and-general-approach-final-pack)
* [EDA in details, baseline and advanced models](discourse.aicrowd.com/t/explainer-eda-in-details-baseline-and-advanced-models/3745/1)
* [Seismic Facies Identification Starter](discourse.aicrowd.com/t/explainer-seismic-facies-identification-starter-pack/3735)
* [Detectron2 & COCO Dataset 🔥 • Web Application & Visualizations • End-to-End Baseline & Tensorflow](discourse.aicrowd.com/t/explainer-detectron2-coco-dataset-web-application-visualizations-end-to-end-baseline-tensorflow/3799/1)
* [PyTorch starter 0.857 F1-Score on public LB](discourse.aicrowd.com/t/explainer-pytorch-starter-0-857-f1-score-on-public-lb/3790)
* [Need extra features? Different input approach? Try Seismic Attributes! ](discourse.aicrowd.com/t/explainer-need-extra-features-different-input-approach-try-seismic-attributes/3766)
* [End to End solution that gives above 80% Accuracy](discourse.aicrowd.com/t/end-to-end-solution-that-gives-above-80-accuracy/3778)

# Author
S.P. Mohanty <mohanty@aicrowd.com>
