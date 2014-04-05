

INSERT INTO manager_category VALUES (1, 'Cameras', 1);
INSERT INTO manager_category VALUES (2, 'Lenses', 2);
INSERT INTO manager_category VALUES (3, 'Batteries', 3);
INSERT INTO manager_category VALUES (4, 'Accessories', 4);
INSERT INTO manager_category VALUES (5, 'Other', 5);

INSERT INTO manager_condition VALUES (1, 'New');
INSERT INTO manager_condition VALUES (2, 'Used - Like New');
INSERT INTO manager_condition VALUES (3, 'Used - Good');
INSERT INTO manager_condition VALUES (4, 'Used - Poor');
INSERT INTO manager_condition VALUES (5, 'Used - As Is');

INSERT INTO manager_subcategory VALUES (1, 'Digital SLR', 1);
INSERT INTO manager_subcategory VALUES (2, 'Digital Compact', 1);
INSERT INTO manager_subcategory VALUES (3, 'Film', 1);

-- User:       webmaster
-- Password:   Password1
INSERT INTO account_user VALUES (99999, 'pbkdf2_sha256$12000$6452F1Q5YyYq$6dEZTD4EYWRlIsz0P3RDcBd72SJ0a538qFYrlk+r+Wo=', '2014-02-25 18:28:42.571127-07', true, 'webmaster', 'Website', 'Administrator', 'webmaster@digitallifemyway.com', true, true, '2014-02-05 20:09:48.693779-07', '801-555-5555', 'What is your mother''s maiden name?', 'Smith', '123 Center St', '', 'Provo', 'UT', 84606);
INSERT INTO account_employee VALUES (99999, 99999, '2013-08-18', 100000.00);

--Walk-in user for instore sales
-- User:       walkin
-- Password:   Password1
INSERT INTO account_user VALUES (99998, 'pbkdf2_sha256$12000$qUOT08R8yqNQ$k52VxNgEPb6uM2Pjd+6QRVGOghs43ishGmwYW70Zkag=', '2014-03-31 14:40:36.489433-06', false, 'Walkin', 'Walk', 'In', 'walkin@digitallifemyway.com', false, true, '2014-03-31 14:40:36.489433-06', '8015555555', 'w', 'w', 'Walkin', 'Customer', 'Walkin', 'CU', 0, NULL, NULL);

--Online employee for commissionless sales
INSERT INTO account_user VALUES (99997, 'pbkdf2_sha256$12000$KtdZGGXbhCmO$mTqlC1+rqiidlW9PUlXJw1H7KZCwLvKKa0axoUAbCzg=', '2014-03-31 12:37:52.256626-06', false, 'onlinesales', 'Online', 'Sales', 'os@digitallifemyway.com', false, true, '2014-03-31 12:37:52.256626-06', '8015555555', 'w', 'w', 'Online', 'Sales', 'ONLINE', 'SA', 0, NULL, NULL);
INSERT INTO account_employee VALUES (99998, 99997, '2010-10-10', 0.00);

--Online "Store" for records
INSERT INTO manager_store VALUES (99999, 'Online', 'Online', 'Sales', 'OS', 'OS', 0, '0000000000', true, 99999);
