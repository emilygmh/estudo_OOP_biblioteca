from livro import Livro
from biblioteca import Biblioteca

def main():
    biblioteca = Biblioteca()

    # Criando livros
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, "978-0-261-10238-3")
    livro2 = Livro("Dom Quixote", "Miguel de Cervantes", 1605, "978-3-16-148410-0")
    livro3 = Livro("Python para Iniciantes", "João Silva", 2020, "123-4-56-789012-3")

    # Adicionando livros
    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    print("\n📚 Lista de Livros:")
    biblioteca.listar_livros()

    print("\n🔍 Buscando livros com 'python':")
    biblioteca.buscar_por_titulo("python")

    print("\n❌ Removendo livro com ISBN 978-3-16-148410-0:")
    biblioteca.remover_livro_por_isbn("978-3-16-148410-0")

    print("\n📚 Lista de Livros após remoção:")
    biblioteca.listar_livros()

if __name__ == "__main__":
    main()
