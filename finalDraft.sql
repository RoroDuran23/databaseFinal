CREATE TABLE Parks (
    parkID INT PRIMARY KEY,
    locationID INT,
    parkName VARCHAR(100),
    parksize INT,
    parkCapacity INT,
    numSectors INT,
    isOpen BIT,

    FOREIGN KEY (locationID) REFERENCES Sections(sectionID)
);

CREATE TABLE Sections (
    sectionID INT PRIMARY KEY,
    parkID INT,
    sectionName VARCHAR(100),
    sectionColorTheme VARCHAR(100),
    numAttractions INT,

    FOREIGN KEY (parkID) REFERENCES Parks(parkID)
);

CREATE TABLE Location (
    locationID INT PRIMARY KEY,
    locationName VARCHAR(100),
    locationState VARCHAR(100),
    locationCity VARCHAR(100)
);

CREATE TABLE Restaurants (
    restID INT PRIMARY KEY,
    sectionID INT,
    restName VARCHAR(100),
    restDescription VARCHAR(300),
    restTypeFood VARCHAR(100),
    isOpen BIT,
    maxCapacity INT,
    isFull BIT,
    waitTime TIME,

    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

CREATE TABLE Rides (
    rideID INT PRIMARY KEY,
    sectionID INT,
    rideName VARCHAR(100),
    rideType VARCHAR(100),
    rideDescription VARCHAR(300),
    rideMinHeight DEC,
    rideAvgAge INT,
    rideOpeningYear INT,
    waitTime DEC,

    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

CREATE TABLE Utilities (
    utilityName VARCHAR(100) PRIMARY KEY,
    sectionID INT,
    description VARCHAR(300),
    isAvailable BIT,

    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

CREATE TABLE Shops (
    shopID INT PRIMARY KEY,
    sectionID INT,
    shopType VARCHAR(100),
    shopName VARCHAR(100),
    maxPrice DEC,
    minPrice DEC,
    avgPrice DEC,
    numItems INT,
    isOpen BIT,

    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

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

