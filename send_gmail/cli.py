def main():
    from getpass import getpass
    from .core import Send_Gmail
    email_from = input('your email_from: ')
    email_to = input('your email_to: ')
    title = input('mail title: ')
    text = input('mail text: ')

    mailObj = Send_Gmail(email_from)
    mailObj.send(
        title=title,
        text=text,
        email_to=email_to
    )

if __name__ == '__main__':
    main()
