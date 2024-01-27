import os

options = [
    ('symmetric', 0.2),
    ('symmetric', 0.4),
    ('symmetric', 0.6),
    ('asymmetric', 0.2),
    ('asymmetric', 0.3),
    ('asymmetric', 0.4)
]

for noise_type, noise_rate in options:
    string = "python train.py --backbone res50 --gpus 1 --dataset custom --config_file configs/custom.yaml --noise_type {} --noise_rate {} --save_dir {}".format(
        noise_type, noise_rate, '{}-{}'.format(noise_type, noise_rate))
    os.system(string)
