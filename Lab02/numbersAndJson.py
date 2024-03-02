import math
import json

numbers = [4, 9, 16, 25, 36]
print(numbers)

squareRoots = list(map(lambda number: math.sqrt(number), numbers))
print(squareRoots)

dictionary = {num: sqrt for num, sqrt in zip(numbers, squareRoots)}
print(dictionary)

JsonFile = open("./lab02/newData.json", "w")
JsonFile.write(json.dumps(dictionary))
JsonFile.close()

