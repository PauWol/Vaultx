# VaultX: A Simple File Encryption Tool

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [API Documentation](#api-documentation)

## Introduction

VaultX is a simple file encryption tool that uses the Fernet symmetric encryption algorithm from the cryptography library. It provides a command-line interface (CLI) and a graphical user interface (GUI) for encrypting and decrypting files.

## Features

- Symmetric encryption: Uses the Fernet algorithm for symmetric encryption.
- Password-based encryption: Uses a password to generate a key for encryption and decryption.
- File encryption: Encrypts files with a `.vaultx` extension.
- File decryption: Decrypts files with a `.vaultx` extension.
- GUI and CLI support: Provides both a graphical user interface and a command-line interface.
- Automatic decryption: Prompts for decryption when double-clicking a .vaultx file.
## Usage

### Command-Line Interface (CLI)

To encrypt a file, run the following command:

```bash
vaultx --encrypt path/to/file.txt --key mypassword --no-ui
```
To decrypt a file, run the following command:

```bash
vaultx --decrypt path/to/file.txt.vaultx --key mypassword --no-ui
```

### Graphical User Interface (GUI)

To encrypt a file, run the following command:

```bash
vaultx --encrypt path/to/file.txt
```

To decrypt a file, run the following command:

```bash
vaultx --decrypt path/to/file.txt.vaultx
```

Note: If you want to use the Python files, you will need to adjust the commands. For example, if you want to use the Python files, you can run:

```bash
python vaultx.py --encrypt path/to/file.txt --key mypassword --no-ui
```
```bash
python vaultx.py --decrypt path/to/file.txt.vaultx --key mypassword --no-ui
```
```bash
python vaultx.py --encrypt path/to/file.txt
```
```bash
python vaultx.py --decrypt path/to/file.txt.vaultx
```

### Automatic Decryption

Also, if you want to automatically prompt for decryption when double-clicking a .vaultx file, you can run the vaultx_register file as an administrator.
This will associate the .vaultx files with the vaultx script, and double-clicking a .vaultx file will automatically prompt for decryption.

Note: If you want to use the Python files, you will need to adjust the commands in the vaultx_register to match the vaultx.py script.

For bash:
```bash
vaultx_register
```
or for python:
change this line in the vaultx_register.py file:
```python
app_path = os.path.abspath("vaultx.exe")  # Path to your executable
```
to this:
```python
app_path = os.path.abspath("vaultx_register.py")  # Path to your python script
```
## Installation

To install VaultX, run the following command:

```bash
vaultx_register
```
or for python:
```bash
python vaultx_register.py
```
Note: In order to run this script successfully you will need to run it as an administrator.
