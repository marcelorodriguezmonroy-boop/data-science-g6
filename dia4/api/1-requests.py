import requests
from tabulate import tabulate

    

URL = 'https://randomuser.me/api/?nat=es&results=5' 

response = requests.get(URL)

if response.status_code == 200:
    print('conexión a api exitosa')
    data = response.json()
    rows = []
    for dic_user in data['results']:
        nombre = dic_user['name']['first'] + ' ' + dic_user['name']['last']
        pais = dic_user['location']['country']
        email = dic_user['email']
        telefono = dic_user['phone']
        foto = dic_user['picture']['large']
        rows.append([nombre, pais, email, telefono, foto])
    headers = ['Nombre', 'País', 'Email', 'Teléfono', 'Foto']
    print(tabulate(rows,headers=headers, tablefmt='grid'))


else:
    print(f'{response.status_code} error en la conexión a la api')