from hash_utils import calculate_hash
import os
from datetime import datetime


def generate_hash(file_path):

    if not os.path.isfile(file_path):
        return {
            "success": False,
            "message": "File does not exist."
        }

    hash_value = calculate_hash(file_path)

    file_name = os.path.basename(file_path)

    output_file = "hashes/" + file_name + ".sha256"

    generated_time = datetime.now()

    with open(output_file, "w") as file:
        file.write(f"File: {file_name}\n")
        file.write("Algorithm: SHA-256\n")
        file.write(f"Generated On: {generated_time}\n\n")
        file.write("Hash:\n")
        file.write(hash_value)

    return {
        "success": True,
        "message": "SHA-256 Hash Generated Successfully!",
        "hash": hash_value,
        "filename": file_name,
        "saved": output_file,
        "time": generated_time
    }
