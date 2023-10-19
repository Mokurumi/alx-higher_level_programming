-- lists all shows without the genre Comedy
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results are sorted in ascending order by show title
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT DISTINCT tv_show_genres.show_id
    FROM tv_show_genres
    JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title;
