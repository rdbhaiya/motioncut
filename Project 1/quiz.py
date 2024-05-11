import PySimpleGUI as sg
import json

def load_questions(questions_file):
    with open(questions_file) as json_file:
        questions = json.load(json_file)
    return questions

def open_initial_window():
    initial_layout = [
        [sg.Text("Welcome to the Quiz!", size=(30, 1), font=("Helvetica", 20), justification='center')],
        [sg.Text("Instructions:", size=(30, 2), font=("Helvetica", 14), justification='center')],
        [sg.Text("1. Read each question carefully before answering.", size=(30, 1), font=("Helvetica", 12), justification='left')],
        [sg.Text("2. Type your answer in the box provided.", size=(30, 1), font=("Helvetica", 12), justification='left')],
        [sg.Text("3. Click 'Start Quiz' when you're ready to begin.", size=(30, 1), font=("Helvetica", 12), justification='left')],
        [sg.Button("Start Quiz", size=(10,1), pad=((200, 200), 10), button_color=('white', '#4CAF50'), 
                   border_width=4, font=("Helvetica", 14))]
    ]

    initial_window = sg.Window('Quiz', initial_layout, element_justification='center')

    while True:
        event, _ = initial_window.read()
        if event == sg.WINDOW_CLOSED or event == "Start Quiz":
            initial_window.close()
            open_question_window()
            break

def open_question_window():
    questions = load_questions(r'C:\Users\RUPAM DAS\Desktop\MotionCut\Project 1\questions.json')
    current_question_index = 0
    correct_answers = 0

    while current_question_index < len(questions):
        layout = [
            [sg.Text(questions[current_question_index]["question"], size=(50, 2), font=("Helvetica", 14), key='-QUESTION-')],
            [sg.Text("Options:", size=(50, 1), font=("Helvetica", 12))],
            [sg.Text(f"1. {questions[current_question_index]['option1']}", size=(50, 1), font=("Helvetica", 12), key='-OPTION1-')],
            [sg.Text(f"2. {questions[current_question_index]['option2']}", size=(50, 1), font=("Helvetica", 12), key='-OPTION2-')],
            [sg.Text(f"3. {questions[current_question_index]['option3']}", size=(50, 1), font=("Helvetica", 12), key='-OPTION3-')],
            [sg.Text(f"4. {questions[current_question_index]['option4']}", size=(50, 1), font=("Helvetica", 12), key='-OPTION4-')],
            [sg.InputText(size=(30, 1), key='-ANSWER-', enable_events=True)],
            [sg.Button('Submit', button_color=('white', '#4CAF50')), sg.Button('Exit', button_color=('white', '#4CAF50'))]
        ]

        question_window = sg.Window('Quiz', layout)

        while True:
            event, values = question_window.read()
            if event == sg.WINDOW_CLOSED or event == 'Exit':
                question_window.close()
                break
            elif event == 'Submit':
                selected_answer = values['-ANSWER-'].strip().lower()
                if not selected_answer:
                    sg.popup("Please provide an answer.")
                else:
                    correct_answer = questions[current_question_index]["correct_answer"].lower()
                    if selected_answer == correct_answer:
                        sg.popup("Correct!")
                        correct_answers += 1
                    else:
                        sg.popup(f"Incorrect!\nCorrect answer: {correct_answer}")
                    current_question_index += 1
                    question_window.close()
                    break

    accuracy = (correct_answers / len(questions)) * 100
    sg.popup(f"Quiz completed!\nYour Score: {correct_answers}/{len(questions)} ({accuracy:.2f}%)")

open_initial_window()
