from utils import run_command

def main():
    print("\nPassword Cracking Tools:")
    print("1. John the Ripper")
    print("2. Hashcat")
    print("3. Back")
    choice = input("Select a tool: ")
    if choice == '1':
        hash_file = input("Enter path to hash file: ")
        run_command(["john", hash_file])
    elif choice == '2':
        hash_file = input("Enter path to hash file: ")
        wordlist = input("Enter path to wordlist: ")
        run_command(["hashcat", "-m", "0", "-a", "0", hash_file, wordlist])
    elif choice == '3':
        return
    else:
        print("Invalid choice. Please try again.")
