<html>
<body>

MyStuff - INTEX 2 - Digitallifemyway.com Readme
==============================================================================
Authors: Jordan Carlson, Seth Gremmert, Emily Cookson, Courtney Llera
Group: Section 2 Group 6
Last Modified: April 11, 2014
==============================================================================

All files are organized into "Apps" based on functionality, use cases and how 
the database is structured.  HTML files are rendered into views using python
code contained in .py files of the same name (I.E. login.html is rendered 
using login.py). This allows for a separation between the users and business
logic by only allowing them to interact with the view.

Account
==============================================================================
Includes all of the views and files necessary for the CRUD management of users, 
accounts, and employees. Also containts the functionality to reset forgotten
passwords.  Users also have pages to check their rentals, orders and repairs.

base_app
==============================================================================
Contains base templates for building the file directories of other apps. Also
contains the base template for pages and ajax files.

Catalog
==============================================================================
Contains all of the views needed for searching, creating, and transacting 
actions with product items in the database.

Manager
==============================================================================
Includes all of the views for the CRUD management of items, invetory, repairs,
stores, rentals and fees etc.

MyStuff_Initial_Values.sql
==============================================================================
An SQL database file that contains initial values to populate the tables in 
the databse



Make sure to download the richtext editor Summernote

<pre><code>pip install django-summernote</code></pre>




</body>
</html>
