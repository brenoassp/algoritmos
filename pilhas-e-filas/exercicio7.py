import random

class NoFolha: # Chamado de nó informação
    x = None
    nome = None
    idade = None
    sexo = None
    prox = None
    anterior = None

    def __init__(self, x, nome, idade):
        self.x = x
        self.nome = nome
        self.idade = idade


class No: # Chamado de nó desvio
    '''
     x é a chave, portanto preciso de um novo nó que conterá a informação de fato.
     Esse outro nó estará presente apenas na lista mais inferior da skiplist.
    '''
    x = None
    prox = None
    desc = None


class SkipList:
    head = None

    def contido(self, no_anterior, no_atual, valor):
        if no_atual.x == valor:
            return True
        if isinstance(no_atual, NoFolha) and no_atual.x > valor:
            return False
        elif valor > no_atual.x:
            return self.contido(no_atual, no_atual.prox, valor)
        else:
            if not no_anterior:
                return False
            return self.contido(None, no_anterior.desc, valor)

    def contido(self, valor):
        return self.contido(None, self.head, valor)

    # def folha_anterior_insercao(self, no_anterior, no_atual, valor):
    #     if no_atual.x == valor:
    #         raise ValueError("ja existe a chave")
    #     if isinstance(no_atual, NoFolha) and no_atual.x > valor:
    #         return no_anterior
    #     elif valor > no_atual.x:
    #         return self.contido(no_atual, no_atual.prox, valor)
    #     else:
    #         # if not no_anterior:
    #         #     return False
    #         return self.contido(None, no_anterior.desc, valor)
    #
    # def folha_anterior_insercao(self, valor):
    #     return self.folha_anterior_insercao(None, self.head, valor)
    #
    # def insercao(self, no, num_lista): #lista com nó folha é a lista 0
    #     no_anterior_insercao = self.folha_anterior_insercao(valor)
    #     no.prox = no_anterior_insercao.prox
    #     no_anterior_insercao.prox = no
    #     num_sorteado = random.random()
    #     if num_sorteado > 0.5:
    #         self.insercao()
    #
    # def insercao(self, no_folha):
    #     self.insercao(no_folha, 0)