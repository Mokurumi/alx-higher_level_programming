-- lists all the cities of California state that can be found in the database
-- filter all cities with state_id that is equal to id of California
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
