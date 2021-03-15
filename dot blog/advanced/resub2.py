import re

text = '''挫折を経験した事がない者は、
何も新しい事に挑戦したことが無いということだ。
-　アルベルト・アインシュタイン　-'''

text_new = re.sub('[ぁ-ん]', 'a', text)
print(text_new)

import re

text = '''挫折を経験した事がない者は、
何も新しい事に挑戦したことが無いということだ。
-　アルベルト・アインシュタイン　-'''

text_new = re.sub('[ァ-ン]', 'a', text)
print(text_new)

import re

text = '''挫折を経験した事がない者は、
何も新しい事に挑戦したことが無いということだ。
-　アルベルト・アインシュタイン　-'''

text_new = re.sub('[一-龥]', '〇', text)
print(text_new)