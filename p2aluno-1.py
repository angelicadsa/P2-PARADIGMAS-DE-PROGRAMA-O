class Aluno:
    QUANTIDADE_NOTAS = 3

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    def adicionar_notas(self):
        for i in range(self.QUANTIDADE_NOTAS):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i + 1} (0 a 10): "))
                    if 0 <= nota <= 10:
                        self.notas.append(nota)
                        break
                    print("Nota inválida! Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida! Digite um número.")

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()

        if media >= 7:
            return "Aprovado!"
        elif media >= 5:
            return "Recuperação."
        return "Reprovado."

    def exibir_dados(self):
        print("\n/////////////////////////////")
        print("       DADOS DO ALUNO")
        print("///////////////////////////////")
        print(f"Nome: {self.nome}")
        print(f"Quantidade de letras do nome: {len(self.nome)}")
        print(f"Matrícula: {self.matricula}")

        print("\nNotas:")
        for i, nota in enumerate(self.notas, start=1):
            print(f"Nota {i}: {nota:.2f}")

        print(f"\nMédia: {self.calcular_media():.2f}")
        print(f"Situação: {self.situacao()}")


class SistemaEscolar:
    def executar(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")

        aluno = Aluno(nome, matricula)
        aluno.adicionar_notas()
        aluno.exibir_dados()


if __name__ == "__main__":
    sistema = SistemaEscolar()
    sistema.executar()
