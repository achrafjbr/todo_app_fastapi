from fastapi import status, HTTPException


def rais_exception(st: status, detail):
    raise HTTPException(status_code=st, detail=detail)


def check_email(email: str):
    if '@' not in email:
        return False
    else:
        return True


def check_password(password: str):
    if len(password) < 8:
        return False
    else:
        return True
