
# Virtual Camera

## Description

Virtual Camera using OpenCV and PyVirtualCam (vcam.py)

`vcam.py` is a Python script that sets up a virtual camera using the `v4l2loopback` kernel module and `pyvirtualcam`. 
It captures video from your real camera, processes it using OpenCV, and then streams the processed video to a virtual camera device. 
This allows you to use the virtual camera as an input in applications like Chrome, Zoom, or any other software that supports webcam input.

---

## **Table of Contents**
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Code Structure](#code-structure)
6. [Troubleshooting](#troubleshooting)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)
9. [Contact](#contact)



---


## **Features**
 - **Real-Time Video Capture**: Captures video from your real camera.
 - **Video Processing**: Applies processing (e.g., grayscale conversion) to the video frames.
 - **Virtual Camera Output**: Streams the processed video to a virtual camera.

## **Prerequisites**
- Linux with `v4l2loopback` support
- Python 3.x
- A webcam

## **Installation**

### Step 1: Install Dependencies

 ```bash
 sudo apt update
 sudo apt install v4l2loopback-utils ffmpeg python3-opencv python3-pip
 pip install pyvirtualcam
 ```

### Step 2: Load the v4l2loopback Kernel Module

```bash
sudo modprobe v4l2loopback devices=1 video_nr=7 card_label="VirtualCamera" exclusive_caps=1
```

### Step 3: Clone this Repository

```bash
git clone git@github.com:j1cky/Virtual-Camera.git
cd Virtual-Camera
```

## **Usage**

1. **Run the Script**
   
   Execute the script to start streaming video from your real camera to the virtual camera:

   ```bash
   python3 vcam.py
   ```

2. **Use the Virtual Camera in Applications**

   Open Chrome or any other application that uses a webcam. 
   Select "VirtualCamera" as the video input source.

## **Code Structure**

- `vcam.py`: Main script for capturing and streaming video.

### Example

The script applies a simple grayscale filter to the video. You can customize the processing step in the script:

```python
# Grayscale conversion
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray_rgb = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2BGR)
```

### Stopping the Virtual Camera

To unload the virtual camera, run:

```bash
sudo rmmod v4l2loopback
```

## **Troubleshooting**

- **Error: `Could not open video device`**
  - Ensure your real camera is properly connected and not used by another application.
  - Try different camera indices (e.g., `cv2.VideoCapture(0)`, `cv2.VideoCapture(1)`).

- **No Camera Found in Chrome**
  - Restart Chrome or your system.
  - Check if the virtual camera is listed using:
    ```bash
    v4l2-ctl --list-devices
    ```

- **Lag or Frame Drop Issues**
  - Lower the frame size or FPS in the script:
    ```python
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 15)
    ```

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Acknowledgements**

- [pyvirtualcam](https://github.com/letmaik/pyvirtualcam)
- [v4l2loopback](https://github.com/umlaeute/v4l2loopback)
- OpenCV for Python

## **Contact**

Created by J1cky - Feel free to contact me!
