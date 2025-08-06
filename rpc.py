from xmlrpc import client as xmlrpclib

url="http://localhost:8069/"
username="admin"
pwd="admin"
dbname="gapOdoo_db"

common=xmlrpclib.ServerProxy(url + "/xmlrpc/common")
uid=common.login(dbname,username, pwd)
print(uid)


model=("res.partner")
       # product.template  "res.users"
search=[]
method="search"

operation=xmlrpclib.ServerProxy(url +  "/xmlrpc/object")
list_of_partner_ids=operation.execute(dbname,uid,pwd,model,  method,search)
#print(list_of_partner_ids)
#print(len(list_of_partner_ids))
method="read"
list_of_partner_ids=operation.execute(dbname,uid,pwd,model,  method,list_of_partner_ids)
#print(list_of_partner_ids)

for customer in  list_of_partner_ids:
    print(customer['id'],customer['name'],customer['email'])