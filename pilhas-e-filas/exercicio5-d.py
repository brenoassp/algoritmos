class No:
    valor = None
    proximo = None
    anterior = None


class ListaDuplamenteEncadeadaCircular:
    primeiro = None
    ultimo = None

    def contido(self, valor):
        '''
        Complexidade: O(n)
        '''
        if not self.ultimo:
            return False
        no_atual = self.primeiro
        while no_atual != self.ultimo:
            if no_atual.valor == valor:
                return True
            no_atual = no_atual.proximo
        if no_atual and no_atual.valor == valor:
            return True
        return False

    def inserir(self, valor):
        '''
        Complexidade: O(1)
        '''
        no = No()
        no.valor = valor
        if not self.ultimo:
            self.primeiro = no
            self.ultimo = no
            return
        no.proximo = self.ultimo.proximo
        no.anterior = self.ultimo
        self.ultimo.proximo = no
        self.primeiro.anterior = no
        self.ultimo = no

    def remover(self, valor):
        '''
        Complexidade: O(n)
        '''
        if not self.contido(valor):
            raise ValueError("o valor fornecido nao esta contido na lista")
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            no_atual = self.primeiro
            while no_atual:
                if no_atual.valor == valor:
                    break
                no_atual = no_atual.proximo
            if self.primeiro == no_atual:
                self.primeiro = no_atual.proximo
            elif self.ultimo == no_atual:
                self.ultimo = no_atual.anterior
            no_atual.anterior.proximo = no_atual.proximo
            no_atual.proximo.anterior = no_atual.anterior