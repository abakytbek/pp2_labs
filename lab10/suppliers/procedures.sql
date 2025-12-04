CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);

CREATE OR REPLACE FUNCTION search_records(pattern TEXT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name, phonebook.phone
    FROM phonebook
    WHERE phonebook.first_name ILIKE '%' || pattern || '%'
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE insert_or_update_user(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE phone = p_phone) THEN
        UPDATE phonebook
        SET first_name = p_name
        WHERE phone = p_phone;
    ELSE
        INSERT INTO phonebook(first_name, phone)
        VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

DROP PROCEDURE IF EXISTS insert_many_users(TEXT[], TEXT[]);

CREATE OR REPLACE FUNCTION insert_many_users(names TEXT[], phones TEXT[])
RETURNS TEXT[] AS $$
DECLARE
    i INT;
    bad_phones TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
    
        IF phones[i] !~ '^[0-9]+$' THEN
            bad_phones := array_append(bad_phones, phones[i]);
        ELSE
            INSERT INTO phonebook(first_name, phone)
            VALUES (names[i], phones[i])
            ON CONFLICT (phone) DO NOTHING;
        END IF;

    END LOOP;

    RETURN bad_phones;
END;
$$ LANGUAGE plpgsql;


DROP FUNCTION IF EXISTS get_paginated(INT, INT);

CREATE OR REPLACE FUNCTION get_paginated(limit_count INT, offset_count INT)
RETURNS TABLE(id INT, first_name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT phonebook.id, phonebook.first_name, phonebook.phone
    FROM phonebook
    ORDER BY phonebook.id
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE delete_user(p_name TEXT DEFAULT NULL, p_phone TEXT DEFAULT NULL)
AS $$
BEGIN
    IF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    ELSIF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE first_name = p_name;
    END IF;
END;
$$ LANGUAGE plpgsql;
