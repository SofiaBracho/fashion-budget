# BELLA EXCLUSIVA FASHION BUDGET
### A TOOL FOR SMALL BUSINESS SUCESS
#### Video Demo:  <https://youtu.be/nKtr8huMD88>
#### Description:
Bella exclusiva fashion budget is a web based application that calculates a fair Budget for tailor-made clothing according to the difficulty of manufacturing (depends on garments, materials and size), considering variables like the cost per hour of work and a control variable that the administrator can adjust on code if neccessary acording to marker variations; note that the calculator doesn't consider materials price, because it may vary depending on the place you live and offer/demand.

This application Will be useful for a local business my mother runs as a fashion designer, called Bella Exclusiva. Sometimes she doesn’t now how to calculate a fair deal with clients so I decided to automate that! Also, I added a contact and index page to get the customers know more about the business.

This proyect is my submission for CS50x final section, I applied new knowledge acquired in python and flask, also I was not very familiar with bootstrap but reading some documentation achieved a simple but clean and responsive look.

### Budget Calculation
The budget is calculated based on:

Base difficulty ratings for garment and fabric
Added difficulty for additional options like embellishments, size and gender modifiers to account for more labor, multiplied by hourly rate and control variable.

### Main Files
**app.py:** Main Python/Flask code for the web app routes and logic

**templates/:** Folder containing HTML templates for each page

**static/:** Folder for CSS, JS, images and other static files

**fashion-budget.db:** SQLite database containing garment, fabric, and pricing data

### Technologies used:
#### Frontend:
HTML, CSS, JavaScript, Bootstrap, Leaflet.js
#### Backend:
Python, Flask, Jinja, Sqlite3

### Database
The project database is built with Mysqlite3, consists in 3 tables:
#### Prendas (garments) Table:
```
CREATE TABLE prendas (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  coef_dificultad REAL
);
```
As you can see, this table has 3 columns, the first column is for id (primary key), the second one is the name of the garment (dress, blouse, shirt...), and the last one is for the aproximate dificulty of the manufacturing of each specific garment.

#### Telas (fabrics) Table:
```
CREATE TABLE Telas (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  coef_dificultad REAL
);
```
This table has 3 columns as well, the first column is for id (primary key), the second one is the name of the fabric (cotton, silk, leather...), and the last one is for the aproximate dificulty of working with each specific fabric.

#### Acabados (finishes) Table:
```
CREATE TABLE Acabados (
  id INTEGER PRIMARY KEY,
  nombre TEXT,
  tiempo_extra REAL
);
```
Like the other tables, this also has 3 columnd, the first column is for id (primary key), the second one is the name of the finish (embroidery, zipper, mandarin collar...), and the last one is for the extra time of work needed for each finish.

#### Extra tables:
I also created (but not used yet), a table to register all the budgets calculated in the app, to serve as a history. It can be added in a future version as another section of the web app.
```
CREATE TABLE presupuestos (
  id INTEGER PRIMARY KEY,
  fecha TEXT,
  prenda_id INTEGER,
  tela_id INTEGER,
  cantidad INTEGER,
  acabados TEXT,
  total REAL
);
```
It includes columns for the date of the budget calculation, id of the garment, id of the fabric, quantity, finishes, and the total calculated.

As a complement of this table there's also a Join table to include all the finishes in the budget, because it has a many to many relationship.
```
CREATE TABLE PresupuestosAcabados (
  presupuesto_id INTEGER,
  acabado_id INTEGER,

  PRIMARY KEY(presupuesto_id, acabado_id),
  FOREIGN KEY(presupuesto_id) REFERENCES Presupuestos(id),
  FOREIGN KEY(acabado_id) REFERENCES Acabados(id)
);
```
This join table has only two columns, wich are the id of the budget and the id of the finish. Both columns together forms the primary key, and are also each one of them a foreign key to the finishes and budgets tables respectively.

In this way, I could in the future get all the data needed for a history, from joining the budgets table with others.

### INDEX:
The index section consists in a main block inside the default layout (that includes a nav header and footer). In the main block there is a big image with relative position and in front of the image a title header welcoming the client with a short paragraph and a button calling to action, the button redirects to the budget calculator.

Next, is a section divided by two, in the left side a photo related to fashion design and in the right side a short text explaining what is the business Bella Exclusiva about.

In the last section of this page there is a row using bootstrap with 3 columns, each one having a card element with an image, header and text, refering to the benefits and services offered by Bella Exclusiva.

### CALCULATOR:
As all the other pages, this also includes de layout with the navbar. In the top of the page there is a conditional (if) using python jinja, that checks if an error has ocurred during the budget calculation. If there is an error, shows a bootstrap alert describing the error.

Beside the alert (invisible by default), we can see a row with two columns, in the left side a form including all the necessary inputs to make the calculation, and in the right side a flexible image in relative position and a big text telling the price calculated in usd format (by default is $0,00), followed by a call to action to contact.

### **Form specification**

1. **Type of garment:**

**Type:** select **required**

**Description:** Has different options each one extracted from the db garments table.

**Default option:** disabled (-- Select --)

2. **Type of fabric:**

**Type:** select **required**

**Description:** Has different options each one extracted from the db fabrics table.

**Default option:** disabled (-- Select --)

3. **Gender/age:**

**Type:** select **required**

**Description:** Has male, female and child options, because the manufacturing difficulty may vary depending on this.

**Default option:** disabled (-- Select --)

4. **Amount/Quantity:**

**Type:** number **required**, min 1

**Description:** Is the number of pieces of clothes of the same type you want to budget.

5. **Big size:**

**Type:** check box

**Description:** If the client is bug size (L, XL, XXL), can check the box, it may difficult the manufacturing and increase the amount of fabric needed.

6. **Details/Finishes:**

**Type:** multiple select **required**

**Description:** Has different options each one extracted from the db details table. It has also a none option to indicate if the clothing won't have any finishes. It sends a list to the python backend.

### CONTACT:

Is a simple contact page that includes de nav bar in the layout and a container with two columns++. In the left column three elements each one with an icon and contact info (email, phone, instagram). On the right side, a map powered by leaflet, a javaScript open source library for maps pinning the direction of the fashion workshop Bella Exclusiva.

### APP.PY

The calculator() route handles form submission:

1. Get inputs with request.form
2. Lookup base difficulty ratings from database
3. Add any extra difficulty for selected options
4. Apply size/gender modifiers
5. Multiply by pricing constants to get total
6. Render template with calculated budget

### Future Improvements
Some potential enhancements:

* User accounts and order history
* Admin interface to manage pricing factors
* Whatsapp notifications & order confirmations
* Improved design and UX