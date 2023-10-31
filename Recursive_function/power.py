def power(n , index):

    if index == 0:

        return 1
    else:

        return power ( n , index - 1 ) * n



print(power(5 , 4 ))
