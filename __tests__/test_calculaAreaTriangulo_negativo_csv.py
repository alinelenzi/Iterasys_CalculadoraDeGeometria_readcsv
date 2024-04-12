import pytest;
from calculadoraGeometrica import calculaAreaTriangulo;
from utils.utils import read_csv;

@pytest.mark.parametrize('base, altura, resultado_esperado',
                        read_csv('./fixtures/massa_triangulo_negativo.csv')
                        )
def test_calculaAreaTriangulo_csv(base, altura, resultado_esperado):
    resultado_obtido = calculaAreaTriangulo(float(base),float(altura))
    if type(resultado_esperado) == float:
        resultado_esperado = float(resultado_esperado)
    assert resultado_obtido == resultado_esperado