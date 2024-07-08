-- Drop the temporary table if it already exists
DROP TEMPORARY TABLE IF EXISTS temp_attributes_keys_sorted_rows;
DROP TABLE IF EXISTS attributes_keys_sorted_rows;

-- Set the initial row variable
SET @row := -1;

-- Define the attribute IDs list
SET @attribute_ids_list = '1,2,3';

-- Create the temporary table
CREATE TEMPORARY TABLE temp_attributes_keys_sorted_rows AS
SELECT *
FROM attributes_keys
WHERE attribute_id IN (
    SELECT CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(@attribute_ids_list, ',', numbers.n), ',', -1) AS UNSIGNED) AS attribute_id
    FROM (
        SELECT @row := @row + 1 AS n
        FROM (
            SELECT 0 AS dummy UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
        ) AS A,
        (
            SELECT 0 AS dummy UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
        ) AS B,
        (
            SELECT 0 AS dummy UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
        ) AS C,
        (
            SELECT 0 AS dummy UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4
        ) AS D
    ) AS numbers
    WHERE numbers.n <= 1 + (CHAR_LENGTH(@attribute_ids_list) - CHAR_LENGTH(REPLACE(@attribute_ids_list, ',', '')))
    AND TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(@attribute_ids_list, ',', numbers.n), ',', -1)) != ''
);

-- Create the attributes_keys_sorted_rows table
CREATE TABLE attributes_keys_sorted_rows AS
SELECT * FROM temp_attributes_keys_sorted_rows;

-- Drop the temporary table
DROP TEMPORARY TABLE IF EXISTS temp_attributes_keys_sorted_rows;
DROP TABLE IF EXISTS attributes_keys_sorted_column_sums;

CREATE TABLE attributes_keys_sorted_column_sums AS
SELECT
    GREATEST(SUM(CASE WHEN Chicken > 1 THEN 1 ELSE Chicken END), 0) AS Chicken,
    GREATEST(SUM(CASE WHEN Pizza > 1 THEN 1 ELSE Pizza END), 0) AS Pizza,
    GREATEST(SUM(CASE WHEN Burger > 1 THEN 1 ELSE Burger END), 0) AS Burger,
    GREATEST(SUM(CASE WHEN Salad > 1 THEN 1 ELSE Salad END), 0) AS Salad,
    GREATEST(SUM(CASE WHEN Pasta > 1 THEN 1 ELSE Pasta END), 0) AS Pasta,
    GREATEST(SUM(CASE WHEN Sushi > 1 THEN 1 ELSE Sushi END), 0) AS Sushi,
    GREATEST(SUM(CASE WHEN Steak > 1 THEN 1 ELSE Steak END), 0) AS Steak,
    GREATEST(SUM(CASE WHEN Tacos > 1 THEN 1 ELSE Tacos END), 0) AS Tacos,
    GREATEST(SUM(CASE WHEN Soup > 1 THEN 1 ELSE Soup END), 0) AS Soup,
    GREATEST(SUM(CASE WHEN Sandwich > 1 THEN 1 ELSE Sandwich END), 0) AS Sandwich,
    GREATEST(SUM(CASE WHEN Fries > 1 THEN 1 ELSE Fries END), 0) AS Fries,
    GREATEST(SUM(CASE WHEN Hotdog > 1 THEN 1 ELSE Hotdog END), 0) AS Hotdog,
    GREATEST(SUM(CASE WHEN Curry > 1 THEN 1 ELSE Curry END), 0) AS Curry,
    GREATEST(SUM(CASE WHEN Rice > 1 THEN 1 ELSE Rice END), 0) AS Rice,
    GREATEST(SUM(CASE WHEN Fish > 1 THEN 1 ELSE Fish END), 0) AS Fish,
    GREATEST(SUM(CASE WHEN Cake > 1 THEN 1 ELSE Cake END), 0) AS Cake
FROM attributes_keys_sorted_rows;

-- Drop the table if it already exists
DROP TABLE IF EXISTS attributes_keys_sorted_column_sums_transpose;

-- Create the table with key_word and count columns
CREATE TABLE attributes_keys_sorted_column_sums_transpose (
    key_word VARCHAR(50),
    count INT
);

-- Insert the keywords and their counts into the table
INSERT INTO attributes_keys_sorted_column_sums_transpose (key_word, count)
VALUES
    ('Chicken', (SELECT Chicken FROM attributes_keys_sorted_column_sums)),
    ('Pizza', (SELECT Pizza FROM attributes_keys_sorted_column_sums)),
    ('Burger', (SELECT Burger FROM attributes_keys_sorted_column_sums)),
    ('Salad', (SELECT Salad FROM attributes_keys_sorted_column_sums)),
    ('Pasta', (SELECT Pasta FROM attributes_keys_sorted_column_sums)),
    ('Sushi', (SELECT Sushi FROM attributes_keys_sorted_column_sums)),
    ('Steak', (SELECT Steak FROM attributes_keys_sorted_column_sums)),
    ('Soup', (SELECT Soup FROM attributes_keys_sorted_column_sums)),
    ('Sandwich', (SELECT Sandwich FROM attributes_keys_sorted_column_sums)),
    ('Fries', (SELECT Fries FROM attributes_keys_sorted_column_sums)),
    ('Hotdog', (SELECT Hotdog FROM attributes_keys_sorted_column_sums)),
    ('Curry', (SELECT Curry FROM attributes_keys_sorted_column_sums)),
    ('Rice', (SELECT Rice FROM attributes_keys_sorted_column_sums)),
    ('Fish', (SELECT Fish FROM attributes_keys_sorted_column_sums)),
    ('Cake', (SELECT Cake FROM attributes_keys_sorted_column_sums));
