import time
import random
class LoopsPractice:
    def numbers_with_break(self):
        numbers = list(range(1,8))
        for n in numbers:
            print(n)
            if   n == 5:
                break

    def words_loop(self):
        words = [f"str{i}" for i in range(10)]
        for word in words:
            print(word)

    def rotsics_load_monitoring(self):
        print("Мониторинг нагрузки Rostics запущен...")
        iteration = 0
        while iteration < 10:
            load = random.randint(0, 100)
            print(f"Итерация {iteration + 1}: нагрузка = {load}%")
            if load > 85:
                print("  ПРЕДУПРЕЖДЕНИЕ: нагрузка превышает 85%!")
            time.sleep(0.2)
            iteration +=1
        print("Мониторинг завершен.")

practice = LoopsPractice()
practice.numbers_with_break()

print()

practice.words_loop()

print()

practice.rotsics_load_monitoring()

