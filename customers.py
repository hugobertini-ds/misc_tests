from microdot import Microdot 


customers_app = Microdot()


@customers_app.get('') 
def get_customer(request, name): 
    nm = name.replace('..', '').replace('customers', '').replace('/', '')
    if len(nm) > 0:
       # return one customer
       print('get customer details: ' + nm)
       #return send_file('/static/index.html')
       return 'get customer details: ' + nm, 202
    else:
       return get_customers()


def get_customers(): 
    # return all customers 
    print('get customers')
    #return send_file('/static/index.html')
    return 'get customers list', 202
    
    
#@customers_app.get('<name>') 
#def get_customer(request, name): 
#    print('Customer: ' + name)
#    #return send_file('/static/index.html')
#    return 'Customer: ' + name, 202


@customers_app.post('') 
def new_customer(request): 
    # create a new customer
    print('new customer')    
    return 'new customer', 202