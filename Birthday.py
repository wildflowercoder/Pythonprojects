import os 
import random
from termcolor import sleep
from ART.art import *

input(colored('Press {Enter}...','blue'))
os.system('clear')

#read this and print
for i in range(len(code)):
    print(code[i], sep='', end='', flush= True);sleep(.02)


#colours supported by termcolor
color = ['grey','red','green','yellow','blue','magenta','cyan','white',]

input(colored('\n{Enter} ', 'red'))
os.system('reset')

#colorful bars
def colorful_bars(x, times=135):
    if x == 'open':
        bar = '^'
        for i in range(times):
            print(colored(bar,random.choice(color)),end='')


#falling objects
def fall(lists,time):
    for j in range(len(i)):
        print(colored(i[j],random.choice(color)),sep='',end='', flush= True);sleep(time)

colorul_bars('open')

#objects
obj = [cake,man,book]
fall(obj,0.005)
colorful_bars('close')

input()
os.system('reset')

print('Change the background colur to white annd font color to black,')
input('Enter the Command {cntrl+ -} four times and Press {enter]...')

