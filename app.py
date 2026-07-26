from flask import Flask, render_template, request
import os
from generate import generate_hash
from verify import verify_hash

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
HASH_FOLDER = "hashes"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["HASH_FOLDER"] = HASH_FOLDER

# Create required folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(HASH_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    uploaded_file = request.files.get("file")

    if uploaded_file is None or uploaded_file.filename == "":
        return render_template(
            "index.html",
            result={
                "success": False,
                "message": "Please select a file."
            }
        )

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        uploaded_file.filename
    )

    uploaded_file.save(filepath)

    result = generate_hash(filepath)

    # Debug output
    print("\nGenerate Result:")
    print(result)

    return render_template(
        "index.html",
        result=result
    )


@app.route("/verify", methods=["POST"])
def verify():

    uploaded_file = request.files.get("file")

    if uploaded_file is None or uploaded_file.filename == "":
        return render_template(
            "index.html",
            result={
                "success": False,
                "message": "Please select a file."
            }
        )

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        uploaded_file.filename
    )

    uploaded_file.save(filepath)

    result = verify_hash(filepath)

    # Debug output
    print("\nVerify Result:")
    print(result)

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
