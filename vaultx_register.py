import os
import winreg as reg

# Define file type and application details
file_type = "VaultX File"
extension = ".vaultx"
app_path = os.path.abspath("vaultx.exe")  # Path to your executable
icon_path = os.path.abspath("vaultx.ico")  # Path to your icon file

def register_file_association():
    """Register the VaultX file association and context menu entries."""


    # Create the registry entries for the file type
    try:
        # Create the file type key
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, extension) as key:
            reg.SetValue(key, "", reg.REG_SZ, file_type)

        # Create the file type description key
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, file_type) as key:
            reg.SetValue(key, "", reg.REG_SZ, "VaultX Encrypted File")
            reg.SetValue(key, "Icon", reg.REG_SZ, icon_path)

        # Create the command key for opening files
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, f"{file_type}\\shell\\open\\command") as key:
            reg.SetValue(key, "", reg.REG_SZ, f'"{app_path}" "%1"')

        print(f"{extension} files are now associated with {app_path}.")
    except Exception as e:
        print(f"Failed to register file association: {e}")

def add_context_menu_entry():
    """Add context menu entries for encryption and decryption."""
    # Define the keys for encryption and decryption with the appropriate flags
    keys = {
        "VaultX Encrypt": f'"{app_path}" --enc "%1"',
        "VaultX Decrypt": f'"{app_path}" --dec "%1"'
    }

    for entry_name, command in keys.items():
        try:
            # Create the shell key for each entry
            shell_key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, f'*\\shell\\{entry_name}')
            reg.SetValue(shell_key, '', reg.REG_SZ, entry_name)  # Set the display name

            # Create the command key
            command_key = reg.CreateKey(shell_key, 'command')
            reg.SetValue(command_key, '', reg.REG_SZ, command)  # Set the command to execute

            # Optionally set an icon for the context menu entry
            if icon_path:
                reg.SetValue(shell_key, 'Icon', reg.REG_SZ, icon_path)

            print(f'Added context menu entry: {entry_name}')
        except Exception as e:
            print(f'Failed to add entry "{entry_name}": {e}')

if __name__ == "__main__":
    register_file_association()
    add_context_menu_entry()
