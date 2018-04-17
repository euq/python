#a, b, x = map(lambda anm: int(anm),input().split(' '))
#lambda: 無名関数
a, b, x = map(int,input().split(' '))
#int関数はもともと引数なしでも使えるのかmapに渡してるから引数なしなのかどっち？
if a <= x <= a + b:
  print('YES')
else:
  print('NO')

