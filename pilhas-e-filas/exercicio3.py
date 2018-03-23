class No:
    linha = None
    coluna = None
    valor = None
    proximo = None

    def __init__(self, linha, coluna, valor):
        self.linha = linha
        self.coluna = coluna
        self.valor = valor


class Matriz:
    """
    Matriz esparsa
    """
    primeiro = None
    linhas = None
    colunas = None

    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas

    def remover(self, linha, coluna):
        no_atual = self.primeiro
        no_anterior = None

        while no_atual:
            if no_atual.linha == linha and no_atual.coluna == coluna:
                if not no_anterior:
                    self.primeiro = no_atual.proximo
                else:
                    no_anterior.proximo = no_atual.proximo
                return
            no_anterior = no_atual
            no_atual = no_atual.proximo

    def inserir(self, linha, coluna, valor):
        """
        :param linha: indice da linha
        :param coluna: indice da coluna
        :param valor: valor
        """

        if linha >= self.linhas or coluna >= self.colunas: # erro indice invalido
            return

        if valor == 0:
            return

        no = No(linha, coluna, valor)

        if not self.primeiro:
            self.primeiro = no
        else:
            no_atual = self.primeiro
            no_anterior = None
            while no_atual:
                if no_atual.linha == linha and no_atual == coluna:
                    if no.valor == 0:
                        self.remover(linha, coluna)
                    else:
                        no_atual.valor = valor
                    return
                no_anterior = no_atual
                no_atual = no_atual.proximo
            if no_anterior:
                no_anterior.proximo = no

    def busca(self, linha, coluna):
        if linha >= self.linhas or coluna >= self.colunas: # erro indice invalido
            raise ValueError('Indice invalido.')
        no_atual = self.primeiro
        while no_atual:
            if no_atual.linha == linha and no_atual.coluna == coluna:
                return no_atual.valor
            no_atual = no_atual.proximo
        return 0

    def imprime(self):
        for i in range(self.linhas):
            s = ''
            for j in range(self.colunas):
                s += str(self.busca(i, j)) + ' '
            print(s)


def multiplica_matriz(m1, m2):
    """
    Qual a complexidade dessa funcao?

    Para calcular cada elemento da nova matriz é preciso fazer m1.colunas x 2 buscas.
    Busca = O(k). Sendo k a quantidade de valores diferentes de 0. Total: O(nk) = O(m1.colunas * k)

    Para calcular todos os elementos da nova matriz, é preciso multiplicar pela quantidade de elementos m * n
    O(m * k * m * n) = O (m²nk)
    """
    if m1.colunas != m2.colunas:
        raise Exception("impossivel multiplicar as matrizes")
    matriz_resultado = Matriz(m1.linhas, m2.colunas)
    for i in range(m1.linhas):
        for j in range(m1.colunas):
            soma = 0
            for k in range(m1.colunas):
                soma += m1.busca(i, k) * m2.busca(k, j)
            matriz_resultado.inserir(i, j, soma)
    return matriz_resultado


if __name__ == '__main__':
    m1 = Matriz(2, 3)
    m2 = Matriz(3, 3)

    m1.inserir(0, 0, 1)
    m1.inserir(0, 1, 2)
    m1.inserir(0, 2, -3)
    m1.inserir(1, 0, 3)
    m1.inserir(1, 1, 4)

    m2.inserir(0, 0, -2)
    m2.inserir(0, 1, 1)
    m2.inserir(1, 1, 3)
    m2.inserir(2, 0, 5)
    m2.inserir(2, 1, -4)

    m3 = multiplica_matriz(m1, m2)
    """
    resultado esperado
        -17 19 0 
        -6 15 0
    """
    m3.imprime()
