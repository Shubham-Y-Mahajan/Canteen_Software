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
            try:
                id = values['id']
                amount=int(values['amount'])
                if (amount>=0 and id!=''):
                    data=d.get_data(id)
                    if data!=0: # index error checking [for ID field] ( see d.get_data)
                        balance_left=d.update_data(filepath=filepath,data=data,amount=amount)
                        if balance_left>=0:
                            d.write_transaction_db(filepath=filepath, data=data, amount=amount)
                            updated_transactions = d.get_transactions_db(filepath=filepath)
                            window['transactions'].update(values=updated_transactions)
                            window['message'].update(value=f"{data[1]} Balance left = {balance_left}")
                            window['id'].update(value='')
                            window['amount'].update(value='0')

                        else :
                            window['message'].update(value="Insufficient Balance!")
                    else:
                        PySimpleGUI.popup("Enter a valid ID", font=20)

                else: # amount <0 or ID field left blank
                    PySimpleGUI.popup("Enter a valid ID and Amount", font=20)
            except ValueError: #amount field anyhing other than integers
               PySimpleGUI.popup("Enter a valid Amount", font=20)

        case "End Shift":
            rows=d.end_shift(filepath=filepath)
            print(rows)
            updated_transactions = d.get_transactions_db(filepath=filepath)
            window['transactions'].update(values=updated_transactions)
            timestamp=time.strftime("%b-%d-%Y_%H_%M")
            wpc.generate_pdf(rows=rows,timestamp=timestamp)
            window['message'].update(value=f"The Shift has Ended! at {timestamp}")
            window['id'].update(value='')
            window['amount'].update(value='0')


