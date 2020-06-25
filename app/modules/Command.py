from enum import Enum

from modules.SplatoonWeapon import Category, SpecialWeapon, SubWeapon, Buki


class Function(Enum):
    give_me = 'give-me'
    give = 'give'
    help = 'help'

    @classmethod
    def value_of(cls, value):
        for it in Function:
            if it.value == value:
                return it
        raise ValueError


class Option(Enum):
    category = 'category'
    cat = 'cat'
    special = 'special'
    sub = 'sub'

    @classmethod
    def value_of(cls, value):
        for it in Option:
            if it.value == value:
                return it
        raise ValueError


class Command:
    def __init__(self, func: Function, category: Category, special: SpecialWeapon, sub: SubWeapon):
        self.func = func
        self.category = category
        self.special = special
        self.sub = sub

    @staticmethod
    def instantiate(message: str):
        command = message.replace('$', '').split(' ')

        func = Function(command[0])
        print(func.value)
        del command[0]

        category = None
        special = None
        sub = None

        for option in command:
            for enum in Option:
                if option.startswith('--' + enum.value):
                    value = option.replace('--' + enum.value + '=', '')
                    if enum is Option.cat or enum is Option.category:
                        category = Category(value)

                    if enum is Option.special:
                        special = SpecialWeapon(value)

                    if enum is Option.sub:
                        sub = SubWeapon(value)

        return Command(func, category, special, sub)

    def execute(self, replica: bool = False):
        return Buki.get(self.category, self.sub, self.special, replica)
