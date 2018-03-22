from exercicio1 import No, Pilha, ListaSimplesmenteEncadeada


def eh_palindromo(lista):
    pilha = Pilha()
    string_normal = ''
    string_inversa = ''
    no_atual = lista.primeiro

    while no_atual:
        string_normal += no_atual.valor
        pilha.inserir(no_atual.valor)
        no_atual = no_atual.prox

    no_atual = pilha.topo

    while no_atual:
        string_inversa += pilha.remover().valor
        no_atual = pilha.topo

    return string_normal == string_inversa


if __name__ == "__main__":

    teste1 = 'arara'
    lista1 = ListaSimplesmenteEncadeada()

    teste2 = 'carro'
    lista2 = ListaSimplesmenteEncadeada()

    for i in teste1:
        lista1.inserir(i)

    for i in teste2:
        lista2.inserir(i)

    if eh_palindromo(lista1):
        print('A palavra {0} eh palindromo'.format(lista1.get_palavra()))
    else:
        print('A palavra {0} nao eh palindromo'.format(lista1.get_palavra()))

    if eh_palindromo(lista2):
        print('A palavra {0} eh palindromo'.format(lista2.get_palavra()))
    else:
        print('A palavra {0} nao eh palindromo'.format(lista2.get_palavra()))