# text = '私は{}です'
# print(text.format('まさと'))

# text = '私は{}です'
# name = 'まなみ'
# print(text.format(name))

# no = 1
# print(type(no))
# print('私の順位は' + str(no) + '位です')

# text = '私の順位は{}位です'
# no = 1
# print(type(no))
# print(text.format(no))

# text = '私の順位は{}位です'
# no = 1.0
# print(type(no))
# print(text.format(no))

# text = '私は{0}です。順位は{1}位です。あだ名は{adana}です。本当に{0}です。'
# name = 'マッチョ'
# no = 77
# name2 = "きんに君"
# print(text.format(name, no, adana = name2))

text = '順位{user[2]}位のユーザ：「私は{user[0]}です。順位は{user[1]}位です。嘘やん。」'
user_list = ['マッチョ', 1 , 33]
print(text.format(user = user_list))