def word(arg):
	red = []
	l = len(arg)
	i = 1
	while i < l:
		if arg[i-1] == arg[i]:
			red.append(arg[i-1])
		else:
