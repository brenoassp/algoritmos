class NoInfo:

    def __init__(self, chave):
        self.chave = chave


class NoDesvio:

    def __init__(self, noinfo=None):
        self.ehchave = noinfo
        self.filhos = dict()


class TrieRWay:

    def __init__(self):
        self.raiz = NoDesvio()

    def inserir(self, noinfo):
        self.raiz = self.inserir_(self.raiz, noinfo, 0)

    def inserir_(self, no, noinfo, pos):
        if no is None:
            no = NoDesvio()
        if pos == len(noinfo.chave) - 1:
            no.ehchave = noinfo
            return no
        no.filhos[noinfo.chave[pos]] = self.inserir_(no.filhos[noinfo.chave[pos]], noinfo, pos + 1)
        return no

    def contido(self, chave):
        no = self.raiz
        for i in range(len(chave)):
            if chave[i] not in no.filhos:
                return False
            no = no.filhos[chave[i]]
        if no.ehchave is not None:
            return True
        else:
            return False


if __name__ == '__main__':

    rway = TrieRWay()

    rway.inserir(NoInfo('abc'))

    print('{}'.format(rway.contido('abc')))
