# words = ['Python', 'CSS', 'HTML', 'JavaScript']

# def word_edit(word_list):
#     new_words = []
#     for word in word_list:
#         new_word = word.lower()
#         new_words.append(new_word)

#     return new_words

# for text in word_edit(words):
#     print(text)


words = ['Python', 'CSS', 'HTML', 'JavaScript']

words_gen = (word.lower() for word in words if len(word) < 7)

for text in words_gen:
    print(text)
    print(type(words_gen))