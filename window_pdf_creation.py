from fpdf import FPDF
import PySimpleGUI
from database import get_transactions_db
import time
def create_window():
    PySimpleGUI.theme("BlueMono")
    clock = PySimpleGUI.Text('', key="now")
    label_1 = PySimpleGUI.Text("Enter ID:")
    input_box_1 = PySimpleGUI.InputText(tooltip="Enter ID", key="id")
    label_2 = PySimpleGUI.Text("Enter Amount:")
    input_box_2 = PySimpleGUI.InputText(tooltip="Enter amount", key="amount", default_text="0")

    add_button = PySimpleGUI.Button("Add")
    list_box = PySimpleGUI.Listbox(values=get_transactions_db("student_database.db"), key='transactions',
                                   enable_events=True, size=(50, 10))
    
    EndShift_button = PySimpleGUI.Button("End Shift")
    exit_button = PySimpleGUI.Button("Exit")
    Message = PySimpleGUI.Text("Shift has started !", key="message")

    window = PySimpleGUI.Window('Three_Musketeers.inc', layout=[[clock], [label_1, input_box_1],
                                                            [label_2, input_box_2, add_button],
                                                            [list_box]
        , [exit_button, EndShift_button], [Message]]
                                , font=('Helvetica', 20))

    return window

def generate_pdf(rows,timestamp):
    pdf = FPDF(orientation="P", unit="mm", format="A4")

    pdf.add_page()

    # TITLE ROW
    pdf.set_font(family="Times", size=8, style="B")
    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(148, 255, 255)  # 94FFFF(teal bluish)
    pdf.cell(w=50, h=10, txt=f"{timestamp}", border=1)
    pdf.ln(10)

    revenue=0
    for item in rows:
        pdf.cell(w=60, h=5, txt=f"{item}", border=0, ln=1)
        revenue=revenue+int(item[2])
    pdf.cell(w=60, h=10, txt=f"Total revenue earned from add-ons = {revenue}", border=1, ln=2)
    pdf.output(f"Reports/{timestamp}.pdf")
    
if __name__ == "__main__":
	window=create_window()
	while True:
		event,values=window.read(timeout=200)
		window["now"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
		if(event == PySimpleGUI.WIN_CLOSED):
			break
		print(event)
		print(values)
	
