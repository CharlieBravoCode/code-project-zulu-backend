-- Creation of event table
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    identifier VARCHAR,
    title VARCHAR,
    location INTEGER,
    latitud FLOAT,
    longitud FLOAT
);


-- Fill the events table with random placeholder data 
INSERT INTO events (identifier, title, location, latitud, longitud)
VALUES ('abc123', 'Event 1', 1, 45.50, -73.58),
       ('def456', 'Event 2', 2, 41.50, -81.58),
       ('ghi789', 'Event 3', 3, 32.50, -96.58),
       ('jkl012', 'Event 4', 4, 39.50, -105.58),
       ('mno345', 'Event 5', 5, 35.50, -106.58),
       ('pqr678', 'Event 6', 6, 30.50, -107.58),
       ('stu901', 'Event 7', 7, 28.50, -108.58),
       ('vwx123', 'Event 8', 8, 33.50, -109.58),
       ('yz0456', 'Event 9', 9, 37.50, -110.58),
       ('789abc', 'Event 10', 10, 41.50, -111.58);