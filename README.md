# Cadastro e média de aluno — Programação Orientada a Objetos
# Estudante: Angélica da Silva Alves

Programa de terminal em Python que refatora o trabalho original em C utilizando o paradigma de Programação Orientada a Objetos (POO). O programa solicita nome, matrícula e três notas, valida as notas entre 0 e 10, calcula a média e informa a situação acadêmica.

## Requisitos

- Python 3.8 ou superior
- Nenhuma biblioteca externa

## Como executar

Abra um terminal na pasta do projeto e execute:

```bash
python p2aluno-1.py
```

Em alguns sistemas, o comando pode ser:

```bash
python3 p2aluno-1.py
```

## Exemplo de uso

```text
Digite o nome do aluno: angela da Silva
Digite a matrícula do aluno: 2024001
Digite a nota 1 (0 a 10): 8
Digite a nota 2 (0 a 10): 7,5
Digite a nota 3 (0 a 10): 9
```

O programa aceita ponto ou vírgula como separador decimal. Valores fora do intervalo são rejeitados e solicitados novamente.

## Organização e conceitos de POO

- `Aluno`: representa o aluno e mantém nome, matrícula e notas. A propriedade `media` calcula a média, `situacao` determina o resultado e `exibir_dados()` apresenta o boletim.
- `SistemaEscolar`: controla a interação com o usuário, coleta as entradas e cria o objeto `Aluno`.
- `QUANTIDADE_NOTAS`: constante da classe `Aluno` que define a quantidade de notas consideradas.

A separação entre a entidade (`Aluno`) e a interação (`SistemaEscolar`) torna o código mais organizado e fácil de manter.

## Regras de situação

- Média maior ou igual a 7: **Aprovado**
- Média maior ou igual a 5 e menor que 7: **Recuperação**
- Média menor que 5: **Reprovado**

## cod feito com amor e odio!! aproveiteee//////////////////////
