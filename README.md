# Object Detection and Tracking with Python

## Overview

This is a program that **detects objects, specifically moving objects, in front of a computer webcam**. The main features are:

- **Detects moving objects** as they appear within the camera’s video frame.
- **Records the timestamp** when an object enters and when it exits the video frame.
- Visually, when an object is present, a **green rectangle** is displayed around it in the video feed.

## Workflow

1. **Detection and Tracking**
    - When an object enters the video frame, the program recognizes it and draws a green rectangle.
    - If the object leaves, the rectangle disappears, indicating no object is detected.
    - This sequence can repeat: you appear, move away, show up again, and so on.

2. **Developed from Scratch**
    - This application will be built using **Python** from scratch.
    - You will learn key concepts such as:
        - Image processing
        - Video processing
        - Object detection and motion tracking

3. **Recording Entry and Exit Times**
    - The program keeps track of **when objects enter and leave** by recording timestamps for each event.

4. **Interactive Graph Output**
    - Pressing `q` quits the application.
    - Upon exit, a **graph** is displayed that shows the times when objects were present in the video frame.
    - The graph is interactive, meaning you can see **exact intervals** during which the object was detected.

## Use Cases

- **General Object Detection**
    - Useful for monitoring any movement in front of a webcam.

- **Animal or Person Detection**
    - Deploy the Python program to a **Raspberry Pi server** (a small, affordable server).
    - Place it in locations where you want to observe animals or people.
    - Example: Detect when an animal or person enters/leaves the view.

## Summary Table

| Feature              | Description                                                             |
|----------------------|-------------------------------------------------------------------------|
| Motion Detection     | Identifies moving objects in webcam video                               |
| Timestamp Logging    | Records entry and exit times of detected objects                        |
| Real-Time Feedback   | Draws green rectangle around detected object in video feed              |
| Graph Generation     | Displays intervals of activity on an interactive graph after quitting   |
| Versatile Usage      | Can be run on a Raspberry Pi for remote monitoring                      |

## Conclusion

This project offers a practical introduction to real-time computer vision and can be extended for a variety of surveillance and monitoring applications using Python.
