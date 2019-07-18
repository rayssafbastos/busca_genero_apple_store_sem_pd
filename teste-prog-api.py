import json, requests

# ************ Obtendo Dados ************




#response = requests.get("http://jsonplaceholder.typicode.com/comments")  #busca o arquivo json com as informações
#print (response.status_code)
#print (response.content)

#comments = response.json()    #transforma as strings do json em objetos pra manusear no código
#print (comments[0]['body'])


#para listar os 10 primeiros comments

#for comment in comments[0:10]:         
#    print (comment['name'])



#para obter um objeto específico

#response = requests.get("http://jsonplaceholder.typicode.com/comments/1")
#print(response.content)
#comment = response.json()
#print (comment['name'])

# Se quisermos descobrir a qual post que o comment acima se refere

#post = requests.get("http://jsonplaceholder.typicode.com/posts/%d" % comment['postId'])
#print (post.content)
#post = post.json()
#print (post)
#print (post['title'])



# ************ Inserindo Dados ************


#dados = data={"postId": 1, "name": "John Doe", "email": "john@doe.com", "body": "This is it!"}
#response = requests.post("http://jsonplaceholder.typicode.com/comments/", data=dados)
#print (response.status_code)
#print (response.content)



# ************ Alterando Registros ************
#alterar o campo email do comentário de id 10

#dados = {"email": "john@doe.com"}
#response = requests.put("http://jsonplaceholder.typicode.com/comments/10", data=dados)
#print( response.status_code)



# ************ Removendo Registros ************
#Para apagar o comment de id 10, utilizamos a função delete da requests

#response = requests.delete("http://jsonplaceholder.typicode.com/comments/10")
#print( response.status_code)


# ************ Acessando recursos aninhados ************
# Para obter todos os comments relacionados ao post de id 2


#response = requests.get("http://jsonplaceholder.typicode.com/posts/2/comments")
#print (response.content)


#Apesar dessas diferenças entre uma API e outra, o mecanismo de acesso às mesmas não muda. 
# Você vai precisar de uma biblioteca para emitir requisições HTTP (requests ou urllib2) 
# e uma biblioteca para fazer a decodificação dos dados retornados (json, simplejson ou 
# alguma biblioteca para manipulação de XML).