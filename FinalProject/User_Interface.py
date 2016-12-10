from Tkinter import *
import tkMessageBox
import sys 
import os
import pandas as pd
import csv
from collections import defaultdict
from PIL import ImageTk, Image

path = os.path.split(os.path.realpath(sys.argv[0]))[0]

def getData():
	radioValue = analysis.get()
	if radioValue == "analysis_1":
		platform = parameter1.get()
		os.system("python " + path + "/Analysis1.py " + platform)
		window = Toplevel(app)
		window.title("Total Global Sales based on Platforms")
		window.config(height = '800', width = '800')
		
		resultUser1 = pd.read_csv(path + '/Result/Analysis1_User_Result.csv', sep=",", usecols = ["Platform", "Total_Global_Sales"])
		noti = Label(window, text = resultUser1)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# result1 = pd.read_csv(path + '/Result/Analysis1_Result.csv', sep=",", usecols = ["Platform", "Total_Global_Sales"])
		# noti = Label(window, text = result1)
		# noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# imgPath1 = r(path + "/Result/Image_Analysis_1.png")
		# img1 = PhotoImage(file = imgPath1)
		# panel1 = Label(window, image = img1)
		# panel1.pack()
		
	elif radioValue == "analysis_2":
		district = parameter1.get()
		os.system("python " + path + "/Analysis2.py " + district)
		window = Toplevel(app)
		window.title("Favorite Genre of Video Games based on Districts")
		window.config(height = '800', width = '800', bg = "green")

		resultUser2 = pd.read_csv(path + '/Result/Analysis2_User_Result.csv', sep=",", usecols = ["District", "Genre", "Total_District_Sales"])
		noti = Label(window, text = resultUser2)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)
		
		# result2 = pd.read_csv(path + '/Result/Analysis2_Result.csv', sep=",", usecols = ["District", "Genre", "Total_District_Sales"])
		# noti = Label(window, text = result2)
		# noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# imgPath2 = r(path + "/Result/Image_Analysis_2.png")
		# img2 = PhotoImage(file = imgPath2)
		# panel2 = Label(window, image = img2)
		# panel2.pack()

	elif radioValue == "analysis_3":
		publisher = parameter1.get()

		os.system("python " + path + "/Analysis3.py " + publisher)
		window = Toplevel(app)
		window.title("Total Global Sales based on Publishers in different years ")
		window.config(height = '800', width = '800', bg = "green")

		resultUser3 = pd.read_csv(path + '/Result/Analysis3_User_Result.csv', sep=",", usecols = ["Publisher", "Total_Global_Sales"])
		noti = Label(window, text = resultUser3)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# result3 = pd.read_csv(path + '/Result/Analysis3_Result.csv', sep=",", usecols = ["Publisher", "Total_Global_Sales"])
		# noti = Label(window, text = result3)
		# noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# imgPath3 = r(path + "/Result/Image_Analysis_3.png")
		# img3 = PhotoImage(file = imgPath3)
		# panel3 = Label(window, image = img3)
		# panel3.pack()

	elif radioValue == "analysis_4":
		platform = parameter1.get()
		genre = parameter2.get()

		os.system("python " + path + "/Analysis4.py " + platform + " " + genre)
		window = Toplevel(app)
		window.title("Total Global Sales based on Platform and Genre")
		window.config(height = '800', width = '800', bg = "green")

		resultUser4 = pd.read_csv(path + '/Result/Analysis4_User_Result.csv', sep=",", usecols = ["Platform", "Genre" ,"Total_Global_Sales"])
		noti = Label(window, text = resultUser4)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# imgPath4 = r(path + "/Result/Image_Analysis_4.png")
		# img4 = PhotoImage(file = imgPath4)
		# panel4 = Label(window, image = img4)
		# panel4.pack()

	elif radioValue == "analysis_5":
		district = parameter1.get()

		os.system("python " + path + "/Analysis4.py " + district)
		window = Toplevel(app)
		window.title("Total Global Sales based on Year and District")
		window.config(height = '800', width = '800', bg = "green")

		resultUser5 = pd.read_csv(path + '/Result/Analysis5_User_Result.csv', sep=",", usecols = ["District", "Year", "Total_District_Sales"])
		noti = Label(window, text = resultUser5)
		noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# result5 = pd.read_csv(path + '/Result/Analysis5_Result.csv', sep=",", usecols = ["Year", "District", "Total_District_Sales"])
		# noti = Label(window, text = result5)
		# noti.grid(row = 0, column = 0, sticky="nsew", padx=1, pady=1)

		# imgPath5 = r(path + "/Result/Image_Analysis_5.png")
		# img5 = PhotoImage(file = imgPath5)
		# panel5 = Label(window, image = img5)
		# panel5.pack()

app = Tk()
app.title("Video Game Global Sales Information")
app.geometry('500x500+300+300')
app.configure(background='green')

labelText = StringVar()
labelText.set("Choose Information Search Request, and Input Information")
label1 = Label(app, textvariable = labelText, height = 5)
label1.configure(background='green')
label1.pack()

analysis = StringVar()
analysis.set(None)

textA1 = StringVar()
textA1.set("Total Global Sales based on Platforms")
labelA1 = Label(app, textvariable = textA1, height = 1)
labelA1.configure(background='green')
labelA1.pack()

radio1 = Radiobutton(app, text = "(Please input Platform)", value = "analysis_1", variable = analysis)
radio1.configure(background='green')
radio1.pack()

textA2 = StringVar()
textA2.set("Favorite Genre of Video Games based on Districts")
labelA2 = Label(app, textvariable = textA2, height = 1)
labelA2.configure(background='green')
labelA2.pack()

radio2 = Radiobutton(app, text = "(Please input District)", value = "analysis_2", variable = analysis)
radio2.configure(background='green')
radio2.pack()

textA3 = StringVar()
textA3.set("Total Global Sales based on Publishers in different years")
labelA3 = Label(app, textvariable = textA3, height = 1)
labelA3.configure(background='green')
labelA3.pack()

radio3 = Radiobutton(app, text = "(Please input Publisher)", value = "analysis_3", variable = analysis)
radio3.configure(background='green')
radio3.pack()

textA4 = StringVar()
textA4.set("Total Global Sales based on Platform and Genre")
labelA4 = Label(app, textvariable = textA4, height = 1)
labelA4.configure(background='green')
labelA4.pack()

radio4 = Radiobutton(app, text = "(Please input Platform and Genre)", value = "analysis_4", variable = analysis)
radio4.configure(background='green')
radio4.pack()

textA5 = StringVar()
textA5.set("Total Global Sales based on Year and District")
labelA5 = Label(app, textvariable = textA5, height = 1)
labelA5.configure(background='green')
labelA5.pack()

radio5 = Radiobutton(app, text = "(Please Input District)", value = "analysis_5", variable = analysis)
radio5.configure(background='green')
radio5.pack()

text1 = StringVar()
text1.set("First Input: ")
label2 = Label(app, textvariable = text1, height = 2)
label2.configure(background='green')
label2.pack()

parameter1 = StringVar(None)
yourParameter1 = Entry(app, textvariable = parameter1)
yourParameter1.pack()

text2 = StringVar()
text2.set("Second Input: ")
label3 = Label(app, textvariable = text2, height = 2)
label3.configure(background='green')
label3.pack()

parameter2 = StringVar(None)
yourParameter2 = Entry(app, textvariable = parameter2)
yourParameter2.pack()

button = Button(app, text = "Get Info", width = 15, command = getData)
button.pack(padx = 15, pady = 15)

app.mainloop()
