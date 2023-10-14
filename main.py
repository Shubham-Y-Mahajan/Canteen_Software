import database as d
import window_pdf_creation as wpc
import PySimpleGUI
import time
import os


filepath="student_database.db"
window=wpc.create_window()

while True:

    event,values=window.read(timeout=200)
    window["now"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    if (event == PySimpleGUI.WIN_CLOSED):
        break

    print(event)
    print(values)
    match event:
        case "Exit":
            break;
        case "Add":
            pass
        case "End Shift":
            pass

# test commit modification





