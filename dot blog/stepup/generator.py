# def gener1():
#     yield 'Python'
#     yield 'CSS'
#     yield 'HTML'
#     yield 'JavaScript'
    
# gener = gener1()

# print(next(gener))
# print('######## for roop start #######')
# for word in gener:
#     print(word)

words = ['Python', 'CSS', 'HTML', 'JavaScript']

def word_edit(word_list):
    new_words = []
    for word in word_list:
        new_word = word.lower()
        new_words.append(new_word)

    return new_words

for text in word_edit(words):
    print(text)

words = ['Python', 'CSS', 'HTML', 'JavaScript']
    
def word_edit_gen(word_list):
    for word in word_list:
        yield word.lower()

for text in word_edit_gen(words):
    print(text)