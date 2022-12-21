from codigo.BytebankClass import Funcionario
import pytest
from pytest import mark

data_deflault='01/01/1999'
salario_deflault = 1111
nome_default='Rodrigo Teste'

class TestClass:
    def test_idade_recebendo_13_11_2000_retornara_22(self):
        entrada = '13/11/2000'
        esperado = 22

        func_test = Funcionario(nome_default,entrada,salario_deflault)

        resultado= func_test.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        esperado = 90000

        funconario_teste = Funcionario(nome_default, '11/11/2000', entrada_salario)
        funconario_teste.decrescimo_salario() # when
        resultado = funconario_teste.salario

        assert resultado == esperado  # then

    @mark.calcular_bonus
    def teste_quando_calcular_bonus_recebe_1000_retorna_100(self):
        entrada = 1000
        esperado = 100

        funconario_teste = Funcionario(nome_default, '11/11/2000', entrada)
        resultado = funconario_teste.calcular_bonus()

        assert resultado == esperado  # then
    @mark.calcular_bonus
    def teste_quando_calcular_bonus_receber_salario_muito_alto(self):
        with pytest.raises(Exception):
            entrada = 10000000

            funconario_teste = Funcionario(nome_default, '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()

            assert resultado

