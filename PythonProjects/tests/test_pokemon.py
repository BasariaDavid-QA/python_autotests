import  requests
import pytest 

token = '8be11293fbe29b21f0f452277cdf76fb'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    respons = requests.get(f'{host}/trainers', params = {"trainer_id": 3219})
    assert  respons.status_code == 200
