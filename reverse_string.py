def reverse(sentence):
    if len(sentence) == 0:
        return sentence
    else:
        return reverse(sentence[1:]) + sentence[0]

print(reverse('12'))