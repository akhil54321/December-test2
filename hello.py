from hello import say_hello
from calc import add
from greet import greet

def test_say_hello():
    assert say_hello() == "Hello from GitHub Actions 🚀"

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_greet():
    assert greet("Akhil") == "Hello, Akhil!"
