ticket = input()

first3 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
last3 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

if first3 == last3:
    print("YES")
else:
    print("NO")
