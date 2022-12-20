import math

def welcome():
    print('''
    Welcome to Calculator!!! have fun with math
'''       
    )

def calculate():
    operation = input('''
    Por favor informe a formula matematica desejada:
    + for add
    - for sub
    * for mult
    / for div
    ** for power
    %  for modulo
    '''
    )

    num_1 = float(input('Entre com o primeiro numero:'))
    num_2 = float(input('Entre com o segundo numero:'))

    if operation == '+':
        print('{} + {} = '.format(num_1, num_2))
        print(num_1 + num_2)

    elif operation == '-':  
        print('{} - {} = '.format(num_1, num_2))
        print(num_1 - num_2)

    elif operation == '*':    
        print('{} * {} = '.format(num_1, num_2))
        print(num_1 * num_2)

    elif operation == '/':    
        print('{} / {} = '.format(num_1, num_2))
        print(num_1 / num_2)
        
    else:
        print('Caractere nao identificado, tente novamente.')
    
    again()
    
    contador = 0
    

def again():
        
    calc_again = input('''   
        Do you want to calculate again?
        Please type Y for YES or N for NO.
''')
        
    if calc_again.upper() == 'Y':
        calculate() 
        BREAK   
    elif calc_again.upper() == 'N':
        print('See you later... ')
            
    else:
       again()
    
welcome()     
calculate()