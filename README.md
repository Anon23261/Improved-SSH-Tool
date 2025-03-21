# SSH Penetration Testing Tool

This Python tool utilizes the Paramiko library to perform various SSH penetration testing tasks, including brute-forcing, command execution, and interactive shell access. It is designed for use in authorized penetration testing scenarios, where explicit permission has been granted.

## Features

* **SSH Brute-Forcing:**
    * Attempts to brute-force SSH credentials using a provided password list.
    * Implements threading for faster execution (with rate limiting).
    * Includes timeouts to prevent indefinite hangs.
    * Provides detailed logging of attempts and results.
* **SSH Command Execution:**
    * Executes commands on the remote machine and displays the output.
    * Logs command execution and results.
* **Interactive SSH Shell:**
    * Provides an interactive shell for more complex command execution.
    * Allows for more interactive post-exploitation.
* **Logging:**
    * All actions are logged to `ssh_pentest.log` for auditing and reporting.
    * Detailed logging of errors.
* **Error Handling:**
    * Robust error handling to manage connection failures and other exceptions.
* **Rate Limiting:**
    * Rate limiting is implemented to prevent account lockouts.

## Requirements

* Python 3.x
* Paramiko library (`pip install paramiko`)

## Usage

1.  **Installation:**
    * Clone the repository or download the Python script.
    * Install the required dependencies: `pip install paramiko`.

2.  **Configuration:**
    * Create a password list file (e.g., `passwords.txt`).
    * Modify the example usage in the script to match your target machine's details.

3.  **Execution:**
    * Run the Python script: `python your_script_name.py`.
    * The script will log all activity to `ssh_pentest.log`

### Example Usage

```python
# Example usage (replace with target details)
#ssh_brute_force("target_machine", "testuser", "passwords.txt")
#ssh_command("target_machine", "testuser", "testpass", "whoami")
#ssh_interactive_shell("target_machine", "testuser", "testpass")
