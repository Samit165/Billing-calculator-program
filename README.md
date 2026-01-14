# Billing-calculator-program

##  Overview

This project is a **Python-based invoice calculation module** designed to test and demonstrate **core accounting logic within a software environment**.
The program accepts item details from the user, applies business rules such as **bulk discount**, **tax calculation**, and **round-off**, and then displays a detailed invoice summary.

This project was developed as part of a technical assessment focusing on **accuracy, validation, and financial logic**.

---

##  Features

* User input validation for all fields
* Accurate subtotal calculation
* Automatic bulk discount application
* Tax calculation based on discounted subtotal
* Financial rounding to **2 decimal places**
* Clear and structured invoice output

---

##  Input Details

The program takes the following inputs from the user:

* **Item Name** (String)
* **Quantity** (Integer, must be greater than 0)
* **Unit Price** (Decimal, must be greater than 0)
* **Tax Rate** (Percentage between 0 and 100)

---

##  Business Logic Implemented

### 1. Subtotal Calculation

```
Subtotal = Quantity × Unit Price
```

### 2. Bulk Discount Rule

* If subtotal **exceeds 1000**, a **5% discount** is applied.

```
Discount = 5% of Subtotal
```

### 3. Tax Calculation

* Tax is calculated **after discount**.

```
Tax Amount = Discounted Subtotal × (Tax Rate / 100)
```

### 4. Rounding Rule

* All financial values are rounded to **exactly 2 decimal places**.

---

## Output Displayed

The program displays the following details:

* Item Name
* Quantity
* Unit Price
* **Original Subtotal**
* **Discount Amount (if applicable)**
* **Tax Amount**
* **Grand Total**

---

## Sample Test Case

**Input:**

```
Item Name : Laptop
Quantity  : 1
Unit Price: 1200
Tax Rate  : 18%
```

**Expected Output Logic:**

* Subtotal = 1200.00
* Discount (5%) = 60.00
* Discounted Subtotal = 1140.00
* Tax (18%) = 205.20
* **Grand Total = 1345.20**

---

##  How to Run the Program

1. Ensure Python is installed on your system.
2. Clone the repository or download the ZIP file.
3. Run the script using:

```bash
python invoice.py
```

4. Enter the required input values when prompted.

---

## Project Structure

```
├── invoice.py
├── README.md
```

---

## Notes

* The program uses **only core Python**, no external libraries.
* Proper exception handling is implemented for invalid inputs.
* Developed strictly following assessment instructions.

---

## Author

**Samit Kundu**
Python Trainee / Student Developer
