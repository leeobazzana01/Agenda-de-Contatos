class pessoa:
    def __init__(self, id, nome, sobrenome, email, numero):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email 
        self.numero

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Sobrenome: {self.sobrenome} | Email: {self.email} | Numero: {self.numero}" 
    
class gerenciador_pessoas:
    def __init__(self):
        self.registro = {}

    def adiciona_pessoa(self, pessoa):
        if pessoa.id in self.regristro:
            print(f"O contado '{pessoa.nome}' já existe na Agenda!!")
            return False
        
        self.registro[pessoa.id] = pessoa
        print(f"Contato '{pessoa.nome}' adicionado com sucesso!")
        return True
    
    def remover_pessoa(self, id):
        if id in self.registro:
            pessoa_removida = self.registro.pop(id)
            print(f"O Contato '{pessoa_removida.nome} foi removido com sucesso!!")
            return True

        print(f"Erro: ID {id} não encontrado!")
        return False

    def mostrar_registro(self):
        print("CONTATOS NA AGENDA")
        
        for id, pessoa in self.registro.items():
            print(pessoa)
        
        print("------------------\n")


