

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

-- Shipping options
INSERT INTO catalog_shipping VALUES (10, 'Standard (4-7 business days)', 10.00);
INSERT INTO catalog_shipping VALUES (11, 'Express (2-3 business days)', 20.00);
INSERT INTO catalog_shipping VALUES (12, 'Next-Day (1 business day)', 40.00);


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


--Catalog Items
INSERT INTO manager_catalogitem VALUES (99994, 'D4', 'Nikon', 999.00, 899.00, 0.13, '<p>askdfl;j</p><p>laskdflksdalksadk</p>', '<p>asdfasdf</p><p><ol><li>asdfsadf<br></li><li>asdflkj</li><li>asdflkasdjfsadkf</li><li>asdf</li></ol></p>', 'NKD4BLK', 2, '2', '2014-04-07', 99999, 1, true, '/static/catalog/images/products/default.png', true, 0);
INSERT INTO manager_catalogitem VALUES (99995, '50x Zoom Lens', 'Nikon', 450.00, 400.00, 0.12, '<p>aksjdf 50x asfdkja;sd</p><p><br></p>', '<p>50x</p>', 'NK50ZLNS', 2, '2', '2014-04-07', 99999, 3, true, '/static/catalog/images/products/default.png', false, 0);
INSERT INTO manager_catalogitem VALUES (99997, 'Eso T5', 'Canon', 899.00, 850.00, 0.12, '<p>asdflk5</p>', '<p>asdf</p>', '213', 2, '2', '2014-04-07', 99999, 1, true, '/static/catalog/images/products/canont5.jpg', true,  0);
INSERT INTO manager_catalogitem VALUES (99993, 'D50', 'Nikon', 599.00, 499.00, 0.12, '<p>This is a lengthy description</p>', '<p><ul><li>blah<br></li><li>bklkasfdl</li><li>kffk</li><li>fkkf</li><li>dssd</li></ul></p>', 'NKD50BLK', 2, '2', '2014-04-07', 99999, 1, true, '/static/catalog/images/products/nikond50.jpg', true, 0);
INSERT INTO manager_catalogitem VALUES (99996, 'C4 Rechargeable Battery', 'Canon', 150.00, 100.00, 0.10, '<p>flaksdjh</p>', '<p>askfd</p>', 'C123456', 2, '2', '2014-04-07', 99999, 1, true, '/static/catalog/images/products/default.png', false, 0);
INSERT INTO manager_catalogitem VALUES (99992, 'Lithium Ion AA Batteries', 'Energizer', 12.95, 10.95, 0.08, '<p>High quality Energizer Lithium Ion AA Batteries.&nbsp;</p>', '<p><ul><li>Long Lasting</li><li>Rechargeable</li><li>Something Else</li><li>Stats and Info</li></ul></p>', 'ENAABATLI1', 15, '3 Days', '2014-04-07', 99999, 3, true, '/static/catalog/images/products/default.png', false, 0);
INSERT INTO manager_catalogitem VALUES (99991, '1 v2', 'Nikon', 799.00, 699.00, 0.12, '<p style="text-align: justify; font-size: 11px; line-height: 14px; margin-bottom: 14px; padding: 0px; color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans;">Lorem ipsum dolor sit amet, consectetur adipiscing elit. In quis placerat urna. Donec tincidunt malesuada magna sed porttitor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Cras pellentesque ullamcorper feugiat. Cras et eros eleifend, molestie erat eget, fringilla nibh. Pellentesque et ullamcorper metus, a vestibulum erat. Pellentesque scelerisque hendrerit dui quis elementum. Aenean cursus arcu a odio facilisis, ac ultricies leo commodo. Morbi in lectus nisl. Suspendisse viverra interdum dui non pretium. Etiam eget molestie velit. Nulla leo nisi, accumsan in iaculis malesuada, varius id augue.</p><p style="text-align: justify; font-size: 11px; line-height: 14px; margin-bottom: 14px; padding: 0px; color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans;">Quisque convallis nec arcu a placerat. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Fusce fermentum nibh et diam adipiscing, ac bibendum justo laoreet. Donec tempor tempor hendrerit. Nullam iaculis dui ut fringilla gravida. In hac habitasse platea dictumst. Vestibulum venenatis lacus sit amet sollicitudin tincidunt. Sed sollicitudin dictum venenatis. Nulla scelerisque condimentum magna, et convallis elit commodo vitae.</p>', '<p><ul><li><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Quisque convallis nec arcu a placerat.&nbsp;</span><br></li><li><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Cum sociis natoque penatibus et magnis dis parturient montes,&nbsp;</span><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">nascetur ridiculus mus.&nbsp;</span><br></li><li><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Fusce fermentum nibh et diam adipiscing, ac bibendum justo laoreet.&nbsp;</span><br></li><li><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Donec tempor tempor hendrerit.&nbsp;</span><br></li><li><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Nullam iaculis dui ut fringilla gravida. In hac habitasse platea dictumst.&nbsp;</span><br></li><li><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Vestibulum venenatis lacus sit amet sollicitudin tincidunt.&nbsp;</span><br></li><li><span style="color: rgb(0, 0, 0); font-family: Arial, Helvetica, sans; font-size: 11px; line-height: 14px; text-align: justify;">Sed sollicitudin dictum venenatis. Nulla scelerisque condimentum magna, et convallis elit commodo vitae.</span><br></li></ul></p>', 'NK1V2BLK', 2, '2 Weeks', '2014-04-07', 99999, 1, true, '/static/catalog/images/products/nikon1v2.jpg', true,  0);

