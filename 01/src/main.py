
from cadastro.cadastro_view import CadastroView
from relatorio.relatorio_view import RelatorioView

cadastro_view = CadastroView()
relatorio_view = RelatorioView()

while True:
    print("""" ----- Inicialização ------
    1 - Cadastrar funcionario
    2 - Relatorio
    3 - Sair
    """)
    opcao = input("Digite a opcão desejada: ")

    match opcao:
        case "1":
            cadastro_view.executar()

        case "2":
            relatorio_view.exibir_relatorio()

        case "3":
            break

        case _:
            print("Entrada invalida!")
