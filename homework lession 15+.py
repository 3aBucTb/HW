file_name = input("Введіть назву файлу: ")


file_content = """Hello, this is a sample text with email addresses:
example1@example.com
user123@email.com
test.email@example.org
"""

import re


def replace_emails(text, mask_type):
    if mask_type == "simple":
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.sub(email_pattern, '*@*', text)
    elif mask_type == "complex":
        def mask_email(match):
            email = match.group(0)
            first_letter = email[0]
            last_letter = email[-1]
            masked = f"{first_letter}{'*' * (len(email) - 2)}{last_letter}"
            return masked

        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        return re.sub(email_pattern, mask_email, text)


def main():
    input_file_name = input("Введіть назву файлу для обробки: ")
    mask_type = input("Виберіть тип маскування (simple/complex): ").lower()

    try:
        with open(input_file_name, 'r') as file:
            content = file.read()

        replaced_content = replace_emails(content, mask_type)

        output_file_name = f"masked_{input_file_name}"
        with open(output_file_name, 'w') as output_file:
            output_file.write(replaced_content)

        print("Замінено email та збережено у новий файл:", output_file_name)

    except FileNotFoundError:
        print(f"Файл {input_file_name} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка: {e}")


if __name__ == "__main__":
    main()
