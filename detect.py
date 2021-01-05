import cv2
import pytesseract
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ss():
    newScreenshot = pyautogui.screenshot(region=(1000, 950, 920, 95)) ## This takes a screenshot of a part of your screen. From x=1000 to 920 to right, from y=950 to 95 to down.
    newScreenshot.save("ss.png") ## This saves it.

list1=["group", "Group"]           ## Theese are the words that when the bot reads one of them, it sends a message.
list2=["hand", "up", "raise"]      ## Theese are the words that when the bot reads more than one of them, it sends a message.
myString=""                        ## This is where we will store our text from the screenshot.
def display():
    img = cv2.imread("ss.png")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      ## If I remember correct, this makes the image black and white which makes the function run faster.
    global myString
    myString = (pytesseract.image_to_string(img))   ## This reads the text on the image and stores in myString.

while 1:
    ss()        ## Take screenshot.
    display()   ## Take out the text.

    count=0

    for a in list1:                         
        if a in myString:                           ## If any of the words from the list is on the screen,
            open("text.txt", "w").write("1")        ## it writes "1" in the text file. This is how sexs.py and detect.py communicate.
            time.sleep(10)                          ## Wait 10 seconds.

    for a in list2:                                 ## This counts how many from the list2 are located on the screen.
        if a in myString:
            count += 1

    if count > 1:                                   ## This is the same but this sends the message if more than one words are located.
        open("text.txt", "w").write("1")
        time.sleep(10)

    time.sleep(1)
