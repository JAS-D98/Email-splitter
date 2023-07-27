def main():
    print('Welcome to the email splitter: ')
    print('')

    email=input('Enter your email here: ')
    (username, domain)=email.split('@')
    (domain, extension)=domain.split('.')

    print('Username: ', username)
    print('Domain ', domain)
    print('Extension ', extension)
    print('')

while True:
    main()
