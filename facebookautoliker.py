import pyautogui
import time

def autoLike(max_likes):
	num_likes = 0
	while (num_likes < max_likes):
		unliked_button = pyautogui.locateOnScreen('unliked_button.png')
		print(unliked_button)
		if (unliked_button == None):
			pyautogui.press('pgdn')
		else:
			clickx, clicky = pyautogui.center(unliked_button)
			if (clickx>200) and (clickx<600):
				pyautogui.click(x=clickx, y=clicky)
				num_likes += 1
	print(unliked_button)
	print(clickx, clicky)
	time.sleep(1)

def alt_tab():
	time.sleep(1)
	pyautogui.click(x=460, y=750)
	time.sleep(1)
	pyautogui.hotkey('ctrl', '1')

alt_tab()
autoLike(10)