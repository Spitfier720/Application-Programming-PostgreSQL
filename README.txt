# Setting Up The Program:

This requires pgAdmin 4, which is a GUI for PostgreSQL. You can download it from [here]
(https://www.pgadmin.org/download/).

1. Open up pgAdmin 4 and create a new Database, named "students".
2. Create a new table in the "students" database using the following command:
```
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
)
```
3. Insert some data into the table either manually, or you can use the following command to insert some sample data:
```
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
```

# Running the Program:
Either using an IDE of choice or the command line will run the program.
The program will prompt for input until an exit code is given.

# Video Demonstration:
A video demonstration of the program can be found [here](https://youtu.be/EPhj8m7zml4).