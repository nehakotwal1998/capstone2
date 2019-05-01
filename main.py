"""
importing all necessary libraries

"""
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import matplotlib.pyplot as plt

from PIL import Image, ImageTk
from tkinter import filedialog



LARGE_FONT=("Verdana",24)
MED_FONT=("Verdana",18)



class ImageGhosting(Tk):

	"""
	general image ghosting class

	"""

	def __init__(self,*args,**kwargs):

		"""
		passing arguements

		"""

		Tk.__init__(self,*args,**kwargs)
		Tk.configure(self)
		
		self.container=Frame(self)
		self.container.grid()
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
			
		self.geometry("750x480")
		self.title('IMAGE GHOSTING')
		self.show_frame(Main)
		#assigning a title


	def show_frame(self, cont):
		frame=cont(parent=self.container, controller=self)
		frame.grid(row=0,column=0,sticky="nsew")
		frame.tkraise()


class Main(Frame):

	def __init__(self, parent, controller):

		"""
		Constructor function for the Main Class
		Executed by interpreter to create an instance of this class.
		Attributes:
			self.parent
			self.controller
			
		"""

		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text="ImageGhosting", font=LARGE_FONT)

		choose_image_btn = Button(self , text='Choose your Image' , command=self.on_choose_image)
		choose_filter_btn = Button(self , text='Choose our Filters' , command=self.on_choose_filter)
		show_btn = Button(self , text='Show Image' , command=self.show_image)
		filter_btn = Button(self , text='Show Filter' , command=self.show_filter)
		haunted_btn = Button(self , text='Ghosted Image' , command=self.show_haunted_image)

		heading_label.grid(row=2, column=5, padx=120,pady=30)
		
		choose_image_btn.grid(row=5, column=5, padx=120, pady=10)
		choose_filter_btn.grid(row=6, column=5, padx=120, pady=10)
		show_btn.grid(row=7, column = 5 , padx=120 , pady = 10)
		filter_btn.grid(row=8, column=5, padx=120, pady=10)
		haunted_btn.grid(row=9, column=5, padx=120, pady=10)

	def on_choose_image(self):

		"""
		function for choosing image

		"""
		global choose_image
		choose_image = filedialog.askopenfilename()
		print(choose_image)

	def on_choose_filter(self):

		"""
		function for choosing filter

		"""
		global choose_filter
		choose_filter = filedialog.askopenfilename()
		print(choose_filter)

	def show_image(self):

		"""
		function for showing image

		"""
		image = Image.open(choose_image)
		plt.imshow(image)
		plt.show()

	def show_filter(self):

		"""
		function for showing image

		"""
		filt = Image.open(choose_filter)
		
		plt.imshow(filt)
		plt.show()

	def show_haunted_image(self):

		"""
		function for showing final image

		"""

		image = Image.open(choose_image)
		filt = Image.open(choose_filter)

		image.putalpha(7)
		filt.putalpha(30)

		ghosted_image = Image.alpha_composite(image,filt)
		ghosted_image.show()


app = ImageGhosting()
app.mainloop()








