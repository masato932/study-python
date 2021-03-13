# text = '''人に言うべき事は、最後まできちんと言うが良い。
# 全部は言いたくないことだったら、
# むしろ初めから黙っていよ。'''

# text_new = text.replace('初めから', '最初から')
# print(text_new)

text = '''人に言うべき事は、最後まできちんと言うが良い。
全部は言いたくないことだったら、
むしろ初めから黙っていよ。'''

text_new = text.replace('初めから', '')
print(text_new)

text = '''人に言うべき事は、最後まできちんと言うが良い。
全部は言いたくないことだったら、
むしろ初めから黙っていよ。'''

text_new = text.replace('きちんと', '').replace('全部は', '全ては').replace('初めから', '最初から')
print(text_new)