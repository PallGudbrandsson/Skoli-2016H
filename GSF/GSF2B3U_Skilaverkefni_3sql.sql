delimiter $$

DROP PROCEDURE IF EXISTS booking $$
CREATE PROCEDURE booking(cardProvider varchar(35), cardOwner varchar(55), 
	payType bit(1), class int(11), returnFl tinyint(1), pID varchar(35), 
	pName varchar(75), dPriceID int(11), dSeatID int(11), rPriceID int(11), 
	rSeatID int(11), dFnum char(5), dFDate DATE, rFNum int(11), rFDate DATE)
BEGIN
	
	DECLARE dFCode int(11);
	DECLARE rFCode int(11);

	SELECT flightCode INTO dFCode FROM flights WHERE flightDate = dFDate AND flightNumber = dFnum
	SELECT flightCode INTO rFCode FROM flights WHERE flightDate = rFDate AND flightNumber = rFnum

	INSERT INTO bookings (timeOfBooking, paymentType, cardIssuedBy, cardholdersName, classID, returnFlight) VALUES(NOW(), payType, cardProvider, cardOwner, class, returnFl);
	INSERT INTO bookedflights (bookingNumber, flightCode, flightOrder) VALUES(LAST_INSERT_ID(), dFcode, 1);
	INSERT INTO passengers (pID, pName, seatID, bookedFlightID)VALUES(pID, pName, dPriceID, dSeatID, LAST_INSERT_ID());

	INSERT INTO bookings (timeOfBooking, paymentType, cardIssuedBy, cardholdersName, classID, returnFlight) VALUES(NOW(), payType, cardProvider, cardOwner, class, returnFl);
	INSERT INTO bookedflights (bookingNumber, flightCode, flightOrder) VALUES(LAST_INSERT_ID(), rFcode, 1);
	INSERT INTO passengers (pID, pName, seatID, bookedFlightID)VALUES(pID, pName, dPriceID, dSeatID, LAST_INSERT_ID());
END