from tournament import *

def register_8_players():
    register_player("Brandon")
    register_player("Jeff")
    register_player("Mackie")
    register_player("Duncan")
    register_player("Mo")
    register_player("Chris")
    register_player("Ricardo")
    register_player("Colin")
    print "Players registered: %s" % count_players()

def random_matches(n):
    num_players = count_players()
    for i in range(n):
        p1 = random.randint(0,num_players-1)
        p2 = random.randint(0,num_players-1)
        while p1 == p2:
            p2 = random.randint(0,num_players-1)
        players = player_standings()
        report_match(players[p1][0], players[p2][0])
    print "Matches reported: %s" % count_matches()



# def play():
#     """
#     Play a tournament
#     """
#     num_players = count_players()
#     rounds = math.log(num_players, 2)
#     for r in range(rounds):
#         standings = player_standings()
#         [id1, id2, id3, id4] = [row[0] for row in standings]
#         if random.randint(0,1):
#             report_match(id1, id2)
#         else:
#             report_match(id2, id1)
#         if random.randint(0,1):
#             report_match(id3, id4)
#         else:
#             report_match(id4, id3)
#     print player_standings()


if __name__ == '__main__':
    delete_matches()
    delete_players()
    register_8_players()
    play_one_round()
    # random_matches(8)
