# Password Generator

This script generates random passwords. It allows customization of the password length and the number of passwords to generate. By default, the first password generated is copied to the clipboard.

## Usage / Installation
.gen_pass bash script in dotfiles dir may be used to launch script from bash to easily get passwords

You can run the script from the command line using the following syntax:<br>
```python
python3 generate_password.py [-n NUMBER] [-l LENGTH]
```


### Options:

- `-n NUMBER`, `--number NUMBER`: Specify the number of passwords to generate. Default is 1.
- `-l LENGTH`, `--length LENGTH`: Specify the length of the passwords. Default is 12.

For example, to generate 5 passwords of length 20 and copy the first one to the clipboard, you would run:<br>
```python
python3 generate_password.py -n 5 -l 20
```

## Add bash function to call python script
- Add .gen_pass to user root dir`
- Add source ~/.gen_pass to .bashrc or wherever you add user function calls to unix startup file
- Setup venv by issuing `python3 -m venv venv`
- Call function with standard arguments by executing `gen_pass` in terminal (requires venv-folder to run). The first password generated will be copied to clipboard
