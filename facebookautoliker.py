import pyautogui
import time
import sys
import tkinter as tk

class Application(tk.Frame):

	def __init__(self, master=None):
		super().__init__(master)
		self.pack()

		self.create_fixed_like_buttons()
		self.boundary_frame = tk.Frame(self, width=480, height=20)
		self.boundary_frame.pack()
		self.create_status_bar()
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
		self.auto_like_ten = tk.Button(self.fixed_button_frame, fg='orange')
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

	def create_status_bar(self):
		self.status_bar_frame = tk.Frame(self, width=480, height=50)
		self.status_bar_frame.pack()

		self.location_found_label = tk.Label(self.status_bar_frame, text="Placeholder")
		self.location_found_label.pack()
		
		self.label_one = tk.Label(self.status_bar_frame)
		self.label_one.pack()
		self.label_one["text"] = "Time since last screen capture: {}".format("N/A")
		self.label_two = tk.Label(self.status_bar_frame)
		self.label_two.pack()
		self.label_two["text"] = "Button Coordinates: {}".format("N/A")
		self.label_three = tk.Label(self.status_bar_frame)
		self.label_three.pack()
		self.label_three["text"] = "Total Time Elapsed: {}".format("N/A")

		self.percent_label_var = tk.IntVar()
		self.percent_label_var.set(0)
		self.percent_label = tk.Label(self.status_bar_frame, text=("{}%".format(self.percent_label_var.get())))
		self.percent_label.pack(side="left")

		self.canvas = tk.Canvas(self.status_bar_frame, width=450, height=30)
		self.canvas.pack(side="left")

		self.red_rectangle = self.canvas.create_rectangle(40, 0, 440, 30, fill="gray")
		self.green_rectangle = self.canvas.create_rectangle(40, 0, 40, 30, fill="green")
		
		self.num_likes_var = tk.IntVar()
		self.max_likes_var = tk.IntVar()
		self.num_likes_var.set(0)
		self.max_likes_var.set(0)

		self.progress_label = tk.Label(self.status_bar_frame, text="{}/{} Likes".format(self.num_likes_var.get(), self.max_likes_var.get()))
		self.progress_label.pack(side="right")

	def start_status_bar(self):
		self.canvas.itemconfig(self.red_rectangle, fill="red")
		self.update()

	def end_status_bar(self):
		self.canvas.coords(self.red_rectangle, 40, 0, 0, 30)
		self.canvas.coords(self.green_rectangle, 40, 0, 440, 30)

	def clean_status_bar(self):
		#Maybe I'll do a clear button in the future
		pass

	def update_status_text(self, a, b, c):
		self.label_one["text"] = "Time since last screen capture: {} seconds ".format(a)
		self.label_two["text"] = "Button Coordinates: {}".format(b)
		self.label_three["text"] = "Total Time Elapsed: {} seconds".format(int(c))
		self.update()

	def update_status_bar(self, num_likes, max_likes):
		self.percent_label["text"] = "{}%".format(int(num_likes * 100 / max_likes))
		self.progress_label["text"] = "{}/{} Likes".format(num_likes, max_likes)


		x = int(num_likes / max_likes * 400)
		self.canvas.coords(self.red_rectangle, 40 + x, 0, 440, 30)
		self.canvas.coords(self.green_rectangle, 40, 0, 40 + x, 30)
		self.update()

	def autoLike(self, max_likes):
		self.alt_tab()
		num_likes = 0
		unliked_button = None
		clickx = clicky = 0
		total_time_tracker = time.time()
		self.start_status_bar()
		while (num_likes < max_likes):
			start_time = time.time()
			unliked_button = pyautogui.locateOnScreen('unliked_button.png')
			elapsed_time = time.time() - start_time

			self.update_status_text(elapsed_time, unliked_button, start_time - total_time_tracker)

			time.sleep(1)
			
			if (unliked_button == None):
				pyautogui.press('pgdn')
				time.sleep(1)
			else:
				clickx, clicky = pyautogui.center(unliked_button)
				pyautogui.click(x=clickx, y=clicky)
				pyautogui.moveRel(-50, 0)
				num_likes += 1
				self.update_status_bar(num_likes, max_likes)
				time.sleep(1)
		self.end_status_bar()

	def alt_tab(self):
		pyautogui.click(420, 740)
		pyautogui.hotkey('ctrl', '1')

root = tk.Tk()
root.title = "Facebook Liking Macro"
app = Application(master=root)
app.mainloop()