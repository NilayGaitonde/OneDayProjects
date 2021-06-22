from tkinter import *

def getBMI():
    print('BMI Calculating....')
    height=float(heightText.get())
    wieght=float(weightText.get())
    heightUnit=clickedHeight.get()
    weightUnit=clickedWeight.get()
    height=convertToM(height,heightUnit)
    height=round(height,2)
    wieght=convertTokg(wieght,weightUnit)
    wieght=round(wieght,2)
    BMI=wieght/(height*height)
    print(wieght)
    print(height)
    BMI=round(BMI,2)
    BMIText.insert(0,BMI)
    getCategory(BMI)

def convertToM(height,heightUnit):
    if(heightUnit=='cm'):
        return (height/100)
    elif(heightUnit=='ft'):
        return (height/3.281)
    else:
        return height

def convertTokg(weight,weightUnit):
    if(weightUnit=='pounds'):
        return (weight/2.205)
    else:
        return weight

def getCategory(BMI):
    if(BMI<18.5):
        categoryText.insert(0,'Underweight')
    elif(BMI<24.9):
        categoryText.insert(0,'Healthy')
    elif(BMI<29.9):
        categoryText.insert(0,'Overwieght')
    else:
        categoryText.insert(0,'Obese')

root=Tk()
root.title('BMI CALCULATOR')
root.geometry('300x150')

heightLabel=Label(root,text='Height:').grid(row=0,column=0)

weightLabel=Label(root,text='Weight:').grid(row=1,column=0)

heightText=Entry(root)
heightText.grid(row=0,column=1)

weightText=Entry(root)
weightText.grid(row=1,column=1)

optionsWeight=['kg','pounds']
clickedWeight=StringVar()
clickedWeight.set('kg')
dropWeight=OptionMenu(root,clickedWeight,*optionsWeight)
dropWeight.grid(row=1,column=2)

optionsHeight=['cm','m','ft']
clickedHeight=StringVar()
clickedHeight.set('cm')
dropHeight=OptionMenu(root,clickedHeight,*optionsHeight)
dropHeight.grid(row=0,column=2)

BMILabel=Label(root,text='BMI:').grid(row=3,column=0)

BMIText=Entry(root)
BMIText.grid(row=3,column=1)

categoryLabel=Label(root,text='Category:').grid(row=4,column=0)

categoryText=Entry(root)
categoryText.grid(row=4,column=1)

submitButton=Button(root,text='Submit',command=getBMI).grid(row=2,column=1)

mainloop()
