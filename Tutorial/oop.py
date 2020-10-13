class PlayerCharater:

    membership = True

    def __init__(self, name='jack'):
        self.name = name

    def run(self):
        print(f'My name {self.name}')

player1 = PlayerCharater()
player1.address = "example@mail.com"
print(player1)
print(player1.address)
print(player1.membership)

player1.run()
