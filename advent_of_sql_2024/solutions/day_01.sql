SELECT
c.name,
w.wishes ->> 'first_choice' primary_wish,
w.wishes ->> 'second_choice' backup_wish,
w.wishes -> 'colors' ->> 0 favoite_color,
JSON_ARRAY_LENGTH(w.wishes -> 'colors') color_count,
CASE
    WHEN t.difficulty_to_make = 1 THEN 'Simple Gift'
    WHEN t.difficulty_to_make = 2 THEN 'Moderate Gift'
    ELSE 'Complex Gift'
END AS gift_complexity,
CASE 
    WHEN t.category = 'outdoor' THEN 'Outside Workshop'
    WHEN t.category = 'educational' THEN 'Learning Workshop'
    ELSE 'General Workshop'
END AS workshop_assignment
FROM children c
INNER JOIN wish_lists w
ON c.child_id = w.child_id
INNER JOIN toy_catalogue t
ON w.wishes ->> 'first_choice' = t.toy_name
ORDER BY c.name ASC
;