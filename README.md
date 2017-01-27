# Swiss Style Tournament Results

Track a [Swiss-style tournament](https://en.wikipedia.org/wiki/Swiss-system_tournament).
Register players, pair players, record match
winners, and see player standings.



This is my Tournament Results project for my Udacity Full Stack Nanodegree.

## Installation

Here's how to get up and running.

### 1. Launch Virtual Machine

If not already installed, install [Vagrant](http://vagrantup.com/) and
[VirtualBox](https://www.virtualbox.org/).

From within `/vagrant` directory within repo.

```
vagrant up
vagrant ssh
```

Once in Vagrant VM, navigate to synced `tournament` directory from within the VM:

```
cd /vagrant/tournament
```

### 2. Build Database

This project is built with PostgreSQL.

To build the database, run:

```sql
psql

\i tournament.sql
```

Exit psql with `\q`.

### 3. Make Sure Everything Is Installed

Run this command:

```python
python tournament_script.py
```

This registers 8 players and runs a full tournament. It then outputs final
standings

You should receive output like this:

```python
Players registered: 8
Tournament complete.
Player standings:
    Colin, wins: 3
    Mackie, wins: 2
    Duncan, wins: 2
...
```

## Getting Started

Here are the python functions you can use from the tournament.py module.

```python
# Delete all matches from database
delete_matches()

# Delete all players from database
delete_players()

# Return number of matches played
count_matches()

# Return number of players registered
count_players()

# Add a player. Name should be a string.
register_player(name)

# Shows all players, ordered by wins, then by score, then by id.
# Return a list of tuples with player data: (id, name, wins, matches).
player_standings()

# Record a match to database. Winner and Loser should be player ids.
report_match(winner, loser):

# Pairs players for next round.
# Returns a list of tuples, each of which contains (id1, name1, id2, name2)
swiss_pairings()

# Play one round of tournament.
# All matches reported to database. By default, each player has a
# 50/50 chance of winning. Can change this by inputting a different match_f
play_one_round(match_f=win_half):

# Play a full tournament
play_tournament(match_f=win_half):
```

## Running The Tests

A test file is included to be sure all built in commands work properly.

Test is run with:

```python
python tournament_test.py
```

## Acknowledgments

* Starting code provided by [Udacity](https://github.com/udacity/fullstack-nanodegree-vm)
