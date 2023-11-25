import tkinter as tk
from tkinter import messagebox
from questions import questions

class DragDropListbox(tk.Listbox):
    def __init__(self, master, **kwargs):
        super().__init__(master, selectmode=tk.SINGLE, **kwargs)

        self.drag_data = {"x": 0, "y": 0, "item": None}

        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<B1-Motion>", self.on_drag)
        self.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        widget = event.widget
        index = widget.nearest(event.y)
        item = widget.get(index)

        if item:
            self.drag_data["item"] = item
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_drag(self, event):
        widget = event.widget
        index = widget.nearest(event.y)

        if self.drag_data["item"]:
            current_index = widget.get(0, tk.END).index(self.drag_data["item"])

            if index < current_index:
                widget.delete(current_index)
                widget.insert(index, self.drag_data["item"])
            else:
                widget.delete(current_index)
                widget.insert(index, self.drag_data["item"])

    def on_release(self, event):
        self.drag_data["item"] = None

class CodeQuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("Code Quiz")
        self.questions = questions
        self.current_question_index = 0
        self.selected_order = []

        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text=self.questions[self.current_question_index]['question'])
        self.question_label.pack(pady=10)

        self.code_listbox = DragDropListbox(self.master)
        for line in self.questions[self.current_question_index]['code']:
            self.code_listbox.insert(tk.END, line)
        self.code_listbox.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=10)

    def submit_answer(self):
        selected_indices = [self.code_listbox.nearest(y) for y in range(0, self.code_listbox.winfo_height(), 20)]
        correct_order = self.questions[self.current_question_index]['correct_order']

        if selected_indices == correct_order:
            messagebox.showinfo("Correct", "Your answer is correct!")
            self.current_question_index += 1

            if self.current_question_index < len(self.questions):
                self.update_question()
            else:
                messagebox.showinfo("Quiz Completed", "Congratulations! You have completed the quiz.")
                self.restart_quiz()
        else:
            messagebox.showerror("Incorrect", "Your answer is incorrect. Please try again.")
            self.restart_quiz()

    def update_question(self):
        if self.current_question_index < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question_index]['question'])
            self.code_listbox.delete(0, tk.END)
            for line in self.questions[self.current_question_index]['code']:
                self.code_listbox.insert(tk.END, line)
        else:
            messagebox.showinfo("Quiz Completed", "Congratulations! You have completed the quiz.")
            self.restart_quiz()

    def restart_quiz(self):
        self.current_question_index = 0
        self.update_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeQuizApp(root, questions)
    root.mainloop()
