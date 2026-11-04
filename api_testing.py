import os

import requests
from dotenv import load_dotenv
load_dotenv()
url = os.getenv("URL")
parameter = {"id":10}
tim= 10

try:
    # # fetch
    # response= requests.get(f"{url}/users", params= parameter, timeout=tim)
    # response.raise_for_status()
    # data = response.json()
    # for x in data:
    #     # for y in x:
    #     #     print(y)
    #     print(x)
    # # print(data)


    # insert
    user = {
            "name":" 'Clementina DuBuque'",
            'username': 'Moriah.Stanton',
            'email': 'Rey.Padberg@karina.biz',
            'address': '-38.2386 57.2232',
            'phone': '024-648-3804', 'website': 'ambrose.net',
            'company': 'Hoeger LLC, Centralized empowering task-force ,target end-to-end models'
            }
    response = requests.post(url=f"{url}/users", data=user,timeout=tim)
    print(response.json())
    print(response.status_code)

    # update(patch)
    user = {
        "name": 'Clementina DuBuque',
        'username': 'Moriah.Stanton',
        'email': 'Rey.Padberg@karina.biz',
        'address': '-38.2386 57.2232',
        'phone': '024-648-3804', 'website': 'ambrose.net',
        'company': 'Hoeger LLC, Centralized empowering task-force ,target end-to-end models'
    }

    response.raise_for_status()



except requests.exceptions.RequestException as error:
    print("user error:",error)
except ValueError as e:
    print("value error: ",e)