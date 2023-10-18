-- lists all cities contained in the database with the name of their state
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
