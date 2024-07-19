from play_class import Play

game_on = True
play = Play()

while game_on:
    play.loop_story()
    play.profile_question_check()
    play.stats_update()
    if play.check_health() is True:
        game_on = False
        break
    elif play.check_time() is True:
        game_on = False
        break
    elif play.go_home() is True:
        game_on = False
        break
    elif play.check_end_game() is True:
        game_on = False
        break
