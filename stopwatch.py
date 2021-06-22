import tkinter
from datetime import datetime
from tkinter.constants import LEFT
counter=66600
running=False
def counter_label(label):
    def count():
        if running:
            global counter
            if counter==66600:
                display='Starting.....'
            else:
                tt=datetime.fromtimestamp(counter)
                string=tt.strftime('%H:%M:%S')
                display=string
            label['text']=display
            label.after(1000,count)
            counter+=1
    count()
def Start(label):
    global running
    running=True
    counter_label(label)
    startButton['state']='disabled'
    stopButton['state']='normal'
    resetButton['state']='normal'

def Stop():
    global running
    startButton['state']='normal'
    stopButton['state']='disable'
    resetButton['state']='normal'
    running=False

def Reset(label):
    global counter
    counter=66600

    if running==False:
        resetButton['state']='disabled'
        label['text']='WELCOME!'
    else:
        label['text']='Starting.........'

root=tkinter.Tk()
root.title('Stopwatch')
root.minsize(width=250,height=70)

label=tkinter.Label(root,text='WELCOME!',font='Verdana 30 bold')
label.pack()

f=tkinter.Frame(root)

startButton=tkinter.Button(f,text='Start',width=6,command=lambda:Start(label))
startButton.pack(side=LEFT)

stopButton=tkinter.Button(f,state='disabled',text='Stop',width=6,command=Stop)
stopButton.pack(side=LEFT)

resetButton=tkinter.Button(f,state='disabled',text='Reset',width=6,command=lambda:Reset(label))
resetButton.pack(side=LEFT)

f.pack(anchor='center',pady=5)
root.mainloop()