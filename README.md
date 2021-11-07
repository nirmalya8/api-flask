# Creating and Testing an API in Python using Flask
Creating and Testing APIs in Python using Flask

# How to run this code?

Step 1: Clone the repository and enter into the directory. 


Step 2: Create a virtual environment using `pipenv` (Installation: pip install pipenv) and grab a shell using `pipenv shell`. 


Step 3: Install the required packages using: `pip install -r requirements.txt` 


Step 4: To check out the API, the `app.py` file needs to be run using `python app.py` or `python3 app.py`, depending on your Python version. The link in the terminal is to be opened and the available routes are to be checked before running them. 


Step 5: If you are interested to run the tests as well, you can run `pytest test.py` in the terminal. But, before running the tests, you have to make sure that your app is running otherwise it will give a connection error. A good way to achieve this would be to use two separate terminals. One for running the app and another for running the `pytest` command. //

# Available Routes
1. `'/'` : The initial route, which just returns a Hello World Message
2. `'/showmenu'` : Route to show the menucard
3. `'/order/<int: id>'`: Route to order item `id` from the menucard. Can order a certain item any number of times.
4. `'/show'`: Route to show current orders
5. `'/delete/<int: id>'`: Route to delete item `id` from the list of orders returned by `'/show'`


