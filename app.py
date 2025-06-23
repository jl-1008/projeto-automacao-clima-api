import requests  # Biblioteca para fazer requisições HTTP

# Função que busca os dados do clima de uma cidade
def obter_clima(cidade):
    chave_api = "726b811a5ad65da89dc4b2ec1f511afc"  # Substitua pela sua chave da API do OpenWeather
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave_api}&lang=pt_br&units=metric"

    print(f"🔍 URL gerada: {url}")  # Exibe a URL gerada para depuração
    
    resposta = requests.get(url)  # Envia uma requisição GET para a URL da API

    if resposta.status_code == 200:
        dados = resposta.json()  # Converte a resposta JSON em um dicionário Python
        print(f"\n📍 Cidade: {dados['name']}")
        print(f"🌡️ Temperatura: {dados['main']['temp']}°C")
        print(f"☁️ Clima: {dados['weather'][0]['description']}")
    else:
        print("⚠️ Erro ao obter dados do clima. Verifique o nome da cidade ou a chave da API.")

# Código principal: só será executado se o arquivo for rodado diretamente
if __name__ == "__main__":
    cidade = input("Digite o nome da cidade: ")  # Pergunta ao usuário a cidade
    obter_clima(cidade)  # Chama a função para buscar o clima


