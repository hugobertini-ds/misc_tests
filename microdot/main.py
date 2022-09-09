from microdot import Microdot 
from customers import customers_app 


def create_app(): 
    app = Microdot() 
    app.mount(customers_app, url_prefix='/<re:customers.*:name>') 
    return app 


app = create_app() 
app.run(port=8080)
