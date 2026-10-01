# 🔐 Secure Password Entropy Analyzer & Generator

A command-line tool built in Python that evaluates password strength using **information theory (Shannon entropy)** and generates cryptographically secure passwords using Python's `secrets` module. 

Unlike basic password checkers that rely on superficial character-count rules, this tool calculates the exact bit-entropy of a password based on its length and character pool size.

---

## 🚀 Features

* **Information-Theory Entropy Calculation:** Measures password strength in bits using the standard formula: $E = L \times \log_2(R)$.
* **Dynamic Character Pool Detection ($R$):** Automatically inspects strings for lowercase letters, uppercase letters, numbers, and standard ASCII symbols.
* **Cryptographically Secure Generator (CSPRNG):** Utilizes Python's `secrets` module instead of the insecure pseudo-random `random` module to generate high-entropy passwords.
* **Granular Strength Ratings:** Classifies passwords from "Very Weak" to "Cryptographically Robust" based on established security thresholds.
* **Zero Dependencies:** Built entirely using Python standard libraries (`math`, `secrets`, `string`), making it lightweight and instantly runnable.

---

## 🧮 The Math Behind It

The security of a password can be quantified using **Shannon Entropy**:

$$E = L \times \log_2(R)$$

* **$L$ (Length):** Total number of characters in the password.
* **$R$ (Pool Size):** Total number of unique possible characters drawn from:
  * Lowercase letters (a-z): 26
  * Uppercase letters (A-Z): 26
  * Numbers (0-9): 10
  * Punctuation symbols: 32

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Standard Libraries:** `math`, `secrets`, `string`

---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/password-entropy-analyzer.git](https://github.com/your-username/password-entropy-analyzer.git)
   cd password-entropy-analyzer
