# Equipe: Raquel Lucena, Emilly Jullyane e Caíque Fernandes

class Node:
    def __init__(self, dado):
        self.dado = dado
        self.anterior = None
        self.proximo = None
    

class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f"Música: {self.nome}\nArtista: {self.artista}\nDuração: {self.duracao}\n"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def inserirNoFim(self, dado):
        novoNo = Node(dado)
        if self.head is None:
            self.head = self.tail = novoNo
        else:
            self.tail.proximo = novoNo
            novoNo.anterior = self.tail
            self.tail = novoNo

    def inserirNoInicio(self, dado):
        novoNo = Node(dado)
        if self.head is None:
            self.head = self.tail = novoNo
        else:
            novoNo.proximo = self.head
            self.head.anterior = novoNo
            self.head = novoNo

    def inserirEmPosicao(self, posicao, dado):
        if posicao == 1:
            self.inserirNoInicio(dado)
            return
        novoNo = Node(dado)
        atual = self.head
        contador = 1
        while atual and contador < posicao - 1:
            atual = atual.proximo
            contador += 1
        if atual is None:
            print("Posição inválida.")
            return
        if atual.proximo is None:
            self.inserirNoFim(dado)
        else:
            novoNo.proximo = atual.proximo
            novoNo.anterior = atual
            atual.proximo.anterior = novoNo
            atual.proximo = novoNo

    def removerPorNome(self, nome_musica):
        atual = self.head
        if not atual:
            print("A playlist está vazia.")
            return
        while atual and atual.dado.nome != nome_musica:
            atual = atual.proximo
        if not atual:
            print("Música não encontrada.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        else:
            self.head = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        else:
            self.tail = atual.anterior
        print(f"Sucesso!")

    def moverParaPosicao(self, nome_musica, nova_posicao):
        atual = self.head
        while atual and atual.dado.nome != nome_musica:
            atual = atual.proximo
        if not atual:
            print(f"Música '{nome_musica}' não encontrada.")
            return
        dado_musica = atual.dado
        self.removerPorNome(nome_musica)
        self.inserirEmPosicao(nova_posicao, dado_musica)

    def imprimir(self):
        atual = self.head
        if not atual:
            print("A playlist está vazia.")
            return
        while atual:
            print(atual.dado)
            atual = atual.proximo

    def tocarPlaylist(self):
        atual = self.head
        loop = False
        while atual:
            print(f"Tocando agora:\n{atual.dado}")
            opcao = input("1 - Avançar\n2 - Retroceder\n3 - Ativar/Desativar loop\n4 - Parar: ")
            if opcao == '1':
                atual = atual.proximo or (self.head if loop else None)
            elif opcao == '2':
                atual = atual.anterior or (self.tail if loop else None)
            elif opcao == '3':
                loop = not loop
                if loop:
                    self.tail.proximo = self.head
                    self.head.anterior = self.tail
                else:
                    self.tail.proximo = None
                    self.head.anterior = None
            elif opcao == '4':
                break
            else:
                print("Opção inválida.")
            if not atual:
                print("Fim da playlist.")
                return


# Funções para manipulação da playlist
def adicionarMusica():
    global playlist
    nome = input("Nome da música: ")
    artista = input("Nome do artista: ")
    duracao = input("Duração da música: ")
    musica = Musica(nome, artista, duracao)
    playlist.inserirNoFim(musica)


def removerMusica():
    global playlist
    nome = input("Nome da música a remover: ")
    playlist.removerPorNome(nome)


def mudarPosicaoMusica():
    global playlist
    nome = input("Nome da música a mover: ")
    posicao = int(input("Nova posição: "))
    playlist.moverParaPosicao(nome, posicao)


def listarPlaylistAtual():
    global playlist
    print("Playlist atual:")
    playlist.imprimir()


# Inicialização e controle principal
playlist = DoublyLinkedList()

while True:
    print("Escolha uma opção:\n1 - Adicionar música\n2 - Remover música\n3 - Mover música para outra posição\n4 - Listar playlist atual\n5 - Tocar playlist\n6 - Sair\n")
    opcao = input("Opção: ")

    if opcao == '1':
        adicionarMusica()
    elif opcao == '2':
        removerMusica()
    elif opcao == '3':
        mudarPosicaoMusica()
    elif opcao == '4':
        listarPlaylistAtual()
    elif opcao == '5':
        playlist.tocarPlaylist()
    elif opcao == '6':
        break
    else:
        print("Opção inválida.")
