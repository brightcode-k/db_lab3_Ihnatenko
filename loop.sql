DO $$
DECLARE
    math_score scoring.math_score%TYPE;
	reading_score scoring.reading_score%TYPE;
	writing_score scoring.writing_score%TYPE;
    stud_id scoring.stud_id%TYPE;
BEGIN
    math_score := 43;
	reading_score := 68;
	writing_score := 88;
    stud_id := 7;
    FOR counter IN 1..10
        LOOP
            INSERT INTO scoring(math_score,reading_score,writing_score,stud_id)
            VALUES (counter + math_score, counter + reading_score, counter + writing_score, stud_id + counter);
        END LOOP;
END;
$$
SELECT * FROM scoring