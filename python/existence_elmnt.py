list=[47, 64, 69, 37, 76, 83, 95, 97]
print(len(list))
dict={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}
print(dict.values())
list2=[print(dict['Yassine']), print(dict['Imane']), print(dict['Mohammed']), print(dict['Abir'])]
print(len(list2))
i=0
j=0
while(i<=len(list) & j<=len(list2)):
   if list[i]==list2[j]:
      print(list)