import requests

token = '8be11293fbe29b21f0f452277cdf76fb'
host = 'https://api.pokemonbattle.me:9104'

response = requests.post(f'{host}/pokemons', json = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
},headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token } ) 

response_activation = requests.put ( f'{host}/pokemons', json = {
    "pokemon_id": "18038",
    "name": "Popa",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token } )

response_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "18038"
},headers = {'Content-Type'  :  'application/json',
               'trainer_token' : token })

print(response_pokeball.text)