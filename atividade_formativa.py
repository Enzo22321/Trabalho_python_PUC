'''
Lista de jogos...
'''
import json
import datetime
data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
def carregar_jogos():
    try:
        with open("games.json", "r",) as arquivo:
            game_list = json.load(arquivo)
        print("Jogos carregados com sucesso!")
        return game_list

    except FileNotFoundError:
        print("Arquivo não encontrado. Criando lista vazia.")
        return []
    except json.JSONDecodeError:
        print("Arquivo corrompido. Criando lista vazia.")
        return []
game_list = carregar_jogos() 
command_list = ("About", "Quit", "Add", "List", "Update", "Delete", "Save", "Load",)
print("Lista de comandos...")
print(command_list)
def salvar_jogos(game_list):
    with open("games.json", "w") as arquivo:
        json.dump(game_list, arquivo, indent=4)
    print("Jogos salvos com sucesso")
def sobre(game_list):
    print("Enzo Yan Wilkosz. Criador desse programa")
def sair(game_list):
    with open("games.json", "w") as arquivo:
        json.dump(game_list, arquivo, indent=4)
    print("Fechando programa...")
def adicionar(game_list):
     try:
        comando_add = input("Quantos jogos voce gostaria de adicionar? ")
        comando_add = int(comando_add)
     except ValueError:
         print("Digite um numero")
         return
     if comando_add == 0 or comando_add < 0:
        print("ERROR: Comando invalido... Digite um número válido.")
     for i in range(1, comando_add + 1):
         name = input("Digite o nome do " + str(i) + "º jogo: ")
         if name.strip() == "":
             print("Nome invalido")
             continue
         if any(g["name"].lower() == name.lower() for g in game_list):
            print("Jogo já existe.")
            continue
         game = {
                "name": name,
                "concluido": False,
                "historico": [],
            }
         game_list.append(game)
         print(f"O jogo {game['name']} foi adicionado!")
def listar(game_list):
    if len(game_list) == 0:
            print("Nenhum jogo encontrado. Tente carregar 'Load' a lista ):")
    else:
        print("Jogos na Lista:")
        for i in range(len(game_list)):
             print(str(i + 1) + ". " + game_list[i]["name"])
def atualizar(game_list):
    updt = input("Qual jogo gostaria de atualizar? : ").strip().lower()    
    for game in game_list:
        if game["name"].strip().lower() == updt:    
            status = input("Jogo foi concluído? (s/n): ")
            if status == "s":
                game["concluido"] = True
                entrada_atualizacao = (data, game["name"], game["concluido"])
                game["historico"].append(entrada_atualizacao)
                print("Jogo atualizado com sucesso!")
                return
    return None                    
def deletar(game_list):
    dlt = input("Qual jogo gostaria de deletar? : ").strip().lower()     
    for game in game_list:
            if game["name"].strip().lower() == dlt:
                found = True
                game_list.remove(game)
                print(f"O jogo {game["name"]} foi deletado!")
                entrada_remocao = (data, game["name"])
                game["historico"].append(entrada_remocao)
                return
    return None
while True:
    try:
        comando = input("Por favor digite um comando: ").strip().lower()
    except KeyboardInterrupt:
        print("Parada forçada!")

    if comando == "about":
        sobre(game_list)
    elif comando == "quit":
        sair(game_list)
        break
    elif comando == "add":
        adicionar(game_list)
    elif comando == "list":
        listar(game_list)
    elif comando == "update":
        atualizar(game_list)
    
    elif comando == "delete":
        deletar(game_list)
    elif comando == "save":
        salvar_jogos(game_list)

    elif comando == "load":
        game_list = carregar_jogos()
    else:
        print("ERROR: Comando não expecififcado... Digite um comando válido.")

print("Até logo!")


