import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == 'roll':
        return str(random.randint(1,6))
