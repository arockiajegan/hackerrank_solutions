#Script Author : AROCKIA JEGAN F
#visit_me @ www.arcokiajegan.com
#Description --> Performing If/Else operation to find a value comes under Weird/Not Weird with certain condtions

n = int(input())
if n % 2 == 1: 
    print ("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20: 
    print("Weird")
elif n > 20: 
    print ("Not Weird")
else:
    ("Not Weird")
