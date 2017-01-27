-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament

CREATE TABLE players (
  id serial PRIMARY KEY,
  name text
);

CREATE TABLE matches (
  id serial PRIMARY KEY,
  winner integer REFERENCES players (id),
  loser integer REFERENCES players (id)
);

-- For adding multi-tournament functionality
CREATE TABLE tournament (
  id serial PRIMARY KEY,
  name text
)

-- A view for count of wins for each player
CREATE VIEW win_counts_v AS
  SELECT
    players.id,
    count(matches.id) AS win_count
  FROM players
  LEFT JOIN matches ON players.id = matches.winner
  GROUP BY players.id;

-- A view for count of matches for each player
CREATE VIEW match_counts_v AS
  SELECT
    players.id,
    count(matches.id) AS match_count
  FROM players
  LEFT JOIN matches
  ON players.id = matches.winner OR players.id = matches.loser
  GROUP BY players.id;

-- A view for each player's score (sum of beaten opponents' scores)
CREATE VIEW score_v AS
  SELECT
    players.id,
    COALESCE(sum(wins.win_count), 0) AS score
  FROM players
  LEFT JOIN matches ON players.id = matches.winner
  LEFT JOIN win_counts_v AS wins ON wins.id = matches.loser
  GROUP BY players.id;
