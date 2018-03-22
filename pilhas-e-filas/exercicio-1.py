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
    lista_rev = ListaSimplesmenteEncadeada()
    pilha_aux = Pilha()

    no_atual = lista.primeiro

    while no_atual:
        pilha_aux.inserir(no_atual.valor)
        no_atual = no_atual.prox

    while pilha_aux.topo:
        lista_rev.inserir(pilha_aux.remover().valor)

    return lista_rev


if __name__ == '__main__':
    lista = ListaSimplesmenteEncadeada()

    for i in range(0,5):
        lista.inserir(i)

    lista_rev = lista_reversa(lista)

    lista_rev.imprimir()
