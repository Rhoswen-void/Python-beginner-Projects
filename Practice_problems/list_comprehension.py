doubles = [i * 2 for i in range(1,11)]
triples = [i * 3 for i in range(1,11) if i % 3 == 0]
squares = [i ** 2 for i in range(1,11) ]

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
fruits = [fruit.upper() for fruit in fruits]

number = [-10, -5, 0, 5, 10]
positive_numbers = [i for i in number if i > 0]
negative_numbers = [i for i in number if i < 0]

fruit_chars = [fruit[0] for fruit in fruits]
print(doubles)
print(triples)
print(squares)
print(fruits)
print(positive_numbers)
print(negative_numbers)
print(fruit_chars)