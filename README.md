# eljohnniewalker
**eljohnniewalker** automates the process of testing the security of JWT tokens.   It attempts to crack the token signature, if the secret key is not found, it forges a token modifying the header algorithm to `"None"` and removes the signature to test for insecure implementations accepting unsigned tokens.
