import pytest;
from calculadoraGeometrica import calculaAreaQuadrado;
from utils.utils import read_csv;

@pytest.mark.parametrize('lado, resultado_esperado',
                        read_csv('./fixtures/massa_quadrado_negativo.csv')
                        )

def test_calculaAreaQuadrado_csv(lado, resultado_esperado):
    resultado_obtido = calculaAreaQuadrado(float(lado))
    if type(resultado_esperado) == float:
        resultado_esperado = float(resultado_esperado)
    assert resultado_obtido == resultado_esperado