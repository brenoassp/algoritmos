class No:
    valor = None
    proximo = None


class Fila:
    head = None #inicio
    tail = None #fim

    def contido(self, valor):
        '''
        Complexidade: O(n)
        '''
        no_atual = self.head
        while no_atual:
            if no_atual.valor == valor:
                return True
            no_atual = no_atual.proximo
        return False

    def inserir(self, valor):
        '''
        Complexidade: O(1)
        '''
        no = No()
        no.valor = valor
        if self.tail:
            self.tail.proximo = no
            self.tail = no
        else:
            self.head = no
            self.tail = no
        return

    def remover(self):
        '''
        Complexidade: O(1)
        '''
        no_removido = self.head
        self.head = self.head.proximo
        if not self.head:
            self.tail = None
        return no_removido
