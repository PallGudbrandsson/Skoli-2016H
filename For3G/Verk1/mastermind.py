from random import randint

def numInList(list1, list2):
	num = 0
	for x in xrange(0,len(list1)):
		for a in xrange(0,len(list1)):
			if list2[x] == list1[a]:
				num = num + 1


def numInPlace(list1,list2):
	num = 0
	for x in xrange(0,len(list1)):
		if list1[x]==list2[x]:
			num = num + 1
	return num

computerList = [randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9)]
userList = []
win = False

while win ==  False:

	for x in xrange(1,6):
		userList.append(input("select num " + str(x)+" "))

	if numInPlace(computerList,userList) == 5:
		print("you win")
		break

	print(str(numInList(computerList, userList)))
	print("correct number in the wrong place")

	print(str(numInPlace(computerList, userList)))
	print("in the correct place")
	break

