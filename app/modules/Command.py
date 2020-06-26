from enum import Enum
from typing import List

from modules.SplatoonWeapon import Category, SpecialWeapon, SubWeapon, Buki, Custom


class Function(Enum):
    give_me = 'give-me'
    give = 'give'
    help = 'help'


class Option(Enum):
    category = 'category'
    cat = 'cat'
    special = 'special'
    sub = 'sub'
    custom = 'custom'


class Command:
    def __init__(self, func: Function, categories: List[Category], specials: List[SpecialWeapon], subs: List[SubWeapon],
                 customs: List[Custom]):
        self.func = func
        self.categories = categories
        self.specials = specials
        self.subs = subs
        self.customs = customs

    @staticmethod
    def instantiate(message: str):
        command = message.replace('$', '').split(' ')

        func = Function(command[0])
        del command[0]

        categories = []
        specials = []
        subs = []
        customs = []

        for option in command:
            for enum in Option:
                if option.startswith('--' + enum.value + '='):
                    value = option.replace('--' + enum.value + '=', '')

                    if enum is Option.cat or enum is Option.category:
                        categories.append(Category(value))

                    if enum is Option.special:
                        specials.append(SpecialWeapon(value))

                    if enum is Option.sub:
                        subs.append(SubWeapon(value))

                    if enum is Option.custom:
                        customs.append(Custom(value))

        return Command(func, categories, specials, subs, customs)

    def execute(self, replica: bool = False):
        return Buki.get(self.categories, self.subs, self.specials, self.customs, replica)
