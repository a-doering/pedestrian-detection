# Pedestrian Detection
Perform pedestrian detection on a video using a pretrained Faster R-CNN with ResNet-101 as backbone from the [Detectron2 Model Zoo](https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md).

## Usage
Once the installation step (below) is completed, you can run the detector using the following command in your terminal (from the pedestrian-detection directory) with the standard configuration, where the detections are displayed (--show) and also saved (--save, only works if you let it run on the whole video). The saved video is in /output_videos/your_video_name.mp4
```sh
python3 main.py /path/to/my/your_video_name.mp4 --save --show
```
If you are unsure how to run it, you can get helpful information by running this:
```sh
python3 main.py --help
```

### Configuration
To change the configuration, you can change some general parameters in `configs/main_config.yaml`, or use a different object detector from the model zoo, if you also modify/add the configurations of the model to 

## Installation
Tested on Debian 10.0 with x86_64, CUDA 11.3, python3.7.
```sh
git clone https://github.com/a-doering/pedestrian_detection.git
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Install pytorch and detectron2 with matching releases
pip install torch==1.8.0+cu101 torchvision==0.9.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.8/index.html
```

## Description
OpenCV is used to read a video file, in this case an .mp4 file, as this is convenient to display while the inference is running, as well as for saving. The detection framework was chosen to get to know the Detectron2 library by facebook research, its ease to use compared to pedestrian detectors from other repositories and has a decent performance, according to the [Detectron2 Model Zoo](https://github.com/facebookresearch/detectron2/blob/master/MODEL_ZOO.md).

## Import as package
You can import the repository as a package in a file, e.g. `test_importing.py` if the directory structure is as follows:

```sh
|
|---__init__.py
|---test_importing.py
|---pedestrian_detection/
```

Import in `test_importing.py` like:
```python
from pedestrian_detection import main
```

