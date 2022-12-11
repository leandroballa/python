city = str(input('Em qual cidade você mora? ')).strip()

if city.upper().split()[0].find('SANTO') >= 0:
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
