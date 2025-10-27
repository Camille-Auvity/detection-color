# detection-color
Detects colored objects (red, green, or blue) in real-time using a webcam feed.

# Real-Time Color Detection with OpenCV

This Python script uses **OpenCV** and **NumPy** to detect objects of a specific color (red, green, or blue) in real-time using your webcam.

## 🧠 Overview

The program captures video from your webcam, converts the frames to **HSV color space**, and applies color thresholds to isolate objects of a chosen color.  
By default, the script detects **blue** objects, but you can easily modify it to detect **red** or **green** by uncommenting the corresponding code blocks.

## 🚀 Features
- Real-time video capture and color detection
- Adjustable color ranges in HSV space
- Simple to switch between red, green, and blue detection
- Displays both the original frame and the binary mask

## 🧩 Requirements

Make sure you have Python 3 installed, then install the dependencies:

```bash
pip install opencv-python numpy
```
