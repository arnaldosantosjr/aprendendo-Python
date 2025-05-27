# magic8.py
import random
magic8 = random.randint(1, 9)
question = input('Faça uma pergunta:')

if magic8 == 1:
    answer = 'Yes - definitely'
elif magic8 == 2:
    answer = 'It is decidedly so'
elif magic8 == 3:
    answer = 'Without a doubt'
elif magic8 == 4:
    answer = 'Reply hazy, try again'
elif magic8 == 5:
    answer = 'Ask again later'
elif magic8 == 6:
    answer = 'Better not tell you now'
elif magic8 == 7:
    answer = 'My sources say no'
elif magic8 == 8:
    answer = 'Outlook not so good'
elif magic8 == 9:
    answer = 'Very doubtful' 
else:
    answer  =  answer = 'Error'

print('Magic 8 Ball:  ' + answer)