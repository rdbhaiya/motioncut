import PySimpleGUI as sg
def count_word(input_text):
    word=input_text.split() #here the text from the user is split into words in a list 
    return(len(word))       #here simply the length of the list,give us the total words
layout = [
    [sg.Text("ENTER YOUR SENTENCE OR PARAGRAPH",font=("Helvetica",10), justification='center')],
    [sg.Multiline(size=(50,12), key='-INPUT-', autoscroll=True)],
    [sg.Button("Count", size=(10,1),button_color=('white', '#4CAF50'), 
                   border_width=4, font=("Helvetica", 10))],
    [sg.Text("",key='-WORD-',font=("Helvetica",15), justification='center')]
]

window_size = (400,320)
window = sg.Window('Word Counter', layout, size=window_size)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Count':
        counted_words=count_word(values['-INPUT-'])    
        if counted_words==0:
            sg.popup('Please enter some Text')
        else:
            window['-WORD-'].update(value=f'Number of words in the file is {counted_words}') 
window.close()
