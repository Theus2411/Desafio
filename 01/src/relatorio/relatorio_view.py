from database.dados import DADOS
from salario.salario_controller import SalarioController


class RelatorioView:
    def __init__(self):
        self.salario_core = SalarioController()
        self.relatorio = []
        pass
    def adicionar_dados(self, nome, salario, inns, irrf, liquido):
        self.relatorio.append({
            'nome': nome,
            'salario': salario,
            'inss': inns,
            'irrf': irrf,
            'liquido': liquido,
        })


    def obter_dados(self):
        for funcionario in DADOS:
            match funcionario["type"]:
                case "estagiario":
                    salario, inns, irrf, liquido = self.salario_core.calcular_salario_estagiario(funcionario)

                case "clt":
                    salario, inns, irrf, liquido = self.salario_core.calcular_salario_clt(funcionario)

                case "freelancer":
                    salario, inns, irrf, liquido = self.salario_core.calcular_salario_freelancer(funcionario)

            self.relatorio.append(self.adicionar_dados(funcionario["nome"], salario, inns, irrf, liquido))


    def exibir_relatorio(self):
        self.obter_dados()
        print("==================== Relatorio ====================")
        for relatorio in self.relatorio:
            if relatorio == None:
                continue

            print(f"Nome:  {relatorio["nome"]}")
            print(f"Salario Bruto: R${relatorio["salario"]}")
            print(f"Desconto Inss: R${relatorio["inss"]}")
            print(f"Desconto irrf: R${relatorio["irrf"]}")
            print(f"Valor Liquido: R${relatorio["liquido"]}")
            print("======================================")


if __name__ == '__main__':
    relatorio = RelatorioView()
    relatorio.obter_dados()
