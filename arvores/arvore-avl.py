class No:

    def __init__(self, chave):
        self.chave = chave
        self.dir = None
        self.esq = None
        self.fb = 0


class ArvoreAVL:

    def __init__(self):
        self.raiz = None
        self.n = 0

    def insere(self, no):  # similar ao da ABB, com correção para ajustar os fbs executando rotações
        if not isinstance(no, No):
            raise Exception("deve ser fornecido um objeto do tipo No para insercao")
        if self.raiz is None:
            self.raiz = no
        else:
            filho_avo_atualizar = 'N'
            atual = self.raiz
            avo = None
            while True:
                # se nenhum do filhos for None, avo será o atual antes de descer o atual
                if atual.esq is not None and atual.dir is not None:
                    avo = atual
                if no.chave < atual.chave:  # inserir a esquerda
                    if atual.esq is None:
                        atual.esq = no
                        atual.fb += 1
                        return
                    elif atual.dir is None:
                        pai = atual
                        atual = atual.esq

                        if no.chave < atual.chave:
                            # LL
                            atual.esq = no
                            rotacao_dir(pai, avo, filho_avo_atualizar)
                            pai.fb -= 1
                            return
                        else:
                            # LR
                            no.esq = atual
                            pai.esq = no
                            rotacao_dir(pai, avo, filho_avo_atualizar)
                            return
                    else:
                        filho_avo_atualizar = 'E'
                        atual = atual.esq
                else:  # inserir a direita
                    if atual.esq is not None and atual.dir is not None:
                        avo = atual
                    if no.chave > atual.chave:  # inserir a esquerda
                        if atual.dir is None:
                            atual.dir = no
                            atual.fb += 1
                            return
                        elif atual.esq is None:
                            pai = atual
                            atual = atual.dir

                            if no.chave > atual.chave:
                                # RR
                                atual.dir = no
                                rotacao_esq(pai, avo, pai.dir, filho_avo_atualizar)
                                pai.fb -= 1
                                return
                            else:
                                # RL
                                no.dir = atual
                                pai.dir = no
                                rotacao_esq(pai, avo, pai.dir, filho_avo_atualizar)
                                return
                        else:
                            filho_avo_atualizar = 'D'
                            atual = atual.esq


    def imprime(self):
        self.imprime_(self.raiz)

    def imprime_(self, raiz):
        if raiz:
            self.imprime_(raiz.esq)
            print(raiz.chave)
            self.imprime_(raiz.dir)


def rotacao_dir(no, avo, filho_avo_atualizar):
    # tem que garantir que filho a esquerda
    # do no passado como parametro não é None

    aux = no.esq
    no.esq = aux.dir
    aux.dir = no
    if avo:
        if filho_avo_atualizar == 'D':
            avo.dir = aux
        elif filho_avo_atualizar == 'E':
            avo.esq = aux
    return aux


def rotacao_esq(pai, avo, filho_dir, filho_avo_atualizar):
    if not filho_dir:
        raise Exception("filho_dir nao pode ser None")
    pai.dir = filho_dir.esq
    filho_dir.esq = pai
    if avo:
        if filho_avo_atualizar == 'D':
            avo.dir = filho_dir
        elif filho_avo_atualizar == 'E':
            avo.esq = filho_dir
    return filho_dir


if __name__ == '__main__':
    print('teste')