from livro import livro
from pilha import pilha


l1 = livro(1, "Ensaio sobre a cegueira", 569, "José Saramago")
l2 = livro(2, "Crime e Castigo", 788, "Fiodor Dostoievsky")
l3 = livro(3, "A monatnha mágica", 239, "Thomas Mann")
l4 = livro(4, "Dom quixote", 621, "Miguel de Cervantes")

p1 = pilha()

p1.adicionar(l1)
p1.adicionar(l2)
p1.adicionar(l3)
p1.adicionar(l4)
p1.imprimir()
p1.excluir()
p1.imprimir()
p1.excluir()
p1.imprimir()
p1.excluir()
p1.imprimir()
p1.adicionar(l3)
p1.adicionar(l4)
p1.imprimir()
p1.excluir()
p1.imprimir()
p1.excluir()
p1.excluir()
p1.imprimir()
p1.adicionar(l3)
p1.imprimir()
