n, m, x = map(int, input().split(' '))
#ai = list(map(int, input().split(' ')))
#listにしなきゃいけない場合とは？
ai = map(int, input().split(' '))
lcost, rcost = 0, 0
for gate in ai:
  if gate < x:
#   lcost = lcost + 1
    lcost += 1
  else:
#   rcost = rcost + 1
    rcost += 1
    
print(min(lcost, rcost))

#atcoderで提出するとREになるのはなぜ…？
