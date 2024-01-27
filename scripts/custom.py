import os

string = "python train.py --num_of_workers 1 --root /kaggle/input/extracting-attributes-from-fashion-images-jan-2024/train --backbone res50 --gpus 1 --dataset custom --config_file configs/custom.yaml --save_dir . "

os.system(string)
