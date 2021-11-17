from threading import Thread
from random import seed
from random import randint
from time import sleep

#####   Variaveis globais   #####
global request, respond, soma
request = 0
respond = 0
soma = 0
#################################


class mp_thread(Thread):

    def __init__(self, n):
        Thread.__init__(self)
        self.n = n
        self.exec = True
    
    def run(self):
        print(f'Thread {self.n} funcionando!')
        while (self.exec):
            global respond, request, soma
            request = self.n
            if (self.exec == False):
                 exit()
            #####   Secao critica   ####
            local = soma
            seed()
            sleep(randint(0,2))
            soma = local + 1
            print(f'Thread {self.n} soma: {soma}')
            ############################
            respond = 0

    def stop(self):
        self.exec = False
        print(f"Parando Thread {self.n}")

def main():
    execucoes = 20          #numero de execucoes
    num_threads = 4         #numero de threads
    threads = []
    global request, respond, soma
    for i in range(num_threads):
        threads.append(mp_thread(i+1))
        threads[i].start()
    for j in range(execucoes):
        wait = True
        while wait:
            if (request != 0):
                wait = False
        respond = request
        wait = True
        while wait:
            if (respond == 0):
                wait = False
        request = 0

    print(f"Soma total: {soma}")
    for i in range(num_threads):
        threads[i].stop()
main()