sentence = "Python is fun and Python is easy to learn!"
vowels = "aeiouAEIOU"
result = "".join(char.upper() 

if char in vowels 

else char for char in sentence)

print(result)
