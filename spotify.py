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
        return f"Nome da Música: {self.nome}\n Nome do artista: {self.artista}\n Duração da Música: {self.duracao}"
        
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

# Método para inserir no início (prepend)
    def prepend(self, data):
        new_node = Node (data)
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
            if current.data == data:
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
        raise ValueError("Data not found in the list") 

# Método para inserir em uma posição específica (insert)
    def insert(self, index, data):
        if index == 0: 
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            if current is None:
                raise IndexError("Index out of bounds")
            current = current.next
        if current == self.tail:  
            self.append(data)
        else:
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
