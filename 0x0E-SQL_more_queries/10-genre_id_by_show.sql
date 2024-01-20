-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT title, genre.id FROM tv_shows, tv_show_genres INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC tv_show_genres.genre_id;
