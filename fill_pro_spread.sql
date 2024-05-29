-- fill_pro_spread.sql

-- Delete exsiting probability, navie_bayes and spread data
DELETE FROM attributes_keys_probability;
DELETE FROM naive_bayes;
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
    ((Chicken+1) / NULLIF(total, 0)) AS Chicken,
    ((Pizza+1) / NULLIF(total, 0)) AS Pizza,
    ((Burger+1) / NULLIF(total, 0)) AS Burger,
    ((Salad+1) / NULLIF(total, 0)) AS Salad,
    ((Pasta+1) / NULLIF(total, 0)) AS Pasta,
    ((Sushi+1) / NULLIF(total, 0)) AS Sushi,
    ((Steak+1) / NULLIF(total, 0)) AS Steak,
    ((Tacos+1) / NULLIF(total, 0)) AS Tacos,
    ((Soup+1) / NULLIF(total, 0)) AS Soup,
    ((Sandwich+1) / NULLIF(total, 0)) AS Sandwich,
    ((Fries+1) / NULLIF(total, 0)) AS Fries,
    ((Hotdog+1) / NULLIF(total, 0)) AS Hotdog,
    ((Curry+1) / NULLIF(total, 0)) AS Curry,
    ((Rice+1) / NULLIF(total, 0)) AS Rice,
    ((Fish+1) / NULLIF(total, 0)) AS Fish,
    ((Cake+1) / NULLIF(total, 0)) AS Cake
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
        (Chicken + Pizza + Burger + Salad + Pasta + Sushi + Steak + Tacos + Soup + Sandwich + Fries + Hotdog + Curry + Rice + Fish + Cake + 16) AS total
    FROM attributes_keys
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