# Scalable Penalized Regression for Noise Detection in Learning With Noisy Labels [Custom Data]

## Overview
This is the repo for running \[[paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Wang_Scalable_Penalized_Regression_for_Noise_Detection_in_Learning_With_Noisy_CVPR_2022_paper.pdf)\] on custom dataset. This just modifies official code \[[intro](https://yikai-wang.github.io/spr/)\] to be able to implement on custom data.

## Requirements
```
python==3.7.6
numpy==1.19.1
scipy==1.6.0
scikit-learn==0.23.2
torch==1.5.1
torchvision==0.6.0a0+35d732a
```

## Data Preparing

We just need two paths one to a csv file containing image name and their labels, other is to folder containing images:
```
csv file:
│ file_name       │ label │
│Image_train_00001│   0   │
│Image_train_00004│   5   │

Path to iamges folder : /Images/Image_train_00001, Image_train_00002
```
## Change custom.yaml 
```
Arguments you shouuld change:
root : put folder where your images are stored
csv_path : put path to csv file containing image names and their labels
```
## Pretrained Model
The pretained models can be downloaded from [here](https://drive.google.com/drive/folders/1m0SDABpEcJotp1bnbYILP2KnAf2XGPwX?usp=sharing) and should be put in the folder **ckpt**.

## Training
Example training commands are listed in the folder **scripts**.
You could try the following commands as a start.

Train SPR on Custom data:
```
python scripts/custom.py
```

## Evaluation
Example evaluation commands are listed in the folder **scripts**.
You could try the following commands as a start.
