from library import Conversion


def test_conversion():
    # Додатнє число у сантиметрах
    assert Conversion(10) == 3.94

    # Нуль
    assert Conversion(0) == 0

    # Від'ємне число у сантиметрах
    assert Conversion(-5) == -5

    # Текст
    assert Conversion("abc") == "abc"

if __name__ == "__main__":
    test_conversion()
    print("Усі тести пройдені успішно!")
