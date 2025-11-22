from datetime import date

# 1. Нормализация email адресов - приводит адреса к нижнему регистру и убирает пробелы
from datetime import date

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

def add_short_body(email: dict) -> dict:
    email["short_body"] = email["body"].strip()[:10] + "..."
    return email

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

def check_empty_fields(email: dict) -> dict:
    is_subject_empty = not email["subject"].strip()
    is_body_empty = not email["body"].strip()

    return is_subject_empty, is_body_empty

is_subject_empty, is_body_empty = check_empty_fields(email)

print("Пустая тема:", is_subject_empty)
print("Пустое тело:", is_body_empty)

# 6. Маска email отправителя - создает маскированную версию email (первые 2 символа + "***@" + домен)

email = {
    "to": "elinka@malinka.ru",
    "from": "angelinka@kolbaska.ru",
    "subject": "pishu pismo",
    "date": "2025-11-19",
    "body": "I dont understand the difference between email body and email text"
}

def mask_sender_email(sender: str) -> str:
    local, domain = sender.split("@", 1)
    return local[:2] + "***@" + domain
print(mask_sender_email(email["from"]))

# 7. Проверка корректности email - проверяет наличие @ и допустимые домены (.com, .ru, .net)

test_emails = [
    # Корректные адреса
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
]

def get_correct_email(email_list: list[str]) -> list[str]:
    correct_emails = []
    for email in email_list:
        clean_email = email.strip().lower()
        if "@" in clean_email and clean_email.endswith((".com", ".ru", ".net")):
            correct_emails.append(clean_email)
    return correct_emails

print(get_correct_email(test_emails))

# 8. Создание словаря письма - создает базовую структуру письма
email = {
    "to": "elinka@malinka.ru",
    "from": "angelinka@kolbaska.ru",
    "subject": "pismo pishu",
    "date": "2025-11-19",
    "body": "I dont understand the difference between email body and email text"
}
def create_email(sender, recipient, subject, body):
    return {
        'sender': sender,
        'recipient': recipient,
        'subject': subject,
        'body': body
    }
print(create_email(email["to"], email["from"], email["subject"], email["body"]))

# 9. Добавление даты отправки - добавляет текущую дату

email = {
    "to": "elinka@malinka.ru",
    "from": "angelinka@kolbaska.ru",
    "subject": "pismo pishu1",
    "date": "",
    "body": "I dont understand the difference between email body and email text"
}

def add_send_date(email: dict) -> dict:
    email["date"] = date.today().isoformat()
    return email

print(email)
print(add_send_date(email))


#10. Получение логина и домена - разделяет email на логин и домен

email = {
    "to": "elinka@malinka.ru",
    "from": "angelinka@kolbaska.ru",
    "subject": "pismo pishu1",
    "date": "",
    "body": "I dont understand the difference between email body and email text"
}

def extract_login_domain(address: str) -> tuple[str, str]:
    login, domain = address.split("@", 1)
    return login, domain

print(extract_login_domain(email["to"]))
print(extract_login_domain(email["from"]))


#Задание B
def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="default@study.com") -> list[dict]:
    # 1. Проверить, что recipient_list не пустой.
    if not recipient_list:
        return []

    # 2. Проверить корректность email отправителя и получателей
    valid_recipients = get_correct_email(recipient_list)
    valid_sender_list = get_correct_email([sender])
    if not valid_recipients or not valid_sender_list:
        return []

    sender = valid_sender_list[0]

    # 3. Проверить пустоту темы и тела письма
    email = {"subject": subject, "body": message}
    is_subject_empty, is_body_empty = check_empty_fields(email)
    if is_subject_empty or is_body_empty:
        return []

    # 4. Исключить отправку самому себе
    valid_recipients = [r for r in valid_recipients if r != sender]

    # 5. Нормализация
    subject = clean_body_text(subject)
    body = clean_body_text(message)
    valid_recipients = [normalize_addresses(r) for r in valid_recipients]
    sender = normalize_addresses(sender)

    emails = []
    for recipient in valid_recipients:
        # 6. Создать письмо
        email = create_email(sender, recipient, subject, body)

        # 7. Добавить дату отправки
        email = add_send_date(email)

        # 8. Замаскировать email отправителя
        login, domain = extract_login_domain(sender)
        email["masked_sender"] = mask_sender_email(sender)

        # 9. Сохранить короткую версию тела
        email = add_short_body(email)

        # 10. Сформировать итоговый текст письма
        # адаптируем build_sent_text под ключи sender/recipient
        temp_email = {
            "to": email["recipient"],
            "from": email["sender"],
            "subject": email["subject"],
            "date": email["date"],
            "body": email["short_body"]
        }
        email["sent_text"] = build_sent_text(temp_email)
        emails.append(email)
    return emails
result = sender_email(
    recipient_list=["admin@company.ru", "test_123@service.net", "default@study.com"],
    subject="Hello!",
    message="Привет, коллега!"
)

for r in result:
    print(r["sent_text"])