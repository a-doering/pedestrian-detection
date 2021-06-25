# pedestrian-detection

## Installation
```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Install pytorch and detectron2 with matching releases
pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html
```