import tkinter as tk
import math
showString=''

def output(string):
    global showString
    showString=str(showString)+str(string)
    displayLabel['text']=showString

def calculate():
    global showString
    showString=str(eval(showString))
    displayLabel['text']=showString

def pi():
    global showString
    showString=''
    output(math.pi)

def finde():
    global showString
    showString=''
    output(math.e)

def findFact():
    global showString
    showString=math.factorial(int(showString))
    displayLabel['text']=showString

def delete():
    global showString
    showString=showString[:-1]
    displayLabel['text']=showString

def clearAll():
    global showString
    showString=''
    displayLabel['text']=showString

def findLog():
    global showString
    showString=math.log(float(showString))
    displayLabel['text']=showString

def sq(power):
    global showString
    showString=math.pow(float(showString),power)
    displayLabel['text']=showString

def sin():
    global showString
    showString=float(showString)
    showString=round(math.sin(showString),4)
    showString=str(showString)
    displayLabel['text']=showString

def cos():
    global showString
    showString=float(showString)
    showString=round(math.cos(showString),4)
    showString=str(showString)
    displayLabel['text']=showString

def tan():
    global showString
    showString=float(showString)
    showString=round(math.tan(showString),4)
    showString=str(showString)
    displayLabel['text']=showString

def cosec():
    global showString
    showString=float(showString)
    showString=round(math.sin(showString),4)
    showString=round((1/showString),4)
    showString=str(showString)
    displayLabel['text']=showString

def sec():
    global showString
    showString=float(showString)
    showString=round(math.cos(showString),4)
    showString=round(1/showString,4)
    showString=str(showString)
    displayLabel['text']=showString

def cot():
    global showString
    showString=float(showString)
    showString=round(math.tan(showString),4)
    showString=round(1/showString,4)
    showString=str(showString)
    displayLabel['text']=showString


root=tk.Tk()
root.title('Calculator')
root.minsize(width=250,height=250)

display=tk.Frame(root)
displayLabel=tk.Label(display,text=0,font='Verdana 15')
display.grid(row=0)
displayLabel.pack()

buttons=tk.Frame(root)

nineButton=tk.Button(buttons,text=9,width=4,background='DarkOrange1',command=lambda:output('9'))
nineButton.grid(row=3,column=3)

eightButton=tk.Button(buttons,text=8,width=4,background='DarkOrange1',command=lambda:output('8'))
eightButton.grid(row=3,column=2)

sevenButton=tk.Button(buttons,text=7,width=4,background='DarkOrange1',command=lambda:output('7'))
sevenButton.grid(row=3,column=1)

sixButton=tk.Button(buttons,text=6,width=4,background='DarkOrange1',command=lambda:output('6'))
sixButton.grid(row=4,column=3)

fiveButton=tk.Button(buttons,text=5,width=4,background='DarkOrange1',command=lambda:output('5'))
fiveButton.grid(row=4,column=2)

fourButton=tk.Button(buttons,text=4,width=4,background='DarkOrange1',command=lambda:output('4'))
fourButton.grid(row=4,column=1)

threeButton=tk.Button(buttons,text=3,width=4,background='DarkOrange1',command=lambda:output('3'))
threeButton.grid(row=5,column=3)

twoButton=tk.Button(buttons,text=2,width=4,background='DarkOrange1',command=lambda:output('2'))
twoButton.grid(row=5,column=2)

oneButton=tk.Button(buttons,text=1,width=4,background='DarkOrange1',command=lambda:output('1'))
oneButton.grid(row=5,column=1)

zeroButton=tk.Button(buttons,text=0,width=4,background='DarkOrange1',command=lambda:output('0'))
zeroButton.grid(row=6,column=2)

delButton=tk.Button(buttons,text='del',width=4,background='DarkOrange1',command=lambda:delete())
delButton.grid(row=6,column=3)

clearAllButton=tk.Button(buttons,text='CE',width=4,background='DarkOrange1',command=lambda:clearAll())
clearAllButton.grid(row=6,column=1)

addButton=tk.Button(buttons,text='+',width=4,background='DarkOrange1',command=lambda:output('+'))
addButton.grid(row=2,column=4)

subButton=tk.Button(buttons,text='-',width=4,background='DarkOrange1',command=lambda:output('-'))
subButton.grid(row=3,column=4)

divButton=tk.Button(buttons,text='/',width=4,background='DarkOrange1',command=lambda:output('/'))
divButton.grid(row=4,column=4)

multiplyButton=tk.Button(buttons,text='*',width=4,background='DarkOrange1',command=lambda:output('*'))
multiplyButton.grid(row=5,column=4)

remButton=tk.Button(buttons,text='%',width=4,background='DarkOrange1',command=lambda:output('%'))
remButton.grid(row=2,column=1)

calculateButton=tk.Button(buttons,text='=',width=4,background='DarkOrange1',command=lambda:calculate())
calculateButton.grid(row=6,column=4)

squareButton=tk.Button(buttons,text='x^2',width=4,background='DarkOrange1',command=lambda:sq(2))
squareButton.grid(row=2,column=3)

squareRootButton=tk.Button(buttons,text='x^1/2',width=4,background='DarkOrange1',command=lambda:sq(0.5))
squareRootButton.grid(row=2,column=2)

piButton=tk.Button(buttons,text='pi',width=4,background='DarkOrange1',command=lambda:pi())
piButton.grid(row=1,column=3)

eButton=tk.Button(buttons,text='e',width=4,background='DarkOrange1',command=lambda:finde())
eButton.grid(row=1,column=2)

factButton=tk.Button(buttons,text='n!',width=4,background='DarkOrange1',command=lambda:findFact())
factButton.grid(row=1,column=1)

logButton=tk.Button(buttons,text='ln',width=4,background='DarkOrange1',command=lambda:findLog())
logButton.grid(row=1,column=4)

sinButton=tk.Button(buttons,text='sin',width=4,background='DarkOrange1',command=sin)
sinButton.grid(row=0,column=1)

cosButton=tk.Button(buttons,text='cos',width=4,background='DarkOrange1',command=cos)
cosButton.grid(row=0,column=2)

tanButton=tk.Button(buttons,text='tan',width=4,background='DarkOrange1',command=tan)
tanButton.grid(row=0,column=3)

cosecButton=tk.Button(buttons,text='cosec',width=4,background='DarkOrange1',command=cosec)
cosecButton.grid(row=1,column=1)

secButton=tk.Button(buttons,text='sec',width=4,background='DarkOrange1',command=sec)
secButton.grid(row=1,column=2)

cotButton=tk.Button(buttons,text='cot',width=4,background='DarkOrange1',command=cot)
cotButton.grid(row=1,column=3)

powerButton=tk.Button(buttons,text='^(**)',width=4,background='DarkOrange1',command=lambda:output('**'))
powerButton.grid(row=0,column=4)

display.pack(anchor='center',pady=5)
buttons.pack()
root.mainloop()


