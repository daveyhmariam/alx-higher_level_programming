-- script that lists all shows from hbtn_0d_tvshows_rate by their rating

SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS 'ratings'
FROM tv_shows, tv_show_ratings
WHERE tv_shows.id = tv_show_ratings.show_id
GROUP BY title
ORDER BY ratings DESC;