from hash_utils import calculate_hash
import os
import hmac


def verify_hash(file_path):

    if not os.path.isfile(file_path):
        return {
            "success": False,
            "message": "File does not exist."
        }


    current_hash = calculate_hash(file_path)

    file_name = os.path.basename(file_path)

    hash_file = "hashes/" + file_name + ".sha256"


    if not os.path.isfile(hash_file):
        return {
            "success": False,
            "message": "Hash file not found."
        }


    with open(hash_file, "r") as file:

        content = file.read()

        saved_hash = content.split("Hash:\n")[-1].strip()



    if hmac.compare_digest(current_hash, saved_hash):

        return {
            "success": True,
            "status": "original",
            "message": "File Integrity Verified!",
            "current_hash": current_hash,
            "stored_hash": saved_hash
        }


    return {

        "success": True,
        "status": "modified",
        "message": "WARNING! File has been Modified.",
        "current_hash": current_hash,
        "stored_hash": saved_hash

    }
