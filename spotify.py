class Node:
    def __init__(self, data):
        self.data = data  # O dado armazenado será um objeto da classe Musica
        self.prev = None  # Referência ao nó anterior
        self.next = None  # Referência ao próximo nó

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f"Nome da Música: {self.nome}\nNome do artista: {self.artista}\nDuração da Música: {self.duracao}"

class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    # Método para inserir no início (prepend)
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:  # Se a lista estiver vazia
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Método para inserir no final (append)
    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # Método para remover um nó específico (remove)
    def remove(self, data):
        current = self.head
        while current:
            if (current.data.nome == data.nome and
                current.data.artista == data.artista and
                current.data.duracao == data.duracao):
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        raise ValueError("Música não encontrada na playlist")

    # Método para inserir em uma posição específica (insert)
    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Posição fora dos limites")
            current = current.next
        if current == self.tail:
            self.append(data)
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    # Método para contar o número de músicas
    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    # Método para exibir a playlist
    def print_playlist(self):
        current = self.head
        if not current:
            print("A playlist está vazia.")
        else:
            while current:
                print(current.data)
                current = current.next

def main():
    playlist = Playlist()
    while True:
        print('---- Escolha uma opção ---\n')
        print('1 - Adicionar música')
        print('2 - Remover música')
        print('3 - Mover música para outra posição')
        print('4 - Listar playlist atual')
        print('5 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            print('---- Adicionar música na playlist ----\n')
            nome = input("Digite o nome da música: \n")
            artista = input("Digite o nome do artista: \n")
            duracao = input("Digite a duração da música: \n")
            if nome and artista and duracao:
                nova_musica = Musica(nome, artista, duracao)
                playlist.append(nova_musica)
                print("Música adicionada com sucesso!\n")
            else:
                print("Todos os campos devem ser preenchidos!\n")
        
        elif opcao == '2':
            print('---- Remover música da playlist ----\n')
            nome = input('Nome da música: \n')
            artista = input('Nome do artista: \n')
            duracao = input('Duração da música: \n')
            if nome and artista and duracao:
                musica_remover = Musica(nome, artista, duracao)
                try:
                    playlist.remove(musica_remover)
                    print("Música removida com sucesso!")
                except ValueError:
                    print('Erro: Música não encontrada na playlist.')
            else:
                print("Todos os campos devem ser preenchidos!\n")

        elif opcao == '3':
            print('---- Mover música para outra posição ----\n')   
            nome = input('Nome da música: \n')
            artista = input('Nome do artista: \n')
            duracao = input('Duração da música: \n')
            if nome and artista and duracao:
                try:
                    nova_posicao = int(input("Digite a nova posição (0-index): \n"))
                    if nova_posicao < 0 or nova_posicao >= playlist.count():
                        print("Erro: Posição fora dos limites.")
                        continue
                    musica_mover = Musica(nome, artista, duracao)
                    playlist.remove(musica_mover)
                    playlist.insert(nova_posicao, musica_mover)
                    print('Música movida com sucesso!')
                except ValueError:
                    print('Erro: Música não encontrada na playlist.')
                except IndexError:
                    print('Erro: Posição fora dos limites.')
            else:
                print("Todos os campos devem ser preenchidos!\n")

        elif opcao == '4':
            print("Playlist atual: ")
            playlist.print_playlist()

        elif opcao == '5':
            print("Encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
