n = int(input())
character = []
for _ in range(n):
    character.append(int(input()))

symbols = dict()
for i in enumerate(character):
    symbols[i[0]] = i[1]
print(symbols) 


