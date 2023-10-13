from fpdf import FPDF # for pdf generation
import PySimpleGUI # for window creation
import time
def create_window():
    PySimpleGUI.theme("BlueMono")
    clock = PySimpleGUI.Text('', key="now")
    label_1 = PySimpleGUI.Text("Enter ID:")
    input_box_1 = PySimpleGUI.InputText(tooltip="Enter ID", key="id")
    label_2 = PySimpleGUI.Text("Enter Amount:")
    input_box_2 = PySimpleGUI.InputText(tooltip="Enter amount", key="amount", default_text="0")

    add_button = PySimpleGUI.Button("Add")
    list_box = PySimpleGUI.Listbox(values='', key='transactions',
                                   enable_events=True, size=(50, 10)) # values should be transactions stored in database
    
    EndShift_button = PySimpleGUI.Button("End Shift")  # this will trigger pdf creation
    exit_button = PySimpleGUI.Button("Exit")
    Message = PySimpleGUI.Text("Shift has started !", key="message")
    

    window = PySimpleGUI.Window('Three_Musketeers.inc', layout=[[clock], [label_1, input_box_1],
                                                            [label_2, input_box_2, add_button],
                                                            [list_box]
        						  , [exit_button,EndShift_button], [Message]]
                                			, font=('Helvetica', 20))

    return window

def generate_pdf(rows,timestamp):
    pass
    
if __name__ == "__main__":
	window=create_window()
	while True:
		event,values=window.read(timeout=200)
		
		if(event == PySimpleGUI.WIN_CLOSED):
			break
		print(event)
		print(values)
	
