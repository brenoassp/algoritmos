import math


class No:

    def __init__(self, chave):
        self.chave = chave
        self.dir = None
        self.esq = None


class ArvoreBinaria:

    def __init__(self):
        self.raiz = None
        self.n = 0

    def insere(self, no): #insere igual da abb feito apenas para testar outras funções
        if not isinstance(no, No):
            raise Exception("deve ser fornecido um objeto do tipo No para insercao")
        if self.raiz is None:
            self.raiz = no
        else:
            atual = self.raiz

            while True:
                if no.chave == atual.chave:
                    raise Exception("Nao eh possivel inserir dois nos com a mesma chave")
                elif no.chave < atual.chave:
                    if atual.esq is None:
                        atual.esq = no
                        self.n += 1
                        return
                    else:
                        atual = atual.esq
                elif no.chave > atual.chave:
                    if atual.dir is None:
                        atual.dir = no
                        self.n += 1
                        return
                    else:
                        atual = atual.dir

    def imprime(self):
        self.imprime_(self.raiz)

    def imprime_(self, raiz):
        if raiz:
            self.imprime_(raiz.esq)
            print(raiz.chave)
            self.imprime_(raiz.dir)


def rotacao_dir(no, avo):
    # tem que garantir que filho a esquerda
    # do no passado como parametro não é None

    aux = no.esq
    no.esq = aux.dir
    aux.dir = no
    if avo:
        avo.dir = aux
    return aux


def cria_espinha_dorsal(arv):
    pai = arv.raiz
    avo = None
    raiz_nova_arvore = None
    while pai is not None:
        if not avo and not pai.esq:
            raiz_nova_arvore = pai
        if pai.esq is not None:
            pai = rotacao_dir(pai, avo)
        else:
            avo = pai
            pai = pai.dir
    arv.raiz = raiz_nova_arvore


def rotacao_esq(pai, avo, filho_dir):
    if not filho_dir:
        raise Exception("filho_dir nao pode ser None")
    pai.dir = filho_dir.esq
    filho_dir.esq = pai
    if avo:
        avo.dir = filho_dir
    return filho_dir


def rotacoes_esq_cada_2_nos(arv, numero_rotacoes, comeca_raiz=True):
    if comeca_raiz:
        avo = None
        pai = arv.raiz
        filho_dir = pai.dir
    else: # começa do filho direito
        avo = arv.raiz
        pai = avo.dir
        filho_dir = pai.dir
    for i in range(numero_rotacoes):
        if not avo:
            arv.raiz = rotacao_esq(pai, avo, filho_dir)
            avo = arv.raiz
            pai = avo.dir
            filho_dir = pai.dir
        else:
            avo.dir = rotacao_esq(pai, avo, filho_dir)
            avo = avo.dir
            pai = avo.dir
            filho_dir = pai.dir


def criar_arvore_altura_minima(arv):
    m = int(math.pow(2, math.floor(math.log(arv.n + 1, 2)))) - 1
    rotacoes_esq_cada_2_nos(arv, arv.n - m)
    while m > 1:
        m = int(math.floor(m / 2))
        rotacoes_esq_cada_2_nos(arv, m, comeca_raiz=False)


if __name__ == '__main__':
    ab = ArvoreBinaria()

    ab.insere(No(15))
    ab.insere(No(17))
    ab.insere(No(19))
    ab.insere(No(20))
    ab.insere(No(25))
    ab.insere(No(30))
    ab.insere(No(32))
    ab.insere(No(40))
    ab.insere(No(50))

    # ab.imprime()

    cria_espinha_dorsal(ab)
    criar_arvore_altura_minima(ab)
    print('\n')

    ab.imprime()
