-- Delete all data from the keys_attributes table
DELETE FROM keys_attributes;

-- Reset the auto-increment value of the attribute_id column
ALTER TABLE keys_attributes AUTO_INCREMENT = 1;