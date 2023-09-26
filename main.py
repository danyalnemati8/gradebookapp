import tkinter as tk
from tkinter import ttk
import csv

#Root has beem defined
root = tk.Tk()
root.title("Gradebook System")


# Declared entry widgets as global variables sid to final exam 
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
delete_student_window = None  

# Creating a function to import data from CSV
def import_data():
    try:
        with open('Student_data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            data = []
            for row in csv_reader:
                data.append(row)  # Add each row to the data list
            
            # Display the data in the GUI (you can update this part according to your GUI layout)
            data_text.delete(1.0, tk.END)  # Clear the existing text
            for row in data:
                data_text.insert(tk.END, ', '.join(row) + '\n')  # Display data in a Text widget
            
            status_label.config(text="Data imported successfully!")
    except FileNotFoundError:
        status_label.config(text="File not found!")

# Created a function to add a new student
def add_student():
    global sid_entry, first_name_entry, last_name_entry, email_entry
    global hw1_entry, hw2_entry, hw3_entry, quiz1_entry, quiz2_entry, quiz3_entry, quiz4_entry
    global midterm_exam_entry, final_exam_entry
    global add_student_window

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
def delete_student():
    global delete_student_window
    global sid_entry  # Declare sid_entry as a global variable

    # Create a new Toplevel window
    delete_student_window = tk.Toplevel(root)
    delete_student_window.title("Delete Student")

    # Create and configure GUI elements
    sid_label = ttk.Label(delete_student_window, text="Enter SID to delete:")
    sid_label.grid(row=0, column=0)

    sid_entry = ttk.Entry(delete_student_window)
    sid_entry.grid(row=0, column=1)

    def confirm_delete():
        sid_to_delete = sid_entry.get()
        # Open the CSV file and create a temporary list to store the data
        data_to_keep = []
        student_deleted = False

        with open('Student_data.csv', 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] != sid_to_delete:
                    data_to_keep.append(row)
                else:
                    student_deleted = True

        if student_deleted:
            # Rewrite the CSV file with the updated data
            with open('Student_data.csv', 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data_to_keep)

            # Update the displayed data
            data_text.delete(1.0, tk.END)
            for row in data_to_keep:
                data_text.insert(tk.END, ', '.join(row) + '\n')

            status_label.config(text=f"Student with SID {sid_to_delete} deleted.")
        else:
            status_label.config(text=f"Student with SID {sid_to_delete} not found.")

    delete_button = ttk.Button(delete_student_window, text="Delete", command=confirm_delete)
    delete_button.grid(row=1, column=0, columnspan=2)

# Created a function to search by SID
def search_by_sid():
    
    search_window = tk.Toplevel(root)
    search_window.title("Search by SID")
    
    search_label = ttk.Label(search_window, text="Enter SID to search for:")
    search_label.grid(row=0, column=0)
    
    search_entry = ttk.Entry(search_window)
    search_entry.grid(row=0, column=1)
    
    search_button = ttk.Button(search_window, text="Search", command=lambda: perform_sid_search(search_entry.get()))
    search_button.grid(row=1, column=0, columnspan=2)

search_button = ttk.Button(root, text="Search by SID", command=search_by_sid)


# Updates the perform_sid_search function to accept search_sid as an argument
def perform_sid_search(search_sid):
    
    student_found = False

    with open('Student_data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == search_sid:  # SID is in the first column
                # Display the student's information
                student_found = True
                display_search_result(row) # Display the student's information basically the whole row
                break

    # If student not found, display a message
    if not student_found:
        display_search_result("Student with SID " + search_sid + " not found.")

# Update the display_search_result function to create a label to display the information
def display_search_result(result):

    result_window = tk.Toplevel(root)
    result_window.title("Search Result")

    result_label = ttk.Label(result_window, text=result)
    result_label.pack()
# Create a function to compute the final letter score
def compute_final_score(hw1, hw2, hw3, quiz1, quiz2, quiz3, quiz4, midterm_exam, final_exam):
    # Define grading criteria (you can adjust these as needed)
    hw_weight = 0.2
    quiz_weight = 0.2
    midterm_weight = 0.3
    final_exam_weight = 0.3

    # Calculate weighted scores for each component
    hw_score = (hw1 + hw2 + hw3) / 3
    quiz_score = (quiz1 + quiz2 + quiz3 + quiz4) / 4

    # Calculate the final score
    final_score = (hw_score * hw_weight +
                   quiz_score * quiz_weight +
                   midterm_exam * midterm_weight +
                   final_exam * final_exam_weight)

    # Determine the final letter grade based on the final score (you can define your grading scale)
    if final_score >= 90:
        letter_grade = 'A'
    elif final_score >= 80:
        letter_grade = 'B'
    elif final_score >= 70:
        letter_grade = 'C'
    elif final_score >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    return final_score, letter_grade

    

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
    
    # Open the CSV file and write the new student data
    with open('Student_data.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(new_student)

    # Display the new student data in the Text widget
    data_text.insert(tk.END, ', '.join(new_student) + '\n')

    # Close the "Add Student" dialog
    add_student_window.destroy()

# Create the main window
root = tk.Tk()
root.title("Gradebook System")

# Create and configure GUI elements
import_button = ttk.Button(root, text="Import Data", command=import_data)
add_button = ttk.Button(root, text="Add Student", command=add_student)
delete_button = ttk.Button(root, text="Delete Student", command=delete_student)
delete_button.pack()
# Rest of your GUI layout...
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
