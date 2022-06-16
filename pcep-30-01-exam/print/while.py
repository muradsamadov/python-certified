secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

numberinput = int(input('enter the integer number: '))

while numberinput !=secret_number:
    print('try againt')
    numberinput = int(input('enter the integer number: '))
print('well done')