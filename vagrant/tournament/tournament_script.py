#!/usr/bin/env python
#
# Helper scripts for running tournament.
#

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


if __name__ == '__main__':
    delete_matches()
    delete_players()
    register_8_players()
    standings = play_tournament()
    print "\nMatch played. Player standings:"
    for player in standings:
        print "    %s, wins: %s" % (player[1], player[2])
