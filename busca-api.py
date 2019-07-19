import json
import requests
from pprint import pprint


def frequencia_do_nome_por_sexo(nome, sexo):
    results = []
    print('buscando {} Genero {}'.format(nome, sexo))
    local = "https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?sexo={sexo}".format(nome=nome, sexo=sexo)
    response = requests.get(local)  #busca o arquivo json com as informações
    contents = response.json()    #transforma as strings do json em objetos pra manusear no código
    if not contents:
        return 0
    
    frequencess = contents[0]['res']

    for i, frequenc in enumerate(frequencess):
    
        x = frequenc['frequencia']
        results.append(x)

    soma_sexo = sum(results)
    return soma_sexo


nomes = ['alex', 'ariel', 'sasha', 'charlie', 'dominique']
dicionario = {}

for i, name in enumerate(nomes):
    total_feminino = frequencia_do_nome_por_sexo(name, 'F')
    total_masculino = frequencia_do_nome_por_sexo(name, 'M')
    total = total_feminino + total_masculino
    dicionario[name] = {
        'Masculino': total_masculino * 100 / total, 
        'Feminino': total_feminino * 100 / total
    }

pprint(dicionario)