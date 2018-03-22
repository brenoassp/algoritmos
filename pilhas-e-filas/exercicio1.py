class No:
    valor = None
    prox = None


class ListaSimplesmenteEncadeada:
    primeiro = None
    ultimo = None

    def inserir(self, valor):
        no = No()
        no.valor = valor
        if not self.ultimo:
            self.primeiro = no
            self.ultimo = no
        else:
            self.ultimo.prox = no
            self.ultimo = no

    def imprimir(self):
        no_atual = self.primeiro
        while no_atual:
            print('{} '.format(no_atual.valor))
            no_atual = no_atual.prox

    def tamanho(self):
        no_atual = self.primeiro
        tam = 0
        while no_atual:
            tam += 1
            no_atual = no_atual.prox
        return tam

    def get_palavra(self):
        no_atual = self.primeiro
        palavra = ''
        while no_atual:
            palavra += no_atual.valor
            no_atual = no_atual.prox
        return palavra

class Pilha:
    topo = None

    def inserir(self, valor):
        no = No()
        no.prox = self.topo
        no.valor = valor
        self.topo = no

    def remover(self):
        if not self.topo: # pilha vazia
            return
        no = self.topo
        self.topo = self.topo.prox
        return no


def lista_reversa(lista):
    """
    Constroi uma lista lista_rev a partir de lista que contem os valores em ordem reversa.
    Primeira parte exercicio 1
    """
    lista_rev = ListaSimplesmenteEncadeada()
    pilha_aux = Pilha()

    no_atual = lista.primeiro

    while no_atual:
        pilha_aux.inserir(no_atual.valor)
        no_atual = no_atual.prox

    while pilha_aux.topo:
        lista_rev.inserir(pilha_aux.remover().valor)

    return lista_rev


def lista_soma(lista):
    """
    Constroi uma lista l2 a partir de lista quando o tamanho da lista fornecida for par
    """
    if lista.tamanho() % 2 != 0:
        return
    else:
        pilha = Pilha()
        no_atual = lista.primeiro
        #while no_atual:


if __name__ == '__main__':
    lista = ListaSimplesmenteEncadeada()

    for i in range(0,5):
        lista.inserir(i)

    lista_rev = lista_reversa(lista)

    lista_rev.imprimir()
