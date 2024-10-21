import time
from threading import Thread
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово №{i}\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')
time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()
print(f'Работа потоков {time_end - time_start}')

time_start_2 = datetime.now()
first = Thread(target=write_words, args=(10, 'example5.txt'))
second = Thread(target=write_words, args=(30, 'example6.txt'))
third = Thread(target=write_words, args=(200, 'example7.txt'))
fourth = Thread(target=write_words, args=(100, 'example8.txt'))

first.start()
second.start()
third.start()
fourth.start()

first.join()
second.join()
third.join()
fourth.join()
time_end_2 = datetime.now()
print(f'Работа потоков {time_end_2 - time_start_2}')