# Invisibility Cloak using OpenCV

A real-time computer vision project that creates an **invisibility cloak effect** using Python and OpenCV. The program captures the background first, detects a dark blue cloth using HSV color segmentation, and replaces the detected cloth area with the previously captured background.

## Project Overview

This project demonstrates how computer vision can be used to create an invisibility effect with a normal webcam.

The basic idea is:

1. Capture the background before the cloak enters the camera view.
2. Detect the dark blue cloak using HSV color detection.
3. Create a mask for the cloak.
4. Replace the cloak area with the captured background.
5. Display the final result in real time.

## Technologies Used

- **Python**
- **OpenCV**
- **NumPy**
- **Webcam**

## Project Structure

```text
Invisibility-cloak-project/
│
├── invisible.py    # Main invisibility cloak program
└── README.md       # Project documentation