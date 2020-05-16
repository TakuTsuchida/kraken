import jwt

def create_token(email: str) -> str:
    return str(jwt.encode({'email': email}, 'secret', algorithm='HS256'))

def decode_token(token: str) -> dict:
    token = bytes(token)
    return jwt.decode(token, 'secret', algorithm='HS256')
