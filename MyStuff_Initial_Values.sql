

-- Categories
INSERT INTO manager_category VALUES (99991, 'Cameras', 1);
INSERT INTO manager_category VALUES (99992, 'Lenses', 2);
INSERT INTO manager_category VALUES (99993, 'Studio & Lighting', 3);
INSERT INTO manager_category VALUES (99994, 'Tripods', 4);
INSERT INTO manager_category VALUES (99995, 'Bags & Cases', 5);

-- Sub Categories
INSERT INTO manager_subcategory VALUES (1, 'Digital SLR', 99991);
INSERT INTO manager_subcategory VALUES (2, 'Digital Compact', 99991);
INSERT INTO manager_subcategory VALUES (3, 'Film', 99991);
INSERT INTO manager_subcategory VALUES (4, 'Batteries', 99991);
INSERT INTO manager_subcategory VALUES (5, 'Accessories', 99991);
INSERT INTO manager_subcategory VALUES (6, 'Standard', 99992);
INSERT INTO manager_subcategory VALUES (7, 'Wide Angle', 99992);
INSERT INTO manager_subcategory VALUES (8, 'Portrait', 99992);
INSERT INTO manager_subcategory VALUES (9, 'Telephoto', 99992);
INSERT INTO manager_subcategory VALUES (10, 'Macro', 99992);
INSERT INTO manager_subcategory VALUES (11, 'Fisheye', 99992);
INSERT INTO manager_subcategory VALUES (12, 'Dedicated Flash', 99993);
INSERT INTO manager_subcategory VALUES (13, 'Macro Ring Light Flash', 99993);
INSERT INTO manager_subcategory VALUES (14, 'Hammerhead Flash', 99993);
INSERT INTO manager_subcategory VALUES (15, 'Light Reflectors', 99993);
INSERT INTO manager_subcategory VALUES (16, 'Softboxes', 99993);
INSERT INTO manager_subcategory VALUES (17, 'Umbrellas', 99993);
INSERT INTO manager_subcategory VALUES (18, 'Diffusers', 99993);
INSERT INTO manager_subcategory VALUES (19, 'Lamps & Bulbs', 99993);
INSERT INTO manager_subcategory VALUES (20, 'Travel & Compact', 99994);
INSERT INTO manager_subcategory VALUES (21, 'Photo ', 99994);
INSERT INTO manager_subcategory VALUES (22, 'Monopods', 99994);
INSERT INTO manager_subcategory VALUES (23, 'Light Stands', 99994);
INSERT INTO manager_subcategory VALUES (24, 'Backpacks', 99995);
INSERT INTO manager_subcategory VALUES (25, 'Shoulder Bags', 99995);
INSERT INTO manager_subcategory VALUES (26, 'Sling Bags', 99995);
INSERT INTO manager_subcategory VALUES (27, 'Belt Packs', 99995);
INSERT INTO manager_subcategory VALUES (28, 'Hard Cases', 99995);
INSERT INTO manager_subcategory VALUES (29, 'Soft Cases', 99995);
INSERT INTO manager_subcategory VALUES (30, 'Camera & Lense', 99995);
INSERT INTO manager_subcategory VALUES (31, 'Tripod', 99995);
INSERT INTO manager_subcategory VALUES (32, 'Lighting', 99995);

-- Conditions
INSERT INTO manager_condition VALUES (1, 'New');
INSERT INTO manager_condition VALUES (2, 'Used - Like New');
INSERT INTO manager_condition VALUES (3, 'Used - Good');
INSERT INTO manager_condition VALUES (4, 'Used - Poor');
INSERT INTO manager_condition VALUES (5, 'Used - As Is');


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
