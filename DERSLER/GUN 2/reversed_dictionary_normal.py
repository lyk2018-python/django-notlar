#!usr/bin/env python
fatih = {
		"lyk" : "2018",
		"gorev" : "hoca",
		"key" : "fatih",
		"sınıf" : "201",
		}
tunahan = { 
		"lyk" : "2018",
		"gorev" : "yarım hoca",
		"key" : "fatih",
		}

print("Fatih:", fatih)

keys = fatih.keys()
values = fatih.values()

first = list(keys)
second = list(values)

reverseFatih = {}
for i in range(len(first)):
	reverseFatih.update({second[i]:first[i],})
print("Reverse Fatih:", reverseFatih)
print("Tunahan:", tunahan)