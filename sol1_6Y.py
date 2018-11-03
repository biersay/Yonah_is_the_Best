def compress(s):
	if type(s) != str:
		print("Give me strings or give me death!")
		return(-1)
	l = len(s)
	output = ''
	if l == 0:
		return(output)
	current = s[0]
	i = 1
	count = 1
	while i < l:
		while(i < l and s[i] == current):
			count += 1
			i += 1
		if i < l:
			output = output + current + str(count)
			current = s[i]
			count = 1
		i += 1
	output = output + current + str(count)
	if len(output) < len(s):
		return(output)
	else:
		return(s)
