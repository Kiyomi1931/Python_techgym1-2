import random

print('じゃんけんスタート')

print('自分の手を入力してください')
my_hand = int(input('0:グー, 1:チョキ, 2:パー'))
you_hand = random.randint(0, 2)
print(you_hand)#相手の手を確認するために挿入
hand_diff = my_hand - you_hand

if my_hand==you_hand:
  print('あいこ')
elif hand_diff==-1 or hand_diff==2:
  print('勝ち')
else:
  print('負け')