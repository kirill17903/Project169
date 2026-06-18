def get_day(number):
    match number:
        case 1: return "Понедельник"
        case 2: return "Вторник"
        case 3: return "Среда"
        case 4: return "Четверг"
        case 5: return "Пятница"
        case 6: return "Суббота"
        case 7: return "Воскресенье"
        case _: return "Неверный номер"

print(get_day(1))
print(get_day(5))
print(get_day(9))