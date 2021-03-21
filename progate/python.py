import utils
import random

print("じゃんけんをはじめます")
print("何を出すのか決めてください")

player_name = "にんじゃわんこ"
player_hand = random.randint(0,2)
computer_name = "コンピューター"
computer_hand = random.randint(0,2)

if utils.validate(player_hand):
  utils.print_hand(player_hand,player_name)
  utils.print_hand(computer_hand,computer_name)

  result = utils.judge(player_hand, computer_hand)
  print("結果は"+result+"でした")

else:
  print("正しい数値を入力してください")