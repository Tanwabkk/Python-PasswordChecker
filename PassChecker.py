import math
import re

def calculate_entropy(password):
    """Calculates the pool size based on character types used 
       and computes mathematical bit entropy."""
    pool_size = 0
    if re.search(r'[a-z]', password):
        pool_size += 26
    if re.search(r'[A-Z]', password):
        pool_size += 26
    if re.search(r'[0-9]', password):
        pool_size += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        pool_size += 32  
        
    if pool_size == 0 or len(password) == 0:
        return 0.0
        
   
    entropy = len(password) * math.log2(pool_size)
    return round(entropy, 2)

def audit_password(password):
    print(f"\n--- Auditing Password: '{password}' ---")
    
    # Check length
    if len(password) < 8:
        print("[-] Warning: Password is shorter than 8 characters.")
    
    # Common weak patterns check
    weak_patterns = ["12345", "password", "qwerty", "admin", "welcome"]
    if any(p in password.lower() for p in weak_patterns):
        print("[-] Critical: Contains a common dictionary pattern or sequence!")
    
    # Entropy calculation
    entropy = calculate_entropy(password)
    print(f"[+] Calculated Entropy: {entropy} bits")
    
    if entropy < 28:
        print("[!] Strength Rating: VERY WEAK (Easily brute-forced instantly)")
    elif entropy < 36:
        print("[!] Strength Rating: WEAK (Vulnerable to basic dictionary attacks)")
    elif entropy < 60:
        print("[*] Strength Rating: MODERATE (Acceptable for low-risk accounts)")
    else:
        print("[*] Strength Rating: STRONG (Highly resilient against cracking)")

if __name__ == "__main__":
    user_pass = input("Enter a password to test: ")
    audit_password(user_pass)
