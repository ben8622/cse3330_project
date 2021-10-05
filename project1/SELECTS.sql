-- Part 2, #3 --
SELECT Name, Salary
FROM  Player
WHERE TEAM_ID = (
    SELECT Id
    FROM Team
    WHERE (name = 'Vegas Golden Knights')
);

-- Part 2, #4 --
SELECT *
FROM InjuryRecord
WHERE PLAYER_ID = (
  SELECT id
  FROM Player
  WHERE (name = 'Dylan Coghlan')
);

-- Part 2, #5 --
SELECT Captain , Name
FROM Team;

-- Part 2, #6 --
SELECT name, count
FROM (
	SELECT team_id, COUNT(team_id) AS count
	FROM Player
	GROUP BY team_id
) temp 
JOIN Team ON Team.id = temp.team_id
ORDER BY count DESC;

-- Part 2, #7 --
SELECT name, wins, losses, ties
FROM (
	SELECT HostTeam, COUNT(CASE WHEN HostTeamScore < GuestTeamScore THEN 1 END) as losses, COUNT(CASE WHEN HostTeamScore > GuestTeamScore THEN 1 END) as wins, COUNT(CASE WHEN HostTeamScore = GuestTeamScore THEN 1 END) as ties
	FROM Game
	GROUP BY HostTeam
) temp
JOIN Team ON Team.id = temp.HostTeam
ORDER BY wins DESC;