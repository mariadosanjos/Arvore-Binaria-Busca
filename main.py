from binarySearchTree import BinarySearchTree
from binaryTree import TreeException
tree = BinarySearchTree()
texto = []

#Menu do programa principal
while True:
    try:

        print('''
      Árvores Binárias de Busca

      (d) Digitar texto
      (e) Exibir palavras do texto Ascendente/Descendente
      (c) Exibir frequência de ocorrência das palavras
      (b) Mostrar o nível de desbalanceamento da árvore
      (s) Sair
            ''')

        opcao = input('Insira a opção desejada: ').lower()

        #Opção para digitar o texto.
        if opcao == 'd':
            frase = input('Digite a frase: ')
            if frase.replace(" ","").isalpha():
              texto = frase.split()
              tree = BinarySearchTree()
              print ("\nTexto inserido com sucesso!")
              for p in texto:
                tree.insert(p)
            else:
              print("\nTexto inserido inválido. Por favor, digite uma frase contendo apenas letras.")

        #Opção para exibir as palavras de forma ascendente e descendente.
        elif opcao == 'e':
          if tree.vazia() == False:                       
                print('\nAscendente')
                tree.ascendente()             
              
                print()
                print('\nDescendente')
                tree.descendente()
                print()
          else:
            print ('\nErro na operação. Nenhum texto foi inserido. Por favor, digite um texto e tente novamente.')


        #Opção para exivir a frenquência de ocorrência das palavras.
        elif opcao == 'c':
          try:
            tree.frequencia(texto)
          except TreeException as e:
            print (e)

        #Opção para mostrar o nível de desbelanceamento da árvore.
        elif opcao == 'b':        
          try:
            tree.balanceamento()
          except TreeException as e:
            print(e)

        #Opção para encerrar o programa.
        elif opcao == 's':
            break

        else:
            print(
                '\nOpção inválida. Por favor, insira um valor referente à uma das opções que estejam no menu. ')

        # Tratamento de erro caso o usuário pressione as teclas que encerram a aplicação.

    except KeyboardInterrupt:
        print('\n !- Erro na Operação -!')
        print('\nComando de teclas para encerrar a aplicação estão pressionadas. Por favor, para sair do programa, insira a opção correspondente, no menu principal.')
