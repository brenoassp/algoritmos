class No:

    def __init__(self, chave):
        self.chave = chave

    def __lt__(self, no):
        return self.chave < no.chave

    def __str__(self):
        return '{0}'.format(self.chave)

class MaxHeap:

    def __init__(self):
        self.vetor = []
        self.n = 0

    def inserir(self, no):
        self.vetor.append(no)
        self.sobe(self.n)
        self.n += 1

    def sobe(self, indice):
        if indice == 0:
            return
        if indice % 2 == 1: # se for impar eh filho esquerdo
            pai = int((indice - 1) / 2)
            if self.vetor[pai] < self.vetor[indice]:
                aux = self.vetor[pai]
                self.vetor[pai] = self.vetor[indice]
                self.vetor[indice] = aux
                self.sobe(pai)
        else:
            pai = int((indice / 2) - 1)
            if self.vetor[pai] < self.vetor[indice]:
                aux = self.vetor[pai]
                self.vetor[pai] = self.vetor[indice]
                self.vetor[indice] = aux
                self.sobe(pai)

    def imprimir(self):
        for i in range(self.n):
            print(self.vetor[i])


if __name__=='__main__':
    heap = MaxHeap()

    for i in range(7):
        heap.inserir(No(i))

    heap.imprimir()