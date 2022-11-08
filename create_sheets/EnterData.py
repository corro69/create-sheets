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
    [sg.Text("Make: "), sg.Text(size=(40,1), key='OUTPUT1')],
    [sg.InputText()],
    [sg.Text("")],    
    [sg.Text("Model: "), sg.Text(size=(40,1), key='OUTPUT2')], 
    [sg.InputText()], 
    [sg.Text("")],
    [sg.Text("Serial Number: "), sg.Text(size=(40,1), key='OUTPUT3')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Asset Number: "), sg.Text(size=(40,1), key='OUTPUT4')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Assigned Location: "), sg.Text(size=(40,1), key='OUTPUT5')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Incident Number: "), sg.Text(size=(40,1), key='OUTPUT6')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Reason For Repair: "), sg.Text(size=(40,1), key='OUTPUT7')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("In Posession Of: "), sg.Text(size=(40,1), key='OUTPUT8')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Date: "), sg.Text(size=(40,1), key='OUTPUT9')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Date Received: "), sg.Text(size=(40,1), key='OUTPUT10')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Timestamp: "), sg.Text(size=(40,1), key='OUTPUT11')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("Email Address: "), sg.Text(size=(40,1), key='OUTPUT12')], 
    [sg.InputText()],
    [sg.Text("")],
    [sg.Text("")],
    [sg.Column(col_layout, element_justification='center', expand_x=True)],
]

window = sg.Window("Sheets App",layout, size=(400,800))

def Save_Data():
    make = values[0]
    model = values[1]
    serial = values[2]
    asset = values[3]
    location = values[4]
    incident = values[5]
    reason = values[6]
    posession = values[7]
    date = values[8]
    received = values[9]
    timestamp = values[10]
    email = values[11]

    window['OUTPUT1'].update(make)
    window['OUTPUT2'].update(model)
    window['OUTPUT3'].update(serial)
    window['OUTPUT4'].update(asset)
    window['OUTPUT5'].update(location)
    window['OUTPUT6'].update(incident)
    window['OUTPUT7'].update(reason)
    window['OUTPUT8'].update(posession)
    window['OUTPUT9'].update(date)
    window['OUTPUT10'].update(received)
    window['OUTPUT11'].update(timestamp)
    window['OUTPUT12'].update(email)

    with open('test.csv', 'a', newline='') as csvfile:
        fieldnames = ['Make','Model','Serial Number','Asset Number','Assigned Location','Incident Number','Reason for Repair','In Posessin Of','Date','Timestamp','Email Address']
        csv_writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        csv_writer.writerow({'Make':make,'Model':model,'Serial Number':serial,'Asset Number':asset,'Assigned Location':location,'Incident Number':incident,'Reason for Repair':reason,'In Posessin Of':posession,'Date':date,'Timestamp':timestamp,'Email Address':email})

def readcsv():
    with open('test.csv', 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for line in csv_reader:
            window['OUTPUT14'].update(line)

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
