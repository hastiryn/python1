while True:
    try:
        user_input1=input('enter a number: ')
        operator=input('what do you wanna do')
        user_input2=input('enter an other number')
        
        if operator=='+':
            result=float(user_input1)+float(user_input2)
        elif operator=='-':
            result=float(user_input1)-float(user_input2)
        elif operator=='/':
            result=float(user_input1)/float(user_input2)
        elif operator=='*':
            result=float(user_input1)*float(user_input2)
        else:
            raise ValueError("only use '+ , - , * , / '  ")
        print(f'your result: {result}')

        again=input('do you want an other calcuation(yes/no)')
        if again.lower() !='yes':
            print('by')
            break

        
    except ValueError:
        print('enter number')
    except ZeroDivisionError:
        print('numbers cant be divided by zero')
    
    

    
                 






















                 
