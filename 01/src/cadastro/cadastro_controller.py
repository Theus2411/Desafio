import os

from database.dados import DADOS

class CadastroController:
    def __init__(self):
        pass

    def cadastrar_estagiario(self):
        nome, salario, horas = self.pedir_dados("estagiario")
        DADOS.append({
            "nome": nome,
            "salario": salario,
            "type": 'estagiario',
        })


    def cadastrar_clt(self):
        nome, salario, horas = self.pedir_dados("clt")
        DADOS.append({
            "nome": nome,
            "salario": salario,
            "type": 'clt',
        })

    def cadastrar_freelancer(self):
        nome, salario, horas = self.pedir_dados("freelancer")
        DADOS.append({
            "nome": nome,
            "salario": salario,
            "horas": horas,
            "type": 'freelancer',
        })


    def pedir_dados(self, type:str):
        try:
            horas = None
            nome = input("Nome: ")

            if nome.replace(' ', '').isalpha():
                pass
            else:
                raise Exception("Numeros não permitidos neste lugar, nao use!")

            if nome is None:
                print("Entrada invalida!")
                input("Pressione enter para continuar...")
                return None

            if type == 'clt' or type == 'estagiario':
                salario = float(input("Salario: "))

            elif type == 'freelancer':
                salario = float(input("Ganho por hora: "))
                horas = int(input("Horas trabalhadas por dia: "))
            else:
                print("Entrada invalida!")
                input("Pressione enter para continuar...")


            return nome, salario, horas


        except Exception:
            print("Entrada invalida!")
            os.system("clear")
            return self.pedir_dados(type)





