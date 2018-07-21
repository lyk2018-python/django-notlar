#!usr/bin/env python
fatih = {
		"lyk" : "2018",
		"gorev" : "hoca",
		"key" : "fatih",
		"sınıf" : "201",
		}
print("Dictionary:", fatih)
print("Dictionary Comprehension:", [key for key,value in fatih.items()])
print("Reversed Dictionary:", dict((value,key) for key,value in fatih.items()))