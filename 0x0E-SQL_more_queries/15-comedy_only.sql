-- lists all genres lists all Comedy shows in the database
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record displays: tv_shows.title
-- Results are sorted in descending order by genre name
SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title;
