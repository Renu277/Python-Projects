import PySimpleGUI as sg

sg.theme("DarkAmber")

layout = [[sg.Text("My First Window")],
          [sg.InputText(key='-IN-')],
          [sg.Submit(), sg.Cancel()]        
          
]

window = sg.Window('IBDPs first window', layout)

event, values = window.read()

window.close()

sg.popup('You entered', values['-IN-'])