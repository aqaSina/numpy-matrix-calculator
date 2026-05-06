
```markdown
# Matrix Calculator (NumPy)

This project is a functional matrix calculator developed in Python
using the powerful NumPy library. It allows you to input your own \(2 \times 2\) matrices,
use randomly generated matrices, and then perform various operations
such as element-wise multiplication, matrix multiplication, addition, subtraction, and division.

## Features

-   **Matrix Input:**
    -   Option to manually input custom \(2 \times 2\) matrices.
    -   Option to use randomly generated \(2 \times 2\) matrices.
-   **Matrix Editing:**
    -   Ability to edit the first matrix after initial input.
    -   Ability to edit the second matrix after initial input.
-   **Matrix Operations:**
    -   Display of both input matrices.
    -   **Element-wise Multiplication**
    -   **Matrix Multiplication**
    -   **Matrix Addition**
    -   **Matrix Subtraction** (Matrix 1 - Matrix 2)
    -   **Matrix Division** (Matrix 1 / Matrix 2 - element-wise)
-   **Result Display:** Clear presentation of input matrices and operation results.

## How to Run

1.  **Program Start:** Upon running the script, you will be prompted to choose between entering your own matrices or using random ones:
    *   `1`: Manual Matrix Input
    *   `2`: Random Matrices

2.  **First Matrix Input:**
    *   If you choose `1`, the program will ask for 4 inputs for the values of a \(2 \times 2\) matrix (e.g., `a11`, `a12`, `a21`, `a22`).
    *   After entering the values, you will be asked:
        *   `1`: To **edit the first matrix** (This option returns you to the stage of re-entering the first matrix values. Note: In this specific implementation, it may loop back without allowing edits in the same step, primarily for re-entry).
        *   `2`: To **proceed to input the second matrix**.

3.  **Second Matrix Input:**
    *   After selecting `2` in the previous step (or directly if you chose random matrices initially),
    the program will prompt you for the second matrix, similar to the first (4 inputs for a \(2 \times 2\) matrix).
    *   After entering the second matrix, you will be asked again:
        *   `1`: To **execute the operations**. The program will proceed with the entered matrices.
        *   `2`: To **edit the second matrix**. If you choose this option, the program will execute the operations immediately after applying the edits.

4.  **Display and Operations:**
    *   Once both matrices are defined, the program will first display both matrices.
    *   Then, a menu for selecting operations will appear:
        *   `0`: Re-display both the first and second matrices.
        *   `1`: Element-wise multiplication (Matrix 1 * Matrix 2).
        *   `2`: Matrix multiplication (Matrix 1 @ Matrix 2).
        *   `3`: Matrix addition (Matrix 1 + Matrix 2).
        *   `4`: Matrix subtraction (Matrix 1 - Matrix 2).
        *   `5`: Matrix division (Matrix 1 / Matrix 2 - element-wise).

## Example Input and Output

**Manual Input Scenario:**

```
Do you want to enter your own matrices or use random matrices? (1 or 2): 1
Enter the first matrix:
matrix 1 position (row=0 , col=0): 1 ___
matrix 1 position (row=0 , col=1): 2 ___
matrix 1 position (row=1 , col=0): 3 ___
matrix 1 position (row=1 , col=1): 4 ___

Choose: 1 (Edit Matrix 1) or 2 (Proceed to Matrix 2): 2
Enter the second matrix:
matrix 2 position (row=0 , col=0): 5 ___ 
matrix 2 position (row=0 , col=1): 6 ___
matrix 2 position (row=1 , col=0): 7 ___
matrix 2 position (row=1 , col=1): 8 ___

Choose: 1 (Run Program) or 2 (Edit Matrix 2): 1

Matrix 1:
[[1 2]
 [3 4]]

Matrix 2:
[[5 6]
 [7 8]]

Operations Menu:
0: Display both matrices ///
1: Element-wise multiplication ///
2: Matrix multiplication ///
3: Matrix addition ///
4: Matrix subtraction (Matrix 1 - Matrix 2) ///
5: Matrix division (Matrix 1 / Matrix 2) ///
Select operation (0-5): 3

Result of Matrix Addition:
[[ 6  8]
 [10 12]]
```

**Random Matrix Scenario:**

```
Do you want to enter your own matrices or use random matrices? (1 or 2): 2

Matrix 1:
[[23 56]
 [89 87]]

Matrix 2:
[[51 19]
 [22 38]]

Choose: 1 (Run Program) or 2 (Edit Matrix 2): 1

Operations Menu:
... (Similar to the example above)
Select operation (0-5): 2

Result of Matrix Multiplication:
[[2864 4509] 
 [3888 4538]]
```

## Requirements

-   Python 3.x
-   NumPy

## Development Notes

-   This project provides a solid foundation for adding more features, such as support for larger matrix dimensions (\(3 \times 3\), \(n \times n\)),
more complex operations (determinant, inverse, transpose), or loading matrices from external files (CSV, TXT).
-   The current code is designed for educational and practice purposes. For professional use, further optimizations and comprehensive error handling could be implemented.
```

