country = tuple ("I LOVE INDIA")

print(country)

country = 1, 2

print(country)
print(type(country))


# touple is not modifiable but if it is adresses any muteable type init then e can modify it.

states = ("KA", "AP", "KL", "TN", [1,2,3])

states[-1].append(77)

print(states)
print(type(states))