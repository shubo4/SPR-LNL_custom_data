import os

string = "python train.py --num_of_workers 1 --tqdm 1 --root /kaggle/input/extracting-attributes-from-fashion-images-jan-2024/train --gpus 1 --dataset custom --config_file configs/custom.yaml --save_dir /kaggle/working "

os.system(string)
