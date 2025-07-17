# eljohnniewalker - JWT Token Signature Tester and Cracker

## Description

**eljohnniewalker** automates the process of testing the security of JWT tokens.  
It attempts to crack the token signature using **jwt-cracker** with a predefined secrets dictionary (`scraped-JWT-secrets.txt`).
The dictionnary can also be found in the following [github.com/danielmiessler](https://github.com/danielmiessler/SecLists/tree/master/Passwords)
If the secret key is not found, it forges a token modifying the header algorithm to `"None"` and removes the signature to test for insecure implementations accepting unsigned tokens.

---

## Requirements

- Python 3.x (tested on 3.6+)  
- `jwt-cracker` installed and available in your system PATH: [jwt-cracker GitHub](https://github.com/lmammino/jwt-cracker)  

---

## Installation

1. Clone or download this repository.

2. Make sure you have Python 3 installed.

3. Download and install **jwt-cracker**:  
   ```bash
   npm install --global jwt-cracker


## Usage
Run the script with the JWT token you want to test as the only argument:
    ```bash
    python eljohnniewalker.py <jwt_token>

The script will:

Attempt to crack the JWT signature with jwt-cracker using the scraped-JWT-secrets.txt dictionary.

Display the number of secrets tried and the cracking time.

If unsuccessful, forge and print a token with the algorithm set to "None" and without signature.

## Notes
Make sure jwt-cracker is installed and accessible from the command line (jwt-cracker command must work).

The script counts the lines in the secrets file to show how many keys it will try. Feel free to suggest modifications to add secrets.

Forged tokens with "alg":"None" can help identify vulnerable JWT implementations accepting unsigned tokens.

Remember that the cracker will only work with these three algorithms: HS256, HS384 & HS512 (supported by jwt-cracker)

## Contact
For questions or issues, feel free to contact dcentgame50@gmail.com!
