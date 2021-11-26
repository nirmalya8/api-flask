# Creating and Testing an API in Python using Flask
There are two API files, namely `app.py` and `restructured_app.py`. Both of these containt the same API, but implemented in different ways and can be run in different ways. `app.py` contains a more elaborate approach, with routes for each and every task. 

`restructured_app.py` shows a minimalistic approach, keeping in mind the best practices of creating APIs. The main goal was to reduce the number of routes and focusing on including all requests under the same route. 

Running both these files will yield similar results, but the procedure for running will be different. 

# How to run this code?

The first three steps to run the app will be the same for both files.
Step 1: Clone the repository and enter into the directory. 


Step 2: Create a virtual environment using `pipenv` (Installation: pip install pipenv) and grab a shell using `pipenv shell`. 


Step 3: Install the required packages using: `pip install -r requirements.txt` 

To run `app.py`:


Step 4: To check out the API, the `app.py` file has to be run using `python app.py` or `python3 app.py`, depending on your Python version. The link in the terminal is to be opened and the available routes are to be checked before running them. 


Step 5: If you are interested to run the tests as well, you can run `pytest test.py` in the terminal. But, before running the tests, you have to make sure that your app is running otherwise it will give a connection error. A good way to achieve this would be to use two separate terminals. One for running the app and another for running the `pytest` command. 

To run `restructured_app.py`:


Step 4: The cuRL command helps us in running this file. We send the data as JSON payloads and run it from the terminal, while the file `restructured_app.py` is running. It can also be run from another python file by using the cuRL command in Python. The cuRL commands are given under the available routes section. 

# Available Routes
For `app.py`: <br />
        1. `'/'` : The initial route, which just returns a Hello World Message <br />
        2. `'/showmenu'` : Route to show the menucard <br />
        3. `'/order/<int: id>'`: Route to order item `id` from the menucard. Can order a certain item any number of times. <br />
        4. `'/show'`: Route to show current orders <br />
        5. `'/delete/<int: id>'`: Route to delete item `id` from the list of orders returned by `'/show'` <br />
        6. `'/price'` : Route to show the total price of items ordered <br />
        7. `'/additem'` : Route to add an item into the menu (PUT) <br />
        8. `'/delitem'` : Route to delete an item from the menu (DELETE) <br />

For `restructured_app.py`: <br />
1. `'/'`: Returns a hello world message. It can be run using:
```
curl -X GET http://127.0.0.1:5000/
```
2. `'/showmenu'`: Returns the menucard as a JSON. It can be run using:
```
curl -X GET http://127.0.0.1:5000/showmenu
```
3. `'/orders'` : This route can handle 4 requests. <br />
 a. GET Request: Running the GET request for this route will return the list of orders. It can be run using the following curl command: 
 
 
        
        curl -X GET http://127.0.0.1:5000/orders
        
        
 b. POST Request: This request can be used to add an item into the menucard by giving its id in the menucard. It can be run using: 
       
        
        curl -H "Content-Type: application/json" --request POST -d '{"id":2}' http://127.0.0.1:5000/orders
        
        
 c. PUT Request: This request will be used to add an item into the menucard. The input JSON has to be of the format of an item JSON in the Menucard. It can be run using: 
        

        curl -H "Content-Type: application/json" --request PUT -d '{"item1":{"Item" : "Curd", "Price":10}}' http://127.0.0.1:5000/orders

        
 d. DELETE Request: This request is used to delete an item from the menucard, given its id in the menucard. It can be run using: 
        
        

        curl -H "Content-Type: application/json" --request DELETE -d '{"id":1}' http://127.0.0.1:5000/orders



NOTE: Be aware of the double quotes "" and single quotes '', as these might cause errors if changed.
