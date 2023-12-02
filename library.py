def Conversion(length_in_cm):
    if not isinstance(length_in_cm, (int, float)):
        return f"Сталася помилка: Введене значення '{length_in_cm}' не є числом"
    if length_in_cm < 0:
        return f"Сталася помилка: Введене значення {length_in_cm} є від'ємним. Впишіть додатнє число."
    if length_in_cm == 0:
        return 0
    
    inches = length_in_cm / 2.54
    return round(inches, 2)

