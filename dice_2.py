import random
import dice_print as dp
def dice_roll(NumDice):
    count = 0
    a = []
    while (count < NumDice):
        a.append(random.randint(1, 6))
        count = count + 1
    return (a)

def remove_dice(vdice_to_remove,vhand):
    if vdice_to_remove == 'all':
        del(vhand)
        vhand = []
    else:
        for vdice in vdice_to_remove:
            try:
                print(vdice)
                dice = int(vdice)
                vhand.remove(dice)
            except:
                print(f'{vdice} not in hand')

    return(vhand)

def turn():
    roll = 1
    thand = dice_roll(5)
    print(dp.gen_dice(thand))
    while roll < 3:
        roll += 1
        choice = input('Would you like you re roll any dice: yes|no|all ')
        if choice == 'no':
            return(thand)
        elif choice == 'all':
            thand=remove_dice('all',thand)
            # print(f'thand: {thand}')
            print(dp.gen_dice(thand))
        elif choice == 'yes':
            dice_removed = 0
            # number_of_dice = input('how many dice would you like to remove? ')
            # number_of_dice= int(number_of_dice)
            #while dice_removed < number_of_dice:
            dice_to_remove  = ''
            while dice_to_remove == '':
                dice_to_remove = input('which dice would you like to remove: ')
            dice_to_remove_list = dice_to_remove.split(',')
            thand = remove_dice(dice_to_remove_list, thand)
            dice_removed = len(dice_to_remove_list)
            # print(thand)
            print(dp.gen_dice(thand))

        print('time to roll again')
        if choice == 'all':
            rhand = dice_roll(5)
        elif choice == 'yes':
            rhand = dice_roll(dice_removed)
        print(f'rhand: {rhand}')

        thand.extend(rhand)
        print('test')
        # print(thand)
        print(dp.gen_dice(thand))
    return(thand)
    # print(thand)

if __name__ == '__main__':
    None

    turn()
