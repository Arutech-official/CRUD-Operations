import json
import requests
BASE_URL ="http://127.0.0.1:8000/"
ENDPOINT ="api/"

# def get_resource(id=None):
#     data={}
#     if id is not None:
#             data={
#                 'id': id,
#             }
#     resp=requests.get( BASE_URL+ENDPOINT, data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource(4)
# def create_resource():
#     new_emp={
#         'eno':106,
#         'ename':'Dhoni',
#         'esal':1000000000,
#         'eaddr':'Rachi',
#     }
#     resp = requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

# def update_resource(id):
#     new_emp={
#         'id':id,
#         'eno':104,
#         'esal':5000000,
#         'eaddr':'Mumbai',
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(5)

def delete_resource(id):
    data = {
        'id':id,

    }
    resp =requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(5)