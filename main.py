import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import csv

#Root has beem defined
root = tk.Tk()
root.title("Gradebook System")


# Declared entry widgets as global variables sid to final exam, etc.
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
task_name_entry = None
result_text = None
filepath = None

# a function to import data from local destkop must be a csv
def import_data():
    global filepath
    try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            filepath = file_path  
            with open(filepath, 'r') as file:
                csv_reader = csv.reader(file)
                data = []
                for row in csv_reader:
                    data.append(row) 

            data_text.delete(1.0, tk.END)  # Clear the existing text
            for row in data:
                data_text.insert(tk.END, ', '.join(row) + '\n')  # Displays data in a Text widget
            
            status_label.config(text="Data imported successfully!")
    except FileNotFoundError:
        status_label.config(text="File not found!")

# a function to add a new student
def add_student():
    global sid_entry, first_name_entry, last_name_entry, email_entry
    global hw1_entry, hw2_entry, hw3_entry, quiz1_entry, quiz2_entry, quiz3_entry, quiz4_entry
    global midterm_exam_entry, final_exam_entry
    global add_student_window

    # a new Toplevel window
    add_student_window = tk.Toplevel(root)
    add_student_window.title("Add Student")

    # configured GUI elements every category in the csv file
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
    global sid_entry 

    delete_student_window = tk.Toplevel(root)
    delete_student_window.title("Delete Student")
    
    sid_label = ttk.Label(delete_student_window, text="Enter SID to delete:")
    sid_label.grid(row=0, column=0)

    sid_entry = ttk.Entry(delete_student_window)
    sid_entry.grid(row=0, column=1)

    def confirm_delete():
        sid_to_delete = sid_entry.get()
        # Open the CSV file and create a temporary list to store the data
        data_to_keep = []
        student_deleted = False

        with open(filepath, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] != sid_to_delete:
                    data_to_keep.append(row)
                else:
                    student_deleted = True

        if student_deleted:
            # if you delete rewrites the CSV file with the updated data
            with open(filepath, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data_to_keep)
                
            # Updates the displayed data
            data_text.delete(1.0, tk.END)
            for row in data_to_keep:
                data_text.insert(tk.END, ', '.join(row) + '\n')

            status_label.config(text=f"Student with SID {sid_to_delete} deleted.")
        else:
            status_label.config(text=f"Student with SID {sid_to_delete} not found.")

    delete_button = ttk.Button(delete_student_window, text="Delete", command=confirm_delete)
    delete_button.grid(row=1, column=0, columnspan=2)

# a function to search by SID
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

def perform_sid_search(search_sid):
    student_found = False

    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == search_sid:  # SID is in the first column
                # extract scores from the row and convert them to float
                hw_scores = [float(row[4]), float(row[5]), float(row[6])]
                quiz_scores = [float(row[7]), float(row[8]), float(row[9]), float(row[10])]
                midterm_exam = float(row[11])
                final_exam = float(row[12])

                # calculate the final score based on the specified weights given in the document 
                hw_weight = 0.2
                quiz_weight = 0.2
                midterm_weight = 0.3
                final_weight = 0.3

                final_score = (
                    sum(hw_scores) / len(hw_scores) * hw_weight +
                    sum(quiz_scores) / len(quiz_scores) * quiz_weight +
                    midterm_exam * midterm_weight +
                    final_exam * final_weight
                )

                # determines the letter grade based on the final score
                letter_grade = determine_letter_grade(final_score)

                student_info = f"SID: {row[0]}\n"
                student_info += f"Name: {row[1]} {row[2]}\n"
                student_info += f"Email: {row[3]}\n"
                student_info += f"Final Score: {final_score:.2f}\n"
                student_info += f"Letter Grade: {letter_grade}\n"

                show_student_info(student_info)

                student_found = True
                break

    # if student not found, display a message
    if not student_found:
        show_student_info("Student with SID " + search_sid + " not found.")

# determine the letter grade based on the final score
def determine_letter_grade(final_score):
    if final_score >= 90:
        return "A"
    elif final_score >= 80:
        return "B"
    elif final_score >= 70:
        return "C"
    elif final_score >= 60:
        return "D"
    else:
        return "F"

# show student information in a label or pop-up dialog
def show_student_info(info):
    result_window = tk.Toplevel(root)
    result_window.title("Student Information")

    result_label = ttk.Label(result_window, text=info)
    result_label.pack()


# updates the display_search_result function to creates a label to display the information
def display_search_result(result):

    result_window = tk.Toplevel(root)
    result_window.title("Search Result")

    result_label = ttk.Label(result_window, text=result)
    result_label.pack()

# a function to update student scores
def update_scores():
    # a window for updating scores
    update_window = tk.Toplevel(root)
    update_window.title("Update Scores")
    
    sid_label = ttk.Label(update_window, text="Enter SID to update scores:")
    sid_label.grid(row=0, column=0)
    
    sid_entry = ttk.Entry(update_window)
    sid_entry.grid(row=0, column=1)

    hw_label = ttk.Label(update_window, text="New Homework Scores (3 values comma-separated!!!):")
    hw_label.grid(row=1, column=0)
    
    hw_entry = ttk.Entry(update_window)
    hw_entry.grid(row=1, column=1)

    quiz_label = ttk.Label(update_window, text="New Quiz Scores (4 values comma-separated!!!):")
    quiz_label.grid(row=2, column=0)
    
    quiz_entry = ttk.Entry(update_window)
    quiz_entry.grid(row=2, column=1)

    midterm_label = ttk.Label(update_window, text="New Midterm Exam Score:")
    midterm_label.grid(row=3, column=0)
    
    midterm_entry = ttk.Entry(update_window)
    midterm_entry.grid(row=3, column=1)

    final_label = ttk.Label(update_window, text="New Final Exam Score:")
    final_label.grid(row=4, column=0)
    
    final_entry = ttk.Entry(update_window)
    final_entry.grid(row=4, column=1)

    # updates scores when the button is clicked
    def perform_update():
        # use get() to get the entered SID and scores
        update_sid = sid_entry.get()
        new_hw_scores = hw_entry.get().split(',')
        new_quiz_scores = quiz_entry.get().split(',')
        new_midterm_score = midterm_entry.get()
        new_final_score = final_entry.get()
        
        data_to_update = []

        with open(filepath, 'r') as file:
            csv_reader = csv.reader(file)
            student_updated = False

            for row in csv_reader:
                if row[0] == update_sid:
                    # updates the scores for the specified student
                    row[4:7] = new_hw_scores
                    row[7:11] = new_quiz_scores
                    row[11] = new_midterm_score
                    row[12] = new_final_score
                    student_updated = True

                data_to_update.append(row)

        if student_updated:
            # rewrites the CSV file with the updated data
            with open(filepath, 'w', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data_to_update)

            messagebox.showinfo("Success", "Student scores updated successfully.")
            
            data_text.delete(1.0, tk.END)  # clears the existing text
            for row in data_to_update:
                data_text.insert(tk.END, ', '.join(row) + '\n')  # displays updated data

        else:
            messagebox.showerror("Error", "Student with SID not found.")

    update_button = ttk.Button(update_window, text="Update Scores", command=perform_update)
    update_button.grid(row=5, column=0, columnspan=2)

# a function to search by task name
task_name_entry = ttk.Entry(root)
task_name_entry.pack() 
def search_by():
    global task_name_entry, result_text
    task_name = task_name_entry.get().strip()
    valid_task_names = {"HW1", "HW2", "HW3", "Quiz1", "Quiz2", "Quiz3", "Quiz4", "MidtermExam", "FinalExam"}

    if task_name not in valid_task_names:
        messagebox.showerror("Invalid Task Name", "Please enter a valid task name.")
        return

    scores = []  # stores scores for the specified task

    with open(filepath, 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader) 
        task_index = None

        try:
            task_index = header.index(task_name)  
        except ValueError:
            messagebox.showinfo("No Scores", f"No scores found for {task_name}.")

        if task_index is not None:
            for row in csv_reader:
                try:
                    task_score = float(row[task_index])
                    scores.append(task_score)
                except ValueError:
                    pass

            if not scores:
                messagebox.showinfo("No Scores", f"No scores found for {task_name}.")
            else:
                max_score = max(scores)
                min_score = min(scores)
                avg_score = sum(scores) / len(scores)

                result_message = f"Task: {task_name}\n"
                result_message += f"Maximum Score: {max_score}\n"
                result_message += f"Minimum Score: {min_score}\n"
                result_message += f"Average Score: {avg_score:.2f}\n"

                messagebox.showinfo("Task Scores", result_message)
                
search_button = ttk.Button(root, text="Search by Task Name", command=search_by)
search_button.pack()

# a function to export data to CSV
def export_data():
    try:
        with open('Student_data_export.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)

            header = ["SID", "First Name", "Last Name", "Email", "HW1", "HW2", "HW3", "Quiz1", "Quiz2", "Quiz3", "Quiz4", "Midterm Exam", "Final Exam"]
            csv_writer.writerow(header)

            # retrieves and writes the data for each student
            with open(filepath, 'r') as data_file:
                csv_reader = csv.reader(data_file)
                next(csv_reader) 
                for row in csv_reader:
                    csv_writer.writerow(row)

        messagebox.showinfo("Export Successful", "Data exported to Student_data_export.csv successfully.")

    except Exception as e:
        messagebox.showerror("Export Error", f"An error occurred while exporting data: {str(e)}")

def save_student():
    # retrieves the entered data from the entry widgets
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
    
    # new student record
    new_student = [new_sid, new_first_name, new_last_name, new_email, new_hw1, new_hw2, new_hw3, new_quiz1, new_quiz2, new_quiz3, new_quiz4, new_midterm_exam, new_final_exam]
    
    # writew the new student data
    with open(filepath, 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(new_student)
        
    data_text.insert(tk.END, ', '.join(new_student) + '\n')

    add_student_window.destroy()


# main window
root = tk.Tk()
root.title("Gradebook System")

# configuring GUI elements
import_button = ttk.Button(root, text="Import Data", command=import_data)
add_button = ttk.Button(root, text="Add Student", command=add_student)
delete_button = ttk.Button(root, text="Delete Student", command=delete_student)

# setting button to functions
search_button = ttk.Button(root, text="Search by SID", command=search_by_sid)
update_button = ttk.Button(root, text="Update Scores", command=update_scores)
export_button = ttk.Button(root, text="Export Data", command=export_data)
update_button = ttk.Button(root, text="Update Scores", command=update_scores)
search_task_button = ttk.Button(root, text="Search by Task Name", command=search_by)

status_label = ttk.Label(root, text="")
data_text = tk.Text(root, wrap=tk.WORD, height=40, width=150)
data_text.pack()  
# Layout GUI elements
import_button.pack()
add_button.pack()
delete_button.pack()
search_button.pack()
update_button.pack()
search_task_button.pack()
export_button.pack()
status_label.pack()


root.mainloop()
