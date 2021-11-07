from flask import Flask, json, jsonify
app = Flask(__name__) 

menucard = [{'Item' : 'Rice', 'Price':10},{'Item': 'Dal','Price':15},{'Item':'Chicken','Price':20},{'Item':'Mutton', 'Price':25},{'Item':'Fish','Price':20},{'Item':'IceCream','Price':10}]
orders = []

@app.route('/') 
def hello_world():
    response = jsonify('Hello world!')
    response.status_code = 200
    return response

@app.route('/order/<int:id>',methods=['GET','POST'])
def take_orders(id):
    response = {}
    if id<len(menucard) and menucard[id] not in orders:
        d = menucard[id]
        d['Quantity'] = 1
        orders.append(d)
        response = jsonify({'Status':'Added','Item':d})
        response.status_code = 200
    elif id>= len(menucard):
        response = jsonify({'Status': 'Not in menu'})
        response.status_code = 404
    elif menucard[id] in orders:
        for i in orders:
            if i['Item'] == menucard[id]['Item']:
                i['Quantity']+=1
        response = jsonify({'Status': 'Updated quantity','Item':menucard[id]})
        response.status_code =200
    print(f"Orders = {orders} ")
    return response

@app.route('/show',methods=['GET'])
def show_orders():
    response = ' '
    if len(orders)==0:
        response = jsonify({'Your orders':'Haven\'t ordered anything yet'} )
        response.status_code = 404
    else :
        response = jsonify({'Your orders':orders})
        response.status_code = 200
    return response

@app.route('/delete/<int:delid>',methods=['GET','POST'])
def delete_order(delid):
    response = {}
    if(delid<len(orders) and delid>=0):
        for i in range(len(orders)):
            if i == delid:
                orders[i]['Quantity']-=1
    
        for i in orders:
            if i['Quantity'] == 0:
                orders.remove(i)
        response = jsonify({'Status':'Successfully Deleted'})
        response.status_code = 200
    else:
        response = jsonify({'Status':'Wasn\'t in the menu'})
        response.status_code = 404
    print(f"Orders = {orders}")
    return response
            
if __name__ == "__main__":
    app.run(debug=True)

