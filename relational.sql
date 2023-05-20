DROP TABLE IF EXISTS austin_crime;

CREATE TABLE austin_crime (
    incident_number bigint,
    highest_offense_description text,
    highest_offense_code int,
    family_violence char,
    occurred_date_time text,
    occurred_date date,
    occurred_time int,
    report_date_time text,
    report_date date,
    report_time int,
    location_type text,
    address_var text,
    zip_code int,
    council_district int,
    apd_sector text,
    apd_district text,
    pra text,
    census_tract float,
    clearance_status char,
    clearance_date date,
    ucr_category text,
    category_description text,
    x_coordinate int,
    y_coordinate int,
    latitude float,
    longitude float, 
    location_var text
);

--Change the path to get it to work on your computer
--If you get an error saying "could not open file
--(your path) for reading: permission denied"
--Check this link https://stackoverflow.com/questions/14083311/permission-denied-when-trying-to-import-a-csv-file-from-pgadmin

COPY austin_crime
FROM 'C:/Users/joonh/Downloads/Data_SQL/rows.csv' WITH (FORMAT csv, HEADER true, DELIMITER ',');

SELECT * FROM austin_crime;
