# Employee Salary Analysis

A beginner-friendly Python project that analyzes employee salaries and calculates the **total, average, highest, and lowest salary**. It also compares every salary with the average to show who earns above or below it.

## Objective

Practice numerical data processing using Python.

## Tools Used

- Python 3
- Jupyter Notebook
- Pandas (for the bonus summary statistics)

## Dataset

A manually created dataset of 8 employees stored in two Python lists (`employees` and `salaries`). Salaries are in Indian rupees (₹).

| Employee | Salary (₹) |
|----------|-----------|
| Asha | 45,000 |
| Ravi | 52,000 |
| Meena | 38,000 |
| Kiran | 75,000 |
| Swetha | 60,000 |
| Harsh | 42,000 |
| Rupesh | 58,000 |
| Akhil | 90,000 |

## Approach

1. **Store the data** in two lists: `employees` (names) and `salaries` (amounts).
2. **Total salary** is calculated using `sum(salaries)`.
3. **Average salary** is the total divided by the number of employees: `total / len(salaries)`.
4. **Highest and lowest salary** are found using `max(salaries)` and `min(salaries)`.
5. **Names of the highest and lowest earners** are found by getting the position of the value with `salaries.index()` and using that position to pick the name from `employees`.
6. **Compare with the original data:** the average is subtracted from each salary, and each employee is labelled as above average, below average, or equal to average.
7. **Bonus:** Pandas `describe()` gives count, mean, min, max, and quartiles in a single step.

## Total vs Average Salary

- **Total salary** is the sum of all salaries. It shows the overall salary cost.
- **Average salary** is the total divided by the number of employees. It shows the typical salary of one employee.

## How to Run

1. Install Python, Jupyter Notebook, and Pandas:
   ```
   pip install notebook pandas
   ```
2. Clone or download this repository.
3. Open a terminal in the project folder and run:
   ```
   python -m notebook
   ```
4. Open `employee_salary_analysis.ipynb`.
5. Run all cells from top to bottom (`Shift + Enter`).

## Sample Output

```
Total salary: ₹460,000
Average salary: ₹57,500.00
Highest salary: ₹90,000 (Akhil)
Lowest salary: ₹38,000 (Meena)

Employee  Salary    Diff      Status
Asha      45000     -12,500   Below average
Ravi      52000     -5,500    Below average
Meena     38000     -19,500   Below average
Kiran     75000     +17,500   Above average
Swetha    60000     +2,500    Above average
Harsh     42000     -15,500   Below average
Rupesh    58000     +500      Above average
Akhil     90000     +32,500   Above average
```

## Key Insight

The average salary (₹57,500) is pulled upward by the two highest salaries, so only 4 of the 8 employees earn above it. Comparing each salary with the average gives a clearer picture than the average alone.

## Limitations

- If two employees share the highest or lowest salary, `.index()` returns only the first one.
- The program does not handle an empty list (dividing by zero would cause an error).
- Salaries are typed in manually instead of being read from a file.

## Possible Improvements

- Read salaries from a CSV file.
- Add median and standard deviation.
- Group employees by department and compare average salaries.
- Plot a bar chart of salaries with the average line.

## Author

SwethaPulusu
