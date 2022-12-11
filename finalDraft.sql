PRAGMA FOREIGN_KEYS = 1;
CREATE TABLE Parks (
    parkID INT PRIMARY KEY,
    locationID INT,
    parkName VARCHAR(100),
    parksize INT,
    parkCapacity INT,
    numSectors INT,
    isOpen BIT,

    FOREIGN KEY (locationID) REFERENCES Location(locationID)
);

CREATE TABLE Sections (
    sectionID INT,
    parkID INT,
    sectionName VARCHAR(100),
    sectionColorTheme VARCHAR(100),
    numAttractions INT,

    PRIMARY KEY (sectionID),
    FOREIGN KEY (parkID) REFERENCES Parks(parkID)
);

-- if needed
-- DROP TABLE Sections;

CREATE TABLE Location (
    locationID INT PRIMARY KEY,
    locationName VARCHAR(100),
    locationState VARCHAR(100),
    locationCity VARCHAR(100)
);

CREATE TABLE Restaurants (
    restID INT,
    sectionID INT,
    restName VARCHAR(100),
    restDescription VARCHAR(300),
    restTypeFood VARCHAR(100),
    restTypeService VARCHAR(100),
    isOpen BIT,
    maxCapacity INT,
    isFull BIT,
    waitTime TIME,

    PRIMARY KEY (restID),
    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

-- if needed
DROP TABLE Restaurants;

CREATE TABLE Rides (
    rideID INT,
    sectionID INT,
    rideName VARCHAR(100),
    rideType VARCHAR(100),
    rideDescription VARCHAR(300),
    rideMinHeight DEC,
    rideAvgAge INT,
    rideOpeningYear INT,
    waitTime DEC,

    PRIMARY KEY (rideID),
    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

--if needed
DROP TABLE Rides;

CREATE TABLE Utilities (
    utilityID INT,
    sectionID INT,
    utilityName VARCHAR(100),
    description VARCHAR(300),
    isAvailable BIT,

    PRIMARY KEY (utilityID),
    FOREIGN KEY (sectionID) REFERENCES Sections(sectionID)
);

--if needed
DROP TABLE Utilities;

CREATE TABLE Shops (
    shopID INT,
    sectionID INT,
    shopType VARCHAR(100),
    shopName VARCHAR(100),
    maxPrice DEC,
    minPrice DEC,
    avgPrice DEC,
    numItems INT,
    isOpen BIT,

    PRIMARY KEY (shopID),
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


-- Add records
-- PARKS --

-- Disneyland
INSERT INTO Parks(parkID, locationID, parkName, parksize, parkCapacity, numSectors, isOpen)
VALUES (1, 1, 'Disneyland', 100, 85000, 9, 1);

-- Disney World--
INSERT INTO Parks(parkID, locationID, parkName, parksize, parkCapacity, numSectors, isOpen)
VALUES (2, 2, 'Disney World', 500, 320000, 6, 1);

-- SECTIONS --
-- Disneyland --

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (1, 1, 'Main Street, U.S.A.', 'Bright Lights', 1);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (2, 1, 'Adventureland', 'Jungle colors', 4);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (3, 1, 'New Orleans Square', 'Brick', 2);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (4, 1, 'Frontierland', 'Old West', 2);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (5, 1, 'Fantasyland', 'Multicolor', 12);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (6, 1, 'Tomorrowland', 'Futuristic-white', 6);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (7, 1, 'Critter Country', 'Green Forest', 1);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (8, 1, 'Star Wars: Galaxys Edge', 'Grey', 4);

INSERT INTO Sections(sectionID, parkID, sectionName, sectionColorTheme, numAttractions)
VALUES (9, 1, ' Mickeys Toontown', 'Multicolor', 1);

-- Shops --

    --Disneyland
INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES(1, 2, "Tropical", "Adventureland Bazaar", 250, 3, 50, 100, 1);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES(2, 2, "BBQ", "South Seas Trader", 13, 4, 7, 15, 1);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (3, 1, "Music", "20th Century Music Company", 150, 23, 50, 80,1);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (4, 3, "Home decorations", "Cristal d''Orleans", 100, 19, 60, 50, 0);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (5, 4, "Western souvenirs", "Pioneer Mercantile", 150, 5, 40, 250, 1);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (6, 5, "Princesses", "Fairy Tale Treasures", 130, 23, 40, 100, 1);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (7, 6, "Mainly hats", "Autopia Winner’s Circle", 45, 15, 30, 30, 0);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (8, 7, "Hats", "Briar Patch", 40, 20, 25, 30, 1);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (9, 8, "Droids", "Droid Depot", 350, 50, 120, 20, 1);

INSERT INTO Shops(shopID, sectionID, shopType, shopName, maxPrice, minPrice, avgPrice, numItems, isOpen)
VALUES (10, 9, "Themed shop", "Gag Factory/Toontown Five & Dime", 180, 10, 40, 100, 1);

-- RESTAURANTS --
    --Disneyland
INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(1, 1,"Jolly Holiday Bakery Cafe", "In the morning, stop by Jolly Holiday Bakery Cafe on your way into Disneyland for fresh pastries, specialty coffees and a great view.", "Counter Service", "Cafe", 1, 190, 1, 45);

INSERT INTO Restaurants(restID, sectionID,  restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(2, 1,"Gibson Girl Ice Cream Parlor", "Get a delicious ice cream cone, sundae, or float and relax in the old-fashioned ice cream parlor..", "Counter Service", "Ice cream", 1, 40, 0, 10);

INSERT INTO Restaurants(restID, sectionID,  restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(3, 2,"Bengal Barbecue", "Located across from the Jungle Cruise and Indiana Jones Adventure, this quick serve location features chicken and beef skewers topped with Polynisian-inspired sauces.", "Counter Service", "BBQ", 1, 75, 1, 25);

INSERT INTO Restaurants(restID, sectionID,  restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(4, 2,"Tiki Juice Bar", "You can get refreshing Dole pineapple juice or Dole Whip (soft serve ice cream) here. This is located at the entrance to the Tiki Room. During busier times, the Tiki Juice Bar becomes Mobile Order only. Dole Whips can also be found at Tropical Hideaway.", "Counter Service", "Juice Bar", 1, 20, 0, 0);

INSERT INTO Restaurants(restID, sectionID,  restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(5, 2,"South Sea Traders", "Located near the Bengal Barbecue, this fruit stand offers in-season fresh fruit, soft drinks and bottles of water.", "Quick Snacks", "Snacks", 1, 20, 1, 15);

INSERT INTO Restaurants(restID, sectionID,  restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(6, 2,"The Tropical Hideaway", "Formerly Aladdin''s Oasis. Visit with Jungle Cruise skippers as you sit on an open-air dock and enjoy tropical music. At night, torches light the area.", "N/A", "Fruits", 1, 40, 1, 10);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(7, 3,"Blue Bayou Restaurant", "For a special treat, have lunch or dinner at the Blue Bayou Restaurant. This restaurant is located inside the Pirates of the Caribbean attraction, and features appetizers, salads, seafood, chicken & beef dishes as well as its famous Monte Cristo sandwich, all with a New Orleans flair. This restaurant is a little pricey, but has a great atmosphere. Limited same day reservations are taken at the entrance to the restaurant, however advance reservations are recommended.", "Full Service","Full Menu", 1, 40, 1, 40);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(8, 3,"French Market Restaurant", "French Market has covered patio and features southern-themed dishes, including jambalaya, roasted chicken, salmon, and delicious desserts. On weekend afternoons, a jazz band sometimes entertains the guests while they eat.", "Cafeteria","Cafe", 1, 35, 0, 5);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(9, 4,"Hungry Bear Restaurant", "This large restaurant offers American type fare for lunch or dinner, such as chicken sandwiches, cheeseburgers, and fries. You can sit above, or downstairs near the river and watch the boats and canoes go by. Kids meals are also available.", "Counter Service","American", 1, 50, 0, 0);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(10, 4,"Harbour Galley", "This restaurant on the banks of the Rivers of America offers chowder and soups served in bread bowls, plus entree sized salads, baked potatoes and drinks.", "Counter service", "Healthy", 1, 20, 0, 20);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(11, 5,"Rancho del Zocalo Restaurante’", "Dine on classic Mexican specialties for lunch or dinner as you bask in the romance and heritage of early California. Menu items include burritos, nachos and much more. You can sit outside on the Mexican themed patio, which is partially covered.", "Cafeteria", "Mexican", 1, 200, 0, 50);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(12, 5,"River Belle Terrace", "Eat lunch or dinner indoors or out on the terrace overlooking the Rivers of America. Options include BBQ ribs, oven-roasted BBQ chicken or a tasty brisket sandwich. Breakfast is available each morning.", "Full service", "BBQ", 0, 70, 0, 0);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(13, 6,"Red Rose Taverne", "This little restaurant is Beauty and the Beast themed, and serves French-inspired flatbreads, burgers, and sandwiches. It is located on the backside of Fantasyland near the Dumbo attraction. Breakfast, Lunch and Dinner.", "Counter Service", "French", 1, 100, 1, 35);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(14, 7,"Docking Bay 7 Food and Cargo", "Docking Bay 7 Food and Cargo is where Chef Strono “Cookie” Tuggs is serving up his grub for weary travelers. Look for exotic and unusual dishing like smoked Kaadu ribs, Fried Endorian Tip-yip and Batuubon for dessert.", "N/A", "Exotic", 1, 40, 1, 80);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(15, 8,"Pluto''s Dog House", "Hot dogs and cold beverages. Children''s meals. Outdoor seating is available.", "Fast Fod", "Lunch, Dinner, Snack", 1, 20, 0, 20);

INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, restTypeService, isOpen, maxCapacity, isFull, waitTime)
VALUES(16, 9,"Alien Pizza Planet", "This Toy Story-themed restaurant offers pizza, Caesar salad, and pasta. You can eat inside, or “outside” in a covered area.", "Pizza", "Cafeteria", 1, 100, 1, 20);


-- RIDES --

--Disneyland
INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (1, 1, "Disneyland Railroad", "Train", "Hop on board an authentic steam train and ride around the park. There are stops in New Orleans Square, Mickey''s Toontown and Tomorrowland, as well as Main Street. ", -1, 5, 1955, 30);

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES(2, 2, "Indiana Jones Adventure - Temple of the Forbidden Eye", "Car", "Following in Indiana Jones'' footsteps, you make your way through the jungles of Adventureland in search of the legendary Temple of the Forbidden Eye. Here you''ll find the curse of 'Mara', gaze upon her eye and a terrible fate awaits you.", 1.2, 15, 1995, 60);

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (3, 7, "Splash Mountain", "Car; water", "A one mile water log flume ride that takes you on a journey through the backwoods, swamps, and bayous of the old South as you prepare for the final dramatic 52 1/2 feet (more than 5 stories), 47 degree angle & 40+ mph flume drop. ", 1.3, 16, 1989, 15);

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (4, 5, "Peter Pan''s Flight", "indoor; car", "With a sprinkling of pixie dust, your pirate ship takes flight high above the streets of London and into Never Never Land.", -1, 5, 1955, 20);

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (5, 4, "Sailing Ship Columbia", "boat", "Experience a full-circle cruise tour of the Rivers of America around Tom Sawyer Island aboard the first 3-masted windjammer to be built in the United States in over 100 years.", -1, 35, 1958, 0);

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (6, 3, "Pirates of the Caribbean", "indoor; boat", "Guests board their pirate boat and travel through an audio-Animatronic pirate adventure. Watch as the pirates take over a Spanish fort and pillage and plunder the town.", -1, 20, 1967, 45 );

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (7, 8, "Millennium Falcon: Smugglers Run", "spaceship", "Guests can pilot one of the most famous starships in the galaxy in this interactive attraction that has guests creating their own adventures. Settle into the cockpit of the fastest hunk of junk in the galaxy and discover what surprises the bucket of bolts has to offer.", 38, 25, -1, 90);

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (8, 9, "Goofy''s Playhouse", "Playground", "Kids enter Goofy''s yard and play, climb and slide to their heart''s content", -1, 10, 2008, 10);

INSERT INTO Rides(rideID, sectionID, rideName, rideType, rideDescription, rideMinHeight, rideAvgAge, rideOpeningYear, waitTime)
    VALUES (9, 6, "Buzz Lightyear Astro Blasters", "Interactive game", "Board your Space Cruiser and blast your way through several scenes. Aim your weapon and shoot a beam of light at the alien targets while scoring points. The joystick lets you rotate your cruiser as you compete for the highest score", -1, 18, 2005, 45);




--DROP TABLE Parks;
--DROP TABLE Sections;
--DROP TABLE Rides;
--DROP TABLE Location;
--DROP TABLE Restaurants;
--DROP TABLE Utilities;
--DROP TABLE Shops;


-- Requirements

--1. Print/display records from your databse/table
SELECT * FROM Parks;
SELECT * FROM Sections;
SELECT * FROM Rides;
SELECT * FROM Location;
SELECT * FROM Restaurants;
SELECT * FROM Utilities;
SELECT * FROM Shops;

--2. Query for data/results with various parameters/filters
SELECT sectionName,p.parkName
FROM Sections
INNER JOIN Parks P on P.parkID = Sections.parkID
WHERE sectionID = 1 AND p.parkID = 1;

--3. Create a new record
INSERT INTO Restaurants(restID, sectionID, restName, restDescription, restTypeFood, isOpen, maxCapacity, isFull, waitTime)
VALUES(2, 2,"Tiki Juice Bar", "You can get refreshing Dole pineapple juice or Dole Whip (soft serve ice cream) here. This is located at the entrance to the Tiki Room. During busier times, the Tiki Juice Bar becomes Mobile Order only. Dole Whips can also be found at Tropical Hideaway.", "BBQ", 1, 20, 0, 10);

--4. Delete records (soft delete function would be ideal)
DELETE
FROM Shops
WHERE shopID = 1;

--5. Update Records
UPDATE Restaurants
SET waitTime = 85
WHERE Restaurants.restID = 14;

--6. Make use of transactions (commit and rollback)

--7. One query must perform an aggregation/group-by clause

--8. One query must contain a sub-query

--9. Two queries must involve joins across at least 3 tables

--10. Enforce referential integrality (PK/FK Constraints)

--11. Include Database Views, Indexes

--12. Use at least 5 entities
