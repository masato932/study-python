import re

text = '''人に言うべき事は、最後まできちんと言うが良い。
全部は言いたくないことだったら、
むしろ初めから黙っていいよ。'''

text_new = re.sub('^', '「', text, flags=re.MULTILINE)
text_new = re.sub('$', '」', text_new, flags=re.MULTILINE)
print(text_new)