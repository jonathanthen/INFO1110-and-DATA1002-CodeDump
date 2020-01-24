def pamper(cats):
	# Write your code here!
	# You can assume that `cats` is a list.
	if len(cats) == 0:
		print("There are no cats here :(")
		return "No cats :("
	i = 0
	longest = cats[0]
	while i < len(cats):
		print("{} is being fed. {} looks happy!".format(cats[i], cats[i]))
		if len(cats[i]) >= len(longest):
			longest = cats[i]
		i += 1
	return longest
	
	
# You don't have to write anything out here! But if you want to just 
# see what your code is producing, you can uncomment the following
# and make modifications as you see fit:


# Re-comment out this code when you are done testing!
#some_list = ['cat', 'names', 'go', 'here']
#ret = pamper(some_list)
#print(ret)		# Is this what I was expecting?
