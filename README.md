
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

### Step 1: Clone this Repository
   ```bash
   git clone git@github.com:j1cky/Virtual-Camera.git
   cd Virtual-Camera
   ```

### Step 2: Create and activate a virtual environment:

 ```bash
 python3 -m venv .venv
 source .venv/bin/activate  # For Linux/Mac
 .venv\Scripts\activate     # For Windows
 ``` 

### Step 3: Install Dependencies

**System Dependencies:**

   First, update your package list and install essential system packages:
   ```bash
   sudo apt update
   sudo apt install v4l2loopback-utils ffmpeg python3-opencv python3-pip
   ```

**Python Dependencies:**

 To install Python dependencies, ensure you are in a virtual environment (recommended), to create a virtual environment:
 ```bash
 python3 -m venv venv
 source venv/bin/activate
 ```
 then use `requirements.txt` to install dependencies :
 ```bash
 pip install -r requirements.txt
 ```

## **Usage**

**Run the Script**
   
 Execute the script to start streaming video from your real camera to the virtual camera:

 ```bash
 python3 vcam.py
 ```

**Use the Virtual Camera in Applications**

 Open Chrome or any other application that uses a webcam. 

 Select "VirtualCamera" as the video input source.

## **Code Structure**

- `vcam.py`: Main script for capturing and streaming video.


### Stopping the Virtual Camera

To stop and unload the virtual camera, run:

```bash
ctrl+C
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
