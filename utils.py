import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")

def main_menu():
    print("\nWelcome to Leviathon!")
    print("1. Network Scanning")
    print("2. Vulnerability Assessment")
    print("3. Password Cracking")
    print("4. Exploit")
    print("5. Exit")
    choice = input("Select an option: ")
    return choice
