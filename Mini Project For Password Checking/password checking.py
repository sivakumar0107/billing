st = input('Enter the string: ')
di = {'num': 0, 'up': 0, 'low': 0, 'spe': 0}
count = 0
out = ()
for i in st:
    if '0' <= i <= '9':
        di['num'] += 1
    elif 'A' <= i <= 'Z':
        di['up'] += 1
    elif 'a' <= i <= 'z':
        di['low'] += 1
    elif i in ['#', '@', '&', '!']:
        di['spe'] += 1
if len(st) < 8:
    out += 1,
    print('len is less than 8 character', end=' ')
if di['num'] == 0:
    out += 2,
    count += 1
if di['up'] == 0:
    out += 3,
    count += 1
if di['low'] == 0:
    out += 4,
    count += 1
if di['spe'] == 0:
    out += 5,
    count += 1
if count != 0:
    print(f' The above string does not satisfy the condition {out} we need to add ', end=' ')
    print(f'{count} to the string to satisfy the condition')
else:
    print('The above string satisfy the all conditions')
