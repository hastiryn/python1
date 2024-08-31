##import turtle as t
##colors=['red','blue','yellow','green']
##
##for s in range(0,4):
##    t.rt(120)
##
##    for i in colors:
##        t.color (i)
##        t.fd(300)
##        t.rt(90)


##for i in range(4):
##    try:
##        l=int(input('give me a number'))
##        m=int(input('give me a number'))
##
##        print(l+m)
##    except ValueError:
##        print('try again')


##password=60
##
##for i in range(3):
##    try: 
##        pas=int(input("what is the password"))
##        if pas==password:
##            print('box is opened')
##            break
##        else:
##            print('try again')
##    except ValueError:
##        print('enter a number
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
    
    

    
                 






















                 
