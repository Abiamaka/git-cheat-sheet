from reji import get_marves_info


def hello(name: str) -> str:
    return f"Hello {name}!"


print(hello('rejoice'))


def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))

print(get_marves_info())
