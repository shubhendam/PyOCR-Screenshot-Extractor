# PyOCR Screenshot Extractor

## Introduction
PyOCR Screenshot Extractor is a Python script that enables you to capture selective screenshots, extract text content using OCR, and conveniently paste the extracted text using a custom keyboard shortcut.

This script allows you to define a starting position and an ending position on your screen by positioning your mouse cursor. The selected region is captured as a screenshot, which is then processed to extract text using Optical Character Recognition (OCR). The extracted text is automatically copied to your clipboard, eliminating the need for manual copying and pasting.

## Prerequisites
Before running the script, ensure that you have the following Python libraries installed:

- pyautogui
- Pillow
- cv2
- numpy
- requests
- pyperclip

You can install these libraries using pip. Open a command prompt and run the following command :

pip install -r requirements.txt


## Getting Started
To use the PyOCR Screenshot Extractor, follow these steps:

1. Convert the Python file from .py to .pyw extension to prevent the output window from appearing after executing the script.

2. Create a shortcut of the .pyw file.

3. Right-click on the shortcut and go to "Properties".

4. In the "Shortcut" tab, set a custom shortcut key combination, such as "Ctrl + Alt + O" (or any other desired combination).

![Creating-shortcut](https://github.com/shubhendam/PyOCR-Screenshot-Extractor/assets/41798998/c1a62fdd-9513-4716-900b-b1c7ecc8f9f5)


## Usage
1. Press the assigned shortcut key combination (e.g., Ctrl + Alt + O) from anywhere on your computer.

2. When you hear the first beep sound, position your mouse cursor at the desired starting point for the selective screenshot.

3. When you hear the second beep sound, move your mouse cursor to the desired ending point.

4. After the third beep sound, wait for approximately 2 to 3 seconds for the script to process the image and extract the text.

5. Open a text editor or notepad and press Ctrl + V to paste the extracted text from the clipboard.

![copying](https://github.com/shubhendam/PyOCR-Screenshot-Extractor/assets/41798998/21afeacb-8683-4670-a060-d8a8cbe38b04)



## API Key for OCR.Space
PyOCR Screenshot Extractor uses the OCR.Space API for text extraction. To use the script, you need an API key from OCR.Space. Follow these steps to obtain your API key:

1. Go to the OCR.Space website (https://ocr.space/ocrapi) and sign up for an account.

2. Once registered, go to your account dashboard and navigate to the "API Key" section.

3. Copy your API key and replace the "YOUR_API_KEY" value in the script with your actual API key.


## Acknowledgements
- [pyautogui](https://pyautogui.readthedocs.io/) - Python library for GUI automation
- [Pillow](https://pillow.readthedocs.io/) - Python imaging library
- [OCR.Space API](https://ocr.space/ocrapi) - OCR API service

Feel free to contribute, report issues, or suggest enhancements to make this project even better.
