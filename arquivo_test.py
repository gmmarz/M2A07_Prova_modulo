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
            print('Para Matricula digitar apenas números inteiros')
        if not continuar_operacao():
            return dic_alunos

def remover_alunos(dic_alunos:dict)-> dict:
    
    while True:
        if len(dic_alunos) == 0:
            print('Dicionário de alunos vazio')
            print('Não é possível continuar com a remoção')
            return dic_alunos
        else:

            try:
                aluno_id = int(input('Digite a matrícula do aluno: '))
                if aluno_id not in dic_alunos:
                    print('Matricula digitada não existe. Não é possível excluir')
                else:
                    print(f'Matricula: {aluno_id}, nome: {dic_alunos[aluno_id]} foi removido')
                    dic_alunos.pop(aluno_id)
            except ValueError:
                print('Para Matricula digitar apenas números inteiros')
        if not continuar_operacao():
            return dic_alunos
            
    

dic_alunos = {1: 'gui', 2: 'bi', 3: 'Theo'}

dic_alunos = adicionar_aluno(dic_alunos)

print(dic_alunos)

print('TESTE PARA REMOVER')

dic_alunos = remover_alunos(dic_alunos)

print(dic_alunos)
