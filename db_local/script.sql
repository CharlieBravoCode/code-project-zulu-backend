-- Creation of event table
CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    identifier VARCHAR,
    title VARCHAR,
    location INTEGER,
    latitud FLOAT,
    longitud FLOAT
);

-- Fill the events table with random placeholder data 
INSERT INTO events (id, identifier, title, location, latitud, longitud)
VALUES (1, 'abc123', 'Event 1', 1, 45.50, -73.58),
       (2, 'def456', 'Event 2', 2, 41.50, -81.58),
       (3, 'ghi789', 'Event 3', 3, 32.50, -96.58),
       (4, 'jkl012', 'Event 4', 4, 39.50, -105.58),
       (5, 'mno345', 'Event 5', 5, 35.50, -106.58);
       (6, 'pqr678', 'Event 6', 6, 30.50, -107.58),
       (7, 'stu901', 'Event 7', 7, 28.50, -108.58),
       (8, 'vwx123', 'Event 8', 8, 33.50, -109.58),
       (9, 'yz0456', 'Event 9', 9, 37.50, -110.58),
       (10, '789abc', 'Event 10', 10, 41.50, -111.58);