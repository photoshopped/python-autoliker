import pyautogui
import time
import sys
import tkinter as tk

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

		self.create_fixed_like_buttons()
		self.boundary_frame = tk.Frame(self, width=480, height=320)
		self.boundary_frame.pack()
		self.create_custom_like_button()

	def create_fixed_like_buttons(self):
		self.fixed_button_frame = tk.Frame(self, width=480, height=240)
		self.fixed_button_frame.pack(side="top")

		self.fixed_button_label = tk.Label(self.fixed_button_frame, text="Quick Access Buttons")
		self.fixed_button_label.pack(side="top")

		self.auto_like_five = tk.Button(self.fixed_button_frame, fg='green')
		self.auto_like_five["text"] = "Press This\nTo Auto Like Five Times"
		self.auto_like_five["command"] = lambda: (self.autoLike(5))
		self.auto_like_five.pack(side="left")
		self.auto_like_ten = tk.Button(self.fixed_button_frame, fg='yellow')
		self.auto_like_ten["text"] = "Press This\nTo Auto Like Ten Times"
		self.auto_like_ten["command"] = lambda: (self.autoLike(10))
		self.auto_like_ten.pack(side="left")
		self.auto_like_fifteen = tk.Button(self.fixed_button_frame, fg='red')
		self.auto_like_fifteen["text"] = "Press This\nTo Auto Like Fifteen Times"
		self.auto_like_fifteen["command"] = lambda: (self.autoLike(15))
		self.auto_like_fifteen.pack(side="left")

	def create_custom_like_button(self):
		self.custom_button_frame = tk.Frame(self, width=480, height=440)
		self.custom_button_frame.pack(side="bottom")

		self.custom_button_label = tk.Label(self.custom_button_frame, text="Enter a number of likes 1-100")#next feature: likes or loves
		self.custom_button_label.pack(side="top")

		self.custom_number_of_likes_label = tk.Label(self.custom_button_frame, text="Number of Likes: ")
		self.custom_number_of_likes_entry = tk.Entry(self.custom_button_frame)
		self.custom_number_of_likes_entry.insert(0, "1")#not sure what this 0 does will need to look at documnetation later
		self.custom_number_of_likes_entry.pack(side="left")
		self.custom_number_of_likes_label.pack(side="left")
		self.custom_number_of_likes_submit = tk.Button(self.custom_button_frame, text="Go!")
		self.custom_number_of_likes_submit["command"] = lambda: (self.autoLike(int(self.custom_number_of_likes_entry.get())))
		self.custom_number_of_likes_submit.pack(side="left")


	def autoLike(self, max_likes):
		#self.alt_tab()
		num_likes = 0
		unliked_button = None
		clickx = clicky = 0
		while (num_likes < max_likes):
			start_time = time.time()
			unliked_button = pyautogui.locateOnScreen('unliked_button.png')
			elapsed_time = time.time() - start_time

			sys.stdout.write('Time to print: %s\n' % elapsed_time)
			sys.stdout.write(str(unliked_button).join(' \n'))
			sys.stdout.write('%d likes out of %d\n\n' % (num_likes, max_likes))
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