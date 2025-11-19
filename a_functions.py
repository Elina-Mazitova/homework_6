# 1. Нормализация email адресов - приводит адреса к нижнему регистру и убирает пробелы
test_emails = [
    " hello@test.com  ",
    "User@user.net",
    "Example.elinka@domain.com "]

def normalize_addresses(value: str) -> str:
    return value.strip().lower()
for email in test_emails:
    print(normalize_addresses(email))

# 2. Сокращенная версия тела письма - создает короткую версию тела (первые 10 символов + "...")
email_body = 'I wrote text to check ability to show only ten symbols of message'

def add_short_body(value: str) -> str:
    return value.strip()[:10]+"..."
print(add_short_body(email_body))

# 3. Очистка текста письма - заменяет табы и переводы строк на пробелы
#
# 4. Формирование итогового текста письма - создает форматированный текст письма
#
# 5. Проверка пустоты темы и тела - проверяет, заполнены ли обязательные поля
#
# 6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)
#
# 7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)
#
# 8. Создание словаря письма - создает базовую структуру письма
#
# 9. Добавление даты отправки - добавляет текущую дату

#10. Получение логина и домена - разделяет email на логин и домен