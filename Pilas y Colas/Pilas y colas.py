import random
import time
from queue import Queue


class RandomNumbersGenerator:

    def __init__(self, min_value, max_value, num_values):
        self.min_value = min_value
        self.max_value = max_value
        self.num_values = num_values

    def generate(self):
        return [random.randint(self.min_value, self.max_value) for _ in range(self.num_values)]

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class Program:

    def run(self):
        while True:
            print('-----------Bienvenido--------------')
            print('1. Insertar y extraer números en una pila')
            print('2. Insertar y extraer números en una cola')
            print('3. Salir')
            print('-----------------------------------')
            option = input('Ingrese una opción: ')

            if option == '1':
                generator = RandomNumbersGenerator(-10000000, 10000000, 1000000)
                numbers = generator.generate()

                stack = Stack()
                start_time = time.time()
                for number in numbers:
                    stack.push(number)
                end_time = time.time()

                insert_time = end_time - start_time

                start_time = time.time()
                while not stack.is_empty():
                    stack.pop()
                end_time = time.time()

                extract_time = end_time - start_time

                print(f'Se insertaron {len(numbers)} números en la pila en {insert_time} segundos')
                print(f'Se extrajeron {len(numbers)} números de la pila en {extract_time} segundos')

            elif option == '2':
                generator = RandomNumbersGenerator(-10000000, 10000000, 1000000)
                numbers = generator.generate()

                queue = Queue()
                start_time = time.time()
                for number in numbers:
                    queue.put(number)
                end_time = time.time()

                insert_time = end_time - start_time

                start_time = time.time()
                while not queue.empty():
                    queue.get()
                end_time = time.time()

                extract_time = end_time - start_time

                print(f'Se insertaron {len(numbers)} números en la cola en {insert_time} segundos')
                print(f'Se extrajeron {len(numbers)} números de la cola en {extract_time} segundos')

            elif option == '3':
                break

            else:
                print('Opción inválida')

if __name__ == '__main__':
    program = Program()
    program.run()