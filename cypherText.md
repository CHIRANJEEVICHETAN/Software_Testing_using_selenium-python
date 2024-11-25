### **Encryption Using the Hill Cipher**

#### **Plaintext:**  
"Paymoremoney"  

#### **Key Matrix (K):**
\[
K = 
\begin{bmatrix}
17 & 17 & 5 \\
21 & 18 & 21 \\
2 & 2 & 19
\end{bmatrix}
\]

---

### **Step-by-Step Encryption Process:**

1. **Divide Plaintext into Groups of 3 Letters:**  
   - Convert each letter to its numeric equivalent (A = 0, B = 1, ..., Z = 25).  
   - Plaintext: "Paymoremoney"  
     - **Numeric Equivalent:** P = 15, A = 0, Y = 24, M = 12, O = 14, R = 17, E = 4, M = 12, O = 14, N = 13, E = 4, Y = 24.  
     - Grouped as:  
       \[
       \text{Groups: } 
       \begin{bmatrix}
       15 & 0 & 24 \\
       12 & 14 & 17 \\
       4 & 12 & 14 \\
       13 & 4 & 24
       \end{bmatrix}
       \]

2. **Matrix Multiplication:**  
   For each group of plaintext, perform matrix multiplication with the key matrix \( K \), followed by mod 26 operation.

   #### Example Calculation for the First Group: \([15, 0, 24]\)
   - Multiply:
     \[
     \begin{bmatrix}
     15 & 0 & 24
     \end{bmatrix}
     \cdot
     \begin{bmatrix}
     17 & 17 & 5 \\
     21 & 18 & 21 \\
     2 & 2 & 19
     \end{bmatrix}
     =
     \begin{bmatrix}
     303 & 303 & 531
     \end{bmatrix}
     \]
   - Apply Modulo 26:
     \[
     \begin{bmatrix}
     303 & 303 & 531
     \end{bmatrix}
     \mod 26 =
     \begin{bmatrix}
     17 & 17 & 11
     \end{bmatrix}
     \]
   - Result: **RRL**.

3. **Continue for All Groups:**  
   Repeat the above process for each group:
   - Group \([12, 14, 17]\): Produces **MWB**.  
   - Group \([4, 12, 14]\): Produces **KAS**.  
   - Group \([13, 4, 24]\): Produces **PDH**.

---

### **Final Ciphertext:**  
**"RRLMWBKASPDH"**

---

This process encrypts the plaintext using the Hill cipher technique with the provided key matrix. Let me know if you need clarification or further steps for decryption!
