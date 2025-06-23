# import requests


# # Substitua pelo sua chave de API
# chave_api = "726b811a5ad65da89dc4b2ec1f511afc"



# # Cidade que vamos testar 
# cidade = "Recife"


# # Construindo a URL da requisição

# url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
#   # DEBUG

# #Fazendo a requisição GET à API

# resposta = requests.get(url)

# # Verificando seu deu tudo certo (código 200)

# if resposta.status_code == 200:
#     dados = resposta.json() # Converte o retorno JSON para dicionário Python
#     print(f"Clima em {cidade}: {dados['weather'][0]['description'].capitalize()}")
#     print(f"Temperatura: {dados['main']['temp']}°C")
# else:
#     print("Erro ao obter dados da API:", resposta.status_code)    


import requests

def obter_clima(cidade):
    chave_api = "726b811a5ad65da89dc4b2ec1f511afc"  # Substitua pela sua chave real da OpenWeather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"
    
    print(f"🔍 URL gerada: {url}")  # <- Adiciona isso antes da requisição

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"🌤️ Clima em {cidade}: {dados['weather'][0]['description'].capitalize()}")
        print(f"🌡️ Temperatura: {dados['main']['temp']}°C")
    else:
        print("⚠️ Erro ao obter dados do clima. Verifique o nome da cidade ou a chave da API.")

if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")
    obter_clima(cidade)
