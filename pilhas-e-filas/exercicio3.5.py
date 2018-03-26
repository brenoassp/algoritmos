class No:
    valor = None
    linha = None
    coluna = None
    no_direita = None
    no_baixo = None

    def __str__(self):
        return 'linha {0} coluna {1} valor {2}'.format(self.linha, self.coluna, self.valor)


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
        def insere_meio_linha(no):
            no_buscado = self.busca(linha, coluna)
            if not no_buscado:
                no_anterior_linha = None
                no_atual_linha = self.lista_linhas[linha]
                while no_atual_linha and (no_atual_linha.coluna < no.coluna):
                    no_anterior_linha = no_atual_linha
                    no_atual_linha = no_atual_linha.no_direita
                if not no_atual_linha:
                    no_anterior_linha.no_direita = no
                elif not no_anterior_linha:
                    no.no_direita = no_atual_linha
                    self.lista_linhas[linha] = no
                else:
                    no.no_direita = no_atual_linha
                    no_anterior_linha.no_direita = no
            else:
                no_buscado.valor = valor
            return no

        def insere_meio_coluna(no):
            no_buscado = self.busca(linha, coluna)
            if not no_buscado:  # não existe nó para essa posição ainda
                no_anterior_coluna = None
                no_atual_coluna = self.lista_colunas[coluna]
                while no_atual_coluna and (no_atual_coluna.linha < no.linha):
                    no_anterior_coluna = no_atual_coluna
                    no_atual_coluna = no_atual_coluna.no_baixo
                if not no_atual_coluna:  # o nó inserido estará na maior linha (com no_baixo null)
                    no_anterior_coluna.no_baixo = no
                elif not no_anterior_coluna:  # o nó inserido estará entre dois nós OU será o primeiro nó da coluna
                    no.no_baixo = no_atual_coluna
                    self.lista_colunas[coluna] = no
                else:
                    no.no_baixo = no_atual_coluna
                    no_anterior_coluna.no_baixo = no
            else:
                no_buscado.valor = valor
            return no

        def insere_meio(no, posicao):
            '''
            :param no:
            :param posicao: 'L' linha, 'C' coluna ou 'A' ambos
            :return:
            '''
            if posicao == 'A':
                insere_meio_linha(no)
                insere_meio_coluna(no)
            elif posicao == 'L':
                self.lista_colunas[no.coluna] = insere_meio_linha(no)
            elif posicao == 'C':
                self.lista_linhas[no.linha] = insere_meio_coluna(no)
            else:
                raise ValueError("Posicao invalida")

        if linha >= self.linhas or coluna >= self.colunas:
            raise ValueError("Indice invalido")

        no = No()
        no.valor = valor
        no.linha = linha
        no.coluna = coluna

        primeira_linha = self.lista_linhas[linha]
        primeira_coluna = self.lista_colunas[coluna]

        if not primeira_linha and not primeira_coluna:
            self.lista_linhas[linha] = no
            self.lista_colunas[coluna] = no
            return
        if primeira_linha and primeira_coluna:
            insere_meio(no, 'A')
            return
        if primeira_coluna and not primeira_linha:
            insere_meio(no, 'C')
            return
        if not primeira_coluna and primeira_linha:
            insere_meio(no, 'L')
            return

        return

    def imprimir(self):
        for i in self.lista_linhas:
            if i:
                no_atual = i
                while no_atual:
                    print(no_atual)
                    no_atual = no_atual.no_direita


if __name__ == '__main__':

    m = Matriz(5, 5)
    m.inserir(0, 0, 40)
    m.inserir(0, 1, 30)
    m.inserir(1, 0, 200)
    m.inserir(1, 1, 37)
    m.inserir(2, 1, 8)

    m.imprimir()
