import tkinter as tk #Import the entire tkinter library
from tkinter import * #Import the entire library from tkinter
import os #Allows usage of OS commands

#Windows Form Config
window = tk.Tk() #Creates a windows form
window.title("Saving Password") #Title of the screen
window.geometry('500x100') #Define the resolution of the form
path = '' #Path of the file (Insert your file)

#Function to save your password
def savePassword(): 
    isFile = os.path.isfile(path) #Verify path, returns bool
    userPassword = txt_frame1.get() #userPassword recieves the input inserted on txt_frame1

    if isFile: #Same as if isFile == True
        userFile = open("password.txt", "a") #Opens the file
        userFile.write(f'{userPassword}\n') #Write inside the file, does not overwrite
        userFile.close() #Close the file, to avoid file corruption
    else:
        userFile = open("password.txt", "x") #Creates the file
        userFile = open("password.txt", "a") #Opens the file
        userFile.write(userPassword) #Write inside the file, does not overwrite
        userFile.close() #Close the file, to avoid file corruption

#Form customization
frame1 = Frame(window, width = 150, height = 100) #Creates a frame
frame1.grid(row = 0, column = 0, padx = 5, pady = 5)

lbl_frame1 = Label(frame1, text="Digite uma senha:") #Creates a label on frame1
lbl_frame1.pack(side = "left") #Puts the label on left side of the form

txt_frame1 = Entry(frame1, width = 40) #Creates a text field on frame1
txt_frame1.pack(side = "left") #Puts the text in side of label

btn_frame1 = Button(frame1, text = "Submit", padx= 10, command = savePassword) #Creates a button that executes the savePassword function
btn_frame1.pack(side = "right") #Puts the button in the side of text

window.mainloop() #Shows the form
