from collections import Counter
from node import Node
ROOT = "root"

class TreeException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None
    

    #Método para mostrar o texto de forma ascendente.
    def ascendente(self, node=None):        
      if node is None:
            node = self.root
      if node.left:
            self.ascendente(node.left)
      print(node, end=' ')
      if node.right:
          self.ascendente(node.right)
        

    #Método para mostrar o texto de forma descendente.
    def descendente(self, node=None):
        if node is None:
            node = self.root
        if node.right:
            self.descendente(node.right)
        print(node, end=' ')
        if node.left:
            self.descendente(node.left)

    #Método para fazer a contagem das palavras repetidas ou não.
    def frequencia(self, list):
        list = list
        counts = Counter(list)
        if self.vazia():
          raise TreeException ("\nErro na operação. Nenhum texto foi inserido. Por favor, digite um texto e tente novamente")
        else:
          for i in counts:
              print(f'{i} = {counts[i]}')
 

    #Método que faz chamada da função altura para trazer a altura da árvore esquerda e direta.
    def balanceamento(self, node=None):

        if self.vazia():
          raise TreeException ("\nErro na operação. Nenhum texto foi inserido. Por favor, digite um texto e tente novamente")
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.altura(node.left)
        if node.right:
            hright = self.altura(node.right)

        # condição que define se a árvore está balanceada ou não.
        print(f'\nFator de balanceamento da árvore: {hleft - hright}')
        if hleft - hright == 1 or hleft - hright == 0 or hleft - hright == -1:
            print('Árvore balanceada')
        else:
            print('Árvore Desbalanceada')

    # Método que acessa todo o lado esquerdo e depois todo o lado direito das sub-árvores trazendo a altura delas com chamadas recursivas.
    def altura(self, node=None):

        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.altura(node.left)
        if node.right:
            hright = self.altura(node.right)

        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1
            
    #Método para verificar se a árvore está vazia
    def vazia(self):
      if self.root != None:
        return False
      else:
        return True
