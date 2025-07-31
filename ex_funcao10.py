'''10.Crie uma função que recebe um número entre 1 e 20
e imprime o número por extenso. Ex.: 1/um, 9/nove, 
15/quinze, etc. Se o valor não estiver no intervalo,
informar que é inválido.'''
def extenso(num) :
    lista=['zero','um','dois','três','quatro','cinco',
           'seis','sete','oito','nove','dez','onze',
           'doze','treze','catorze','quinze','dezesseis',
           'dezessete','dezoito','dezenove','vinte']
    
    if num > 20 or num < 1 :
        print("Inválido.")
    else:
        print(lista[num])
##########################################################
extenso(15)        
