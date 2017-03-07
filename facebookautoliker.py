import pyautogui
import time

def autoLike(max_likes):
	num_likes = 0
	while (num_likes < max_likes):
		unliked_button = pyautogui.locateOnScreen('unliked_button.png')
		if (unliked_button == None):
			pyautogui.press('pgdn')
		else:
			_, y = pyautogui.center(unliked_button)
			pyautogui.click(x=400, y=400)
			num_likes += 1
	time.sleep(1)

def alt_tab():
	time.sleep(1)
	pyautogui.click(x=460, y=750)
	time.sleep(1)
	pyautogui.hotkey('ctrl', '1')

alt_tab()
autoLike(10)