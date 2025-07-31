🏥 Hospital Management System (OOP in Python)
This is a simple Hospital Management System built using Object-Oriented Programming (OOP) concepts in Python. It allows basic management of doctors, patients, nurses, and rooms within a hospital environment.

📌 Features
✅ Add doctors, patients, nurses, and rooms

🏨 Admit and discharge patients

🧑‍⚕️ Assign doctors and nurses to patients

📋 Maintain patient medical history

🚪 Track room occupancy and availability

🔍 Search doctors, patients, nurses by ID

🧱 Classes Overview
1. Person (Base Class)
Attributes: name, age, gender, contact

Method: get_details()

2. Doctor (Inherits from Person)
Extra Attributes: doctor_id, specialization, availability, patients_list

Methods: add_patients(), view_patients(), get_schedule()

3. Patient (Inherits from Person)
Extra Attributes: patient_id, disease, admit_status, assigned_doctor, medical_history

Methods: add_medical_record(), assign_doctor(), discharge(), get_summary()

4. Nurse (Inherits from Person)
Extra Attributes: nurse_id, shift, assigned_patients

Methods: assign_patient(), get_assigned_patients()

5. Room
Attributes: room_no, room_type, assigned_patient, is_occupied

Methods: assign_patient(), vacate_room(), get_status()

6. HospitalManagementSystem
Manages: doctors, patients, nurses, rooms

Core Methods:

add_*() — to add doctors, patients, nurses, rooms

assign_doctor_to_patient(), assign_nurse_to_patient()

admit_patient(), discharge_patient()

find_*() — search by ID

show_all_patients(), show_all_rooms()

🚀 Getting Started
🛠 Requirements
Python 3.x

▶️ Run the Program
bash
Copy
Edit
python hospital_system.py
The demo section at the bottom of the script will run and show how doctors, patients, and rooms are managed.

📌 Example Usage
python
Copy
Edit
# Creating system
hms = hospitalManagementSystem()

# Adding data
hms.add_doctor(doctor("Dr. Sharma", 45, "Male", "9876543210", "D101", "Cardiology"))
hms.add_patient(patient("Ankit", 30, "Male", "9876500000", "P201", "Heart Disease"))
hms.add_nurse(nurse("Sister Maya", 28, "Female", "9876500001", "N301", "Day"))
hms.add_room(room("R1", "General"))

# Assignments and admission
hms.assign_doctor_to_patient("D101", "P201")
hms.admit_patient("P201", "General")

# Outputs
hms.show_all_patients()
hms.show_all_rooms()
📂 File Structure
bash
Copy
Edit
hospital_system.py   # Main script
README.md            # Project documentation
📚 Concepts Used
Object-Oriented Programming:

Inheritance

Encapsulation

Polymorphism (via method overriding)

Composition (classes using other class instances)

Lists and Iteration

🙋‍♂️ Author
Nimit — Python OOP enthusiast.

📝 License
This project is for educational purposes. Use freely for learning or teaching OOP in Python.
