import math
import secrets
import string


def calculate_entropy(password):
 
  if not password:
    return 0, 0, 0

  length = len(password)


  has_lower = any(c in string.ascii_lowercase for c in password)
  has_upper = any(c in string.ascii_uppercase for c in password)
  has_digits = any(c in string.digits for c in password)
  has_symbols = any(c in string.punctuation for c in password)

  pool_size = 0
  if has_lower:
    pool_size += 26
  if has_upper:
    pool_size += 26
  if has_digits:
    pool_size += 10
  if has_symbols:
    pool_size += len(string.punctuation)  

  if pool_size == 0:
    return 0, length, 0

  entropy = length * math.log2(pool_size)
  return entropy, length, pool_size


def evaluate_strength(entropy):
  """Evaluates password strength based on entropy bit thresholds."""
  if entropy < 28:
    return "Very Weak (Instantly crackable)"
  elif entropy < 36:
    return "Weak (Vulnerable to basic brute-force)"
  elif entropy < 60:
    return "Moderate (Safe from casual guessing, but vulnerable to target attacks)"
  elif entropy < 128:
    return "Strong (Highly secure against standard brute-force)"
  else:
    return "Very Strong (Cryptographically robust)"


def generate_secure_password(length=16, use_symbols=True):
  """Generates a cryptographically secure random password.

  Note: We use the 'secrets' module instead of 'random' because 'secrets' is
  designed for security-sensitive values (CSPRNG).
  """
  alphabet = (
      string.ascii_letters
      + string.digits
      + (string.punctuation if use_symbols else "")
  )
  return "".join(secrets.choice(alphabet) for _ in range(length))


def main():
  print("==========================================")
  print("  Password Entropy Analyzer & Generator   ")
  print("==========================================")

  while True:
    print("\nOptions:")
    print("1. Check password entropy and strength")
    print("2. Generate a secure random password")
    print("3. Exit")

    choice = input("\nSelect an option (1-3): ").strip()

    if choice == "1":
      pwd = input("Enter password to analyze: ")
      entropy, length, pool = calculate_entropy(pwd)
      strength = evaluate_strength(entropy)

      print("\n--- Analysis Results ---")
      print(f"  Length: {length} characters")
      print(f"  Character Pool Size (R): {pool} possible characters")
      print(f"  Entropy Score: {entropy:.2f} bits")
      print(f"  Rating: {strength}")

    elif choice == "2":
      try:
        length_input = input(
            "Enter desired length (default 16, min 8): "
        ).strip()
        length = int(length_input) if length_input else 16
        if length < 8:
          length = 8
          print("Length adjusted to minimum of 8 for security.")
      except ValueError:
        length = 16

      secure_pwd = generate_secure_password(length)
      entropy, length, pool = calculate_entropy(secure_pwd)
      strength = evaluate_strength(entropy)

      print("\n--- Generated Secure Password ---")
      print(f"  Password: {secure_pwd}")
      print(f"  Entropy: {entropy:.2f} bits")
      print(f"  Rating: {strength}")

    elif choice == "3":
      print("Exiting program....")
      break
    else:
      print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
  main()
