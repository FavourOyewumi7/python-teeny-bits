li = list(map(int, input('Enter a list on numbers seperated by commas: ').strip().split(',')))


print('You have {} values in your list, they are {}'.format(len(li), li))




def gett(wee):
	listo = []
	if max(wee) in wee:
		listo.append(max(wee))
		print('This is the first large number: {}'.format(max(wee)))
		wee.remove(max(wee))
		print('Length of list after 1st deduction is {}'.format(len(li)))
		print(li)
	if max(wee) in wee:
		listo.append(max(wee))
		print('This is the second large number: {}'.format(max(wee)))
		wee.remove(max(wee))
		
	print(listo)
	print(listo[0]*listo[1])

gett(li)

