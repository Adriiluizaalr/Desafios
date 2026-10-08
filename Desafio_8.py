# Na mesma linha dos exercicios anteriores crie uma função chamada pode_ver_filme que recebe a idade e a classificação indicativa do filme
# classificacao: 'L' (Livre), 'Maior de 12', 'Maior de 14', 'Maior 16', 'Maior 18'

#Exemplo:
# idade = 10
# classificacao = 'Maior de 12'
# resposta = "Não pode assitir o filme"


def pode_ver_filme(idade, classificacao):
    if classificacao == 'L':
        pode = True
    elif classificacao == 'Maior de 12' and idade >= 12:
        pode = True
    elif classificacao == 'Maior de 14' and idade >= 14:
        pode = True
    elif classificacao == 'Maior 16' and idade >= 16:
        pode = True
    elif classificacao == 'Maior 18' and idade >= 18:
        pode = True
    else:
        pode = False

    if pode:
        resposta = "Pode assistir o filme"
    else:
        resposta = "Não pode assitir o filme"
        
    print(resposta)
    return resposta

idade = 10
classificacao = 'Maior de 12'

pode_ver_filme(idade, classificacao)




