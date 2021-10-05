-- Insert Teams --
INSERT INTO Team VALUES (1,'Vegas Golden Knights','Las Vegas','Peter DeBoer','Mark Stone');
INSERT INTO Team VALUES (2,'Tampa Bay Lightning','Tampa','Jon Cooper','Steven Stamkos');
INSERT INTO Team VALUES (3,'Colorado Avalanche','Denver','Jared Bednar','Gabriel Landeskog');
INSERT INTO Team VALUES (4,'Washington Capitals','Washington D.C.','Peter Laviolette','Alexander Ovechkin');
INSERT INTO Team VALUES (5,'Florida Panthers','Miami','Joel Quenneville','Aleksander Barkov');
INSERT INTO Team VALUES (6,'New York Islanders','Elmont','Barry Trotz','Anders Lee');
INSERT INTO Team VALUES (7,'St. Louis Blues','St. Louis','Craig Berube','Ryan OReilly');
INSERT INTO Team VALUES (8,'Philadelphia Flyers','Philadelphia','Alain Vigneault','Claude Giroux');
INSERT INTO Team VALUES (9,'Chicago Blackhawks','Chicago','Jeremy Colliton','Jonathan Toews');
INSERT INTO Team VALUES (10,'Calgary Flames','Calgary','Darryl Sutter','Connor Mackey');

-- Insert Players --
INSERT INTO Player VALUES(1,1,'Robin Lehner','GT',1,4520890);
INSERT INTO Player VALUES(2,1,'Dylan Coghlan','D',6,2520890);
INSERT INTO Player VALUES(3,1,'Tomas Jurco','RW',4,11462000);
INSERT INTO Player VALUES(4,1,'Alex Pietrangelo','D',1,2520890);
INSERT INTO Player VALUES(5,1,'Cody Glass','C',4,12500000);
INSERT INTO Player VALUES(6,1,'Gage Quinney','F',5,4520890);
INSERT INTO Player VALUES(7,1,'Max Pacioretty','LW',4,4520890);
INSERT INTO Player VALUES(8,1,'Paul Stastny','C',2,12000000);
INSERT INTO Player VALUES(9,1,'Daniel Carr','LW',6,11000000);
INSERT INTO Player VALUES(10,1,'Brayden McNabb','D',1,11000000);
INSERT INTO Player VALUES (12,2,'Steven Stamkos','C',4,2520890);
INSERT INTO Player VALUES (26,5,'Aleksander Barkov','C',3,8400000);
INSERT INTO Player VALUES (30,6,'Anders Lee','C',6,9200000);

-- Insert Games --
INSERT INTO Game VALUES (1,1,5,5,4,'2020-12-12');
INSERT INTO Game VALUES (2,5,4,6,2,'2020-12-13');
INSERT INTO Game VALUES (3,2,7,4,1,'2020-12-14');
INSERT INTO Game VALUES (4,5,6,3,3,'2020-12-15');
INSERT INTO Game VALUES (5,10,1,2,1,'2020-12-17');
INSERT INTO Game VALUES (6,6,7,1,0,'2020-12-20');
INSERT INTO Game VALUES (7,2,3,6,0,'2020-12-23');
INSERT INTO Game VALUES (8,3,4,5,1,'2020-12-25');
INSERT INTO Game VALUES (9,4,5,5,6,'2020-12-28');
INSERT INTO Game VALUES (10,5,6,6,3,'2021-01-03');
INSERT INTO Game VALUES (11,1,9,6,3,'2021-01-10');
INSERT INTO Game VALUES (12,7,8,4,5,'2021-01-13');
INSERT INTO Game VALUES (13,2,9,3,1,'2021-01-14');
INSERT INTO Game VALUES (14,9,5,5,2,'2021-01-16');
INSERT INTO Game VALUES (15,3,10,1,3,'2021-02-03');
INSERT INTO Game VALUES (16,2,7,5,1,'2021-02-03');
INSERT INTO Game VALUES (17,4,9,2,1,'2021-02-03');
INSERT INTO Game VALUES (18,6,1,3,4,'2021-02-05');
INSERT INTO Game VALUES (19,8,3,3,2,'2021-02-05');
INSERT INTO Game VALUES (20,1,5,5,5,'2021-02-10');

-- Insert InjuryRecord --
INSERT INTO InjuryRecord VALUES(1,11,'High-impact contact from other players','Broken collarbone');
INSERT INTO InjuryRecord VALUES(2,22,'Rigid board collision','MCL strains or tears');
INSERT INTO InjuryRecord VALUES(3,41,'Ice collision to the head','Concussion');
INSERT INTO InjuryRecord VALUES(4,32,'Sudden Stop to board impact' ,'Hamstring Pull');
INSERT INTO InjuryRecord VALUES(5,22,'Ice Impact','Ankle Sprain');
INSERT INTO InjuryRecord VALUES(6,19,'Falling on the ice','Seperated Sholder');
INSERT INTO InjuryRecord VALUES(7,25,'High-impact contact on ice','Concssion');
INSERT INTO InjuryRecord VALUES(8,6,'Falling on the ice','Broken collarbone');
INSERT INTO InjuryRecord VALUES(9,10,'Sudden Stop to board impact ','Sholder Sprain');
INSERT INTO InjuryRecord VALUES(10,2,'Board and Player Impact','AC Seperation');