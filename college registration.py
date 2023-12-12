import tkinter as tk
from tkinter import messagebox

class CollegeRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("COLLEGE REGISTRATION")
        self.root.geometry("700x1200")  # Set window size

        # Set background color
        self.root.configure(bg='#e6f7ff')  # Light blue

        # Create and place labels and entry widgets with colorful styling
        self.label_name = tk.Label(root, font=("Arial",16 ) , text="Name:", bg='#e6f7ff')  # Light blue
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_name = tk.Entry(root, font=("Arial" , 16), bg='#cce5ff')  # Lighter blue
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_age = tk.Label(root, font=("Arial",16 ) , text="Age:", bg='#e6f7ff')
        self.label_age.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_age = tk.Entry(root, font=("Arial", 16 ) , bg='#cce5ff')
        self.entry_age.grid(row=1, column=1, padx=10, pady=10)

        self.label_email = tk.Label(root,font=("Arial", 16 ) , text="Email:", bg='#e6f7ff')
        self.label_email.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_email = tk.Entry(root, font=("Arial", 16) , bg='#cce5ff')
        self.entry_email.grid(row=2, column=1, padx=10, pady=10)

        self.label_student_id = tk.Label(root, font=("Arial", 16) ,text="Student_ID:", bg='#e6f7ff')
        self.label_student_id.grid(row=3, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_student_id = tk.Entry(root, font=("Arial", 16 ) , bg='#cce5ff')
        self.entry_student_id.grid(row=3, column=1, padx=10, pady=10)

        self.label_phone_no = tk.Label(root,font=("Arial", 16) , text="Phone_No:", bg='#e6f7ff')
        self.label_phone_no.grid(row=4, column=0, padx=10, pady=10, sticky=tk.E)

        self.entry_phone_no = tk.Entry(root, font=("Arial", 16 ) , bg='#cce5ff')
        self.entry_phone_no.grid(row=4, column=1, padx=10, pady=10)

        self.label_gender = tk.Label(root, font=("Arial", 16 ), text="Gender:", bg='#e6f7ff')
        self.label_gender.grid(row=5, column=0, padx=10, pady=10, sticky=tk.E)

        self.gender_var = tk.StringVar()
        self.gender_var.set("MALE")

        self.gender_menu = tk.OptionMenu(root, self.gender_var, "MALE", "FEMALE")
        self.gender_menu.config(bg='#cce5ff')
        self.gender_menu.grid(row=5, column=1, padx=10, pady=10)

        self.label_course = tk.Label(root, font=("Arial", 16) , text="Course:", bg='#e6f7ff')
        self.label_course.grid(row=6, column=0, padx=10, pady=10, sticky=tk.E)

        self.course_var = tk.StringVar()
        self.course_var.set("COMPUTER SCIENCE")

        self.course_menu = tk.OptionMenu(root, self.course_var, "COMPUTER SCIENCE", "INFORMATION MANAGEMENT", "PUBLIC ADMINISTRATION", "LIBRARY INFORMATICS")
        self.course_menu.config(bg='#cce5ff')
        self.course_menu.grid(row=6, column=1, padx=10, pady=10)

        self.label_college = tk.Label(root, font=("Arial", 16 ) , text="College:", bg='#e6f7ff')
        self.label_college.grid(row=7, column=0, padx=10, pady=10, sticky=tk.E)

        self.college_var = tk.StringVar()
        self.college_var.set("MALINJA")

        self.college_menu = tk.OptionMenu(root, self.college_var, "MALINJA", "MAHSURI", "MASRIA", "MURNI")
        self.college_menu.config(bg='#cce5ff')
        self.college_menu.grid(row=7, column=1, padx=10, pady=10)

        # Create and place the buttons with colorful styling
        self.submit_button = tk.Button(root, text="Submit", command=self.register_student, bg='#4CAF50', fg='white')  # Green button
        self.submit_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.read_button = tk.Button(root, text="Read Data", command=self.read_data, bg='#FFD700', fg='black')  # Gold button
        self.read_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(root, text="Update Data", command=self.update_data, bg='#FF4500', fg='white')  # OrangeRed button
        self.update_button.grid(row=10, column=0, columnspan=2, pady=5)

        self.delete_button = tk.Button(root, text="Delete Data", command=self.delete_data, bg='#8B0000', fg='white')  # DarkRed button
        self.delete_button.grid(row=11, column=0, columnspan=2, pady=5)

        # Initialize data store
        self.student_data = []
        self.student_id = tk.StringVar()


    def register_student(self):
    # Get values from the entry widgets
        name = self.entry_name.get()
        age = self.entry_age.get()
        email = self.entry_email.get()            
        student_id = self.entry_student_id.get()
        phone_no = self.entry_phone_no.get() 
        gender = self.gender_var.get()
        course = self.course_var.get()
        college = self.college_var.get()

        if not all([name, age, email, gender, student_id, phone_no, course, college]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        # Perform registration
        registration_data = {
            "Name": name,
            "Age": age,
            "Email": email,
            "Student_ID": student_id,
            "Phone_No": phone_no,
            "Gender": gender,
            "Course": course,
            "College": college,
        }

        self.student_data.append(registration_data)

        # Display a registration confirmation message
        confirmation_message = (
            f"Registration successful!\n\n"
            f"Name: {name}\n"
            f"Age: {age}\n"
            f"Email: {email}\n"
            f"Student_Id: {student_id}\n"
            f"Phone_No: {phone_no}\n"
            f"Gender: {gender}\n"
            f"Course: {course}\n"
            f"College: {college}\n"
        )
        messagebox.showinfo("Success", confirmation_message)


        # Clear entry fields after registration
        for entry in [self.entry_name, self.entry_age, self.entry_email, self.entry_student_id, self.entry_phone_no]:
            entry.delete(0, tk.END)

    def read_data(self):
        # Display data in a new window
        data_window = tk.Toplevel(self.root)
        data_window.title("Student Data")

        data_label = tk.Label(data_window, text="Student Data", font=("Helvetica", 16, "bold"))
        data_label.pack(pady=10)

        if not self.student_data:
            message_label = tk.Label(data_window, text="No data available.")
            message_label.pack(pady=10)
        else:
            for i, data in enumerate(self.student_data, start=1):
                data_text = f"Student {i}:\n"
                for key, value in data.items():
                    data_text += f"{key}: {value}\n"
                data_text += "\n"
                data_label = tk.Label(data_window, text=data_text)
                data_label.pack()


    def update_data(self):
        # Implement updating data (replace with your actual logic)
        messagebox.showinfo("Update", "Update data functionality will be implemented here.")

    def delete_data(self):
        # Implement deleting data (replace with your actual logic)
        messagebox.showinfo("Delete", "Delete data functionality will be implemented here.")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = CollegeRegistrationApp(root)
        root.mainloop()
    except Exception as e:
        print(f"An error occurred: {e}")