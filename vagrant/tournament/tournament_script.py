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

def play_match(pair):
    """
    Determines winner and loser of match, based on 50/50 probability.

    Args:
      pair: tuple representing player pair (id1, name1, id2, name2)

    Returns:
      A tuple containing 2 tuples "(winner, loser)", one for winner and one for loser, each
      containing:
        id: player's id
        name: player's name
    """
    # Determine winner and loser positions (0 or 1)
    w = random.randint(0,1)
    l = (w+1) % 2
    ids = (pair[0], pair[2])
    names = (pair[1], pair[3])
    print "%s beats %s" % (names[w], names[l])
    return ((ids[w], names[w]), (ids[l], names[l]))



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
    play_one_round(play_match)
    print "\nMatch played. Player standings:"
    standings = player_standings()
    for player in standings:
        print "    %s, wins: %s" % (player[1], player[2])
    # random_matches(8)
