# Leviathon

Leviathon is a command-line interface (CLI) tool that automates various Kali Linux hacking tools. It provides a user-friendly menu to select and run different hacking tools with minimal user input.

## Features

- **Network Scanning**: Automate network scanning with tools like Nmap and Masscan.
- **Vulnerability Assessment**: Perform vulnerability assessments using Nikto and OpenVAS.
- **Password Cracking**: Crack passwords with John the Ripper and Hashcat.
- **Exploit**: Utilize Metasploit and Searchsploit for exploiting vulnerabilities.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/leviathon.git
   cd leviathon
   pip install -r requirements.txt
   ./leviathon.py


   
### Explanation:
- **Modular Structure**: The code is organized into separate modules for better maintainability and extensibility.
- **Error Handling**: The `run_command` function in `utils.py` handles errors gracefully.
- **User Feedback**: The script provides clear instructions and feedback to the user.
- **Extensibility**: Adding new tools or features is straightforward by creating new modules under the `tools` directory.

This structure provides a solid foundation for Leviathon and can be easily expanded with additional tools and features.
