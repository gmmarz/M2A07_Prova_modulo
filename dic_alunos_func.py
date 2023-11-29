from func_auxiliares import continuar_operacao

def adicionar_aluno(dic_alunos:dict)-> dict:
    while True:
        try:
            aluno_id = int(input('Digite a matricula do aluno: '))
            if aluno_id in dic_alunos:
                print('Matricula digitada já existe, tente novamente com outra matrícula')
            else:
                aluno_nome = input('Digite o nome do aluno: ')
                dic_alunos.update({aluno_id:aluno_nome}) 
        except ValueError:
            print('Para Matricula digitar apenas número inteiro')
        if not continuar_operacao():
            return dic_alunos
