from classes import GerenciadorPessoas

def menu():
    print("\nSelecione uma opção:")
    print("1. Adicionar Contato")
    print("2. Buscar Contato")
    print("3. Listar Contatos")
    print("4. Remover Contato")
    print("5. Sair")
    return input("Opção: ")

def main():
    agenda = GerenciadorPessoas()
    print("AGENDA DE CONTATOS SIMPLES")

    while True:
        try:
            opcao = menu()

            match opcao:
                case 1:
                    nome = input("Nome: ")
                    sobrenome = input("Sobrenome: ")
                    email = input("Email: ")
                    numero = input("Número: ")
                    agenda.adiciona_pessoa(nome, sobrenome, email, numero)

                case 2:
                    termo = input("Digite o nome ou sobrenome para buscar: ")
                    agenda.buscar_pessoa(termo)

                case 3:
                    agenda.mostrar_registro()

                case 4:
                    try:
                        id_remover = int(input("Digite o ID do contato a remover: "))
                        agenda.remover_pessoa(id_remover)
                    except ValueError:
                        print("ID inválido.")

                case 5:
                    print("Encerrando a execução.")
                    break

                case _:
                    print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Erro durante a execução: {e}")

if __name__ == "__main__":
    main()
