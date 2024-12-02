import numpy as np
import os
import cv2
import pyvirtualcam
import time

import subprocess
import re


def vcam_exist(vcam_name, vcam_number):      # Verify existance of virtual camera name and number

    # Execute the terminal command
    result = subprocess.run(['v4l2-ctl', '--list-devices'], stdout=subprocess.PIPE, text=True)

    # Build a pattern to search for the camera block
    pattern = rf"{vcam_name}.*?\n\s*/dev/video(\d+)"
    
    # Search using the pattern
    match = re.search(pattern, result.stdout, re.DOTALL)
    
    # If a match is found, check the number
    if match:
        found_number = int(match.group(1))
        return found_number == vcam_number
    
    return False

def create_vcam(name: str, vcam_number: int):   # Create virtual camera from terminal
    os.system('sudo modprobe v4l2loopback devices=1 video_nr='+str(vcam_number)+' card_label="'+name+'" exclusive_caps=1')
    return None

def apply_filters(frame, vcam_filter):          # Apply filters, vcam_filter =[1,2,3] to change filter
    match vcam_filter:
        case 1:
            # Example: Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Example: Apply Gaussian blur
            blurred = cv2.GaussianBlur(gray, (15, 15), 0)

            # Example: Edge detection (Canny)
            edges = cv2.Canny(blurred, 50, 150)
            return edges

def get_width_height(cap):                      # Get the real camera's width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return frame_width, frame_height

def run_vcam(cap, vcam_number, vcam_filter):    # Run the virtual camera
    """ 
    vcam_number : Virtual Camera number
    vcam_filter = [1,2,3] to choose filter
    """

    frame_width, frame_height = get_width_height(cap)


    try:
        with pyvirtualcam.Camera(width=frame_width, height=frame_height, fps=30, device='/dev/video'+str(vcam_number)) as cam:
            print('Use the command ctrl+C to interrupt the virtual camera program and delete the virtual camera.')
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to capture frame from the camera.")
                    break

                # Apply filters to the frame
                processed_frame = apply_filters(frame, vcam_filter)
                
                edges_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_GRAY2BGR)

                # Send processed frame to virtual camera
                cam.send(edges_rgb)
                
                cam.sleep_until_next_frame()

    except RuntimeError as e:
        print(f"RuntimeError: {e}")
        print("Make sure no other process is using the virtual camera device.")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt received.")
        # Unload v4l2loopback if needed
        time.sleep(1)
        os.system('sudo rmmod v4l2loopback')
        cap.release()
    finally:
        # Make sure to flush and release the virtual camera properly when the script ends
        print("Closing...")

vcam_number = 7
vcam_name = "VirtualCamera"
vcam_filter = 1


if not vcam_exist(vcam_name, vcam_number):
    create_vcam(vcam_name, vcam_number)
    print(vcam_name+' is created successfully')
else:
    print(vcam_name+' already exists')

# Open the real camera - Verify your real cam id - default 0
cap = cv2.VideoCapture(0)

# Check if the camera opened correctly
if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

run_vcam(cap, vcam_number, vcam_filter)
