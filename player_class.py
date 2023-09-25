class player_class:
    def __init__(self, pid=None, name=None, one=None, two=None, three=None, four=None,
                 five=None, six=None,threekind=None, fourkind=None, fullhouse=None, smallstraight=None, largestraight=None,
                 chance=None, yahtzee=None, yahtzeeb1=None, yahtzeeb2=None):
        self.pid = pid
        self.name = name
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six
        self.fullhouse = fullhouse
        self.threekind = threekind
        self.fourkind = fourkind
        self.smallstraight = smallstraight
        self.largestraight = largestraight
        self.chance = chance
        self.yahtzee = yahtzee
        self.yahtzeeb1 = yahtzeeb1
        self.yahtzeeb2 = yahtzeeb2


    def print_score_card(self):
        # Iterate through all attributes and print their names and values
        for attr_name, attr_value in vars(self).items():
            print(f"{attr_name}: {attr_value}")

    def update_one(self, hand):
        if self.one is None:
            if 1 in hand:
                self.one = sum(item for item in hand if item == 1)
                return True
            else:
                print('No ones present')
                return False
        else:
            print('Ones have already been added to the score card')
            return False

    def update_two(self, hand):
        if self.two is None:
            if 2 in hand:
                self.two = sum(item for item in hand if item == 2)
                return True
            else:
                print('No two present')
                return False
        else:
            print('Two have already been added to the score card')
            return False

    def update_three(self, hand):
        if self.three is None:
            if 3 in hand:
                self.three = sum(item for item in hand if item == 3)
                return True
            else:
                print('No three present')
                return False
        else:
            print('Three have already been added to the score card')
            return False

    def update_four(self, hand):
        if self.four is None:
            if 4 in hand:
                self.four = sum(item for item in hand if item == 4)
                return True
            else:
                print('No four present')
                return False
        else:
            print('Four have already been added to the score card')
            return False

    def update_five(self, hand):
        if self.five is None:
            if 5 in hand:
                self.five = sum(item for item in hand if item == 5)
                return True
            else:
                print('No five present')
                return False
        else:
            print('Five have already been added to the score card')
            return False

    def update_six(self, hand):
        if self.six is None:
            if 6 in hand:
                self.six = sum(item for item in hand if item == 6)
                return True
            else:
                print('No six present')
                return False
        else:
            print('Six have already been added to the score card')
            return False



    def update_threekind(self, hand):
        if self.threekind is None:
            counts = [hand.count(die) for die in range(1, 7)]
            counts.sort(reverse = True)
            for count_die in counts:
                if count_die >= 3:
                    self.threekind = sum(item for item in hand)
                    return True
                else:
                    print('hand does not contain threekind')
                    return False
        else:
             print('threekind have already been added to the score card')
             return False

        return True

    def update_fourkind(self, hand):
        if self.fourkind is None:
            counts = [hand.count(die) for die in range(1, 7)]
            counts.sort(reverse=True)
            for count_die in counts:
                if count_die >= 4:
                    self.fourkind = sum(item for item in hand)
                    return True
                else:
                    print('hand does not contain fourkind')
                    return False
        else:
             print('fourkind have already been added to the score card')
             return False

        return True

    def update_fullH(self, hand):
        if self.fullhouse is None:
            counts = [hand.count(die) for die in range(1,7)]
            counts.sort()
            if counts == [0,0,0,0,2,3]:
                self.fullhouse = 25
            else:
                print('hand does not contain fullhouse')
                return False
        else:
             print('fullhouse have already been added to the score card')
             return False

        return True

    def update_smallstraight(self, hand):
        if self.smallstraight is None:
            self.smallstraight = 30
        else:
             print('smallstraight have already been added to the score card')
             return False

        return True


    def update_largestraight(self, hand):
        if self.largestraight is None:
            self.largestraight = 40
        else:
             print('largestraight have already been added to the score card')
             return False

        return True


    def update_yhatzee(self, hand):
        if self.yhatzee is None:
            self.yhatzee = 50
        else:
             print('yhatzee have already been added to the score card')
             return False

        return True

    def update_yhatzeeb1(self, hand):
        if self.yahtzeeb1 is None:
            self.yahtzeeb1 = 100
        else:
            print('yahtzeeb1 have already been added to the score card')
            return False

        return True

    def update_yhatzeeb1(self, hand):
        if self.yahtzeeb2 is None:
            self.yahtzeeb2 = 100
        else:
            print('yahtzeeb2 have already been added to the score card')
            return False

        return True

    def update_chance(self,hand):
        if self.chance is None:
            self.chance = sum(item for item in hand)
        else:
             print('chance have already been added to the score card')
             return False

        return True

    def scratch(self, attribute):
        current_value = getattr(self, attribute)
        if current_value is None or (isinstance(current_value, str) and not current_value.strip()):
            setattr(self, attribute, 'Scratch')
            return True
        else:
            print('cant scratch already populated')
            return False

    def is_empty(self):
        # Check if any specified attribute is empty (None)
        empty_attributes = [self.one, self.two, self.fullhouse, self.smallstraight,
                            self.largestraight, self.chance, self.yahtzee]

        return any(attr is None for attr in empty_attributes)

if __name__ == '__main__':
    None
    player = player_class('a','b')
    curhand = [4, 4, 1, 4, 5]
    result = player.update_threekind(curhand)
    print(player.fourkind)