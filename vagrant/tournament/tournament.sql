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
    id serial,
    pid integer REFERENCES players (id),
    PRIMARY KEY (id, pid)
);
CREATE TABLE winners (
    match_id integer,
    pid integer REFERENCES players (id),
    PRIMARY KEY (match_id, pid),
    FOREIGN KEY (match_id, pid) REFERENCES matches (id, pid)
);
