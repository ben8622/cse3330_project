-- Part 2, #3 --
SELECT (Name, Salary)
FROM  Player
WHERE TEAM_ID = 1; -- TODO: might wanna grab the name somehow then use ID

-- Part 2, #4 --
SELECT *
FROM InjuryRecord
WHERE PLAYER_ID = 2; -- TODO: might wanna grab the name somehow then use ID

-- Part 2, #5 --
SELECT Captain , Name
FROM Team;

--SELECT Name, TEAM_ID, COUNT(Player.*)
--FROM Player
--WHERE Player

SELECT Team.Name, HostTeamScore, GuestTeamScore 
FROM Game
INNER JOIN Team ON Game.HostTeam = Team.ID;