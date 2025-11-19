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
email_text = "I dont understand\tthe difference\nbetween email body and email text"

def clean_body_text(body: str) -> str:
    return body.replace('\t', ' ').replace('\n', ' ')
print(clean_body_text(email_text))

# 4. Формирование итогового текста письма - создает форматированный текст письма

email = {
    "to": "elinka@malinka.ru",
    "from": "angelinka@kolbaska.ru",
    "subject": "pismo pishu",
    "date": "2025-11-19",
    "body": "I dont understand the difference between email body and email text"
}

def build_sent_text(email: dict) -> str:
    return (f"Кому: {email['to']}, От: {email['from']}\n"
            f"Тема: {email['subject']}, Дата: {email['date']}\n"
            f"{clean_body_text(email['body'])}")
            
print(build_sent_text(email))

# 5. Проверка пустоты темы и тела - проверяет, заполнены ли обязательные поля

email = {
    "to": "elinka@malinka.ru",
    "from": "angelinka@kolbaska.ru",
    "subject": "",
    "date": "2025-11-19",
    "body": "I dont understand the difference between email body and email text"
}

def check_empty_fields(email: dict) -> tuple[bool, bool]:
    is_subject_empty = not email["subject"].strip()
    is_body_empty = not email["body"].strip()

    return is_subject_empty, is_body_empty

is_subject_empty, is_body_empty = check_empty_fields(email)

print("Пустая тема:", is_subject_empty)
print("Пустое тело:", is_body_empty)


# 6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)
#
# 7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)
#
# 8. Создание словаря письма - создает базовую структуру письма
#
# 9. Добавление даты отправки - добавляет текущую дату

#10. Получение логина и домена - разделяет email на логин и домен