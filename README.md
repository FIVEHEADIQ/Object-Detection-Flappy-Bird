
# Welcome to Flappy Bird Fit!

## Purpose

Flappy Bird Fit was created to help gamers get exercise while having fun playing classics like Flappy Bird.

The project uses YOLOv8's Object Detection Model (credits to DAVIDNYARKO123 @ https://github.com/DAVIDNYARKO123/yolov8-silva) and a GUI based on Pygame. Flappy Bird Fit has four difficulties, a broad soundtrack, and adjustable frame rate to fit your needs.

## Requirements
- Python 3.10+ (Windows recommended)
- Camera connected and working
- All required files present:
  - Images: background.jpg, skins in `flappy bird mans/`
  - Weights: `weights/yolov8n.pt`
  - Classes: `utils/coco.txt`
  - Music: MP3 files in project root
- CUDA installed for GPU support (optional)

## Installation
1. Install required packages:
	```bash
	pip install -r requirements.txt
	```
2. Ensure all files are in the correct folders as listed above.

## Usage
1. Run Main.py:
	```bash
	python Main.py
	```
2. Select your camera, difficulty, frame rate, and enjoy Flappy Bird Fit!
3. To change your bird skin, click the 'Skins' button in the main menu, select a skin, then click 'Back' to return.

## Troubleshooting
- If the game crashes or the bird is not visible, check that all required files are present and not corrupted.
- If the camera is not detected, ensure it is connected and working with other apps.
- Only one person should be in the camera frame for proper detection.
- For GPU support, ensure CUDA is installed and matches your PyTorch version.

## Credits
- YOLOv8 model: DAVIDNYARKO123
- Pygame GUI: Flappy Bird Fit contributors

## License
See LICENSE file for details.
