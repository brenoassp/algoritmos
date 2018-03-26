class No:
    valor = None
    proximo = None


class Pilha:
    topo = None

    def contido(self, valor):
        no_atual = self.topo
        while no_atual:
            if no_atual.valor == valor:
                return True
            no_atual = no_atual.proximo
        return False

    def inserir(self, valor):
        no = No()
        no.valor = valor
        no.proximo = self.topo
        self.topo = no
        return

    def remover(self):
        no_removido = self.topo
        self.topo = self.topo.proximo
        return no_removido