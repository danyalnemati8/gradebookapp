import tkinter as tk
from tkinter import ttk
import csv

# Declare entry widgets as global variables
sid_entry = None
first_name_entry = None
last_name_entry = None
email_entry = None
hw1_entry = None
hw2_entry = None
hw3_entry = None
quiz1_entry = None
quiz2_entry = None
quiz3_entry = None
quiz4_entry = None
midterm_exam_entry = None
final_exam_entry = None

add_student_window = None

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
    global sid_entry, first_name_entry, last_name_entry, email_entry
    global hw1_entry, hw2_entry, hw3_entry, quiz1_entry, quiz2_entry, quiz3_entry, quiz4_entry
    global midterm_exam_entry, final_exam_entry

    # Created a new Toplevel window
    add_student_window = tk.Toplevel(root)
    add_student_window.title("Add Student")

    # Created and configured GUI elements
    sid_label = ttk.Label(add_student_window, text="SID:")
    sid_label.grid(row=0, column=0)
    sid_entry = ttk.Entry(add_student_window)
    sid_entry.grid(row=0, column=1)

    first_name_label = ttk.Label(add_student_window, text="First Name:")
    first_name_label.grid(row=1, column=0)
    first_name_entry = ttk.Entry(add_student_window)
    first_name_entry.grid(row=1, column=1)

    last_name_label = ttk.Label(add_student_window, text="Last Name:")
    last_name_label.grid(row=2, column=0)
    last_name_entry = ttk.Entry(add_student_window)
    last_name_entry.grid(row=2, column=1)

    email_label = ttk.Label(add_student_window, text="Email:")
    email_label.grid(row=3, column=0)
    email_entry = ttk.Entry(add_student_window)
    email_entry.grid(row=3, column=1)

    hw1_label = ttk.Label(add_student_window, text="HW1:")
    hw1_label.grid(row=4, column=0)
    hw1_entry = ttk.Entry(add_student_window)
    hw1_entry.grid(row=4, column=1)

    hw2_label = ttk.Label(add_student_window, text="HW2:")
    hw2_label.grid(row=5, column=0)
    hw2_entry = ttk.Entry(add_student_window)
    hw2_entry.grid(row=5, column=1)

    hw3_label = ttk.Label(add_student_window, text="HW3:")
    hw3_label.grid(row=6, column=0)
    hw3_entry = ttk.Entry(add_student_window)
    hw3_entry.grid(row=6, column=1)

    quiz1_label = ttk.Label(add_student_window, text="Quiz1:")
    quiz1_label.grid(row=7, column=0)
    quiz1_entry = ttk.Entry(add_student_window)
    quiz1_entry.grid(row=7, column=1)

    quiz2_label = ttk.Label(add_student_window, text="Quiz2:")
    quiz2_label.grid(row=8, column=0)
    quiz2_entry = ttk.Entry(add_student_window)
    quiz2_entry.grid(row=8, column=1)

    quiz3_label = ttk.Label(add_student_window, text="Quiz3:")
    quiz3_label.grid(row=9, column=0)
    quiz3_entry = ttk.Entry(add_student_window)
    quiz3_entry.grid(row=9, column=1)

    quiz4_label = ttk.Label(add_student_window, text="Quiz4:")
    quiz4_label.grid(row=10, column=0)
    quiz4_entry = ttk.Entry(add_student_window)
    quiz4_entry.grid(row=10, column=1)

    midterm_exam_label = ttk.Label(add_student_window, text="Midterm Exam:")
    midterm_exam_label.grid(row=11, column=0)
    midterm_exam_entry = ttk.Entry(add_student_window)
    midterm_exam_entry.grid(row=11, column=1)
    
    final_exam_label = ttk.Label(add_student_window, text="Final Exam:")
    final_exam_label.grid(row=12, column=0)
    final_exam_entry = ttk.Entry(add_student_window)
    final_exam_entry.grid(row=12, column=1)
    
    # Save buttton added 
    
    save_button = ttk.Button(add_student_window, text="Save", command=save_student)
    save_button.grid(row=13, column=0, columnspan=2)

# Function to save the entered student data
def save_student():
    # Retrieve the entered data from the entry widgets
    new_sid = sid_entry.get()
    new_first_name = first_name_entry.get()
    new_last_name = last_name_entry.get()
    new_email = email_entry.get()
    new_hw1 = hw1_entry.get()
    new_hw2 = hw2_entry.get()
    new_hw3 = hw3_entry.get()
    new_quiz1 = quiz1_entry.get()
    new_quiz2 = quiz2_entry.get()
    new_quiz3 = quiz3_entry.get()
    new_quiz4 = quiz4_entry.get()
    new_midterm_exam = midterm_exam_entry.get()
    new_final_exam = final_exam_entry.get()
    
    # Create a new student record (you can decide how to store this data, e.g., in a list, dictionary, or save to a file)
    new_student = [new_sid, new_first_name, new_last_name, new_email, new_hw1, new_hw2, new_hw3, new_quiz1, new_quiz2, new_quiz3, new_quiz4, new_midterm_exam, new_final_exam]

    # Display the new student data in the Text widget
    data_text.insert(tk.END, ', '.join(new_student) + '\n')

    # Close the "Add Student" dialog
    add_student_window.destroy()


    

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
def search_by():
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
