import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def upadate_figure(data):
    axes =fig.axes
    x =[i[0] for i in data]
    y =[int(i[1]) for i in data]
    axes[0].plot(x,y,'b-')# b- is the color blue
    axes[0].plot(x,y,'r*')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme()
table_content =[]
layout = [
    [sg.Table(
        headings=['Observation', 'Results'],
        values =table_content,
        expand_x= True,
        hide_vertical_scroll= True,
        key='TABLE'
    )],
    [sg.Input(key='Input1', expand_x= True), sg.Button('Submit')],
    [[sg.Canvas(key='CANVAS')]]
]

window =sg.Window('Graph App', layout, finalize = True)


#matplotlip
fig = plt.figure(figsize = (5,4))
fig.add_subplot(111).plot([],[])

figure_canvas_agg = FigureCanvasTkAgg(fig,window['CANVAS'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Submit':
        new_values = values['Input1']
        if new_values.isnumeric():# to check if the input given is numeric
            table_content.append([len(table_content)+1, float(new_values)])# the values of the observation will be incremented by 1
            window['TABLE'].update(table_content)# it is used to update the content of the table
            window['Input1'].update('')# used to clear the input after the submit button is clicked
            upadate_figure(table_content)

window.close()