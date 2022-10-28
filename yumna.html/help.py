a=0
b=0
data5=0
data1=0
z=0
prod=0
prod1=0
prod2=0
cost=0
cost1=0
cost2=0
cost3=0
cost4=0
cost5=0
cost6=0
print("WELCOME TO APNASHOW TICKET BOOKING ONLINE PLATFORM!")
press = int(input("enter 1 fo start booking:"))
loc=["bhopal", "jabalpur", "sagar", "dewas" , "chindwara", "vidisha", "indore", "sehore"]
tre = ["brahmastra", "singham", "deva","dhoom"]
lan = ["english", "hindi", "tamil"]
qua = ["2d", "3d"]
sea=["diamond","dc","middle"]
nam=["sangeet talkies","db talkies","rangmahal talkies","cinepolis talkies","jyoti talkies","bharat talkies"]
tim=["12:00pm","3:00pm","6:00pm","9:00pm"]
bev=["pizza","cola","popcorn","pizza and cola","cola and popcorn","pizza and popcorn","snacks","our combos","none"]
print("")
if press == 1:
    f = open("do.txt")
    content = f.read()
    print(content)
    f.close()
while True:
    data = input("choose location:")
    if data.lower() not in loc:
        print("Not an appropriate choice.")
    else:
        break
print("")
if data in loc:
    q = open("so.txt")
    content1 = q.read()
    print(content1)
    q.close()
print("")
while True:
    data1 = input("choose movie:")
    if data1.lower() not in tre:
        print("Not an appropriate choice.")
    else:
        break
print("")
if data1 in tre:
    for i in lan:
        print(i)
print("")
while True:
    data2 = input("choose language:")
    if data2.lower() not in lan:
        print("Not an appropriate choice.")
    else:
        break
print("")
if data2 in lan:
    print("2d/3d")
while True:
    data3 = input("choose 2d/3d:")
    if data3.lower() not in qua:
        print("Not an appropriate choice.")
    else:
        break
print("")
if data3 in qua:
    f3 = open("tal.txt")
    content3 = f3.read()
    print(content3)
    f3.close()
while True:
    k= input("choose talkies:")
    if k.lower() not in nam:
        print("Not an appropriate choice.")
    else:
        break
print("")
if k in nam:
    f2 = open("ti.txt")
    content2 = f2.read()
    print(content2)
    f2.close()
print("")
while True:
    z= input("choose timing:")
    if z.lower() not in tim:
        print("Not an appropriate choice.")
    else:
        break
print("")
if z in tim:
    while True:
        n = int(input("enter number of seats:"))
        if n<=0:
            print("Not an appropriate choice.")
        else:
            break
print("")
if n>=0:
    for i in sea:
        print(i)
print("")
while True:
    k = input("choose seat type:")
    if k.lower() not in sea:
        print("Not an appropriate choice.")
    else:
        break
print("")
if k in sea:
    f1 = open("piz.txt")
    content = f1.read()
    print(content)
    f1.close()
while True:
    y = input("choose items from the above list or enter none:")
    if y.lower() not in bev:
        print("Not an appropriate choice.")
    else:
        break
print("")
print("Your Receipt!")
print("movie:",data1)
print("language:",data2)
print("location:",data)
print("timing:",z)
print("seat type:",k)
print("seats:",n)
print("audtiorium:s3")
if k == "diamond":
    for i in range(n):
        prod=n*100
    print("ticket price for",n,"diamond seat:", prod)
if k=="middle":
    for i in range(n):
        prod1=n*50
    print("ticket price for",n,"middle seat:", prod1)
if k=="dc":
    for i in range(n):
        prod2=n*20
    print("ticket price for",n,"dc seat:", prod2)
if y=="none":
    cost6=0
    print("food item:",cost6)
if y=="popcorn":
    cost6=20
    print("cost of popcorn:", cost)
if y=="cola":
    cost2=10
    print("cost of cola:",cost2)
if y=="pizza":
    cost1=50
    print("cost of pizza:",cost1)
if y=="pizza and cola":
    cost3=60
    print("cost of pizza and cola:", cost3)
if y=="cola and popcorn":
    cost4=30
    print("cost of cola and popcorn:", cost4)
if y=="pizza and popcorn":
    cost5=70
    print("cost of pizza and popcorn:",cost5)
total1=prod+cost
total2=prod+cost2
total7=prod+cost1
total3=prod1+cost
total4=prod1+cost2
total8=prod1+cost1
total5=prod2+cost
total6=prod2+cost2
total9=prod2+cost1
total16=prod+cost3
total15=prod+cost4
total19=prod+cost5
total20=prod1+cost3
total21=prod1+cost4
total22=prod1+cost5
total26=prod2+cost3
total25=prod2+cost4
total29=prod2+cost5
total30=prod+cost6
total31=prod1+cost6
total32=prod2+cost6
if y not in bev:
    print("invalid")
else:
    if k=="diamond" and y=="popcorn":
        print("total bill:",total1)
    elif k=="diamond" and y=="cola":
        print("total bill:",total2)
    elif k=="diamond" and y=="pizza":
        print("total bill:",total7)
    elif k=="diamond" and y=="pizza and cola":
        print("total bill:",total16)
    elif k=="diamond" and y=="pizza and popcorn":
        print("total bill:",total15)
    elif k=="diamond" and y=="cola and popcorn":
        print("total bill:",total19)
    elif k=="diamond" and y=="none":
        print("total bill:",total30)
    elif k=="middle" and y=="popcorn":
        print("total bill:",total3)
    elif k=="middle" and y=="cola":
        print("total bill:",total4)
    elif k == "middle" and y=="pizza":
        print("total bill:", total8)
    elif k=="middle" and y=="pizza and cola":
        print("total bill:",total20)
    elif k == "middle" and y=="pizza and popcorn":
        print("total bill:",total21)
    elif k=="middle" and y=="cola and popcorn":
        print("total bill:",total22)
    elif k == "middle" and y == "none":
        print("total bill:", total31)
    elif k=="dc" and y=="popcorn":
        print("total bill:",total5)
    elif k=="dc" and y=="cola":
        print("total bill:",total6)
    elif k=="dc" and y=="pizza":
        print("total bill:",total9)
    elif k=="dc" and y=="pizza and cola":
        print("total bill:",total26)
    elif k=="dc" and y=="pizza and popcorn":
        print("total bill:",total25)
    elif k=="dc" and y=="cola and popcorn":
        print("total bill:",total29)
    elif k == "dc" and y == "none":
        print("total bill:", total32)

print("thank you for booking:)")





