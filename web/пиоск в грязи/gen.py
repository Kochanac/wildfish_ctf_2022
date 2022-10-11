import random  
import string  
def rs(length):  
    return ''.join((random.choice(string.ascii_lowercase) for x in range(length))) 
    
flag = 'PbI6bI{в_грязи_найдет_тот_кто_будет_искать}'

start = '''import os
from flask import Flask
from flask import Response

app = Flask(__name__)
'''

handler_format = '''
@app.route("/{}")
def {}():
    resp = Response("{}")
    resp.headers['number'] = "{}"
    return resp
'''

handlers = open('gen_fish.txt').read().split('\n')

pairs  = list(
    zip(
        handlers,
         [
            (x, str(flag.find(x))) for x in flag
        ] 
        + [('', '')] * (len(handlers) - len(flag))
    )
)

random.shuffle(pairs)
print(pairs)

file = open('task.py', 'a')
output = start
for f, s in pairs:
    output += '\n' + handler_format.format(f, rs(8), s[0], s[1]) + '\n'

output += '\n' + '''if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT'))
'''

file.write(output)
file.close()
