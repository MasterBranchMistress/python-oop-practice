# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrapper(*args, **kwargs):
        if user1.get('valid'):
            return fn(*args, **kwargs)
        else:
            print("User is not authenticated. Access denied.")
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)