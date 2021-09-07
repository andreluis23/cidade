from src.classes.Cidade import Cidade, cidade, nome, uf

sair = False

arquivo = open("./src/bd/bd.json",'r')
lista_cidade = json.loads(arquivo.read())
arquivo.close()



while sair == False:
    nome_cidade = input("Digite o nome da cidade: ") 
    populacao_cidade = input("Digite a população: ") 
    sigla_estado = input("Digite a sigla do estado: ") 
    nome_estado = input("Digite o nome do estado: ") 

    uf = {"sigla": sigla_estado, "nome": nome_estado}
    nova_cidade = Cidade(nome_cidade, populacao_cidade, )

    
    lista_cidade.append({
        "nome":nova_cidade.nome, 
        "populacao": nova_cidade.populacao,
        "uf":{
            "sigla": nova_cidade.uf["sigla"],
            "sigla": nova_cidade.uf["sigla"],
        }
    })

    resposta = input("Deseja cadastrar outra cidade? S/N")

    resposta__incorreta = resposta.upper() != "S" and resposta.upper() != "N"
    while resposta__incorreta:

        print("A resposta deve ser S ou N")
        resposta = input("Deseja cadastrar outra cidade? S/N")
    if resposta.upper() == "N":
        sair = True

arquivo = open("./src/bd/bd.json", 'w')
arquivo.write(json.dump(lista_cidade))
arquivo.close()
