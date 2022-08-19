import random # paquete de codigo que contiene funciones para trabajar con la aleatoriedad


def run():
    random_number = random.randint(1, 100) # con el punto se accede al metodo
    choosen_number = int(input('Pick a number between 1 and 100: '))
    while choosen_number != random_number:
        if choosen_number < random_number:
            print('Greather than ' + str(choosen_number) +'!')
        else:
            print('Less than ' + str(choosen_number) +'!')
        choosen_number = int(input('Pick another number: '))
    print('You Win!')


if __name__ == '__main__':
    run()
