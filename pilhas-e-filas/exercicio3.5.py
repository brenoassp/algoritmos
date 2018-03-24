class No:
    valor = None
    linha = None
    coluna = None
    no_direita = None
    no_baixo = None


class Matriz:
    """
    Matriz esparsa, estou considerando que começa com índice 0 nas linhas e colunas
    """
    linhas = None
    colunas = None
    lista_linhas = None
    lista_colunas = None

    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.lista_linhas = [None] * linhas
        self.lista_colunas = [None] * colunas

    def busca(self, linha, coluna):
        if linha >= self.linhas or coluna >= self.colunas:
            raise ValueError("Indice invalido")

        if self.linhas > self.colunas:
            atual = self.lista_linhas[linha]
            while atual:
                if atual.coluna == coluna:
                    return atual
                atual = atual.no_direita
            return None
        else:
            atual = self.lista_colunas[coluna]
            while atual:
                if atual.linha == linha:
                    return atual
                atual = atual.no_baixo
            return None

    def inserir(self, linha, coluna, valor):
        """
        :param linha: indice da linha
        :param coluna: indice da coluna
        :param valor: valor
        """
        if linha >= self.linhas or coluna >= self.colunas:
            raise ValueError("Indice invalido")

        no = No()
        no.valor = valor
        no.linha = linha
        no.coluna = coluna

        if not self.lista_linhas[linha]:
            self.lista_linhas[linha] = no

            if not self.lista_colunas[coluna]:
                self.lista_colunas[coluna] = no
                return
            else:
                no_buscado = self.busca(linha, coluna)
                if not no_buscado: # não existe nó para essa posição ainda
                    no_anterior_coluna = None
                    no_atual_coluna = no_anterior_coluna
                    while no_atual_coluna and (no_atual_coluna.linha < no.linha):
                        no_anterior_coluna = no_atual_coluna
                        no_atual_coluna = no_atual_coluna.no_baixo
                    if not no_atual_coluna: # o nó inserido estará na maior linha (com no_baixo null)
                        no_anterior_coluna.no_baixo = no
                    elif not no_anterior_coluna: # o nó inserido estará entre dois nós OU será o primeiro nó da coluna
                        no.no_baixo = no_atual_coluna
                        self.lista_colunas[coluna] = no
                    else:
                        no.no_baixo = no_atual_coluna
                        no_anterior_coluna.no_baixo = no
                else:
                    no_buscado.valor = valor
                return

