import pyautogui
import time

time.sleep(3)
text = ""
listOfText = []
sentenceEnders = [".", "!", "?"]
sentenceEndersString = ["period", "exclamation", "question"]
indexer = 0
while True:
    time.sleep(2)
    # while text != "":
    try:
        listOfText.append(text)
        if any(ender in sentenceEnders for ender in listOfText[indexer]):
            text = text.capitalize()
        if (text != "") and (text not in sentenceEndersString):
            pyautogui.typewrite(text)
        time.sleep(2)
        if text == "period":
            pyautogui.typewrite(".")
        if text == "exclamation mark":
            pyautogui.typewrite("!")
        if text == "question mark":
            pyautogui.typewrite("?")
        indexer += 1
    except Exception as e:
        print(e)
    text = input("Enter text: ").strip()



