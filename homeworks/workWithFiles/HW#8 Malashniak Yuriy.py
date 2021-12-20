a = int(input('Vvedit chuslo: '))
b = int(input('Vvedit chuslo: '))
c = a + b
f = open("result.txt", "w")
f.write(str(c) + '\n')
f.close()
d = int(input('Vvedit chuslo: '))
e = int(input('Vvedit chuslo: '))
i = d - e
f = open("result.txt", "a")
f.write(str(i))
f.close()