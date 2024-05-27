-- fill_pro_spread.sql

-- Delete exsiting probability and spread data
DELETE FROM keys_attributes_probability;
DELETE FROM attributes_spreading;

-- Fill the probability table
INSERT INTO keys_attributes_probability (
    attribute_id,
    attribute_name,
    Chicken,
    Pizza,
    Burger,
    Salad,
    Pasta,
    Sushi,
    Steak,
    Tacos,
    Soup,
    Sandwich,
    Fries,
    Hotdog,
    Curry,
    Rice,
    Fish,
    Cake
)
SELECT 
    attribute_id,
    attribute_name,
    (Chicken / NULLIF(total, 0)) * 100 AS Chicken,
    (Pizza / NULLIF(total, 0)) * 100 AS Pizza,
    (Burger / NULLIF(total, 0)) * 100 AS Burger,
    (Salad / NULLIF(total, 0)) * 100 AS Salad,
    (Pasta / NULLIF(total, 0)) * 100 AS Pasta,
    (Sushi / NULLIF(total, 0)) * 100 AS Sushi,
    (Steak / NULLIF(total, 0)) * 100 AS Steak,
    (Tacos / NULLIF(total, 0)) * 100 AS Tacos,
    (Soup / NULLIF(total, 0)) * 100 AS Soup,
    (Sandwich / NULLIF(total, 0)) * 100 AS Sandwich,
    (Fries / NULLIF(total, 0)) * 100 AS Fries,
    (Hotdog / NULLIF(total, 0)) * 100 AS Hotdog,
    (Curry / NULLIF(total, 0)) * 100 AS Curry,
    (Rice / NULLIF(total, 0)) * 100 AS Rice,
    (Fish / NULLIF(total, 0)) * 100 AS Fish,
    (Cake / NULLIF(total, 0)) * 100 AS Cake
FROM (
    SELECT 
        attribute_id,
        attribute_name,
        Chicken,
        Pizza,
        Burger,
        Salad,
        Pasta,
        Sushi,
        Steak,
        Tacos,
        Soup,
        Sandwich,
        Fries,
        Hotdog,
        Curry,
        Rice,
        Fish,
        Cake,
        (Chicken + Pizza + Burger + Salad + Pasta + Sushi + Steak + Tacos + Soup + Sandwich + Fries + Hotdog + Curry + Rice + Fish + Cake) AS total
    FROM keys_attributes
) AS subquery;

-- Fill the spread table
INSERT INTO attributes_spreading (attribute_id, attribute_name, key_word_covering)
SELECT 
    attribute_id,
    attribute_name,
    (CASE WHEN Chicken > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Pizza > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Burger > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Salad > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Pasta > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Sushi > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Steak > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Tacos > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Soup > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Sandwich > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Fries > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Hotdog > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Curry > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Rice > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Fish > 1 THEN 1 ELSE 0 END) +
    (CASE WHEN Cake > 1 THEN 1 ELSE 0 END) AS key_word_covering
FROM keys_attributes_probability;