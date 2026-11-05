# Personal book manager
![Static Badge](https://img.shields.io/badge/Python-blue)
  
A simple book manager built with python

## Features
- Add multiple tasks
- Show books
- Save books
- Admin mode

## Requirements
- python
- python-dotenv

## Installation
Install the required packages

```bash
python -m pip install -r reqirements.txt
```

## Environment Setup
Create an `.env` file in the project folder

Use `.env.example` as a template

Add your admin password
```env
BOOK_MANAGER_ADMIN_PASSWORD = "your_password"
```
Replace `your_password` with your admin password

## Run the programe
Run the main file
```bash
python main.py
```
## Project Structure
```
personal_book_manager/
│   .env.example
│   .gitignore
│   books.json
│   main.py
│   README.md
│   requirements.txt
│   tempCodeRunnerFile.py
│
├───Images
│       ScreenShot1.png
│
```

## Screenshot
![Screenshot](Images\ScreenShot1.png)

## How it Works

- Get user's name
- Admin mode
- Add new books 
- show books

## Troubleshooting

1. FileNotFoundError

- What does the error mean? It means that the program cannot find the file it is trying to open.
- Why might it happen? The file may not exist, or its path may be incorrect.
- What do you have to check first? check whether the file exists in the correct directory and whether its name is spelled correctly.

2. JSONDecodeError

- What does the error mean? It means that Python cannot read the data inside the `JSON file`.
- Why might it happen? The `books.json` file might be empty or contain incorrectly formatted JSON data.
- What do you have to check first? open `books.json` and check whether it contains valid JSON data and has the correct structure.

3. python-dotenv ModuleNotFoundError

- What does the error mean? It means that Python cannot find the `python-dotenv` library.
- Why might it happen? The library may not be installed, or it may have been installed in a different Python environment.
- What do you have to check first?  run ```pip show python-dotenv``` to check whether the library is installed.

4. Password Not Being Read from ".env"

- What does the error mean? It means that the program cannot retrieve the password stored in the `.env` file.
- Why might it happen? The variable name might be incorrect, the `.env` file might be in the wrong directory, or ```load_dotenv()``` might not have been called.
- What do you have to check first? check that the `.env` file is in the correct location and that the variable name matches the one used in the Python code.
