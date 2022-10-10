import random  
import string  
def rs(length):  
    return ''.join((random.choice(string.ascii_lowercase) for x in range(length))) 
    
flag = 'PbI6bI{в_грязи_найдет_тот_кто_будет_искать}'

start = '''from flask import Flask

app = Flask(__name__)
'''

handler_format = '''
@app.route("/{}")
def {}():
    return "{}"
'''

handlers = open('dicc.txt').read().split('\n')

pairs  = list(zip(handlers, [f'{x} {flag.find(x)}' for x in flag] + [''] * (len(handlers) - len(flag))))
random.shuffle(pairs)
print(pairs)

file = open('task.py', 'a')
output = start
for f, s in pairs:
    output += '\n' + handler_format.format(f, rs(8), s) + '\n'

file.write(output)
file.close()
