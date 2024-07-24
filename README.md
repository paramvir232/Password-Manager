# Tkinter Password Manager GUI
## Overview
This Python application is a password manager GUI built using Tkinter, designed to securely store and manage credentials for various online accounts. It offers encryption for data security and includes features for password generation, credential storage, and retrieval.

## Features

**Secure Storage:** Encrypts and stores credentials in a JSON file using a specified encryption key.

**Password Generation:** Generates strong, randomized passwords for enhanced security.

**Credential Retrieval:** Easily retrieve stored credentials by searching for a website or specific key.

**Add Entry:** Allows for adding new entries to expand data storage.

**Security Measures:** Limits search attempts to five with correct encryption key; GUI blocks access after unsuccessful attempts.

**Exception Handling:** Robust error handling to prevent crashes and ensure smooth operation.

## Usage
**Installation:**

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/tkinter-password-manager.git
Navigate into the project directory:
bash
Copy code
cd tkinter-password-manager

**Dependencies:**
Python 3.x
Tkinter (usually included with Python distributions)
cryptography library (install via pip if not already installed):
Copy code
pip install cryptography

**Run the Application:**
Execute the main script:
Copy code
python password_manager.py
Functionality:

**Save Credentials:** Enter credentials and press 'Save' to encrypt and store them.
**Retrieve Credentials:** Use the search feature to find stored credentials.
**Generate Password:** Click 'Generate Password' for a strong, randomized password.
**Add Entry:** Expand data storage by adding new entries.

# Security Note:
Ensure you remember your encryption key. Access is restricted after five unsuccessful attempts.
Avoid using a four-digit encryption key (e.g., birth year) for security reasons.

# Contributing
Contributions are welcome! Feel free to fork the repository, create a pull request, or open issues for feature requests or bug reports.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
Special thanks to the Tkinter community and contributors for their excellent resources and support.
