list_d = ['Justin', 'Apple', 'Food', 3231, 'Another', 2014142]
list_e = []

x = 0

print ("[before] list_d=", list_d)
print ("[before] list_e=", list_e)

for item in list_d:
	if isinstance(item, int):
		list_e.append(item)
		list_d.pop(x)
	x += 1

print ("[after] list_d=", list_d)
print ("[after] list_e=", list_e)
