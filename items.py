from utils import Utils

data = Utils.read_from_json('data/items.json')
items, metodos, admins = data['items'], data['metodos'], data['admins']
