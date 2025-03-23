import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'ab16bd7e927b9b15809cd4414e0ad83e'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_regestration = {
    "trainer_token": TOKEN,
    "email": "ayaxx@yandex.ru",
    "password": "Iloveqa1777"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_rename = {
    "pokemon_id": "273823",
    "name": "Переименованный",
    "photo_id": 2
}

body_add_pokell = {
    "pokemon_id": "273823"
}

response = requests.post(url = f'{URL}/trainers/reg' , headers = HEADER, json = body_regestration)
print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers= HEADER, json= body_confirmation)
print(response_confirmation.text)

response_create = requests.post(url = f'{URL}/pokemons', headers= HEADER, json= body_create)
print(response_create.text)
print(response_create.status_code)

pokemon_id = response_create.json()['id']
print(pokemon_id)

message = response_create.json()['message']
print(message)

response_rename = requests.put(url = f'{URL}/pokemons', headers= HEADER, json= body_rename)
print(response_rename.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_add_pokell)
print(response_add_pokeball.text)