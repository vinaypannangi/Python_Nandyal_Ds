# import time
# f1=open("ihub3.txt","w")
# D1=["1001\n","mobile\n","2500\n","samsung\n","12/12/2023\n","12/12/2024\n"]
# f1.writelines(D1)
# print("File is created successfully...")
# f1.close()
# print()
# time.sleep(2)
# print("end of an application")

import time
f1=open("ihub3.txt","w")
D1=["1001\n","mobile1\n","25001\n","samsung\n","12/12/2023\n","12/12/2024\n"]
D2=["1002\n","mobile2\n","25002\n","samsung\n","12/12/2023\n","12/12/2024\n"]
D3=["1003\n","mobile3\n","25003\n","samsung\n","12/12/2023\n","12/12/2024\n"]
D4=["1004\n","mobile4\n","25004\n","samsung\n","12/12/2023\n","12/12/2024\n"]
D5=["1005\n","mobile5\n","25005\n","samsung\n","12/12/2023\n","12/12/2024\n"]
f1.writelines(D1)
f1.writelines(D2)
f1.writelines(D3)
f1.writelines(D4)
f1.writelines(D5)
print("File is created successfully...")
f1.close()
print()
time.sleep(2)
print("end of an application")
