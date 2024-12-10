SELECT
	STRING_AGG(CAST(CHR(value) AS VARCHAR), '') AS letter
FROM
(
  SELECT * FROM letters_a
  UNION ALL
  SELECT * FROM letters_b
)
WHERE value IN (32, 33, 34, 39, 40, 41, 44, 45, 46, 58, 59, 63)
OR value BETWEEN 65 AND 90
OR value BETWEEN 97 AND 122