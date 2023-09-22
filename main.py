import tkinter as tk
from tkinter import ttk
import csv

# Creating a function to import data from CSV
def import_data():
    try:
        with open('Student_data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            
            # A variable to store the data
            data = []
            
            # Iterate through the rows in the Student_data.csv file
            for row in csv_reader:
                data.append(row)  # Add each row to the data list
            
            # Display the data in the GUI (you can update this part according to your GUI layout)
            data_text.delete(1.0, tk.END)  # Clear the existing text
            for row in data:
                data_text.insert(tk.END, ', '.join(row) + '\n')  # Display data in a Text widget
            
            status_label.config(text="Data imported successfully.")
    except FileNotFoundError:
        status_label.config(text="File not found!")

# Create a function to add a new student
def add_student():
    # Created a new Toplevel window
    add_student_window = tk.Toplevel(root)
    add_student_window.title("Add Student")

    # Created and configured GUI elements
    sid_label = ttk.Label(add_student_window, text="SID:")
    sid_entry = ttk.Entry(add_student_window)

    first_name_label = ttk.Label(add_student_window, text="First Name:")
    first_name_entry = ttk.Entry(add_student_window)

    last_name_label = ttk.Label(add_student_window, text="Last Name:")
    last_name_entry = ttk.Entry(add_student_window)

    email_label = ttk.Label(add_student_window, text="Email:")
    email_entry = ttk.Entry(add_student_window)
    
    hw1_label = ttk.Label(add_student_window, text="HW1:")
    hw1_entry = ttk.Entry(add_student_window)
    
    hw2_label = ttk.Label(add_student_window, text="HW2:")
    hw2_entry = ttk.Entry(add_student_window)
    
    hw3_label = ttk.Label(add_student_window, text="HW3:")
    hw3_entry = ttk.Entry(add_student_window)
    
    quiz1_label = ttk.Label(add_student_window, text="Quiz1:")
    quiz1_entry = ttk.Entry(add_student_window)
    
    quiz2_label = ttk.Label(add_student_window, text="Quiz2:")
    quiz2_entry = ttk.Entry(add_student_window)
    
    quiz3_label = ttk.Label(add_student_window, text="Quiz3:")
    quiz3_entry = ttk.Entry(add_student_window)
    
    quiz4_label = ttk.Label(add_student_window, text="Quiz4:")
    quiz4_entry = ttk.Entry(add_student_window)
    
    midterm_exam_label = ttk.Label(add_student_window, text="MidtermExam:")
    midterm_exam_entry = ttk.Entry(add_student_window)
    
    final_exam_label = ttk.Label(add_student_window, text="FinalExam:")
    final_exam_entry = ttk.Entry(add_student_window)
    

# Create a function to search by SID
def search_by_sid():
    # Implement code to search for a student by SID
    pass

# Create a function to compute the final letter score
def compute_final_score(scores):
    # Implement code to compute the final letter score
    pass

# Create a function to update student scores
def update_scores():
    # Implement code to update student scores
    pass

# Create a function to search by task name
def search_by_task_name():
    # Implement code to search by task name
    pass

# Create a function to export data to CSV
def export_data():
    # Implement code to export data to CSV
    pass

# Create the main window
root = tk.Tk()
root.title("Gradebook System")

# Create and configure GUI elements
import_button = ttk.Button(root, text="Import Data", command=import_data)
add_button = ttk.Button(root, text="Add Student", command=add_student)
search_button = ttk.Button(root, text="Search by SID", command=search_by_sid)
update_button = ttk.Button(root, text="Update Scores", command=update_scores)
export_button = ttk.Button(root, text="Export Data", command=export_data)

status_label = ttk.Label(root, text="")
# Create a Text widget to display the data
data_text = tk.Text(root, wrap=tk.WORD, height=40, width=150)
data_text.pack()  # This line adds the Text widget to the GUI

# Layout GUI elements
import_button.pack()
add_button.pack()
search_button.pack()
update_button.pack()
export_button.pack()
status_label.pack()

# Start the Tkinter main loop
root.mainloop()
