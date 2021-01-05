import cv2
import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ss():
    newScreenshot = pyautogui.screenshot(region=(1000, 950, 920, 95))
    newScreenshot.save("ss.png")

kelimeler=["group", "Group"]
kelimeler2=["hand", "up", "raise"]
myString=""
def display():
    img = cv2.imread("ss.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    global myString
    myString = (pytesseract.image_to_string(img))

while 1:
    ss()
    display()

    count=0

    for a in kelimeler:
        if a in myString:
            open("text.txt", "w").write("1")
            time.sleep(10)

    for a in kelimeler2:
        if a in myString:
            count += 1

    if count > 1:
        open("text.txt", "w").write("1")
        time.sleep(10)

    time.sleep(1)