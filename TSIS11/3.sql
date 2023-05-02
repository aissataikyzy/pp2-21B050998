CREATE OR REPLACE PROCEDURE update_phone(
    user_first_name VARCHAR(255), 
    user_last_name VARCHAR(255),
    user_phone VARCHAR(255)
) AS $$
BEGIN
	UPDATE phonebook SET phone = user_phone WHERE first_name = user_first_name and last_name = user_last_name;
END;
$$
LANGUAGE plpgsql;