def main():

    alice = ['Ⅱ', 'Ⅳ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅱ']
    bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']

    print(love_meet(bob, alice))

    alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']
    bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']
    silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

    print(affair_meet(bob, alice, silvester))


def love_meet(bob, alice):

    alice = set(alice)
    bob = set(bob)
    ab = alice.intersection(bob)

    return ab


def affair_meet(bob, alice, silvester):

    alice = set(alice)
    silvester = set(silvester)
    asl = alice.intersection(silvester)

    in_common = set()
    for i in asl:
        if i not in bob:
            in_common.add(i)
    return in_common


main()
