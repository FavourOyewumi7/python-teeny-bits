re = int(input('Enter a number: '))



def fib(re):
    a = 0
    b = 1
    if re <= 0:
        print('Bad input')
    elif re == 1:
        return b
    else:
        for i in range(2, re):
            c = a+b
            a = b
            b = c
        return b
            

def fibb(re):
	fibarr = [0,1]
	if re <= 1:
		return 1
	elif re <len(fibarr):
		return fibarr[re-1]
	else:
		temp = fibb(re-1) + fibb(re-2)
		fibarr.append(temp)
		return temp
    

fibb(re)
