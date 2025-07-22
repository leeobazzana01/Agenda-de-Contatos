class Pessoa:
    def __init__(self, id, nome, sobrenome, email, numero):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email 
        self.numero = numero

    def __str__(self):
        return (
            f"ID: {self.id} | Nome: {self.nome} {self.sobrenome} | " 
            f"Email: {self.email} | Numero: {self.numero}"
            ) 
    
class GerenciadorPessoas:
    def __init__(self):
        self.registro = {}
        self.proximo_id = 1

    def adiciona_pessoa(self, nome, sobrenome, email, numero):
        nova_pessoa = Pessoa(self.proximo_id, nome, sobrenome, email, numero)
        self.registro[self.proximo_id] = nova_pessoa
        print(f"Contato '{nome}' adicionado com sucesso! ID: {self.proximo_id}")
        self.proximo_id += 1

    def buscar_pessoa(self, termo):
        resultados = [p for p in self.registro.values()
                      if termo.lower() in p.nome.lower() or termo.lower() in p.sobrenome.lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("Nenhum contato encontrado.")

    def remover_pessoa(self, id):
        if id in self.registro:
            pessoa_removida = self.registro.pop(id)
            print(f"Contato '{pessoa_removida.nome}' removido com sucesso.")
        else:
            print(f"Contato com ID {id} não encontrado.")

    def mostrar_registro(self):
        if not self.registro:
            print("Agenda vazia.")
        else:
            print("CONTATOS NA AGENDA:")
            for pessoa in self.registro.values():
                print(pessoa)

