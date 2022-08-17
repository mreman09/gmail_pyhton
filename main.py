import smtplib
import getpass
import imaplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
print(smtp_object)
print(smtp_object.ehlo())

smtp_object.starttls()

print('Email push')
email = input("Enter your email: ")
print('password ')
password = getpass.getpass("Enter your password: ")
# password = input("Enter your password: ")
print('password completed')
smtp_object.login(email, password)
from_address = input("Enter your email: ")
to_address = input("Enter the email of the recipient: ")


def close_program():
    choice = input('Press Y to send another message \nTo exit press N: ').upper()

    while choice not in ['Y', 'N']:
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            choice = input('Y or N: ')


def spam(msg):
    x = 0
    while x < 4:
        smtp_object.sendmail(from_address, to_address, msg)
        x = x + 1


def email_program():
    again = True
    while again:
        subject = input("Enter the subject line: ")
        message = input("Type out the message you want to send: ")
        msg = "Subject: " + subject + '\n' + message
        results = input('\nPress Enter to send\nPress S to spam: ').upper()

        if results.upper() == 'S':
            spam(message)
            again = close_program()
        else:
            smtp_object.sendmail(from_address, to_address, msg)
            again = close_program()


email_program()
