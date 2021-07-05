class pilha:

    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def adicionar(self, livro):

        if self.tamanho == 0:
            self.inicio = livro
            self.tamanho += 1

        else:
            aux = self.inicio
            while aux.proximo:
                aux = aux.proximo

            aux.proximo = livro
            self.tamanho += 1

    def excluir(self):

        if self.tamanho == 0:
            print("\nA pilha está vazia!\n")

        elif self.tamanho == 1:
            self.inicio = None
            self.tamanho -= 1
            print("\nItem excluído da pilha!\n")

        else:
            aux = self.inicio
            while aux.proximo:
                auxAnt = aux
                aux = aux.proximo

            auxAnt.proximo = None
            self.tamanho -= 1
            print("\nItem excluído da pilha!\n")

    def imprimir(self):

        if self.tamanho == 0:
            print("\nA pilha está vazia!\n")

        else:
            aux = self.inicio
            print("-----LISTA DE ITENS-----")
            x = 1
            while aux:
                print(x, "LIVRO:", aux.titulo, "  AUTOR:", aux.autor.nome)
                aux = aux.proximo
                x += 1
            print("------FIM DA PILHA-----\n")
