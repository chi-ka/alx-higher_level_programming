-- List all shows without the genre Comedy
SELECT title
FROM tv_shows
WHERE id NOT IN (
    SELECT show_id
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY title ASC;
