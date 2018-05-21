class No:

    def __init__(self, chave):
        self.chave = chave

    def __lt__(self, no):
        return self.chave < no.chave

    def __gt__(self, no):
        return self.chave > no.chave

    def __str__(self):
        return '{0}'.format(self.chave)


class MaxHeap:

    def __init__(self):
        self.vetor = []
        for i in range(100):
            self.vetor.append(None)
        self.n = 0

    def inserir(self, no):
        self.vetor[self.n] = no
        self.sobe(self.n)
        self.n += 1

    def swap(self, pos1, pos2):
        aux = self.vetor[pos1]
        self.vetor[pos1] = self.vetor[pos2]
        self.vetor[pos2] = aux

    def sobe(self, indice):
        if indice == 0:
            return
        if indice % 2 == 1: # se for impar eh filho esquerdo
            pai = int((indice - 1) / 2)
            if self.vetor[pai] < self.vetor[indice]:
                self.swap(pai, indice)
                self.sobe(pai)
        else:
            pai = int((indice / 2) - 1)
            if self.vetor[pai] < self.vetor[indice]:
                self.swap(pai, indice)
                self.sobe(pai)

    def desce(self, indice):
        if indice <= (self.n/2): # eh pai
            filho = 2 * indice + 1
            if self.vetor[filho]:
                if self.vetor[filho+1]:
                    if self.vetor[filho] < self.vetor[filho + 1]:
                        filho+= 1
                if self.vetor[indice] < self.vetor[filho]:
                    self.swap(indice, filho)
                    self.desce(filho)

    def remover(self):
        if self.n == 0:
            raise Exception("nada para remover")
        removido = self.vetor[0]
        self.vetor[0] = self.vetor[self.n-1]
        self.n -= 1
        self.desce(0)
        return removido

    def imprimir(self):
        for i in range(self.n):
            print(self.vetor[i])


if __name__ == '__main__':
    heap = MaxHeap()

    for i in range(7):
        heap.inserir(No(i))

    heap.remover()

    heap.inserir(No(7))

    heap.imprimir()