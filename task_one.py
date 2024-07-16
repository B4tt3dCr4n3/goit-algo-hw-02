"""Завдання 1. Потрібно розробити програму, яка імітує приймання й обробку заявок: 
програма має автоматично генерувати нові заявки (ідентифіковані унікальним номером 
або іншими даними), додавати їх до черги, а потім послідовно видаляти з черги для 
"обробки", імітуючи таким чином роботу сервісного центру."""

from queue import Queue
import random
import time

# Створення черги заявок
requests_queue = Queue()

def generate_request():
    """Генерує нову заявку та додає її до черги."""
    request_id = random.randint(1, 1000)  # Генерація унікального ID для заявки
    print(f"Генеруємо нову заявку з ID: {request_id}")
    requests_queue.put(request_id)

def process_request():
    """Обробляє заявку, видаляючи її з черги."""
    if not requests_queue.empty():
        request_id = requests_queue.get()
        print(f"Обробляємо заявку з ID: {request_id}")
    else:
        print("Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
try:
    while True:
        generate_request()  # Створення нових заявок
        time.sleep(1)  # Імітація затримки
        process_request()  # Обробка заявок
        time.sleep(1)  # Імітація затримки
except KeyboardInterrupt:
    print("Програма завершена.")
