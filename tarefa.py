class Tarefa:
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.status = "pendente"

    def concluir(self):
        self.status = "concluída"

    def to_dict(self):
        return {"titulo": self.titulo, "descricao": self.descricao, "status": self.status}
