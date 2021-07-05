from autor import autor

class livro:

    def __init__(self, id, titulo, idAutor, nomeAutor):
        self.id = id
        self.titulo = titulo
        self.autor = autor(idAutor, nomeAutor)
        self.proximo = None

