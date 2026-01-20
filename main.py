from patient_manager import add_patient, process_patient, show_queue

while True:
    print("Hospital Triage Simulator")
    print("1. Add Patient")
    print("2. Process Patient")
    print("3. View Queue")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        process_patient()
    elif choice == "3":
        show_queue()
    elif choice == "4":
        print("Exiting program")
        break
    else:
        print("Invalid option\n")
