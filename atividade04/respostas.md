# Atividade 04

## Respostas das questões 1, 2 e 3

**Aluno**: Luís Henrique Lima Santos
**Disciplina**: Teste de Software

### Questão 1

É de suma importância testar-se os requisitos não funcionais, uma vez que o teste serve justamente para garantir que 
um RNF foi atendido. Por exemplo, digamos que um sistema pode receber uma quantidade muito alta de usuários simultaneamente,
se não for realizado um teste de carga, estressando o sistema e observando seu comportamento, será impossível prever
o que irá acontecer no sistema real

### Questão 2

Para os exemplos em questão, será feito para a linguagem python

* Segurança: temo o PYT (Python Taint), que é um projeto open-source para análise e detecção de comandos de injeção, 
cross-site scripting, SQL injection entre outros
* Desempenho: Na linguagem python é possível tanto utilizar a IDE, por meio de comandos de profiling (apenas algumas IDE's
terão essa capacidade) como também é possível utilizar bibliotecas externas como o cprofile
* Usabilidade: Também é possível utilizar a próprio IDE ou extensões, presentes em IDE's como as da Jetbrains por exemplo

### Questão 3

* **Utilizando Testes de Partição de Equivalência**

Para o cartão de crédito, as partições definidas foram:

Dado `X` como o valor limite do cartão de crédito e `Z`, onde `Y = \{Z / Z < X}` como valor que é permitido passar por 
aproximação sem uso de senha. Por exemplo:

Dado, que temos um limite de R$ 1000,00, logo:

* Não são permitos valores negativos
* Valores até R$ 200,00 passam por aproximação sem uso de senha
* Valores acima de R$ 200,00 até 1000,00 são válidos mas precisam de senha
* Valores acima de R$ 1000,00 são inválidos


| Caso de teste | Entrada |                                               Saída |
|:--------------|:-------:|----------------------------------------------------:|
| C1            |   -20   |                          Valor sequer é considerado |
| C2            |   150   |   É possível passar por aproximação sem pedir senha |
| C3            |   500   | É possível passar por aproximação, requisitar senha |
| C4            |  1100   |                    Não é possível realizar a compra |

* **Utilizando Análise do Valor Limite**

Usando como base as restrições e exemplo anterior, mas agora considerando valores limite: entre R$ 0,00 e R$ 1000,00

| Caso de teste | Entrada |                                               Saída |
|:--------------|:-------:|----------------------------------------------------:|
| C1            |   150   |   É possível passar por aproximação sem pedir senha |
| C3            |   500   | É possível passar por aproximação, requisitar senha |
| C4            |  1100   |                    Não é possível realizar a compra |
