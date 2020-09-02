a = input()

sp = a.split(".")

year=int(sp[0])
month=int(sp[1])
day=int(sp[2])

print("%04d.%02d.%02d" % (year,month,day))