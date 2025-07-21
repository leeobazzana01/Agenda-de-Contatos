lista_contatos = []

def adiciona_contato():
    contador = 0
    try:
        quantidade = int(input("Quantidade de Contatos que deseja Adicionar: "))

        while(contador < quantidade):
            nome = input("Nome: ")
            lista_contatos.append({"Nome":{nome}})
            sobrenome = input("Sobrenome: ")
            lista_contatos.append({"Sobrenome":{sobrenome}})
            email = input("Email: ")
            lista_contatos.append({"Email":{email}})
            try:
                contato = int(input("Contato(DDD): "))
                lista_contatos.append({"Contato":{contato}})
            except:
                raise TypeError("Insira um Número no contato")
            print(f"O Contato {nome} {sobrenome} foi inserido com sucesso!")

            contador += 1
            
    except:
        raise TypeError("Quantidade de Contatos Inválida!")

def main():
    print("AGENDA DE CONTATOS SIMPLES")
    inicio = input("Iniciar (S) ou encerrar a execução(N)\n").upper()

    while(inicio == "S"):

        try:
            opcao = int(input("Selecione uma opção: \n1. Adicionar Contato\n2. Buscar Contato\n3. Listar Contatos\n4. Remover Contatos\n"))

            match opcao:
                case 1:
                    print(adiciona_contato())
                case 2:
                    pass
                case 3:
                    print(lista_contatos)
                case 4:
                    pass
                case _:
                    print("Opção Inválida")
    
        except:
            raise TypeError("Tipo Inserido Inválido")
        
        inicio = input("Deseja continuar a Execução? (S)Sim ou (N)Não\n").upper()    
main()