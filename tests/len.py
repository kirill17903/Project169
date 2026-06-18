words = ["cat", "python", "hi", "automation", "dog", "testing"]

def filter_long(words):
    return [word for word in words if len(word) > 5]

print(filter_long(words))