class No:
    valor = 0
    dir = None
    esq = None

    def __init__(self, valor):
        self.valor = valor


class Arvore:
    raiz = None

    def insere(self, valor): #insere de uma ABB para teste
        no = No(valor)
        if self.raiz is None:
            self.raiz = no
        else:
            no_atual = self.raiz
            while True:
                if valor > no_atual.valor:
                    if no_atual.dir is None:
                        no_atual.dir = no
                        return
                    else:
                        no_atual = no_atual.dir
                if valor < no_atual.valor:
                    if no_atual.esq is None:
                        no_atual.esq = no
                        return
                    else:
                        no_atual = no_atual.esq


def morris_in_ordem(raiz):

    print('morris in ordem')

    def visita(p):
        print(p.valor)

    p = raiz
    tmp = None
    while p is not None:
        if p.esq is None:
           visita(p)
           p = p.dir
        else:
            tmp = p.esq
            while tmp.dir is not None and tmp.dir != p:
                tmp = tmp.dir
            if tmp.dir is None:
                tmp.dir = p
                p = p.esq
            else:
                visita(p)
                tmp.dir = None
                p = p.dir


def morris_pre_ordem(raiz):

    print('morris pre ordem')

    def visita(p):
        print(p.valor)

    p = raiz
    tmp = None
    while p is not None:
        if p.esq is None:
            visita(p)
            p = p.dir
        else:
            tmp = p.esq
            while tmp.dir is not None and tmp.dir != p:
                tmp = tmp.dir
            if tmp.dir is None: #visitar p e setar direita do nó
                visita(p)
                tmp.dir = p
                p = p.esq
            else: #já visitou p e sua SAE, entao só ir para direita, mas primeiro consertar a árvore
                tmp.dir = None
                p = p.dir


if __name__ == '__main__':
    arvore = Arvore()

    arvore.insere(5)
    arvore.insere(3)
    arvore.insere(7)

    morris_in_ordem(arvore.raiz)

    morris_pre_ordem(arvore.raiz)