import requests
import urllib3
import json

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

urllib3.disable_warnings()
response = requests.get(url, verify=False)

"""
[
    {
        "Company":"McDonald’s",
        "Item":"Hamburger",
        "price":32.42,
        "description":"Uma explosão de sabores em cada mordida."
    },
    {
        "Company":"McDonald’s",
        "Item":"Cheeseburger",
        "price":38.81,
        "description":"Uma opção saudável e equilibrada."
    },
"""

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    """
    Caso a resposta seja 200, indicando o sucesso da requisição,
    crie um que código percorre cada item nesse objeto, que representa um restaurante.
    Durante esse processo, extraia dados específicos, como o nome do restaurante nome_do_restaurante,
    o item oferecido, o preço price, e a descrição description, como mostra o código abaixo:
    """
    for item in dados_json:
        nome_do_restaurante = item["Company"]
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append(
            {
                "item": item["Item"],
                "price": item["price"],
                "description": item["description"],
            }
        )
else:
    print(f"O erro foi {response.status_code}")
"""
Para finalizar, crie um arquivo .json para cada restaurante:
"""
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f"{nome_do_restaurante}.json"
    with open(nome_do_arquivo, "w", encoding="utf8") as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
