class SalarioController:
    def calcular_salario_estagiario(self, estagiario):
        inss = 0
        irrf= 0
        liquido = estagiario["salario"]
        return estagiario["salario"], inss, irrf, liquido

    def calcular_salario_clt(self, funcionario):
        inss = funcionario["salario"] * 0.08
        irrf = 0

        if funcionario["salario"] > 2000:
            irrf = funcionario["salario"] * 0.10

        liquido = funcionario["salario"] - (irrf + inss)
        return funcionario["salario"], inss, irrf , liquido

    def calcular_salario_freelancer(self,funcionario):
        irrf = 0
        total = funcionario["horas"] * funcionario["salario"]
        inss = total * 0.05
        liquido = total - inss
        return total, inss, irrf, liquido

