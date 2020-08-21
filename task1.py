
# Task 1
#
# Create a class method named `validate`, which should be called from the `__init__` method
# to validate parameter email, passed to the constructor. The logic inside the `validate` method
# could be to check if the passed email parameter is a valid email string

'''Task 1
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email, passed to the constructor. The logic inside the `validate` method could be to check if the passed email parameter is a valid email string.'''

global punctuations
punctuations = ' !()[]{};:\/\'",<>?#$%^&*~'
limited_symbols = ['..', '.-', '._', '-.', '_.', '--', '__', '-_', '_-']


class Validate:

    def __init__(self, email):
        self.email = email
        if not self.final_validation():
            self.email = f'Invalid Email "{email}"'

    def final_validation(self):
        if self.email_check() and self.prefix_check() and self.etta_check() and self.domain_check():
            print(f'Your email is : {self.prefix}@{self.etta}.{self.domain}')
            return True
        else:
            return False

    def email_check(self):
        if type(self.email) is not str:
            print('You passed a wrong type of data.')
            return False

        if not self.email[0].isalnum():
            print('Email should start with letter or number.')
            return False

        count = 0
        for char in self.email:
            if char in punctuations:
                print(f'Not valid email. "{char}" is not allowed.')
                return False
            elif char == '@':
                count += 1
        if count != 1:
            print('Not valid email.')
            return False

        for pair in limited_symbols:
            if pair in self.email:
                print('You can\'t use two special symbols in a raw.')
                return False

        self.prefix = self.email.split('@')[0]
        self.etta = self.email.split('@')[1]

        count = 0
        for char in self.etta:
            if char == '.':
                count += 1
        if count < 1:
            print('Domain name is wrong.')
            return False

        self.etta = self.etta.split('.')[0]
        self.domain_list = self.email.split('.')[1:]
        for item in self.domain_list:
            self.domain = '.'.join(self.domain_list)
            if len(item) < 2:
                print('Very short sub-domain name.')
                return False

        return True

    def prefix_check(self):
        if len(self.prefix) >= 64:
            print('Your prefix (part before "@" symbol) can\'t be longer than 64 characters.')
            return False
        if len(self.prefix) <= 3:
            print('Your prefix (part before "@" symbol) can\'t be shorter than 3 characters.')
            return False
        if self.prefix[-1] in '-_.':
            print('Last symbol should be a letter or number.')
            return False

        return True

    def etta_check(self):
        if self.etta[0] in '-_':
            print('First symbols should be letter or numbers.')
            return False

        if len(self.etta) < 2:
            print('Your domain (part after "@" symbol) can\'t be shorter than 2 characters.')
            return False

        if len(self.etta) > 64:
            print('Your domain (part after "@" symbol) can\'t be longer than 64 characters.')
            return False

        return True

    def domain_check(self):
        if len(self.domain) < 2:
            print('Your domain (part after "." symbol) can\'t be shorter than 2 characters.')
            return False
        for char in self.domain:
            if char in '-_1234567890':
                print('Domain can contain only letters and dots.')
                return False
        if self.domain[-1] == '.':
            print('Email can\'t end with a dot.')
            return False

        return True


correct_mail = Validate('fds-lj@gih.com.gov.ua')
wrong_mail = Validate('fds-lj-@gih.com.gov.ua')

print(correct_mail.email)
print(wrong_mail.email)