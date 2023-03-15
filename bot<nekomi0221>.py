def player_choice(player, score):
    if player == 1:
        if scores[1] <= scores[0]:
            if score <= 20:
                return True
            else:
                return False
        if scores[1] > scores[0]:
            if score <= 10:
                return True
            else:
                return False
