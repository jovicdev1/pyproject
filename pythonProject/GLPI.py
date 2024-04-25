import requests
from bs4 import BeautifulSoup

page = requests.get("http://10.2.0.19/glpi/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=12&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=notold&itemtype=Ticket&start=0&_glpi_csrf_token=d76004ca4bdbc23e1f349b29c5de722aa85f89e995e1f63ac17763ef597bc734&sort%5B%5D=15&order%5B%5D=DESC")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # Obtém o texto que está entre as tags <title>(...)</title>

res = requests.get('http://10.2.0.19/glpi/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=12&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=notold&itemtype=Ticket&start=0&_glpi_csrf_token=d76004ca4bdbc23e1f349b29c5de722aa85f89e995e1f63ac17763ef597bc734&sort%5B%5D=15&order%5B%5D=DESC')

print(res.text)
print(res.status_code)

txt = res.text
status = res.status_code

# Imprima o resultado
print(txt, status)