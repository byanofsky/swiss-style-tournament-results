#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#
from functools import wraps
import psycopg2


def db_connect(f):
    """Decorator for opening and closing db connection."""
    @wraps(f)
    def wrapper(*a, **kw):
        # Connect to database and open cursor
        conn = psycopg2.connect("dbname=tournament")
        cur = conn.cursor()

        # Call function and save return to result
        result = f(cur, conn, *a, **kw)

        # Close cursor and database connections
        cur.close()
        conn.close()

        # Return any results from database call
        return result
    return wrapper


@db_connect
def delete_matches(cur, conn):
    """Remove all the match records from the database."""
    cur.execute("DELETE FROM matches;")
    conn.commit()


@db_connect
def count_matches(cur, conn):
    """Counts total number of matches played."""
    cur.execute("SELECT count(*) FROM matches;")
    row = cur.fetchone()
    count = int(row[0])
    return count


@db_connect
def delete_players(cur, conn):
    """Remove all the player records from the database."""
    cur.execute("DELETE FROM players;")
    conn.commit()

@db_connect
def count_players(cur, conn):
    """Returns the number of players currently registered."""
    cur.execute("SELECT count(*) FROM players;")
    row = cur.fetchone()
    count = int(row[0])
    return count

@db_connect
def register_player(cur, conn, name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    cur.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    conn.commit()

@db_connect
def player_standings(cur, conn):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    cur.execute('''
        SELECT players.id,
               players.name,
               win_c.win_count as wins,
               match_c.match_count as total_matches
        FROM players
        LEFT JOIN win_counts_v as win_c
            ON players.id = win_c.id
        LEFT JOIN match_counts_v as match_c
            ON players.id = match_c.id
        ORDER BY wins DESC, players.id;
    ''')
    return cur.fetchall()

@db_connect
def report_match(cur, conn, winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    cur.execute(
        "INSERT INTO matches (winner, loser) VALUES (%s, %s);",
        (winner, loser)
    )
    conn.commit()


def swiss_pairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = player_standings()
    pairs = []
    while standings:
        p1 = standings.pop(0)
        p2 = standings.pop(0)
        pairs.append((p1[0], p1[1], p2[0], p2[1]))
    return pairs
