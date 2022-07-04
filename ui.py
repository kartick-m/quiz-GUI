from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz_result = None
        self.quiz = quiz_brain
        self.quiz_score=None
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.quiz_score = 0
        self.question_no = 0

        self.canvas = Canvas(width=300, height=250, background='white')
        self.question_text = self.canvas.create_text(
            150, 125,
            text="Quiz question: True or False",
            justify='center',
            fill=THEME_COLOR, width=280,
            font=('Arial', 12, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        tick_image = PhotoImage(file='./images/true.png')
        self.tick = Button(image=tick_image, highlightthickness=0, command=self.true_button_pressed)
        self.tick.grid(row=2, column=0)

        wrong_image = PhotoImage(file='./images/false.png')
        self.wrong = Button(image=wrong_image, highlightthickness=0, command=self.false_button_pressed)
        self.wrong.grid(row=2, column=1)

        self.score = Label(text=f'Score: {self.quiz_score}/{self.question_no}',
                           font=('Arial', 12, 'bold'), foreground='white', background=THEME_COLOR)
        self.score.grid(row=0, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.score.config(foreground=THEME_COLOR)
            self.canvas.itemconfig(self.question_text,
                                   text=f"Quiz Finished.\n\nYour final score was {self.quiz_score}/10.")
            # Now we will change the state of the buttons
            self.tick.config(state='disabled')
            self.wrong.config(state='disabled')

    def true_button_pressed(self):
        self.quiz_result,self.quiz_score = self.quiz.check_answer('True')
        self.score.config(text=f'Score: {self.quiz_score}/{self.quiz.question_number}')
        self.give_feedback(self.quiz_result)

    def false_button_pressed(self):
        self.quiz_result, self.quiz_score = self.quiz.check_answer('False')
        self.score.config(text=f'Score: {self.quiz_score}/{self.quiz.question_number}')
        self.give_feedback(self.quiz_result)

    def give_feedback(self, result:bool):
        if result:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, self.get_next_question)
