class No:
    digito = None
    anterior = None
    proximo = None


class ListaNumero:
    primeiro = None
    ultimo = None

    def __init__(self, *numero_string):
        for i, s in enumerate(numero_string):
            no = No()
            no.digito = int(s)
            if i == 0:
                self.primeiro = no
                self.ultimo = no
            else:
                self.ultimo.proximo = no
                no.anterior = self.ultimo
                self.ultimo = no

    def add_final(self, digito):
        no = No()
        no.digito = digito
        if self.ultimo:
            self.ultimo.proximo = no
            no.anterior = self.ultimo
            self.ultimo = no
        else:
            self.primeiro = no
            self.ultimo = no

    def __add__(self, other):
        l1_atual = self.ultimo
        l2_atual = other.ultimo
        l3 = ListaNumero()
        quociente = 0

        while l1_atual and l2_atual:
            quociente = l1_atual.digito + l2_atual.digito + quociente // 10
            resto = l1_atual.digito + l2_atual.digito + quociente % 10

            l3.add_final(resto)

            l1_atual = l1_atual.anterior
            l2_atual = l2_atual.anterior

        while l1_atual:
            l3.add_final(l1_atual.digito)

        while l2_atual:
            l3.add_final(l2_atual.digito)

        return l3

    def imprime(self):
        no_atual = self.primeiro
        while no_atual:
            print(no_atual.digito)
            no_atual = no_atual.proximo


if __name__ == '__main__':
    l1 = ListaNumero('10000000000')
    l2 = ListaNumero('10')

    l3 = l1 + l2
    l3.imprime()
