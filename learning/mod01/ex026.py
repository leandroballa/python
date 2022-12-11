frase = str(input('Digite uma frase: ')).strip().lower()

print('Sua frase contém {} "a"'.format(frase.count('a')))
print('A primeira vez que a letra "a" aparece em sua frase é {}'.format(frase.find('a')+1))
print('A ultima vez que a letra "a" aparece em sua frase é {}'.format(frase.rfind('a')+1))
