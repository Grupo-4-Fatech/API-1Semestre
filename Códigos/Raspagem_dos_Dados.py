import requests
from bs4 import BeautifulSoup as bs

lista = []
youtube = []
raiz = 'https://fatecsjc-prd.azurewebsites.net/api/'

url = 'https://fatecsjc-prd.azurewebsites.net/api/turmas.php'
html = requests.get(url).text
sopa = bs(html, 'html.parser')
semestres = sopa.findAll('a')

#primeiro semestre tem uma estrutura diferente
print ('Processando primeiro semestre, que é diferente')
url = raiz + semestres[0].attrs['href']
html = requests.get(url).text
sopa = bs(html, 'html.parser')
turmas = sopa.findAll('a')
for t in turmas:
  u = raiz + '2020-1/' + t.attrs['href']
  html = requests.get(u).text
  sopa = bs(html, 'html.parser')
  equipes = sopa.findAll('a')
  for e in equipes:
    yt = e.attrs['href']
    print (yt)
    youtube.append(yt)

#agora vamos tratar o segundo e terceiro semestres
for s in semestres[1:]:
  print ('Processando semestre...')
  url = raiz + s.attrs['href']
  html = requests.get(url).text
  sopa = bs(html, 'html.parser')
  links = sopa.findAll('a')
  for link in links:
    yt = link.attrs['href']
    print (yt)
    youtube.append(yt)

#vamos pegar o github dos links do Youtube
for yt in youtube:
  html = requests.get(yt).text
  ini = html.find(r'https://github.com')
  if ini != -1:
    fim = ini
    while html[fim] != '\\' and html[fim] != '"':
      fim = fim + 1
    print (html[ini:fim])
    lista.append(html[ini:fim])

#gitlab
for yt in youtube:
  html = requests.get(yt).text
  ini = html.find(r'https://gitlab.com')
  if ini != -1:
    fim = ini
    while html[fim] != '\\' and html[fim] != '"':
      fim = fim + 1
    print (html[ini:fim])
    lista.append(html[ini:fim])


if lista:
    with open('links.txt', 'a') as file:
        file.writelines('\n'.join(lista))
