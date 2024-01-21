-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT  tv_genres.name, tv_shows.title
FROM tv_genres LEFT JOIN
tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title <> "Dexter"


