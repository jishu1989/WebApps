animals=['tiger','lion','panda','elephant']

fish=['salmon','kuva','ahven']

#for x in animals:
#    print(x)

print(animals[0])
print(animals[1:])
print(animals[1:3])

animals.extend(fish)
print(animals)

animals.append('bear')
print(animals)

animals.sort()
print(animals)


animals.sort(reverse=True)
print(animals)


animals.append('bear')
print(animals)

print(animals.count("bear"))
