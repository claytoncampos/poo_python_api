from fastapi import FastAPI, Query
import requests
import urllib3


app = FastAPI()


@app.get("/api/hello")
def hello_world():
    """
    Endponit que exibe mensagem basica da programação
    """
    return {"Hello": "World"}


@app.get("/api/restaurantes/")
def get_restaurantes(restaurante: str = Query(None)):
    """
    Endpoint para visualizar os cardápios dos Restaurantes.

    """
    url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

    urllib3.disable_warnings()
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        dados_json = response.json()
    if restaurante is None:
        return {"Dados": dados_json}

    dados_restaurante = []
    for item in dados_json:
        if item["Company"] == restaurante:
            dados_restaurante.append(
                {
                    "item": item["Item"],
                    "price": item["price"],
                    "description": item["description"],
                }
            )
        return {"Restaurante": restaurante, "Cardapio": dados_restaurante}

    else:
        return {"Erro": f"{response.status_code} - {response.text}"}
