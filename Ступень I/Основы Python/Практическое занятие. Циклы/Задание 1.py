sentence = input("Предложение: ").split()
dict_ = dict.fromkeys(sentence, 0)
for word in sentence:
    if word in dict_:
        dict_[word] += 1

print(max(dict_, key=dict_.get))
