
hello, ola = 'hello world', 'ola mundo'

my_test = ('a','b')

minha_lista =[1,2,3]

meu_teste ={
    'teste': 'valor'
}

o_teste_supremo = True

if True:
    if o_teste_supremo == True:
        print ("true")
    else:
        print("false")

def teste():
    for i in  range(5):
        print(i)

map(lambda x: x * 2, minha_lista)

class Reptile:
    def __init__(self, length):
        self.length = length

class Skane(Reptile):
    def slither(self):
        print("I'm a snake 🐍")