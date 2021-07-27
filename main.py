first  = str(input('First  : '))
second = str(input('Second : '))

#Identify variables order
xy = ''

#################################################################################
def make_vars(eq):
    global xy
    
    #remove spaces
    eq = eq.replace(' ','')
    
    a = ''
    b = ''
    
    #Identify variables order
    ab = ''
    
    #add counter to get position
    counter = -1
    
    for i in eq.split('=')[0]:
        counter+=1
        
        #to make variables
        if i.isalpha():
            #add 1 to contantless variables 
            if counter==0 or a=='+' or a=='-':
                a+='1'
            elif not(eq.split('=')[0][counter-1].isnumeric()) and not(len(ab)==0):
                b+='1'
                
            ab+=i
            continue
        
        #check second variable or first
        if len(ab)==0:
            a += i
        else:
            b += i
    #str to int
    else:
        a = int(a)
        b = int(b)
    
    #to variable swap
    if ab==xy or xy=='':
        xy = ab
        return [a,b]
    else:
        return [b,a]
#######################################################################################

#Results    
p = int(first.split('=')[1])
q = int(second.split('=')[1])

#Get variables from string
a,b = make_vars(first)
c,d = make_vars(second)

#Formula
e = a*d - b*c
x = (p*d - b*q)/e
y = (a*q - p*c)/e

print(f'{xy[0]} = {x}\n{xy[1]} = {y}')
