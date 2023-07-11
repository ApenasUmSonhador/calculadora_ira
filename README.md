# calculadora_ira
Algoritmo capaz de calcular o IRA Individual de maneira mais fácil.

Lógica:
    1. Receber do usuário disciplina do curso (código).
    2. Receber carga horária da disciplina.
    3. Receber nota final da disciplina.
        3.1 Descobrir se disciplina foi trancada/reprovada por nota/reprovada por falta/ aprovada.
    4. Receber periodo que a disciplina foi cursada.
    5. Colocar (1), (2), (3), (4) e (5) em um dicionário para consulta posterior.
    6. Calcular somatório das cargas horárias das disciplinas trancadas (T).
    7. Calcular somatório das cargas horárias das disciplinas cursadas ou trancadas (C).
    8. Calcular IRA individual via:
        IRA = (1 - (0.5 * T)/C)*((somatorio: nota final * periodo * carga horaria)/somatorio: carga horaria * periodo) * 1000
    9. Devolver ao usuário o IRA e os (5).
