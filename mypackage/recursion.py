def sum_array(array):
    '''Return sum of all items in array'''
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def factorial(n):

    '''Return n!'''
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):

    '''Return word in reverse'''
    if len(word)==0:
        return word
    else:
        return reverse(word[1:]) + word[0]        
