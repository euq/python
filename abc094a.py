#a, b, x = map(lambda anm: int(anm),input().split(' '))
#lambda: 無名関数
a, b, x = map(int,input().split(' '))
if a <= x <= a + b:
  print('YES')
else:
  print('NO')

