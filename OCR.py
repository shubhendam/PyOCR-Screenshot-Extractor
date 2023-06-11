import pyautogui
import time
import winsound
import cv2
import numpy as np
import requests
import io
import json
import pyperclip

#pip install Pillow --upgrade    -- use this

def capture_screenshot():

    # initial point indicator beep
    winsound.Beep(1000, 500)
    # Get the initial mouse position
    initial_pos = pyautogui.position()
    #optional
    print('starting')
    time.sleep(2)


    # final point indicator beep
    winsound.Beep(1000, 500)
    #optional
    print('ending')

    # Wait for the mouse button to be released
    while True:
        current_pos = pyautogui.position()

        # Check if the mouse button was released
        if current_pos != initial_pos:
            break

    # Get the coordinates of the selected rectangle
    left = min(initial_pos[0], current_pos[0])
    top = min(initial_pos[1], current_pos[1])
    width = abs(current_pos[0] - initial_pos[0])
    height = abs(current_pos[1] - initial_pos[1])

    # Capture the selected area as a screenshot
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    screenshot.save('screenshot.jpg')

#code has started beep
winsound.Beep(1000, 500)
time.sleep(1)
capture_screenshot()

#load image
img = cv2.imread("screenshot.jpg")

#get image height width info
#height , width , _ = img.shape


#ocr api call
url_api = "https://api.ocr.space/parse/image"

#compress the image cuz 1mb max
_, compressedimage = cv2.imencode(".jpg", img,[1, 90])  #compress to jpg, image, [1=compressJPG ,90= compression number

#incode the image
file_bytes = io.BytesIO(compressedimage)

#request api call
result = requests.post(url_api,
              files={"screenshot1.jpg": file_bytes},
              data = {"apikey" :"<YOUR_API_KEY>"})

#just result will give response 200 as print cuz  that means all good
#print(result)

#convert to json so to can extract test from dictonary
#print(result.content.decode())

result = result.content.decode()
result = json.loads(result)

#just take parsedtest only 
test_detected = result.get("ParsedResults")[0].get("ParsedText")

#copy the variable
pyperclip.copy(test_detected)

#print
print(test_detected)
winsound.Beep(1200, 300)
winsound.Beep(1200, 300)

#show image
cv2.imshow("Img", img)
#cv2.waitKey(0)
cv2.destroyAllWindows()
