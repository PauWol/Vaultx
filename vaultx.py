import base64
import hashlib
import os
import click
import json
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet, InvalidToken

def generate_key(password: str) -> bytes:
    """Generate a key from the given password."""
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def read_file(file_path: str) -> bytes:
    with open(file_path, 'rb') as file:
        return file.read()

def write_file(file_path: str, content: bytes):
    with open(file_path, 'wb') as file:
        file.write(content)

def encrypt_file(file_path: str, password: str):
    """Encrypt the file at file_path using the given password and save as a .vaultx file."""
    return_message = {
        "file_path": file_path,
        "password": password,
        "success": False,
        "error": "",
        "encrypted_file_path": ""
    }

    try:
        key = generate_key(password)
        fernet = Fernet(key)
        encrypted = fernet.encrypt(read_file(file_path))

        # Save the encrypted file with the .vaultx extension
        encrypted_file_path = file_path + '.vaultx'
        write_file(encrypted_file_path, encrypted)

        # Optionally delete the original file
        os.remove(file_path)
    except Exception as e:
        return_message["error"] = str(e)
        return return_message

    return_message["success"] = True
    return_message["encrypted_file_path"] = encrypted_file_path
    return return_message

def decrypt_file(file_path: str, password: str):
    """Decrypt the file at file_path using the given password and replace with the original file."""
    return_message = {
        "file_path": file_path,
        "password": password,
        "success": False,
        "error": "",
        "encrypted_file_path": ""
    }

    try:
        key = generate_key(password)
        fernet = Fernet(key)
        decrypted = fernet.decrypt(read_file(file_path))

        # Replace the encrypted file with the original content
        original_file_path = file_path.replace('.vaultx', '')
        write_file(original_file_path, decrypted)

        # Optionally delete the encrypted file
        os.remove(file_path)
    except InvalidToken:
        return_message["error"] = "Invalid key or the file may be corrupted. Decryption failed."
        return return_message
    except Exception as e:
        return_message["error"] = str(e)
        return return_message

    return_message["success"] = True
    return return_message

def process_file(app, file_path, password, mode):
    """Function to encrypt or decrypt a file based on the mode."""
    if not os.path.exists(file_path):
        messagebox.showerror("Error", "File does not exist.")
        return

    if mode == 'encrypt':
        result = encrypt_file(file_path, password)
    else:  # mode == 'decrypt'
        result = decrypt_file(file_path, password)

    if result["success"]:
        messagebox.showinfo("Success", f"File processed successfully.\nEncrypted File: {result['encrypted_file_path']}")
        app.quit()  # Close the application only if successful
    else:
        messagebox.showerror("Error", result["error"])

def run_ui(file_path=None, mode='decrypt'):
    """Run the Tkinter UI."""
    app = tk.Tk()
    app.title("VaultX " + mode.capitalize())
    app.geometry("300x200")
    app.resizable(False, False)

    try:
        app.iconbitmap("vaultx.ico")
    except Exception as e:
        print(f"Could not set icon: {e}")

    label_text = "Password for Decryption:" if mode == 'decrypt' else "Password for Encryption:"
    tk.Label(app, text=label_text).pack(pady=(20, 5))

    password_entry = tk.Entry(app, width=40, show='*')
    password_entry.pack(pady=(0, 20))
    password_entry.focus()  # Set focus to the password entry

    button_text = "Decrypt" if mode == 'decrypt' else "Encrypt"
    process_button = tk.Button(app, text=button_text, command=lambda: process_file(app, file_path, password_entry.get(), mode))
    process_button.pack(pady=(10, 10))

    def check_password_entry(*args):
        process_button['state'] = 'normal' if password_entry.get() else 'disabled'

    password_entry.bind("<KeyRelease>", check_password_entry)
    password_entry.bind("<Return>", lambda event: process_button.invoke())
    process_button['state'] = 'disabled'

    app.mainloop()

@click.command()
@click.argument('file_path', required=True)
@click.option('--encrypt', '--enc', is_flag=True, help='Encrypt the specified file.')
@click.option('--decrypt', '--dec', is_flag=True, help='Decrypt the specified file.')
@click.option('--key', '--k', 'password', required=False, help='Password used for encryption/decryption (only for no UI mode).')
@click.option('--no-ui', is_flag=True, help='Run without the UI.')
def cli(file_path, encrypt, decrypt, password, no_ui):
    """Command line interface to run the VaultX for encryption or decryption."""
    if encrypt and decrypt:
        raise click.UsageError("Please specify either --encrypt or --decrypt, not both.")

    if no_ui:
        # Password is required only in non-UI mode
        if not password:
            raise click.UsageError("Password is required when running without the UI.")

        mode = 'encrypt' if encrypt else 'decrypt'
        if mode == 'encrypt':
            result = encrypt_file(file_path, password)
        else:
            result = decrypt_file(file_path, password)

        if result["success"]:
            print(f"Success: {result['encrypted_file_path']}")
        else:
            print(f"Error: {result['error']}")
    else:
        # UI mode
        mode = 'decrypt' if not (encrypt or decrypt) else ('encrypt' if encrypt else 'decrypt')
        run_ui(file_path, mode)

if __name__ == "__main__":
    cli()
