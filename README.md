# Loan Payment Calculator 📊

This is a simple **Loan Payment Calculator** written in Python. It calculates **monthly payments**, **interest charges**, and **remaining balance** over the loan period based on user inputs.

### 🚀 Features
- Takes user input for **Loan Amount**, **Annual Interest Rate**, and **Loan Length**
- Computes the **monthly installment (EMI)** using the standard formula
- Displays a **detailed amortization schedule** with interest charges and balances
- Uses Python's `math` module for precise calculations

### 🛠️ How to Run

1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/loan-calculator.git
   cd loan-calculator
   ```

2. **Run the Python Script**
   ```sh
   python loan_calculator.py
   ```

## 📌 Formula Used
The **EMI (Equated Monthly Installment)** formula:

![EMI Formula](https://latex.codecogs.com/png.latex?M%20%3D%20%5Cfrac%7BP%20%5Ctimes%20%5Cleft(%5Cfrac%7Br%7D%7B12%7D%5Cright)%20%5Ctimes%20%5Cleft(1%20%2B%20%5Cfrac%7Br%7D%7B12%7D%5Cright)%5E%7B12t%7D%7D%7B%5Cleft(1%20%2B%20%5Cfrac%7Br%7D%7B12%7D%5Cright)%5E%7B12t%7D%20-%201%7D)

Where:
- **M** = Monthly payment
- **P** = Loan principal
- **r** = Annual interest rate (in decimal)
- **t** = Loan duration (in years)

## 📊 Sample Output
```
Enter Loan Amount  
50000  
Enter an Annual Interest Rate in Percentage  
5  
Enter a Loan Length in Year  
2  
Your Payment will be : Rs2191.28  

Month      StartingBalance   InterestCharge    Payment    EndingBalance  
1          Rs50000.0         Rs208.33          Rs2191.28  Rs48017.05  
2          Rs48017.05        Rs200.07          Rs2191.28  Rs46025.84  
...
24         Rs2170.89         Rs9.04            Rs2191.28  Rs0.0  
```

## 📜 License
This project is **open-source** under the [MIT License](LICENSE).
