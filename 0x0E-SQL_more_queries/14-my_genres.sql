-- lists all genres lists all genres of the show Dexter
-- Each record displays: tv_genres.name
-- Doesn’t display a genre that doesn’t have any shows linked
-- Results are sorted in descending order by genre name
SELECT tv_genres.name
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
