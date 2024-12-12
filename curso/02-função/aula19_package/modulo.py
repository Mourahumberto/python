# tem que importar mesmo mesmo eles estando no mesmo layer, pois o main não está. e o main precisa saber onde fica.
from aula19_package.modulo_b import fala_oi
def soma_modulo(x, y):
    return x + y

fala_oi()