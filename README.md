# Password Generator

This script generates random passwords. It allows customization of the password length and the number of passwords to generate. By default, the first password generated is copied to the clipboard.

## Usage

You can run the script from the command line using the following syntax:<br>
```python
python3 generate_password.py [-n NUMBER] [-l LENGTH] [-c]
```


### Options:

- `-n NUMBER`, `--number NUMBER`: Specify the number of passwords to generate. Default is 1.
- `-l LENGTH`, `--length LENGTH`: Specify the length of the passwords. Default is 15.
- `-c`, `--clipboard`: Use this option to prevent copying the first password to the clipboard.

For example, to generate 5 passwords of length 20 and copy the first one to the clipboard, you would run:<br>
```python
python3 generate_password.py -n 5 -l 20
```


And to generate 5 passwords of length 20 without copying to the clipboard:<br>
```python
python3 generate_password.py -n 5 -l 20 -c
```


## Windows/WSL Linux Compatibility

The script uses the `clip.exe` utility to copy the password to the Windows clipboard. This should work both in native Windows environments and within the Windows Subsystem for Linux (WSL).

However, keep in mind that clipboard access in WSL may depend on the specific version and configuration of WSL. In some cases, you might need to manually enable clipboard access or use a different method to copy text to the clipboard.

## Add bash function to call python script
- Add .gen_pass to user root dir`
- Add source ~/.gen_pass to .bashrc or wherever you add user function calls to unix startup file
- Setup venv by issuing `python3 -m venv venv`
- Call function with standard arguments by executing `gen_pass` in terminal (requires venv-folder to run). The first password generated will be copied to clipboard
