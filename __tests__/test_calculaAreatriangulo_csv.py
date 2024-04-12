import pytest;
from calculadoraGeometrica import calculaAreaTriangulo;
from utils.utils import read_csv;

@pytest.mark.parametrize('base, altura, resultado_esperado',
                        read_csv('./fixtures/massa_triangulo.csv')
                        )
def test_calculaAreaTriangulo_csv(base, altura, resultado_esperado):
    resultado_obtido = calculaAreaTriangulo(float(base),float(altura))
    assert resultado_obtido == float(resultado_esperado)