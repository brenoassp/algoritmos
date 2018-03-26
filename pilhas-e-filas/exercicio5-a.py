class No:
    valor = None
    proximo = None
    anterior = None


class ListaDuplamenteEncadeada:
    primeiro = None
    ultimo = None

    def contido(self, valor):
        no_atual = self.primeiro
        while no_atual:
            if no_atual.valor == valor:
                return True
            no_atual = no_atual.proximo
        return False

    def inserir(self, valor):
        no = No()
        no.valor = valor
        if self.ultimo:
            self.ultimo.proximo = no
            no.anterior = self.ultimo
            self.ultimo = no
        else:
            self.primeiro = no
            self.ultimo = no
        return

    def remover(self, valor):
        if not self.contido(valor):
            raise ValueError("o valor fornecido nao esta contido na lista")
        no_atual = self.primeiro
        while no_atual:
            if no_atual.valor == valor:
                break
            no_atual = no_atual.proximo
        if not no_atual.anterior:
            self.primeiro = no_atual.proximo
            no_atual.anterior = None
        else:
            no_atual.anterior.proximo = no_atual.proximo
            if no_atual.proximo:
                no_atual.proximo.anterior = no_atual.anterior
            else:
                self.ultimo = no_atual.anterior