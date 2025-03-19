from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Allows frontend to communicate with backend

# Replace with your OpenAI API key

# Course details

COURSES = {
    "AI & ML": "Gaint offers a 6-months AI & ML course for ₹50,000, covering everything from basics to advanced concepts.",
    "IoT": "Gaint offers a 3-months IoT course for ₹30,000, covering everything from basics to advanced concepts.",
    "Testing": "Gaint offers a 3-month Testing course for ₹35,000, covering everything from basics to advanced concepts.",
    "Data Science": "Gaint offers a 6-months Data Science course for ₹50,000, covering everything from basics to advanced concepts.",
    "Data Analytics":"Gaint offers a 3-months Data Analytics course for ₹40,000, covering everything from basics to advanced concepts.",
    "Full Stack(Frontend and Backend)":"Gaint offers a 5-months Full Stack course for ₹40,000, covering everything from basics to advanced concepts.",
    "Digital Marketing":"Gaint offers a 3-months Digital Marketing course for ₹30,000, covering everything from basics to advanced concepts.",
    "Cloud Computing": "Gaint offers a 3-months Cloud Computing course for ₹35,000, covering everything from basics to advanced concepts.",
    "Python": "Gaint offers a 3-months Python course for ₹30,000, covering everything from basics to advanced concepts.",
    "Cyber Security": "Gaint offers a 3-months Cyber Security course for ₹35,000, covering everything from basics to advanced concepts."
}

# FAQs
FAQS = {
    "workshop": [
        "We offer workshops in AI Agent, AI & ML, IoT, Data Science, Cloud, Fullstack, Cyber Security, Digital Marketing and Testing both online and offline.",
        "Register at https://gaintclout.com/ or fill this form: https://acesse.one/dqYL1.",
        "Yes! Upon completion, you will receive a certificate.",
        "Workshop fees vary depending on the topic and duration, The duration it varies from 1 day to 3 days."
    ],
    "training": [
        "Our training programs cover AI & ML, IoT, Fullstack Development, Cloud Computing, Python, Data Analytics, Data Science, Testing, Cyber Security, and Digital Marketing with hands-on projects.",
        "Training duration varies from 3 months to 6 months based on the course.",
        "Yes! You will receive an industry-recognized certificate.",
        "We provide mentorship and real-world projects."
    ],
    "internship": [
        "We offer internships in AI Agent, AI & ML, IoT, Fullstack Development, Cloud Computing, Python, Data Analytics, Data Science, Testing, Cyber Security, and Digital Marketing ",
        "Internships can be remote or in-office, lasting from 1 to 3 months.",
        "Yes, we offer both paid and unpaid internships.",
        "Outstanding interns may receive pre-placement offers."
    ],
    "courses": ["We offer courses AI & ML, IoT, Fullstack Development, Cloud Computing, Python, Data Analytics, Data Science, Testing, Cyber Security, and Digital Marketing "],
    "hi": ["Hi, How Can I Help You regarding courses, workshops and internship ?"],
    "hello": ["Hi, How Can I Help You regarding courses, workshops and internship ?"],
    "Contact": ["For more details, contact Rohini Reddy at 9014241014 or visit https://gaintclout.com/."],
    "website link": ["https://gaintclout.com/."],
    "office location": ["Orbit Auro reality opposite to T hub, shilpagram craft, Raidurg."],
    "Registration link": ["https://acesse.one/dqYL1."]
}

def chatbot_response(user_input):
    """Handles chatbot logic"""
    user_input_lower = user_input.lower()

    # Check for course queries
    for course, details in COURSES.items():
        if course.lower() in user_input_lower:
            return f"{details} Would you like more details contact:9014241014 or email:info@gaintclout.com ?"

    # Check for workshop, training, or internship queries
    for category, responses in FAQS.items():
        if category in user_input_lower:
            return "\n".join(responses)

    # If no predefined answer, call OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

@app.route("/")
def index():
    """Render the HTML page."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """Handles chatbot interaction via API"""
    data = request.get_json()
    user_input = data.get("message", "")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
