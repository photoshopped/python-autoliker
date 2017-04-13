import pyautogui
import time
import sys
import tkinter as tk

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

		self.frame = tk.Frame(master, width=480, height=620)
		self.frame.pack()

		self.create_fixed_like_buttons()
		self.create_custom_like_button()

	def create_fixed_like_buttons(self):
		self.auto_like_five = tk.Button(self, fg='green')
		self.auto_like_five["text"] = "Press This\nTo Auto Like Five Times"
		self.auto_like_five["command"] = lambda: (self.autoLike(5))
		self.auto_like_five.pack(side="top")
		self.auto_like_ten = tk.Button(self, fg='yellow')
		self.auto_like_ten["text"] = "Press This\nTo Auto Like Ten Times"
		self.auto_like_ten["command"] = lambda: (self.autoLike(10))
		self.auto_like_ten.pack(side="top")
		self.auto_like_fifteen = tk.Button(self, fg='red')
		self.auto_like_fifteen["text"] = "Press This\nTo Auto Like Fifteen Times"
		self.auto_like_fifteen["command"] = lambda: (self.autoLike(15))
		self.auto_like_fifteen.pack(side="top")

	def create_custom_like_button(self):
		pass


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
root.title = "Facebook Liking Macro"
app = Application(master=root)
app.mainloop()