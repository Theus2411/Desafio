import os

from database.dados import DADOS
from cadastro.cadastro_controller import CadastroController


class CadastroView:
    def __init__(self):
        self.core = CadastroController()
        pass



    def exibir_menu(self):
        print("""
        --------- Cadastro --------
        1 - Estagiario
        2 - CLT
        3 - Freelancer
        4 - Listar funcionario
        5 - Voltar
        """)

    def ler_comando(self):
        return int(input("Escolha sua opção? "))


    def opcao_menu(self):
        while True:
            os.system("clear")
            self.exibir_menu()
            opcao = self.ler_comando()

            match opcao:
                case 1:
                    self.core.cadastrar_estagiario()
                case 2:
                    self.core.cadastrar_clt()
                case 3:
                    self.core.cadastrar_freelancer()
                case 4:
                    os.system("clear")
                    for funcionario in DADOS:
                        print(funcionario["nome"])
                    input("Digite qualquer tecla para sair!")
                case 5:
                    break

                case _:
                    print("Opção invalida!")
                    input("Digite qualquer tecla para sair!")

    def executar(self):
        self.opcao_menu()




if __name__ == '__main__':
    cadastro = CadastroView()
    cadastro.executar()