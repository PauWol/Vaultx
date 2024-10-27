This document provides instructions for unregistering the `.vaultx` file association and deleting the associated registry keys for the VaultX application.

**Warning**
Be careful while editing the Windows Registry. Deleting or modifying the wrong keys can cause serious system issues. Always back up the registry before making changes.

## Instructions to Unregister VaultX File Association

### Step 1: Open the Registry Editor
Press Win + R on your keyboard to open the Run dialog.
Type `regedit` and press Enter.

### Step 2: Navigate to HKEY_CLASSES_ROOT\.vaultx (Recommended)
In the Registry Editor, expand the folders in the left pane until you reach:
```path
Computer\HKEY_CLASSES_ROOT\.vaultx
```
Right-click on this key and select Delete.

Alternatively, you can use the search function (`Strg + F`) to locate the key. However, we **strongly recommend against** using this method as it may lead to false deletion of other registry keys that could cause system issues.

### Step 3: Navigate to HKEY_CLASSES_ROOT\VaultX File
In the Registry Editor, expand the folders in the left pane until you reach:
```path
Computer\HKEY_CLASSES_ROOT\VaultX File
```
Right-click on this key and select Delete.

### Step 4: Delete Subkeys under HKEY_CLASSES_ROOT*\shell
In the Registry Editor, expand the folders in the left pane until you reach:
```path
Computer\HKEY_CLASSES_ROOT\*\shell
```
Right-click on the `VaultX Decrypt` and `VaultX Encrypt` subkeys and select Delete.

## Important Notes
**Double-check the key name before deleting to avoid accidentally removing other keys that may affect your system's functionality.**
**Backup the Registry**: Before making any changes, it's a good practice to create a backup of your registry settings. You can do this by selecting `File > Export` in the Registry Editor.

## Conclusion
You have successfully unregistered the `.vaultx` file association and removed the associated registry keys for VaultX. If you have any questions or encounter issues, please refer to the official Windows documentation or seek assistance from a knowledgeable source.