DROP PROCEDURE IF EXISTS create_attributes_keys_sorted_columns;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_attributes_keys_sorted_columns`(IN column_list VARCHAR(255))
BEGIN
    -- Drop the table if it already exists
    SET @drop_sql = CONCAT('DROP TABLE IF EXISTS attributes_keys_sorted_columns;');
    PREPARE drop_stmt FROM @drop_sql;
    EXECUTE drop_stmt;
    DEALLOCATE PREPARE drop_stmt;
    -- Create the table
    SET @sql = CONCAT(
        'CREATE TABLE attributes_keys_sorted_columns AS ',
        'SELECT attribute_id, attribute_name, ', column_list,
        ' FROM attributes_keys;'
    );
    PREPARE stmt FROM @sql;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END;
DROP PROCEDURE IF EXISTS copy_attributes_keys;
CREATE DEFINER=`root`@`localhost` PROCEDURE `copy_attributes_keys`()
BEGIN
    -- Drop the table if it already exists
    DROP TABLE IF EXISTS final_attributes_keys;
    CREATE TABLE final_attributes_keys LIKE attributes_keys;
    -- Set all values to 0 in the copied table
    INSERT INTO final_attributes_keys
    SELECT attribute_id, attribute_name,
           0 AS Chicken, 0 AS Pizza, 0 AS Burger, 0 AS Salad,
           0 AS Pasta, 0 AS Sushi, 0 AS Steak, 0 AS Tacos,
           0 AS Soup, 0 AS Sandwich, 0 AS Fries, 0 AS Hotdog,
           0 AS Curry, 0 AS Rice, 0 AS Fish, 0 AS Cake
    FROM attributes_keys;
END;
DROP PROCEDURE IF EXISTS copy_sorted_columns_to_final_attributes_keys;
CREATE DEFINER=`root`@`localhost` PROCEDURE `copy_sorted_columns_to_final_attributes_keys`()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE col_name VARCHAR(50);
    DECLARE cur CURSOR FOR 
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'attributes_keys_sorted_columns';
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
    -- Open the cursor
    OPEN cur;
    attribute_loop: LOOP
        FETCH cur INTO col_name;
        IF done THEN
            LEAVE attribute_loop;
        END IF;
        IF EXISTS (
            SELECT 1
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = 'final_attributes_keys'
            AND COLUMN_NAME = col_name
        ) THEN
            -- Update the values in attribute_column_mapping_big with the values from attribute_column_mapping
            SET @sql = CONCAT(
                'UPDATE final_attributes_keys AS big ',
                'INNER JOIN attributes_keys_sorted_columns AS small ON big.attribute_id = small.attribute_id ',
                'SET big.', col_name, ' = small.', col_name
            );
            PREPARE stmt FROM @sql;
            EXECUTE stmt;
            DEALLOCATE PREPARE stmt;
        END IF;
    END LOOP attribute_loop;

    -- Close the cursor
    CLOSE cur;
END;
-- Drop the procedure if it already exists
DROP PROCEDURE IF EXISTS create_final_attributes_keys;
CREATE PROCEDURE `create_final_attributes_keys`()
BEGIN
    -- Initialize the variable to store the list of keywords
    SET @keyword_list = NULL;
    SET @row_count = (SELECT COUNT(*) FROM attributes_keys_sorted_rows);
    -- Select and concatenate the keywords where count is less than the number of rows in final_attributes
    SELECT GROUP_CONCAT(key_word) INTO @keyword_list
    FROM attributes_keys_sorted_column_sums_transpose
    WHERE count > @row_count - 1;
    -- Call the stored procedure with the list of keywords
    CALL create_attributes_keys_sorted_columns(@keyword_list);
    CALL copy_attributes_keys();
    CALL copy_sorted_columns_to_final_attributes_keys();
END;
DROP PROCEDURE IF EXISTS create_attributes_keys_sorted_rows;
CREATE PROCEDURE `create_attributes_keys_sorted_rows`(IN attribute_ids_list VARCHAR(255))
BEGIN
    -- Drop the table if it already exists
    DROP TABLE IF EXISTS attributes_keys_sorted_rows;
    -- Set the initial row variable
    SET @row := -1;
    CREATE TABLE attributes_keys_sorted_rows AS
    SELECT *
    FROM attributes_keys
    WHERE attribute_id IN (
        SELECT CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(attribute_ids_list, ',', numbers.n), ',', -1) AS UNSIGNED) AS attribute_id
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
        WHERE numbers.n <= 1 + (CHAR_LENGTH(attribute_ids_list) - CHAR_LENGTH(REPLACE(attribute_ids_list, ',', '')))
        AND TRIM(SUBSTRING_INDEX(SUBSTRING_INDEX(attribute_ids_list, ',', numbers.n), ',', -1)) != ''
    );
END;