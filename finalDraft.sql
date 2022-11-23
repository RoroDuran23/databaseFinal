CREATE TABLE Parks (
    parkID INT PRIMARY KEY,
    locationID INT,
    parkName VARCHAR(100),
    parksize INT, --in acres
    parkCapacity INT,
    numSectors INT,
    isOpen BIT,

    FOREIGN KEY (locationID) REFERENCES Sections(sectionID)
);

CREATE TABLE Sections (
    sectionID INT,
    parkID INT,
    sectionName VARCHAR(100),
    sectionColorTheme VARCHAR(100),
    numAttractions INT,

    PRIMARY KEY (sectionID, parkID),
    FOREIGN KEY (parkID) REFERENCES Parks(parkID)
);

--if needed
--DROP TABLE Sections;

CREATE TABLE Location (
    locationID INT PRIMARY KEY,
    locationName VARCHAR(100),
    locationState VARCHAR(100),
    locationCity VARCHAR(100)
);

CREATE TABLE Restaurants (
    restID INT,
    sectionID INT,
    parkID INT,
    restName VARCHAR(100),
    restDescription VARCHAR(300),
    restTypeFood VARCHAR(100),
    isOpen BIT,
    maxCapacity INT,
    isFull BIT,
    waitTime TIME,

    PRIMARY KEY (restID, sectionID, parkID),
    FOREIGN KEY (parkID) REFERENCES Parks(parkID),
    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

--if needed
--DROP TABLE Restaurants;

CREATE TABLE Rides (
    rideID INT,
    sectionID INT,
    parkID INT,
    rideName VARCHAR(100),
    rideType VARCHAR(100),
    rideDescription VARCHAR(300),
    rideMinHeight DEC,
    rideAvgAge INT,
    rideOpeningYear INT,
    waitTime DEC,

    PRIMARY KEY (rideID, sectionID, parkID),
    FOREIGN KEY (parkID) REFERENCES Parks(parkID),
    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

--if needed
DROP TABLE Rides;

CREATE TABLE Utilities (
    utilityID INT,
    sectionID INT,
    parkID INT,
    utilityName VARCHAR(100),
    description VARCHAR(300),
    isAvailable BIT,

    PRIMARY KEY (utilityID, sectionID, parkID),
    FOREIGN KEY (parkID) REFERENCES Parks(parkID),
    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

--if needed
--DROP TABLE Utilities;

CREATE TABLE Shops (
    shopID INT,
    sectionID INT,
    parkID INT,
    shopType VARCHAR(100),
    shopName VARCHAR(100),
    maxPrice DEC,
    minPrice DEC,
    avgPrice DEC,
    numItems INT,
    isOpen BIT,

    PRIMARY KEY (shopID, sectionID, parkID),
    FOREIGN KEY (parkID) REFERENCES Parks(parkID),
    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

--if needed
--DROP TABLE Shops;



-- Making these views

-- Rides by Year view
CREATE VIEW [Rides by Year] AS
SELECT rideName, rideType, rideOpeningYear
FROM Rides
ORDER BY rideOpeningYear;

-- Rides by section
CREATE VIEW [Rides by Section] AS
SELECT rideName, rideType, sectionName, parkName
FROM Parks LEFT JOIN Sections S on Parks.parkID = S.parkID LEFT JOIN Rides R on S.sectionID = R.sectionID
GROUP BY parkName;


-- Sort open shops by price
SELECT shopName, avgPrice, minPrice, maxPrice
FROM Shops
WHERE isOpen = 1
ORDER BY avgPrice ASC;


-- Add records
-- PARKS --

    --Disneyland
INSERT INTO Parks(parkID, locationID, parkName, parksize, parkCapacity, numSectors, isOpen)
VALUES (1, 1, 'Disneyland', 100, 85000, 9, 1);

    --Disney World
INSERT INTO Parks(parkID, locationID, parkName, parksize, parkCapacity, numSectors, isOpen)
VALUES (2, 2, 'Disney World', 500, 320000, 6, 1);

-- SECTIONS --

    --Disneyland
INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (1, 1, 'Main Street, U.S.A.', 'Bright Lights', 1);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (2, 1, 'Adventureland', 'Jungle colors', 4);

-- Shops --

    --Disneyland
INSERT INTO Shops(shopID, sectionID, parkID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES(1, 2, 1, "Tropical", "Adventureland Bazaar", 250, 3, 50, 100, 1);

INSERT INTO Shops(shopID, sectionID, parkID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES(2, 2, 1, "BBQ", "South Seas Trader", 13, 4, 7, 15, 1);



-- RESTAURANTS --
    --Disneyland
INSERT INTO Restaurants(restID, sectionID, parkID, restName, restDescription, restTypeFood, isOpen, maxCapacity, isFull, waitTime)
VALUES(1, 2,1,"Bengal Barbecue", "Located across from the Jungle Cruise and Indiana Jones Adventure, this quick serve location features chicken and beef skewers topped with Polynisian-inspired sauces.", "BBQ", 1, 75, 0, 25);




SELECT * FROM Parks;
SELECT * FROM Sections;
SELECT * FROM Rides;
SELECT * FROM Location;
SELECT * FROM Restaurants;
SELECT * FROM Utilities;
SELECT * FROM Shops;
