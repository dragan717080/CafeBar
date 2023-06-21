from utils import Utils

data = Utils.read_from_json('items.json')
items, metodos, admins = data['items'], data['metodos'], data['admins']
