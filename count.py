mylist = input('Enter your list: ')
mylist = [int(x) for x in mylist.split(' ')]

points = [0,15,10,10,25,15,15,20,10,25,20,25,25,5,20,30,20,15,10,5,5,15,20,20,20,20,15,15,20,25,15,20,20,20,15,40,15,30,35,20,25,15,20,15,25,20,25,20,25,20,10]

total = 0
for index in mylist:
	total += points[index]

print (total)