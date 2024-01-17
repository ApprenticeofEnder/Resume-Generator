from base64 import urlsafe_b64decode, urlsafe_b64encode

TEXT_ENCODING = "utf-8"


def b64_encode(data: bytes):
    return urlsafe_b64encode(data).decode(TEXT_ENCODING)


def b64_decode(data: str):
    return urlsafe_b64decode(data)
