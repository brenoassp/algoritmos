class No:

    def __init__(self, chave):
        self.chave = chave
        self.dir = None
        self.esq = None


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None

    def contido(self, chave):
        return self.contido_(self.raiz, chave)

    def contido_(self, raiz_subarvore, chave):
        if raiz_subarvore is None:
            return False
        if raiz_subarvore.chave == chave:
            return True
        if chave < raiz_subarvore.chave:
            return self.contido_(raiz_subarvore.esq, chave)
        else:
            return self.contido_(raiz_subarvore.dir, chave)

    def contido_sem_recursao(self, chave):
        raiz_sub = self.raiz
        while raiz_sub is not None:
            if raiz_sub.chave == chave:
                return True
            if chave < raiz_sub.chave:
                raiz_sub = raiz_sub.esq
            else:
                raiz_sub = raiz_sub.dir
        return False

    def insere(self, no):
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
                        return
                    else:
                        atual = atual.esq
                elif no.chave > atual.chave:
                    if atual.dir is None:
                        atual.dir = no
                        return
                    else:
                        atual = atual.dir

    def imprime_(self, raiz):
        if raiz:
            self.imprime_(raiz.esq)
            print(raiz.chave)
            self.imprime_(raiz.dir)

    def imprime(self):
        self.imprime_(self.raiz)

    def remove(self, chave):
        self.remove_(self.raiz, chave)

    def remove_(self, raiz, chave):

        def eh_folha(p):
            if p and p.dir is None and p.esq is None:
                return True
            return False

        def swap(p1, p2): #troca apenas informacao do no
            aux = p1.chave
            p1.chave = p2.chave
            p2.chave = aux

        if raiz is None:
            raise Exception("Nao há nenhum elemento com a chave fornecida")
        if raiz.chave == chave:
            if eh_folha(raiz):
                del raiz
                return None
            else:
                if raiz.esq:
                    swap(raiz, raiz.esq)
                    raiz.esq = self.remove_(raiz.esq, chave)
                elif raiz.dir:
                    swap(raiz, raiz.dir)
                    raiz.dir = self.remove_(raiz.dir, chave)
        elif chave < raiz.chave:
            raiz.esq = self.remove_(raiz.esq, chave)
            return raiz
        elif chave > raiz.chave:
            raiz.dir = self.remove_(raiz.dir, chave)
            return raiz


if __name__ == '__main__':
    abb = ArvoreBinariaBusca()

    abb.insere(No(5))
    abb.insere(No(10))

    abb.imprime()

    print("\n")
    abb.remove(5)

    abb.imprime()
