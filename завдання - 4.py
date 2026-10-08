def find_longest(*words):
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


# Цікаво перевірити на прикладі
print(find_longest("левиця", "мавпа", "зебра", "сова"))
