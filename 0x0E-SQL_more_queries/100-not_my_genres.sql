-- lists all genres lists all genres not of the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record displays: tv_genres.name
-- Results are sorted in ascending order by genre name
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN (
    SELECT DISTINCT tv_show_genres.genre_id
    FROM tv_show_genres
    JOIN tv_shows
    ON tv_show_genres.show_id = tv_shows.id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
