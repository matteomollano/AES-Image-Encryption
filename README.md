# How to Run/View this App:

1. Clone the github repository using `git clone [url]`

2. Ensure that you have Python3 installed. Use `python3 --version` in a terminal window to check for installation. <br>
If Python3 is not installed, download it here: https://www.python.org/downloads/

3. Install Flask Framework using `pip install Flask`

4. Create a Flask Virtual Environment for your project. <br>
cd to the root folder of the repository and run the following command: <br>
`python3 -m venv [environment name of your choice]` <br>
Ex: `python3 -m venv flask`

5. Run the following command in the terminal to ensure that Flask has been installed: `ls -ltr`

6. Activate the Flask Virtual Environment by running `. flask/bin/activate` in the terminal. <br>
Use `deactivate` to exit the environment.

7. Install the Crypto library for this project using `pip install pycryptodome`

8. Type `python3 app.py` in the terminal to run the project. <br>

9. To view the website, type `127.0.0.1:5000` into a browser of your choice. This will take you to the home page of the website.


# How to set up an .env (environment variable):

1. Generate a random secret key using `python3 -c 'import os; print(os.urandom(32).hex())'`

2. Install the python-dotenv module using `pip install python-dotenv`

3. Create a new file in your app directory called `.env`

4. Add the line `SECRET_KEY = 'add your secret key here...'` to the `.env` file

5. Ensure that your app.py file contains the following: <br>
`from dotenv import load_dotenv` <br>
`import os` <br>
`load_dotenv()` <br>
`app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')`