#!/usr/bin/env python
#
# Test cases for tournament.py
# These tests are not exhaustive, but they should cover the majority of cases.
#
# If you do add any of the extra credit options, be sure to add/modify these
# test cases as appropriate to account for your module's added functionality.
import random

from tournament import *


def test_count_players():
    """
    Test for initial player count,
             player count after 1 and 2 players registered,
             player count after players deleted.
    """
    delete_matches()
    delete_players()
    c = count_players()
    if c == '0':
        raise TypeError(
            "count_players should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deletion, count_players should return zero.")
    print ("1. count_players() returns 0 after initial"
           "delete_players() execution.")
    register_player("Chandra Nalaar")
    c = count_players()
    if c != 1:
        raise ValueError(
            "After one player registers, count_players() should be 1. Got {c}"
            .format(c=c))
    print "2. count_players() returns 1 after one player is registered."
    register_player("Jace Beleren")
    c = count_players()
    if c != 2:
        raise ValueError(
            "After two players register, count_players() should be 2. Got {c}"
            .format(c=c))
    print "3. count_players() returns 2 after two players are registered."
    delete_players()
    c = count_players()
    if c != 0:
        raise ValueError(
            "After deletion, count_players should return zero.")
    print ("4. count_players() returns zero after registered players are "
           "deleted.\n5. Player records successfully deleted.")


def test_standings_before_matches():
    """
    Test to ensure players are properly represented in standings prior
    to any matches being reported.
    """
    delete_matches()
    delete_players()
    register_player("Melpomene Murray")
    register_player("Randy Schwartz")
    standings = player_standings()
    if len(standings) < 2:
        raise ValueError("Players should appear in player_standings even "
                         "before they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each player_standings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in "
                         "standings, even if they have no matches played.")
    print ("6. Newly registered players appear in the standings "
           "with no matches.")


def test_report_matches():
    """
    Test that matches are reported properly.
    Test to confirm matches are deleted properly.
    """
    delete_matches()
    delete_players()
    matches = count_matches()
    if matches == '0':
        raise TypeError(
            "count_matches should return numeric zero, not string '0'.")
    if matches != 0:
        raise ValueError("After deletion, count_matches should return zero.")
    register_player("Bruno Walton")
    register_player("Boots O'Neal")
    register_player("Cathy Burton")
    register_player("Diane Grant")
    standings = player_standings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    report_match(id1, id2)
    matches = count_matches()
    if matches != 1:
        raise ValueError("After first match, count_matches should return 1.")
    report_match(id3, id4)
    matches = count_matches()
    if matches != 2:
        raise ValueError("After second match, count_matches should return 2.")
    standings = player_standings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError(
                "Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError(
                "Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError(
                "Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."
    delete_matches()
    matches = count_matches()
    if matches != 0:
        raise ValueError("After deletion, count_matches should return zero.")
    standings = player_standings()
    if len(standings) != 4:
        raise ValueError("Match deletion should not change number of players "
                         "in standings.")
    for (i, n, w, m) in standings:
        if m != 0:
            raise ValueError("After deleting matches, players should have "
                             "zero matches recorded.")
        if w != 0:
            raise ValueError("After deleting matches, players should have "
                             "zero wins recorded.")
    print ("8. After match deletion, player standings are properly reset.\n9. "
           "Matches are properly deleted.")


def test_pairings():
    """
    Test that pairings are generated properly both before and after match
    reporting.
    """
    delete_matches()
    delete_players()
    register_player("Twilight Sparkle")
    register_player("Fluttershy")
    register_player("Applejack")
    register_player("Pinkie Pie")
    register_player("Rarity")
    register_player("Rainbow Dash")
    register_player("Princess Celestia")
    register_player("Princess Luna")
    standings = player_standings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    pairings = swiss_pairings()
    if len(pairings) != 4:
        raise ValueError(
            ("For eight players, swiss_pairings should return 4 pairs. "
             "Got {pairs}").format(pairs=len(pairings)))
    report_match(id1, id2)
    report_match(id3, id4)
    report_match(id5, id6)
    report_match(id7, id8)
    pairings = swiss_pairings()
    if len(pairings) != 4:
        raise ValueError(
            ("For eight players, swiss_pairings should return 4 pairs. "
             "Got {pairs}").format(pairs=len(pairings)))
    [
        (pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4),
        (pid5, pname5, pid6, pname6), (pid7, pname7, pid8, pname8)
    ] = pairings
    possible_pairs = set([frozenset([id1, id3]), frozenset([id1, id5]),
                          frozenset([id1, id7]), frozenset([id3, id5]),
                          frozenset([id3, id7]), frozenset([id5, id7]),
                          frozenset([id2, id4]), frozenset([id2, id6]),
                          frozenset([id2, id8]), frozenset([id4, id6]),
                          frozenset([id4, id8]), frozenset([id6, id8])
                          ])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4]),
                       frozenset([pid5, pid6]), frozenset([pid7, pid8])])
    for pair in actual_pairs:
        if pair not in possible_pairs:
            raise ValueError(
                "After one match, players with one win should be paired.")
    print "10. After one match, players with one win are properly paired."


def test_play_one_round():
    """
    Tests standings are correct after one round of play.
    """
    delete_matches()
    delete_players()
    register_player("Brandon")
    register_player("Jeff")
    register_player("Mackie")
    register_player("Duncan")
    register_player("Mo")
    register_player("Chris")
    register_player("Ricardo")
    register_player("Colin")
    standings = player_standings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    play_one_round(lambda p: ((p[0], p[1]), (p[2], p[3])))
    standings = player_standings()
    if ([id1, id3, id5, id7, id2, id4, id6, id8] !=
            [row[0] for row in standings]):
        # Idented due to long conditional
        raise ValueError(
            "After one round played, players should be in correct standings.")
    print "11. After play_one_round is run, players are in proper standings."


def test_play_full_tournament_manual():
    """
    Tests that pairings are correct after a full tournament (in this case,
    3 rounds), done with the play_one_round function.
    Winners are predetermined to allow for testing.
    """
    delete_matches()
    delete_players()
    register_player("Brandon")
    register_player("Jeff")
    register_player("Mackie")
    register_player("Duncan")
    register_player("Mo")
    register_player("Chris")
    register_player("Ricardo")
    register_player("Colin")
    standings = player_standings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    play_one_round(lambda p: ((p[0], p[1]), (p[2], p[3])))
    play_one_round(lambda p: ((p[0], p[1]), (p[2], p[3])))
    play_one_round(lambda p: ((p[0], p[1]), (p[2], p[3])))
    standings = player_standings()
    if ([id1, id5, id2, id6, id3, id4, id7, id8] !=
            [row[0] for row in standings]):
        # Idented due to long conditional
        raise ValueError(
            "After 3 rounds played, players should be in correct standings.")
    print "12. After 3 rounds played, players are in proper standings."


def test_play_full_tournament():
    """
    Tests that standings are correct after a full tournament,
    using play_tournament function.
    Winners are predetermined to allow for testing.
    """
    delete_matches()
    delete_players()
    register_player("Brandon")
    register_player("Jeff")
    register_player("Mackie")
    register_player("Duncan")
    register_player("Mo")
    register_player("Chris")
    register_player("Ricardo")
    register_player("Colin")
    standings = player_standings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    play_tournament(lambda p: ((p[0], p[1]), (p[2], p[3])))
    standings = player_standings()
    if ([id1, id5, id2, id6, id3, id4, id7, id8] !=
            [row[0] for row in standings]):
        raise ValueError(
            "After 3 rounds played, players should be in correct standings.")
    print "13. After 3 rounds played, players are in proper standings."

if __name__ == '__main__':
    test_count_players()
    test_standings_before_matches()
    test_report_matches()
    test_pairings()
    test_play_one_round()
    test_play_full_tournament_manual()
    test_play_full_tournament()
    print "Success!  All tests pass!"
