import numpy as np
import os

'''
Objetivos

    Criar vetor de 4 posicoes
    para tanto temos que criar

    checa_vetor4
    checa_matriz33
    checa_matriz44
    cria_vetor4
    checa_matriz

    cria_operador4 (transformacao homogenea)
    
'''
def checa_vetor3(m):
    #funcao para set vetor nao seja 3,1
    # se nao for 3,1 gerar uma excecao
    if m.shape != (3,1):
        raise ValueError("O seu vetor deve ter 3 linha e 1 coluna")
    else: print('Vetor correto!')
def checa_vetor4(v: np.ndarray) -> None:
    """
    Verifica se um vetor é um vetor de 4 linhas e uma coluna. Caso não seja, levanta uma exceção.
    :param v: vetor a verificar
    :return: nenhum.
    """
    if v.shape != (4, 1):
        raise ValueError('O vetor não é 4x1!')

def checa_matriz33(m: np.array)-> None:
    '''
    '''
    
    if m.shape != (3,3):
        raise ValueError('Matriz deve ser 3x3')

def checa_matriz44(m: np.array)-> None:
    '''
    '''

    if m.shape !=(4,4):
        raise ValueError('Matriz deve ser 4x4')
def produto_escalar(v1: np.ndarray, v2: np.ndarray) -> float:
    """
    Calcula o produto escalar entre dois vetores.
    :param v1: vetor (np.ndarray) coluna de 3 elementos
    :param v2: vetor (np.ndarray) coluna de 3 elementos
    :return: escalar: resultado de v1.v2
    """
    checa_vetor3(v1)
    checa_vetor3(v2)
    return np.sum(v1 * v2)
def norma_vetor(v: np.ndarray) -> float:
    """
    Calcula a norma de um vetor
    :param v: vetor (np.ndarray) coluna de 3 elementos
    :return: escalar: norma do vetor
    """
    return np.sqrt(produto_escalar(v, v))
def ang_vetores(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """
    Calcula o ângulo entre dois vetores em radianos.
    :param v1: vetor (np.ndarray) coluna de 3 elementos
    :param v2: vetor (np.ndarray) coluna de 3 elementos
    :return: escalar: ângulo em radianos
    """
    return np.arccos(produto_escalar(v1, v2) / (norma_vetor(v1) * norma_vetor(v2)))

def checa_matriz_rotacao(m3: np.ndarray, det_tol: float = 0.01) -> None:
    """
    Recebe uma matriz (3, 3), verifica suas dimensões e verifica se seu determinante é 1, pois matrizes de rotação devem
    possuir determinante unitário independente do número de rotações realizadas.
    :param m3: matriz a verificar
    :param det_tol: tolerância do valor do determinante
    :return: não há
    """
    checa_matriz33(m3)
    if np.abs(1-np.linalg.det(m3)) > det_tol:
        raise ValueError('O determinante da matriz não é 1.')
    else: print('Matriz correta!')

def cria_vetor4(v3: np.ndarray) -> np.ndarray:
    """
    Recebe um vetor (3, 1) e cria um vetor (4, 1) após concatenar o valor 1 ao final deste vetor.
    :param v3:
    :return:
    """
    checa_vetor3(v3)
    aux = np.ones([4, 1])
    aux[0:3, 0] = v3[0:3, 0]
    return aux
    
def teste(v1):
    checa_vetor4(v1)
def cria_operador4(m_rot_b_a: np.ndarray = np.eye(3), v_o_a: np.ndarray = np.zeros([3, 1]), det_tol: float = 0.01) \
        -> np.ndarray:
    """
    Cria um operador de construção de vetores por transformação homogênea (4, 4) que recebe um vetor origem escrito na
    base 'a' e uma matriz de rotação que leva da base 'b' para a base 'a'.
    :param m_rot_b_a: matriz de rotação associada
    :param v_o_a: vetor origem associado
    :param det_tol:
    :return:
    """
    checa_matriz33(m_rot_b_a)
    checa_matriz_rotacao(m_rot_b_a, det_tol=det_tol)
    checa_vetor3(v_o_a)
    T = np.append(m_rot_b_a, v_o_a, axis=1)
    T = np.append(T, np.asarray([[0, 0, 0, 1]]), axis=0)
    return T

nat = np.append([[1,2,3],[3,4,5]],[[7,8,9]], axis=0)

vet = np.array([[9],[8],[7]])
res = np.append(nat,vet,axis=1)

res = np.append(res,np.array([[0,0,0,1]]),axis=0)

'''distancia entre retas'''
def __distancia_entre_retas_np(po1: np.ndarray, vs1: np.ndarray, po2: np.ndarray, vs2: np.ndarray) -> float:
    """
    *** FUNÇÃO INTERNA AO MÓDULO ***
    Calcula a distância entre duas retas não paralelas no espaço.
    Um ponto na reta i é dado por: Pi = poi + vsi*t, sendo t um parâmetro livre.
    'distancia_entre_retas'
    :param po1: Vetor posição de um ponto de referência na reta 1
    :param vs1: Vetor orientação da reta 1
    :param po2: Vetor posição de um ponto de referência na reta 2
    :param vs2: Vetor orientação da reta 1
    :return: distância entre as retas (float, positivo ou nulo)
    """
    pass

def constroi_vetor(v_b: np.ndarray,m_rot_b_a: np.ndarray = np.eye(3),v_o_a: np.ndarray = np.zeros([3, 1]),det_tol: float = 0.01) -> np.ndarray:
    """
    Recebe um vetor v_b escrito na base 'b'. A partir da matriz de rotação m_rot_b_a e do vetor origem v_o_a, constroi o
    operador de transformação homogênea que constrói um vetor na base 'a' que aponta para o mesmo ponto que o vetor v_b.
    :param v_b: vetor referência na base 'b'
    :param m_rot_b_a: matriz de rotação que leva de 'b' a 'a'
    :param v_o_a: vetor origem da base 'b' escrito na base 'a'
    :param det_tol: tolerância do determinante
    :return: vetor (3, 1) na base a
    """
    checa_vetor3(v_b)
    checa_matriz33(m_rot_b_a)
    checa_matriz_rotacao(m_rot_b_a)
    checa_vetor3(v_o_a)

    T = cria_operador4(m_rot_b_a, v_o_a, det_tol=det_tol)
    v_b4 = cria_vetor4(v_b)

    v = T @ v_b4

    return np.asarray(v[0:3, :])

def __distancia_entre_retas_np(po1: np.ndarray, vs1: np.ndarray, po2: np.ndarray, vs2: np.ndarray) -> float:
    """
    *** FUNÇÃO INTERNA AO MÓDULO ***
    Calcula a distância entre duas retas não paralelas no espaço.
    Um ponto na reta i é dado por: Pi = poi + vsi*t, sendo t um parâmetro livre.
    'distancia_entre_retas'
    :param po1: Vetor posição de um ponto de referência na reta 1
    :param vs1: Vetor orientação da reta 1
    :param po2: Vetor posição de um ponto de referência na reta 2
    :param vs2: Vetor orientação da reta 1
    :return: distância entre as retas (float, positivo ou nulo)
    """
    pass
def __distancia_entre_retas_p(po1: np.ndarray, po2: np.ndarray, vs: np.ndarray) -> float:
    """
    *** FUNÇÃO INTERNA AO MÓDULO ***
    Calcula a distância entre duas retas paralelas no espaço.
    Um ponto na reta i será dado por Pi = poi + vs*t, sendo t um parâmetro independente.
    A verificação sobre o tamanho dos vetores será feita na função pública 'distancia_entre_retas'
    :param po1: Posição de um ponto de referência na reta 1
    :param po2: Posição de um ponto de referência na reta 2
    :param vs: Vetor direção de ambas as retas
    :return: distância entre as retas (float, não negativo)
    """
    pass
def distancia_entre_retas(po1: np.ndarray, vs1: np.ndarray, po2: np.ndarray, vs2: np.ndarray, angtol=1e-3) -> float:
    """
    Calcula a distância entre duas retas no espaço.
    Um ponto na reta i é dado por: Pi = poi + vsi*t, sendo t um parâmetro livre.
    :param po1: Vetor posição de um ponto de referência na reta 1
    :param vs1: Vetor orientação da reta 1
    :param po2: Vetor posição de um ponto de referência na reta 2
    :param vs2: Vetor orientação da reta 1
    :param angtol: Tolerância de ângulo entre as retas para decidir se são paralelas
    :return: Distância entre as retas (float, positivo ou nulo)
    """
    checa_vetor3(po1)
    checa_vetor3(po2)
    checa_vetor3(vs1)
    checa_vetor3(vs2)

    if np.abs(ang_vetores(vs1, vs2)) <= angtol:
        return __distancia_entre_retas_p(po1, po2, vs1)
    else:
        return __distancia_entre_retas_np(po1, vs1, po2, vs2)



if __name__=='__main__':
    os.system('cls')
   
 

    v1 = np.array([[1],[1],[2],[5]])
    try:
        teste(v1)
        print('ok vetor correto')
    except ValueError as v:
        print(v)

