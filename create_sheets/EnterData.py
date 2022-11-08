from configparser import ConfigParser
from curses import window
from optparse import Values
import PySimpleGUI as sg
from pathlib import Path
import csv

home = str(Path.home())

sg.theme('DarkGray6')

sg.set_options(button_element_size=(12, 1),
               element_padding=(20, 0),
               auto_size_buttons=True,
               border_width=2)

col_layout = [
    [sg.Button("Save"),sg.Button("Search"),sg.Button("Exit")]
]

layout=[
    [sg.Text("")],
    [sg.Text("First Name: "), sg.Text(size=(40,1), key='OUTPUT1')],
    [sg.InputText()],
    [sg.Text("")],    
    [sg.Text("Last Name: "), sg.Text(size=(40,1), key='OUTPUT2')], 
    [sg.InputText()], 
    [sg.Text("")],
    [sg.Text("Email: "), sg.Text(size=(40,1), key='OUTPUT3')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text(size=(60,1),key='OUTPUT4')],
    [sg.Text("")],
    [sg.Text("")],
    [sg.Column(col_layout, element_justification='center', expand_x=True)],
]

window = sg.Window("Sheets App",layout, size=(500,300))

def Save_Data():
    first = values[0]
    last = values[1]
    email = values[2]

    window['OUTPUT1'].update(first)
    window['OUTPUT2'].update(last)
    window['OUTPUT3'].update(email)

    with open('test.csv', 'a', newline='') as csvfile:
        fieldnames = ['first','last','email']
        csv_writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        csv_writer.writerow({'first': first,'last': last,'email': email})

def readcsv():
    with open('test.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for line in csv_reader:
            window['OUTPUT4'].update(line)

    #        print(line['first'])

while True:
    event, values = window.read()
    
    if event == "Save":
        Save_Data()
    if event == "Search":
        readcsv()

    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
