import time
B=0
for x1 in "Software developer":
	if(x1 in ("AEIOUaeiou")):
		B+=1
		print(x1)
print()
print("The number of vowels in given string is:",B)
print()
time.sleep(2)
print("End of an application")