from binaryTree import BinaryTree
from node import Node

#Classe que estrutura a árvore binária de busca onde todos os elementos menores que a raiz são alocados à esquerda e os maiores à direita.
class BinarySearchTree(BinaryTree):

    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
