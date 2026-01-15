
print("Hello, world!")
# aqui no hay necesidad de señalar el tipo de dato
num1 = 10
num2 = 20
sum_result = num1 + num2
print("the sum of", num1, "and", num2, "is:", sum_result)

num3 = input ("Enter a number: ")
print("You entered: ", num3)

num4 = input ("Enter a number: ")
print("You entered: ", num4)
#se agregan los parentesis para especificar el tipo de variable, sino solo concatena
suma2 = int(num3) + int(num4)
print("la suma de {} + {} es: {}".format(num3, num4, suma2))