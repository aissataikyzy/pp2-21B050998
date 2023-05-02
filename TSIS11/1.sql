CREATE OR REPLACE FUNCTION username()
  RETURNS TABLE(first_name VARCHAR(255), last_name VARCHAR(255)) AS
$$
BEGIN
 RETURN QUERY

 SELECT phonebook.first_name, phonebook.last_name
 FROM phonebook;

END; $$

LANGUAGE plpgsql;