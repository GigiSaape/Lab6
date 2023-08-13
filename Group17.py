class Doctor:
    def init(self, doctor_id=None, name=None, specialization=None, working_time=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def str(self):
        return f"Doctor ID: {self.doctor_id}\nName: {self.name}\nSpecialization: {self.specialization}\nWorking Time: {self.working_time}\nQualification: {self.qualification}\nRoom Number: {self.room_number}"

class DoctorManager:
    def init(self):
        self.doctors = []

class PatientManager:
    def init(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def str(self):
        return f"Patient ID: {self.pid}\nName: {self.name}\nDisease: {self.disease}\nGender: {self.gender}\nAge: {self.age}"



class Management:
    def init(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            print("Main Menu:")
            print("1. Doctor Management")
            print("2. Patient Manager")
            print("3. Exit")

            choice = input("Enter your selection: ")

            if choice == '1':
                self.doctor_submenu()
            elif choice == '2':
                self.patient_submenu()
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
def doctor_submenu(self):
        while True:
            print("Doctor Management:")
            print("1. Display Doctors")
            print("2. Search Doctor by ID")
            print("3. Search Doctor by Name")
            print("4. Add New Doctor")
            print("5. Edit Doctor Information")
            print("6. Back to Main Menu")

            choice = input("Enter your selection: ")
            if choice == '1':
                self.doctor_manager.display_doctors_list()
            elif choice == '2':
                self.doctor_manager.search_doctor_by_id()
            # Implement other doctor submenu options here
            elif choice == '6':
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

def patient_submenu(self):
        while True:
            print("Patient Management:")
            # Implement patient submenu options similarly to the doctor submenu

            choice = input("Enter your selection: ")
            # Implement patient submenu logic here

            if choice == '5':
                print("Returning to the main menu.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")


if __name__ == "main":
    management_system = Management()
    management_system.display_menu()
    