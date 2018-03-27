class No:
    x = None
    prox = None
    desc = None


class SkipList:
    head = None

    def contido(self, no, valor):
        if not no:
            return False
        if no.x == valor:
            return True
        return self.contido(no.prox, valor) or self.contido(no.desc, valor)

    def contido(self, valor):
        return self.contido(self.head, valor)
