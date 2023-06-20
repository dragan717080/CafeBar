from subsidiary_functions import read_from_json

data = read_from_json('items.json')
items, metodos, admins = data['items'], data['metodos'], data['admins']
