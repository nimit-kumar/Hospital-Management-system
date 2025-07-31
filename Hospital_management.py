class person:
    def __init__(self, name, age, gender, contact):
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def get_details(self):
        return f"Name-{self.name}\nAge-{self.age}\nGender-{self.gender}\nContact-{self.contact}"


class doctor(person):
    def __init__(self, name, age, gender, contact, doctor_id, specialization, availability=True):
        super().__init__(name, age, gender, contact)
        self.doctor_id = doctor_id
        self.specialization = specialization
        self.availability = availability
        self.patients_list = []

    def view_patients(self):
        if not self.patients_list:
            print("Patients list is empty")
        else:
            print("The list of patients are:")
            for i, j in enumerate(self.patients_list):
                print(f"{i} - {j}")

    def add_patients(self, patient_name=None):
        if patient_name is None:
            patient_name = input("Enter patient name: ")
        self.patients_list.append(patient_name)
        print(f"Patient {patient_name} is added successfully to the list")

    def get_schedule(self):
        return "The availability of doctor is from 11:00 AM to 6:00 PM"


class patient(person):
    def __init__(self, name, age, gender, contact, patient_id, disease, admit_status=False, assigned_doctor=None):
        super().__init__(name, age, gender, contact)
        self.patient_id = patient_id
        self.disease = disease
        self.admit_status = admit_status
        self.assigned = assigned_doctor
        self.medical_history = []

    def add_medical_record(self):
        medical_records = input("Enter medical records, If there is no medical record, please write N/A: ")
        self.medical_history.append(medical_records)
        print("Your medical records added to medical history list\n Thanks")

    def assign_doctor(self, doctor_obj):
        self.assigned = doctor_obj
        print(f"The doctor {doctor_obj.name} is assigned to {self.name}")

    def discharge(self):
        self.admit_status = False
        return "The patient is discharged"

    def get_summary(self):
        print(f"Patient Name: {self.name}\nAge: {self.age}\nGender: {self.gender}")
        if self.assigned:
            print(f"Treated by Doctor: {self.assigned.name}")
        else:
            print("No doctor assigned")


class nurse(person):
    def __init__(self, name, age, gender, contact, nurse_id, shift):
        super().__init__(name, age, gender, contact)
        self.nurse_id = nurse_id
        self.shift = shift
        self.assigned_patients = []

    def assign_patient(self, patient_obj):
        self.assigned_patients.append(patient_obj)
        print(f"The nurse {self.name} is assigned to {patient_obj.name}")

    def get_assigned_patients(self):
        if not self.assigned_patients:
            print("No patient is assigned")
        else:
            print("The assigned patients are:")
            for i, j in enumerate(self.assigned_patients):
                print(f"{i} - {j.name}")


class room:
    def __init__(self, room_no, room_type, assigned_patient=None, is_occupied=False):
        self.room_no = room_no
        self.room_type = room_type
        self.is_occupied = is_occupied
        self.assigned_patient = assigned_patient

    def assign_patient(self, patient_obj):
        self.assigned_patient = patient_obj
        self.is_occupied = True
        print(f"The room {self.room_no} is assigned to {patient_obj.name}")

    def vacate_room(self):
        self.assigned_patient = None
        self.is_occupied = False
        print(f"The room {self.room_no} is now vacant")

    def get_status(self):
        status = "Occupied" if self.is_occupied else "Available"
        return f"Room {self.room_no} ({self.room_type}) - {status}"


class hospitalManagementSystem:
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.rooms = []
        self.nurses = []

    def add_doctor(self, doctor_obj):
        self.doctors.append(doctor_obj)
        print(f"The doctor {doctor_obj.name} is added to the list")

    def add_patient(self, patient_obj):
        self.patients.append(patient_obj)
        print(f"The patient {patient_obj.name} is added to the list")

    def add_nurse(self, nurse_obj):
        self.nurses.append(nurse_obj)
        print(f"The nurse {nurse_obj.name} is added to the list")

    def add_room(self, room_obj):
        self.rooms.append(room_obj)
        print(f"Room {room_obj.room_no} is added to the hospital")

    def admit_patient(self, patient_id, room_type):
        patient = self.find_patient(patient_id)
        if not patient:
            print("Patient is not found")
        else:
            for room in self.rooms:
                if room.room_type == room_type and not room.is_occupied:
                    room.assign_patient(patient)
                    patient.admit_status = True
                    return
            print(f"No available {room_type} rooms")

    def discharge_patient(self, patient_id):
        patient = self.find_patient(patient_id)
        if not patient:
            print("Patient not found.")
            return
        for room in self.rooms:
            if room.assigned_patient == patient:
                room.vacate_room()
                patient.admit_status = False
                print(patient.discharge())
                return
        print("Patient was not admitted.")

    def assign_doctor_to_patient(self, doctor_id, patient_id):
        doctor = self.find_doctor(doctor_id)
        patient = self.find_patient(patient_id)
        if doctor and patient:
            patient.assign_doctor(doctor)
        else:
            print("Doctor or Patient not found.")

    def assign_nurse_to_patient(self, nurse_id, patient_id):
        nurse = self.find_nurse(nurse_id)
        patient = self.find_patient(patient_id)
        if nurse and patient:
            nurse.assign_patient(patient)
        else:
            print("Nurse or Patient not found.")

    def find_doctor(self, doctor_id):
        return next((d for d in self.doctors if d.doctor_id == doctor_id), None)

    def find_patient(self, patient_id):
        return next((p for p in self.patients if p.patient_id == patient_id), None)

    def find_nurse(self, nurse_id):
        return next((n for n in self.nurses if n.nurse_id == nurse_id), None)

    def show_all_patients(self):
        if not self.patients:
            print("No patients found.")
        else:
            for p in self.patients:
                p.get_summary()

    def show_all_rooms(self):
        for room in self.rooms:
            print(room.get_status())


# Usage Example:
hms = hospitalManagementSystem()

# Adding Doctors
d1 = doctor("Dr. Sharma", 45, "Male", "9876543210", "D101", "Cardiology")
hms.add_doctor(d1)

# Adding Patients
p1 = patient("Ankit", 30, "Male", "9876500000", "P201", "Heart Disease")
hms.add_patient(p1)

# Adding Nurse
n1 = nurse("Sister Maya", 28, "Female", "9876500001", "N301", "Day")
hms.add_nurse(n1)

# Adding Rooms
r1 = room("R1", "General")
hms.add_room(r1)

# Assign Doctor and Admit Patient
hms.assign_doctor_to_patient("D101", "P201")
hms.admit_patient("P201", "General")

# View All Patients
print("\n--- All Patients ---")
hms.show_all_patients()

# View All Rooms
print("\n--- Room Status ---")
hms.show_all_rooms()
