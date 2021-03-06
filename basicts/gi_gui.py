#This piece of code can find the Greens Function Coefficients and Inverse Function Coefficients
#for a given vector of phi and theta.
#Created by: Swarup Sahoo (swarupsahoo@utexas.edu)
from tkinter import *
#import ctypes
#def Mbox(title, text, style):
#	ctypes.windll.user32.MessageBoxW(0, text, title, style)

def tsf(phi, theta):

	def showGreens():
		ArrLen=scale.get()
		greensArr.delete('1.0', END)
		if var1.get() == 1:
			for i in range(ArrLen):
				greensArr.insert(INSERT, "G%d:%s" % (i,round(funcTypes.ImpFindGreens(i, phi, theta),4)))
				greensArr.insert(END, "\n")
		else:
			greensArr.insert(INSERT, "Only works for ARMA(2,1) for now")
			for i in range(ArrLen):
				greensArr.insert(INSERT, "G%d:%s" % (i,round(funcTypes.ExpFindGreens(i, phi, theta),4)))
				greensArr.insert(END, "\n")

	def showInverses():
		ArrLen=scale.get()
		InversesArr.delete('1.0', END)
		if var1.get() == 1:
			for i in range(ArrLen):
				InversesArr.insert(INSERT,"I%d:%s" % (i,round(funcTypes.ImpFindInverses(i, phi, theta),4)))
				InversesArr.insert(END,"\n")
		else:
			InversesArr.insert(INSERT, "Only works for ARMA(2,1) for now")
			for i in range(ArrLen):
				InversesArr.insert(INSERT,"I%d:%s" % (i,round(funcTypes.ExpFindInverses(i, phi, theta),4)))
				InversesArr.insert(END,"\n")

	n = len(phi)
	m = len(theta)

	root = Tk()

	frame = Frame(root)
	frame.pack()


	var=IntVar()
	scaleLabel=Label(root, text="# of coefs:         ")
	scaleLabel.pack(anchor=NE)
	scale = Scale(root, variable = var, from_=1, to=11, orient=HORIZONTAL)
	scale.pack(anchor=NE)

	dispframe = Frame(root)
	dispframe.pack()

	root.iconbitmap('icon.ico')
	root.title("G.I.Joe")
	root.geometry('450x410+350+70')


	var1=IntVar()
	R1 = Radiobutton(root, text="Implicit", variable=var1, value=1)
	R1.pack( anchor = NW )
	R2 = Radiobutton(root, text="Explicit", variable=var1, value=2)
	R2.pack( anchor = NW )

	greensArr = Text(dispframe,  height= 11, width=20)
	greensArr.pack(side=LEFT)

	InversesArr = Text(dispframe, height= 11, width=20)
	InversesArr.pack(side=RIGHT)

	modelInfo = Text(frame, height=1, width=len("ARMA(%d,%d)" % (len(phi), len(theta))))
	modelInfo.insert(INSERT, "ARMA(%d,%d)" % (len(phi), len(theta)))
	modelInfo.pack()

	BG = Button(frame, text ="Greens", command = showGreens)
	BG.pack(side=LEFT)
	BI = Button(frame, text ="Inverses", command = showInverses)
	BI.pack(side=RIGHT)
	QuitButton = Button(root, text="Quit", command=root.quit)
	QuitButton.pack(side=BOTTOM)

	root.mainloop()


tsf([1.5,3.0,1.7],[0.7,0.6])
