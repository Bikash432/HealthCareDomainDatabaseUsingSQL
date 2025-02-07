use Medicare_System


CREATE TABLE MedicalPractice (
    Group_PAC_ID NVARCHAR(10) NOT NULL PRIMARY KEY,
    AddressID NVARCHAR(70) NOT NULL UNIQUE,
    Telehealth NVARCHAR(100) NOT NULL,
    Number_of_Group_Member NVARCHAR(100),
    FOREIGN KEY (Group_PAC_ID) REFERENCES PROFESSIONAL_IDENTIFICATION(PAC_ID)
);


use Medicare_System
-- Create Table Address
CREATE TABLE Address (
    AddressID Nvarchar(70) PRIMARY KEY,
    StreetAddress NVARCHAR(100),
    City NVARCHAR(50),
    State NVARCHAR(50),
    ZIPCode INT,
    PhoneNumber CHAR(10),
    FOREIGN KEY (AddressID) REFERENCES MedicalPractice(AddressID)
);
