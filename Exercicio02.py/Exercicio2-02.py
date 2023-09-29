#Questão 2
class Livro:
    def __init__(self, titulo, autor, descricao):
        self.titulo = titulo
        self.autor = autor
        self.descricao = descricao
    def detalhes(self):
        print(f"Autor: {self.autor}\nTítulo: {self.titulo}\nAutor: {self.descricao}")

titulo = input("Digite título do livro: ")
autor = input("Digite o nome do autor: ")
descricao = input("Apresente uma breve descrição do livro: ")

livro = Livro(titulo, autor, descricao)
livro.detalhes()