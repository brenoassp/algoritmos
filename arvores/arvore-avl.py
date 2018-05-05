class No:

    def __init__(self, chave):
        self.chave = chave
        self.dir = None
        self.esq = None
        self.fb = 0


class ArvoreAVL:

    def __init__(self):
        self.raiz = None
        self.n = 0

    def insere(self, no): # similar ao da ABB, com correção para ajustar os fbs executando rotações
        if not isinstance(no, No):
            raise Exception("deve ser fornecido um objeto do tipo No para insercao")
        if self.raiz is None:
            self.raiz = no
        else:
            atual = self.raiz



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


def rotacao_esq(pai, avo, filho_dir):
    if not filho_dir:
        raise Exception("filho_dir nao pode ser None")
    pai.dir = filho_dir.esq
    filho_dir.esq = pai
    if avo:
        avo.dir = filho_dir
    return filho_dir


if __name__ == '__main__':
    print('teste')