from livro import Livro

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro.titulo}' adicionado com sucesso.")

    def remover_livro_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f"Livro com ISBN {isbn} removido.")
                return
        print(f"Nenhum livro encontrado com ISBN {isbn}.")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            for livro in self.livros:
                print(livro)

    def buscar_por_titulo(self, palavra_chave):
        encontrados = [livro for livro in self.livros if palavra_chave.lower() in livro.titulo.lower()]
        if encontrados:
            print("Livros encontrados:")
            for livro in encontrados:
                print(livro)
        else:
            print(f"Nenhum livro encontrado com a palavra '{palavra_chave}' no título.")
