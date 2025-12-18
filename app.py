from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# ================================
# SAFE: Use environment variables in real deployment
# ================================
client = OpenAI(
    api_key=""
)

# ---------------------------------------------------------
# AI Logic
# ---------------------------------------------------------
def run_prototype(model, age, damages):
    system_prompt = """
You are a friendly but highly knowledgeable electronics technician who helps users
decide whether to Repair, Resell, or Recycle a device.

Rules you must follow:
1. Always provide a complete, final answer in one message.
2. NEVER ask follow-up questions.
3. NEVER ask the user for more information.
4. NEVER continue the conversation or wait for more details.
5. Only use the information provided by the user.
6. Keep the language simple, clear, and helpful.
7. Your answer must be short, practical, and easy to understand.
8. Act like a human technician — no robotic tone.

Your output must ALWAYS include EXACTLY these sections:

Recommendation: <Repair/Resell/Recycle>

Why:
- bullet point
- bullet point
- bullet point

Price Estimate:
<simple estimate for resale or repair>

Confidence:
<number>%

Do NOT include any follow-up questions. Do NOT request additional details.
Just respond with the best possible direct answer based on the information you have.

"""

    user_prompt = (
        f"Model: {model}\n"
        f"Age: {age}\n"
        f"Damages: {damages}\n"
        f"Provide the full structured output."
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    return response.choices[0].message.content


# ---------------------------------------------------------
# ROUTES
# ---------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/run", methods=["POST"])
def run_api():
    data = request.get_json(force=True)

    model = data.get("model", "")
    age = data.get("age", "")
    damages = data.get("damages", "")

    output = run_prototype(model, age, damages)
    return jsonify({"output": output})


# ---------------------------------------------------------
# MAIN ENTRY
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)