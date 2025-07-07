import sys
from tools import network_scanning, vulnerability_assessment, password_cracking, exploit
from utils import run_command, main_menu

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            network_scanning.main()
        elif choice == '2':
            vulnerability_assessment.main()
        elif choice == '3':
            password_cracking.main()
        elif choice == '4':
            exploit.main()
        elif choice == '5':
            print("Exiting Leviathon. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
