import requests
from bs4 import BeautifulSoup

url = "https://www.edicoescnbb.com.br/lancamentos"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10136"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')


nome_produto = soup.find_all('div', class_='info-product')

print(f"Produtos encontrados: {len(nome_produto)}")

if nome_produto:
    produto = nome_produto[0]


    print(produto.prettify())


    marca = produto.find('div', class_='product-name')
    if marca:
        marca_text = marca.get_text(strip=True)
    else:
        marca_text = "Marca não encontrada"

    preco = produto.find('span', class_='price-off')
    if preco:
        preco_text = preco.get_text(strip=True)
    else:
        preco_text = "Preço não encontrado"

    print(f"Produto: {marca_text}")
    print(f"Preço: {preco_text}")

else:
    print("Produto não encontrado")
