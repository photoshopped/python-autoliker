import pyautogui
import time
import sys
import tkinter as tk

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.auto_like_five = tk.Button(self)
		self.auto_like_five["text"] = "Press This\nTo Auto Like Five Times"
		self.auto_like_five["command"] = self.autoLike(5)
		self.auto_like_five.pack(side="bottom")

	def autoLike(self, max_likes):
		self.alt_tab()
		num_likes = 0
		unliked_button = None
		clickx = clicky = 0
		while (num_likes < max_likes):
			start_time = time.time()
			unliked_button = pyautogui.locateOnScreen('unliked_button.png')
			elapsed_time = time.time() - start_time

			sys.stdout.write('Time to print: %s\n' % elapsed_time)
			sys.stdout.write(str(unliked_button).join(' \n'))
			sys.stdout.flush()

			time.sleep(1)
			
			if (unliked_button == None):
				pyautogui.press('pgdn')
				time.sleep(1)
			else:
				clickx, clicky = pyautogui.center(unliked_button)
				pyautogui.click(x=clickx, y=clicky)
				pyautogui.moveRel(-50, 0)
				num_likes += 1
				time.sleep(1)

	def alt_tab(self):
		pyautogui.click(420, 740)
		pyautogui.hotkey('ctrl', '1')

root = tk.Tk()
app = Application(master=root)
app.mainloop()