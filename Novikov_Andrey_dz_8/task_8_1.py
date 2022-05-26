import re


def email_parse(email):
    regex = re.compile(r'([A-Za-z0-9]+[.-_]*[A-Za-z0-9]+)@([A-Za-z0-9-]+)\.[A-Z|a-z]{2,}')
    result = re.findall(regex, email)
    if len(result) == 0:
        raise ValueError(f'wrong email: {email}')
    else:
        print({'username': result[0][0], 'domain': result[0][1]})


email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')
