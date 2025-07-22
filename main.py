from classes import pessoa, gerenciadorpessoas

def main():
    contador_usuarios = 0

    print("AGENDA DE CONTATOS SIMPLES")
    inicio = input("Iniciar (S) ou encerrar a execução(N)\n").upper()

    while(inicio == "S"):

        try:
            opcao = int(input("Selecione uma opção: \n1. Adicionar Contato\n2. Buscar Contato\n3. Listar Contatos\n4. Remover Contatos\n"))

            match opcao:
                case 1:
                    usuarios = int(input("Quantos Contatos deseja adicionar?"))

                    while(contador_usuarios < usuarios):
                        nome = input("Nome: ")
                        sobrenome = input("Sobrenome: ")
                        email = input("Email: ")
                        numero = int(input("Numero: "))
                        gerenciadorpessoas.adicionar_pessoa(pessoa(contador_usuarios, nome, sobrenome, email, numero))
                        contador_usuarios += 1
                case 2:
                    pass
                case 3:
                    print(gerenciadorpessoas.mostrar_registro())
                case 4:
                    pass
                case _:
                    print("Opção Inválida")
    
        except:
            raise TypeError("Tipo Inserido Inválido")
        
        inicio = input("Deseja continuar a Execução? (S)Sim ou (N)Não\n").upper()    
main()