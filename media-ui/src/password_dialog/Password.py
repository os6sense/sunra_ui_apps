import bcrypt

class Password(object):
    @classmethod
    def get_hashed_password(self, plain_text_password):
        # Hash a password for the first time
        # (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    @classmethod
    def check_password(self, plain_text_password, hashed_password):
        # Check hased password. Useing bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(plain_text_password, hashed_password)

if __name__ == '__main__':
    Password.get_hashed_password("your_password_here")
