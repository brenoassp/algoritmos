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
