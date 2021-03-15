text = '''人 に 言う べき 事 は 、 最後 まで きちんと 言う が よい 。 全部 は 言い たく ない こと だっ たら 、 むしろ 初め から 黙っ て い よ 。'''
text_new = text.split()
print(text_new)

text = '''人 に 言う べき 事 は 、 最後 まで きちんと 言う が よい 。 全部 は 言い たく ない こと だっ たら 、 むしろ 初め から 黙っ て い よ 。'''
text_new = text.split(' ')
print(text_new)

text = '''人 に 言う べき 事 は 、 最後 まで きちんと 言う が よい 。 全部 は 言い たく ない こと だっ たら 、 むしろ 初め から 黙っ て い よ 。'''
text_new = text.split(maxsplit=5)
print(text_new)