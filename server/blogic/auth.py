import jwt

def create_token(email: str) -> str:
    return jwt.encode({'email': email}, 'secret', algorithm='HS256')

def decode_token(token: str) -> dict:
    return jwt.decode(token, 'secret', algorithm='HS256')
