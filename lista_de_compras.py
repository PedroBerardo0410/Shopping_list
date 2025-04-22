
lista_compras = []

def exibir_menu():
    print("\n===== MENU =====")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Salvar lista em arquivo")
    print("5 - Sair")

def salvar_lista():
    with open("lista_compras.txt", "w") as arquivo:
        for item in lista_compras:
            arquivo.write(f"{item['nome']} - Quantidade: {item['quantidade']}\n")
    print("Lista salva no arquivo 'lista_compras.txt'")

while True:
    exibir_menu()
    opc = input("Escolha uma opção: ")

    if opc == "1":
        item = input("Digite o nome do produto: ").title()
        quantidade = input("Informe a quantidade deste produto: ")
        lista_compras.append({"nome":item, "quantidade": quantidade})
        print(f"{item} adicionado a lista com quantidade de {quantidade}.")
    
    elif opc == "2":
        item_nome = input("Digite o nome do item para remover: ")
        encontrado = False
        for item in lista_compras:
            if item["nome"].lower() == item_nome.lower():
                lista_compras.remove(item)
                print(f"'{item_nome}' removido!")
                encontrado = True
                break
            if not encontrado:
                print("Item não encontrado na lista.")
    
    elif opc == "3":
        if lista_compras:
            print("Sua lista de compras: ")
            for i, item in enumerate(lista_compras, 1):
                print(f"{i}° {item['nome']} - Quantidade: {item['quantidade']}")
        else:
            print("Sua lista está vazia!")
    
    elif opc == "4":
        salvar_lista()
    
    elif opc == "5":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida, tente novamente.")