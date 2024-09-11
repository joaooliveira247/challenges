CREATE TABLE employee(
    Fname VARCHAR(15) NOT NULL,
    Minit CHAR,
    Lname VARCHAR(15) NOT NULL,
    Ssn CHAR(9) NOT NULL,
    Bdate DATE,
    Address VARCHAR(30),
    Sex CHAR,
    Salary NUMERIC(10, 2),
    Super_ssn CHAR(9),
    Dno INT NOT NULL DEFAULT 1,
    CONSTRAINT chk_salary_employee CHECK (Salary > 2000.0),
    CONSTRAINT pk_employee PRIMARY KEY (Ssn)
);

-- Add foreign key constraint to employee table
ALTER TABLE employee
    ADD CONSTRAINT fk_employee
    FOREIGN KEY (Super_ssn) REFERENCES employee(Ssn)
    ON DELETE SET NULL
    ON UPDATE CASCADE;

-- Create departament table
CREATE TABLE departament(
    Dname VARCHAR(15) NOT NULL,
    Dnumber INT NOT NULL,
    Mgr_ssn CHAR(9) NOT NULL,
    Mgr_start_date DATE,
    Dept_create_date DATE,
    CONSTRAINT chk_date_dept CHECK (Dept_create_date < Mgr_start_date),
    CONSTRAINT pk_dept PRIMARY KEY (Dnumber),
    CONSTRAINT unique_name_dept UNIQUE (Dname),
    FOREIGN KEY (Mgr_ssn) REFERENCES employee(Ssn)
);

-- Drop and add foreign key constraint in departament table
ALTER TABLE departament
    DROP CONSTRAINT IF EXISTS fk_dept;
ALTER TABLE departament
    ADD CONSTRAINT fk_dept FOREIGN KEY (Mgr_ssn) REFERENCES employee(Ssn)
    ON UPDATE CASCADE;

-- Create dept_locations table
CREATE TABLE dept_locations(
    Dnumber INT NOT NULL,
    Dlocation VARCHAR(15) NOT NULL,
    CONSTRAINT pk_dept_locations PRIMARY KEY (Dnumber, Dlocation),
    CONSTRAINT fk_dept_locations FOREIGN KEY (Dnumber) REFERENCES departament(Dnumber)
);

-- Drop and add foreign key constraint in dept_locations table
ALTER TABLE dept_locations DROP CONSTRAINT IF EXISTS fk_dept_locations;
ALTER TABLE dept_locations
    ADD CONSTRAINT fk_dept_locations FOREIGN KEY (Dnumber) REFERENCES departament(Dnumber)
    ON DELETE CASCADE
    ON UPDATE CASCADE;

-- Create project table
CREATE TABLE project(
    Pname VARCHAR(15) NOT NULL,
    Pnumber INT NOT NULL,
    Plocation VARCHAR(15),
    Dnum INT NOT NULL,
    PRIMARY KEY (Pnumber),
    CONSTRAINT unique_project UNIQUE (Pname),
    CONSTRAINT fk_project FOREIGN KEY (Dnum) REFERENCES departament(Dnumber)
);

-- Create works_on table
CREATE TABLE works_on(
    Essn CHAR(9) NOT NULL,
    Pno INT NOT NULL,
    Hours NUMERIC(3, 1) NOT NULL,
    PRIMARY KEY (Essn, Pno),
    CONSTRAINT fk_employee_works_on FOREIGN KEY (Essn) REFERENCES employee(Ssn),
    CONSTRAINT fk_project_works_on FOREIGN KEY (Pno) REFERENCES project(Pnumber)
);

-- Drop and create dependent table
DROP TABLE IF EXISTS dependent;
CREATE TABLE dependent(
    Essn CHAR(9) NOT NULL,
    Dependent_name VARCHAR(15) NOT NULL,
    Sex CHAR,
    Bdate DATE,
    Relationship VARCHAR(8),
    PRIMARY KEY (Essn, Dependent_name),
    CONSTRAINT fk_dependent FOREIGN KEY (Essn) REFERENCES employee(Ssn)
);
