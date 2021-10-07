-- Always drop before creating to ensure a clean start --
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Game;
DROP TABLE IF EXISTS Player;
DROP TABLE IF EXISTS InjuryRecord;

-- Create all of our needed tables --
CREATE TABLE Team
(
	Id int PRIMARY KEY,
	Name varchar(255),
	City varchar(255),
	Coach varchar(255),
	Captain varchar(255)
);

CREATE TABLE Game
(
  Id int PRIMARY KEY,
  HostTeam int,
	GuestTeam int,
	HostTeamScore int,
	GuestTeamScore int,
	Date date
);

CREATE TABLE Player
(
	Id int PRIMARY KEY,
	Team_Id int,
	Name varchar (255),
	Position varchar(255),
	SkillLevel int,
	Salary int
);

CREATE TABLE InjuryRecord
(
	ID int PRIMARY KEY,
	PLAYER_ID int,
	INCI_DESC varchar(255),
	INJ_DESC varchar(255)
);