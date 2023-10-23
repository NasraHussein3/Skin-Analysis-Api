CREATE DATABASE skincare;
USE skincare;
-- Error handling start
START TRANSACTION;
-- Create the Results Table 
CREATE TABLE Results (
    ResultsID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Skin_description TEXT,
    Skincare_routine TEXT,
    Recommended_products TEXT,
    Skin_info_ID INT NOT NULL
);
-- Create the table for user information
CREATE TABLE SkinInfo (
    SkinInfoID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    Skin_info VARCHAR(50),
    Age INT,
    Ethnicity VARCHAR(50),
    Gender VARCHAR(30),
    Environment VARCHAR(50),
    Medication VARCHAR(50),
    ResultsID INT NOT NULL,
    FOREIGN KEY (ResultsID) REFERENCES Results(ResultsID)
);

-- Create the Users Table with Foreign Key Constraints
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(50),
    UserName VARCHAR(50),
    ResultsID INT,
    SkinInfoID INT,
    FOREIGN KEY (ResultsID) REFERENCES Results(ResultsID),
    FOREIGN KEY (SkinInfoID) REFERENCES SkinInfo(SkinInfoID)
);

-- Insert information for results
INSERT INTO Results (ResultsID, Skin_description, Skincare_routine, Recommended_products, Skin_info_id)
VALUES (123, 'Ageing skin experiences signs of ageing such as fine lines, wrinkles, and loss of elasticity. Skincare for ageing skin often focuses on anti-ageing ingredients and hydration to minimise the visible effects of ageing','cleanser, moisturiser with spf, weekly mask, eyecream, hydration', 'Glucoside foaming cleanser, Squalane cleanser, Glycolic acid 7% toning solution, Pynogenol 5%, EUK 134 0.1%, Natural moisturising factors + HA, Mineral UV factors SPF 30 with antioxidants', 123),
(456,'Combination skin has a mix of characteristics, often with an oily T-zone (forehead, nose, and chin) and drier or normal skin on the cheeks. It requires a tailored skincare approach','cleanser, toner, moisturiser, sunscreen, treatment, eyecream, masks','Glycopid cream, Squalane cleanser, Glycolic acid 7% toning solution, Hyaluronic acid 2% + B5, Plant-derived squalane, Natural moisturising factors + HA, Mineral UV factors SPF 30 with antioxidants', 456), 
(789,'Dry skin lacks moisture and can feel tight, rough, or flaky. It may be sensitive and prone to irritation. Dry skin requires hydration to maintain its moisture balance','cleanser, moisturiser, sunscreen (morning), hydration Boost (optional), lip balm, exfoliation (1-2 times a week), treatment (optional)','Glycopid cream, Squalane cleanser, Glycolic acid 7% toning solution, Hyaluronic acid 2% + B5, Natural moisturising factors + HA, Mineral UV factors SPF 30 with antioxidants', 789),
(321,'Normal skin is well-balanced and not too oily or too dry. It has small pores, a smooth texture, and is generally free from sensitivity or excessive dryness','cleanser, moisturiser, weekly exfoliation, hydration','Glycopid cream, Squalane cleanser, Glycolic acid 7% toning solution, Multi-peptide + HA Serum, Granactive Retinoid 2% Emulsion, Natural moisturising factors + HA, Mineral UV factors SPF 30 with antioxidants', 321),
(654,'Oily skin is characterised by excess sebum production, which can lead to a shiny or greasy appearance. It is prone to enlarged pores and is more susceptible to acne and blackheads','cleanser, moisturiser, sunscreen, optional creams, exfoliation, nightcream', 'Glucoside foaming cleanser, Squalane cleanser,Glycolic acid 7% toning solution, Niacinamide 10% + zinc 1%, Natural moisturising factors + HA, Salicylic acid 2% Masque, Mineral UV factors SPF 30 with antioxidants', 654),
(987,'Acne-prone skin is susceptible to frequent breakouts, including blackheads, whiteheads, and spots. It may require specialised products to manage acne','cleanser, moisturiser, sunscreen, spot treatment, ocassinally exfoliation, healthy lifestyle','Glucoside foaming cleanser, Squalane cleanser, Glycolic acid 7% toning solution, Salicylic Acid 2% Solution, Natural moisturising factors + Beta Glucan, Mineral UV factors SPF 30 with antioxidants', 987);

-- Insert information into the SkinInfo
INSERT INTO SkinInfo (SkinInfoID, Skin_info, Age, Ethnicity, Gender, Environment, Medication, ResultsID)
VALUES (123, 'Ageing','28','White British','Female','Rural','Norethisterone', 123),
(456, 'Combination','32','Mixed Ethnic Group','Female','Rural','Antihistamine', 456),
(789, 'Dry skin','30','Asian British','Female','Urban','Naproxen', 789),
(321, 'Normal skin','21','Other','Female','Suburban','None', 321),
(654, 'Oily skin','24','Black British','Female','Rural','Roaccutane', 654),
(987, 'Acne prone','29','White Other','Female','Urban','Levest', 987);

-- Populate Users table with data
INSERT INTO Users (UserID, FirstName, LastName, Email, Username, ResultsID, SkinInfoID)
VALUES 
('0009','Lauren','Southall','lauren.southall@example.com','laso09', 123, 123),
('0005','Jessica','Palmer','jessica.palmer@example.com','jessp05', 456, 456),
('0001','Mimi','Brown','mimi.brown@example.com','mimib01', 789, 789),
('0002','Nasra','Hussein','nasra.hussein@example.com','nas02', 321, 321),
('0003','Minka','Ansa','minka.ansa@example.com','mink03', 654, 654),
('0004','Remi','Xue','remi.xue@example.com','xue04', 987, 987);

-- Select data from tables
SELECT * FROM Results;
SELECT * FROM Users;
SELECT * FROM SkinInfo;

-- Join tables to retrieve desired information
SELECT Users.UserID, Users.UserName, SkinInfo.Skin_info, SkinInfo.Age, SkinInfo.Ethnicity, SkinInfo.Gender, SkinInfo.Environment, SkinInfo.Medication
FROM Users
INNER JOIN SkinInfo
ON Users.SkinInfoID = SkinInfo.SkinInfoID
INNER JOIN Results
ON Users.ResultsID = Results.ResultsID;

SELECT SkinInfo.SkinInfoID, SkinInfo.Skin_info, Results.ResultsID, Results.Skin_description, Results.Skincare_routine, Results.Recommended_products
FROM SkinInfo
INNER JOIN Results
ON SkinInfo.SkinInfoID = Results.Skin_info_ID;


-- ADDITIONS TO CONSIDER::

-- queries for each API endpoint:
-- get all skincare data from Results table
SELECT *
FROM Results;
-- Get skincare routine by skin type
SELECT Results.Skincare_routine
FROM Results
INNER JOIN SkinInfo ON Results.Skin_info_ID = SkinInfo.SkinInfoID
WHERE SkinInfo.Skin_info = 'user_selected_skin_type';
-- List all available skin types
SELECT DISTINCT Skin_info FROM SkinInfo;
-- Delete all skincare data
DELETE FROM Results;
DELETE FROM SkinInfo;

-- Allow users to update information and preferences:
-- Update skin information:
UPDATE SkinInfo
SET
   Age = 'new_age',
   Ethnicity = 'new_ethnicity',
   Gender = 'new_gender',
   Environment = 'new_environment',
   Medication = 'new_medication'
WHERE
   Skin_info = 'user_selected_skin_type';
-- Update skincare preferences:
UPDATE Results
SET
   Skin_description = 'new_skin_description',
   Skincare_routine = 'new_skincare_routine',
   Recommended_products = 'new_recommended_products'
WHERE
   ResultsID = (SELECT ResultsID FROM SkinInfo WHERE Skin_info = 'user_selected_skin_type');
-- Error handling end
COMMIT;