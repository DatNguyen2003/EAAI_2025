CREATE TABLE attributes_spreading (
    attribute_id INT PRIMARY KEY,
    attribute_name VARCHAR(255),
    key_word_covering INT
);
INSERT INTO attribute_spreading (attribute_id, attribute_name, key_word_covering)
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
FROM keys_attributes;