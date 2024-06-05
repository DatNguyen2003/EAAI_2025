-- fill_pro_spread.sql

-- Delete exsiting probability, navie_bayes and spread data
DELETE FROM attributes_keys_probability;
DELETE FROM attributes_spreading;

-- Fill the probability table
INSERT INTO attributes_keys_probability (
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
    ((Chicken) / NULLIF(total, 0)) AS Chicken,
    ((Pizza) / NULLIF(total, 0)) AS Pizza,
    ((Burger) / NULLIF(total, 0)) AS Burger,
    ((Salad) / NULLIF(total, 0)) AS Salad,
    ((Pasta) / NULLIF(total, 0)) AS Pasta,
    ((Sushi) / NULLIF(total, 0)) AS Sushi,
    ((Steak) / NULLIF(total, 0)) AS Steak,
    ((Tacos) / NULLIF(total, 0)) AS Tacos,
    ((Soup) / NULLIF(total, 0)) AS Soup,
    ((Sandwich) / NULLIF(total, 0)) AS Sandwich,
    ((Fries) / NULLIF(total, 0)) AS Fries,
    ((Hotdog) / NULLIF(total, 0)) AS Hotdog,
    ((Curry) / NULLIF(total, 0)) AS Curry,
    ((Rice) / NULLIF(total, 0)) AS Rice,
    ((Fish) / NULLIF(total, 0)) AS Fish,
    ((Cake) / NULLIF(total, 0)) AS Cake
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
    FROM final_attributes_keys
) AS subquery;

-- Fill the spread table
INSERT INTO attributes_spreading (attribute_id, attribute_name, key_word_covering)
SELECT 
    attribute_id,
    attribute_name,
    (CASE WHEN Chicken > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Pizza > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Burger > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Salad > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Pasta > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Sushi > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Steak > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Tacos > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Soup > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Sandwich > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Fries > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Hotdog > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Curry > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Rice > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Fish > 0.01 THEN 1 ELSE 0 END) +
    (CASE WHEN Cake > 0.01 THEN 1 ELSE 0 END) AS key_word_covering
FROM attributes_keys_probability;