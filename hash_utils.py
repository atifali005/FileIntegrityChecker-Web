# hash_utils.py
# This module calculates the SHA-256 hash of a file.

import hashlib

def calculate_hash(file_path):
    # Create a SHA-256 hash object
    sha256 = hashlib.sha256()

    # Open the file in binary mode
    with open(file_path, "rb") as file:

        # Read the file in chunks
        while True:
            data = file.read(4096)

            if not data:
                break

            # Update the hash object
            sha256.update(data)

    # Return the hexadecimal hash
    return sha256.hexdigest()
