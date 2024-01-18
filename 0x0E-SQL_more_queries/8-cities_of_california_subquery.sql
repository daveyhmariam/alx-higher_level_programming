-- lists all the cities of California that can be found in the database hbtn_0d_usa

SELECT id
FROM hbtn_0d_usa.states
WHERE name = 'California' AS states_id;
SELECT id, name FROM cities
WHERE state_id = states_id
GROUP BY id, name
ORDER BY id ASC;