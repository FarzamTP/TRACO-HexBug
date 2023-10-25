# Tracking Olympiad

### Goal

This is a project preseneted by Prof. Dr. Andreas Kist at FAU. The aim of this project is to detect the precise location of all Hexbugs in videos. We are provided with 100 videos, containing ~ 101 frame each, alognside the annotations of Hexbugs' heads' location at each frame.

### Approach

#### Pre-processing
Given data are in `mp4` format. We need to extract every single frame and save it in specific directories.

#### Step I
We are trying to detect the Hexbugs in the each frame using Yolo v5 algorithm. By doing so, we are left with cropped images containing the Hexbugs. By doing so, we got rid of void disturbing areas in the image.

#### Step II
After obtaining the cropped images, we use `Resnet50` model for feature extraction, and then we add `Dense` layers at the top of the model to perform regression. Now, we have created a model that is capable of estimating the head's coordination.

#### Post-processing
After computing the head's position, we need to reverse the process to retrieve head's original coordination in the original frame.

### How to run
1. Clone this git repository.
```bash
git clone https://github.com/FarzamTP/TRACO-HexBug.git
```
2. Enter the directory
```bash
cd TRACO-HexBug
```
3. [Pre-processing frames]
```bash
jupyter notebook frame_prepration.ipynb
```
```bash
jupyter notebook hexbug_object_detection_YOLO_torch.ipynb
```

4. [Training]
```bash
jupyter notebook hexbug_head_detection_resnet.ipynb
```

5. [Load Model]
```bash
jupyter notebook load_model.ipynb
```

### Note
To download the annotated dataset for Yolo, you need an `api_key`. Please use your `Roboflow` account to export the dataset using your key.

