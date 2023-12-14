-- List all genres not linked to Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
    SELECT genre_id
    FROM tv_shows
    JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY name ASC;
