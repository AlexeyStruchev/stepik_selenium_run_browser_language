# stepik_selenium_run_browser_language
This is a tutorial project from stepic course https://stepik.org/course/575/syllabus:
"Test automation with Selenium and Python".

The project purpose is to send a language information for a browser 
in accept-language header in order a server can determine which page language
must be returned.

The lesson is: https://stepik.org/lesson/237240/step/10?unit=209628

## Automated libraries installation
After cloning the project from git, all necessary libraries can be installed in
console by using the command:

pip install -r requirements.txt

## Tests execution in console 
For all tests a Chrome browser is used. 
Run commands in console by using a language parameter
### Spanish
pytest --language=es test_items.py
### English
pytest --language=es test_items.py
### Russian
pytest --language=es test_items.py
### Without any parameters a default English language is used
pytest test_items.py
 
