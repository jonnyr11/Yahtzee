import dice_2 as d2
import player_class as pc
import sys
game_complete = False


def update_score_card( save_location,player):
    if save_location == 'one':
        update_check = player.update_one(hand)
    elif save_location == 'two':
        update_check = player.update_two(hand)
    elif save_location == 'three':
        update_check = player.update_three(hand)
    elif save_location == 'four':
        update_check = player.update_four(hand)
    elif save_location == 'five':
        update_check = player.update_five(hand)
    elif save_location == 'six':
        update_check = player.update_six(hand)
    elif save_location == 'threekind':
        update_check = player.update_threekind(hand)
    elif save_location == 'fourkind':
        update_check = player.update_fourkind(hand)
    elif save_location == 'smallstraight':
        update_check = player.update_smallstraight(hand)
    elif save_location == 'largestraight':
        update_check = player.update_largestraight(hand)
    elif save_location == 'chance':
        update_check = player.update_chance(hand)
    elif save_location == 'fullhouse':
        update_check = player.update_fullH(hand)
    elif save_location == 'yahtzee':
        update_check = player.update_yahtzee(hand)
    elif save_location == 'yahtzeeb1':
        update_check = player.update_yahtzeeb1(hand)
    elif save_location == 'yahtzeeb2':
        update_check = player.update_yahtzeeb2(hand)
    else:
        print('input invalid')
        update_check = False
    return update_check


if __name__ == '__main__':
    # player list
    players = []

    num_player = input('How many players today? 1-6 ')
    if num_player == '':
        print('no game today')
        sys.exit(1)

    num_player = int(num_player)

    # add players to the game
    if num_player == 0:
        print('no game today')
    elif num_player < 7:
        x = num_player
        z = 1
        while z <= x:
            player_name = input(f'enter the name of player {z} ')
            players.append(pc.player_class(z,player_name))
            z += 1
            # print(z)
            # print(x)

        print('the players today are:')
        for player in players:
            print(f'{player.pid}:{player.name}')

    #Game starts
    print('lets play')

    while game_complete == False:
        active_players = []
        if input('new round, Continue|Exit ') == 'Exit':
            sys.exit(1)

        for player in players:
            #check if any have not yet completed
            if player.is_empty() == True:
                active_players.append(player)

        for player in active_players:
            print(player.print_score_card())
            hand = d2.turn()
            print(player.print_score_card())
            update_check = False
            while update_check == False:
                save_scratch = input('Save score or scratch row? save|scratch ')
                if save_scratch == 'save':
                    save_location = input('which score do you want to populate? ')
                    update_check = update_score_card(save_location, player)
                elif save_scratch == 'scratch':
                    attr = input('Score to scratch ')
                    update_check = player.scratch(attr)
                else:
                    print('invalid input')
                    update_check = False



            print(player.print_score_card())
            print('')
            print('')

    print('Game Over')
    sys.exit(1)