def get_day_name(day: int) -> str:
    match day:
        case 1: return "Понедельник"
        case 2: return "Вторник"
        case 3: return "Среда"
        case 4: return "Четверг"
        case 5: return "Пятница"
        case 6: return "Суббота"
        case 7: return "Воскресенье"
        case _: return "Неправильный номер"

print(get_day_name(4))
print(get_day_name(9))
print(get_day_name(2))





