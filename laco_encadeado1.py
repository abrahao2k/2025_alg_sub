# laço encadeado (while dentro de while)

linha = 1
while linha <= 6 :
    print("ESTOU NA LINHA", linha)
    
    ## controle das colunas #######################
    coluna = 1
    while coluna <= 4 :
        print("=== COLUNA ", coluna)
        coluna += 1
    ##############################################
    
    linha += 1  # vai pra linha seguinte