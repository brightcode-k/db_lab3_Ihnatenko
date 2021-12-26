CREATE TABLE students
(
	stud_id INT PRIMARY KEY,
	name VARCHAR(40) NOT NULL,
	surname VARCHAR(50) NOT NULL,
	level_of_education VARCHAR(60)
);

CREATE TABLE scoring
(
	stud_id INT NOT NULL REFERENCES students (stud_id),
	math_score INT,
	reading_score INT,
	writing_score INT
);

CREATE TABLE gender
(
	stud_id INT NOT NULL REFERENCES students (stud_id),
	gender VARCHAR(2)
);