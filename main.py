from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Your original code goes here ---
# (Do not modify it; just paste it where indicated.)

def run_siteless_prototype(input_data):
    """
    This function wraps the original prototype code.
    Replace the body with your actual code from:
    {SITELESS PROTOTYPE CODE}
    """
    
    # >>> BEGIN ORIGINAL CODE <<<
    # {SITELESS PROTOTYPE CODE}
    # Return some result based on your code's behavior.
    # Make sure your pasted code ends with a variable named `result`.
    # >>> END ORIGINAL CODE <<<
    
    return result


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/run", methods=["POST"])
def run_api():
    user_input = request.get_json().get("input", "")
    output = run_siteless_prototype(user_input)
    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

    from flask import Flask, render_template, request, jsonify
import json
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=""
)

def run_prototype(model, age, damages):
    # --- BEGIN ORIGINAL PROTOTYPE LOGIC (adapted for web input) ---

    system_prompt = """
    You are an expert assistant for determining to either resell, repair, or recycle old tech
    ask follow up question about the item
    site a video if you can
    use simple language
    """

    chat_history = [
        {"role": "system", "content": system_prompt},
    ]

    electronic = f"Electronic: {model}"
    age_old = f"Age: {age}"
    total_damages = f"Damages: {damages}"

    user_prompt = electronic + " | " + age_old + " | " + total_damages

    chat_history.append({"role": "user", "content": user_prompt})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history
    )

    assistant_response = response.choices[0].message.content

    return assistant_response

    # --- END ORIGINAL PROTOTYPE LOGIC ---


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/run", methods=["POST"])
def run_api():
    data = request.get_json()
    model = data.get("model", "")
    age = data.get("age", "")
    damages = data.get("damages", "")

    result = run_prototype(model, age, damages)

    return jsonify({"output": result})


if __name__ == "__main__":
    app.run(debug=True)
