# email_process

basic email processing fishes out timestamps.

# Brian! 

you should be able to start the virtualenvironment from within this dir with the following command:  
`source /venv/bin/activate`  
once that is up and running to exit use:  
`deactivate`  
to process an email you will need to point to a .eml file.  If you drag an email to your desktop it will show the file as the subject line for example the email you send me is `EDL stuffs.`  An example command would be (again from this dir)   
`./email_process.py -m /path/to/desktop/EDL\ stuffs..eml`

---

example output

`...`  
`32:05:18 - Tammy's vein: ***** 01:32:05:18`   
`33:37:20 - Pride's line: ***** 01:33:37:20`   
`33:52:00 - Pride's line: ***** 01:33:52:00`   
`34:08:15 - Pride's line: ***** 01:34:08:15`   
`34:25:04 - Pride's line: ***** 01:34:25:04`   
`34:41:09 - Pride's line: ***** 01:34:41:09`  

---

# prerequisitis
- eml_parser
- libmagic

to isntall eml_parser `pip install eml_parser[file-magic]`
see [here](https://pypi.org/project/eml-parser/) for more info

to install libmagic use homebrew **NOT PIP**