# Diário de Bordo de IA - Enzo Yan Wilkosz

# ## [01/04/2026]

# ### Não tinha certeza como checar para números negativos (linha 18 [if comando_add == 0 or comando_add < 0:] foi a solução dada)

# ### if comando_add == 0 and -1: sorry, but does this line cover all negatives or is python going to take it literally and only do what I want it to do if the number is negative one?

# ### Me explicou o que o meu código antigo realmente fazia e me deu possíveis soluções.

# ### A solução funciona porque compara o comando adicionado a zero e ou se for menor que zero (um número negativo).

# ## [15/04/2026]

# ### Perguntei como checar uma lista vazia

# ### How to check for an empty list?

# ### Me deu três possiveis formas de resolver o problema Citando quais eram melhores/preferiveis e uma solução que funciona mas não é a melhor.

# ### Aprendi 3 jeitos novos de checar uma lista vazia (if not nome_lista; if len(nome_lista) == 0; if nome_lista == [])

# ##[26/04/2026]

# ### Perguntei se poderia me ajudar com a logica do botao update

# ### elif comando == "Update": updt = input("Qual jogo gostaria de atualizar? : ") for game in game_list: if game_list["nome_do_jogo"] == updt: Yeah, I'm not really sure how to do this update thing, the code above is all I could come up with (I'm adding a new command that's supposed to ask the user what they want to change, if the game is completed and add the date they changed the history)

# ### Me respondeu que a minha logica inicial estava boa, so faltava alguns ajustes, me corrigindo no loop e, depois, me dando ideias de como prosseguir.

# ### Entendi como fazer um loop com o dicionario e a descobrir como checar os elementos do dicionario

# ##[26/04/2026]

# ### Perguntei se a minha logica no codigo estava boa

# ### _Copiei o codigo inteiro_ This is the new one, I've changed a few things, also "historico" had to be a list and then I'd have to add a tuple inside it, so let me know if I did that right, also, please check my logic to see if there's something wrong with it 🙏🙏

# ### Me disse que tinha um problema de identacao e disse que a minha logica esta melhorando, mas que eu preciso focar em identacao e produzir 'output' melhor.

# ##[27/04/2026]

# ### Perguntei se havia algum jeito de fazer os comandos serem lidos com qualquer escrita (maisculo/minusculo, etc)

# ### Could you give some sort of solution for the commands? Right now the commands have to be types with the first letter being capitalised, is there a way to change that so any kind of input will registere?

# ### Me deu .strip() e .lower() um para espacos e o outro para minusculas

# ##[03/05/2026]

# ### Perguntei sobre o salvamento em arquivos json.

# ### Will my code work with this implementation of the json method for saving the games?

# ### Me respondeu que o datetime não funcionaria e me deu (.strftime("%d/%m/%Y %H:%M")) para adicionar depois do data = datetime.datetime.now()

# ##[...]
