-- List all shows with their genres and ratings
SELECT
    tv_shows.title,
    GROUP_CONCAT(DISTINCT tv_genres.name ORDER BY tv_genres.name ASC) AS genres,
    IFNULL(SUM(tv_show_ratings.rate), 0) AS rating_sum
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
LEFT JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating_sum DESC, tv_shows.title ASC;
