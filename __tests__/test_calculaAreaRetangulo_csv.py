import pytest;
from calculadoraGeometrica import calculaAreaRetangulo;
from utils.utils import read_csv;

@pytest.mark.parametrize('base, altura, resultado_esperado',
                        read_csv('./fixtures/massa_retangulo.csv')
                        )

def test_calculaAreaRetangulo_csv(base, altura, resultado_esperado):
    resultado_obtido = calculaAreaRetangulo(float(base), float(altura));
    assert resultado_obtido == float(resultado_esperado)