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
    replica = 'with-replica'
    nocat = 'nocat'



class Command:
    def __init__(self, func: Function, categories: List[Category],nocat: bool, specials: List[SpecialWeapon], subs: List[SubWeapon],
                 customs: List[Custom], replica: bool):
        self.func = func
        self.categories = categories
        self.nocat = nocat
        self.specials = specials
        self.subs = subs
        self.customs = customs
        self.replica = replica

    @staticmethod
    def instantiate(message: str):
        command = message.replace('$', '').split(' ')

        func = Function(command[0])
        del command[0]

        categories = []
        nocat = False
        specials = []
        subs = []
        customs = []
        replica = False

        for option in command:
            for enum in Option:
                if option.startswith('--' + enum.value):
                    value = option.replace('--' + enum.value + '=', '')

                    if enum is Option.cat or enum is Option.category:
                        categories.append(Category(value))

                    if enum is Option.nocat:
                        nocat = True

                    if enum is Option.special:
                        specials.append(SpecialWeapon(value))

                    if enum is Option.sub:
                        subs.append(SubWeapon(value))

                    if enum is Option.custom:
                        customs.append(Custom(value))

                    if enum is Option.replica:
                        replica = True

        return Command(func, categories, nocat, specials, subs, customs, replica)

    def execute(self):
        return Buki.get(self.categories, self.nocat, self.subs, self.specials, self.customs, self.replica)
