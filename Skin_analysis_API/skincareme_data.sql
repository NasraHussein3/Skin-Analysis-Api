CREATE DATABASE skincareme;
USE skincareme;

CREATE TABLE dailyroutine (
    SkinType VARCHAR(255) PRIMARY KEY,
    Cleansing VARCHAR(255),
    Toner VARCHAR(255),
    Serum VARCHAR(255),
    Moisturising VARCHAR(255),
    Protect VARCHAR(255)
);

INSERT INTO dailyroutine (SkinType, Cleansing, Toner, Serum, Moisturising, Protect)
VALUES
    ('Oily skin', 
    'Water based cleanser: Glucoside foaming cleanser or Oil based cleanser: Squalane cleanser', 
    'Glycolic acid 7% toning solution', 
    'Niacinamide 10% + zinc 1%', 
    'Natural moisturising factors + HA or Salicylic acid 2% Masque', 
    'Mineral UV factors SPF 30 with antioxidants'),
    
    ('Dry skin', 
    'Water based cleanser: Glycopid cream or Oil based cleanser: Squalane cleanser', 
    'Glycolic acid 7% toning solution', 
    'Hyaluronic acid 2% + B5 or Salicylic acid 2% solution', 
    'Natural moisturising factors + HA', 
    'Mineral UV factors SPF 30 with antioxidants'),
    
    ('Combination skin', 
    'Water based cleanser: Glycopid cream or Oil based cleanser: Squalane cleanser', 
    'Glycolic acid 7% toning solution', 
    'Hyaluronic acid 2% + B5 or 100% Plant-derived squalane', 
    'Natural moisturising factors + HA', 
    'Mineral UV factors SPF 30 with antioxidants'),
    
    ('Normal skin', 
    'Water based cleanser: Glycopid cream or Oil based cleanser: Squalane cleanser', 
    'Glycolic acid 7% toning solution', 
    'Multi-peptide + HA Serum or Granactive Retinoid 2% Emulsion', 
    'Natural moisturising factors + HA', 
    'Mineral UV factors SPF 30 with antioxidants'),
    
    ('Ageing', 
    'Water based cleanser: Glucoside foaming cleanser or Oil based cleanser: Squalane cleanser', 
    'Glycolic acid 7% toning solution', 
    'Pynogenol 5% or EUK 134 0.1%', 
    'Natural moisturising factors + HA', 
    'Mineral UV factors SPF 30 with antioxidants'),
    
    ('Acne prone', 
    'Water based cleanser: Glucoside foaming cleanser or Oil based cleanser: Squalane cleanser', 
    'Glycolic acid 7% toning solution', 
    'Salicylic Acid 2% Solution', 
    'Natural moisturising factors + Beta Glucan', 
    'Mineral UV factors SPF 30 with antioxidants');

CREATE TABLE members (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(50),
    SkinType VARCHAR(50),
    Age INT
);

INSERT INTO members (ID, FirstName, LastName, Email, SkinType, Age)
VALUES
    (1, 'John', 'Doe', 'johndoe@email.com', 'Oily skin', 28),
    (2, 'Alice', 'Smith', 'alicesmith@email.com', 'Combination skin', 35),
    (3, 'Michael', 'Johnson', 'michaeljohnson@email.com', 'Dry skin', 42);



