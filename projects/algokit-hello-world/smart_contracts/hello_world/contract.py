from algopy import ARC4Contract, Box, arc4, subroutine

class HelloWorld(ARC4Contract):
    def __init__(self) -> None:
        self.box_greeting = Box(arc4.String, key='greeting')

    @arc4.abimethod()
    def hello(self, name: arc4.String) -> arc4.String:
        assert name != "", "Name cannot be empty"
        greeting = "Hello, " + name
        self.store_greeting(greeting)
        return greeting
    
    @subroutine
    def store_greeting(self, greeting: arc4.String) -> None:
        self.box_greeting.value = greeting
