#!usr/bin/env python
sozluk ={'elma': 'apple', 'muz': 'banana', 'uzum': 'grapes', 'havuc': 'carrot'}
print(sozluk)
reverse_sozluk = {i:j for j,i in sozluk.items()}

print(reverse_sozluk)
print(reverse_sozluk["apple"])
