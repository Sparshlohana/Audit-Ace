from flask import Flask, jsonify, request

app = Flask(__name__)

# Function to introduce EVA and provide menu options
def eva_introduction():
    return jsonify({
        "message": "Hi there! I'm EVA, your friendly virtual assistant. I'm here to help you learn about our website and how to work with it effectively.",
        "options": [
            {"id": 1, "text": "About the Website's System and Vision"},
            {"id": 2, "text": "Working with the Website"},
            {"id": 3, "text": "Something Else"}
        ]
    })

# Function to handle user's choice
def handle_user_choice(choice):
    if choice == 1:
        return jsonify({
            "message": "Our website is designed to be user-friendly and provide a smooth experience. We're constantly working to improve its functionality and features. Here are some specific aspects you might be interested in:",
            "options": [
                {"id": 1, "text": "Core functionalities of the website"},
                {"id": 2, "text": "Our vision for the future"}
            ]
        })
    elif choice == 2:
        return jsonify({
            "message": "We understand you might have questions about using the website. Here are some common areas where we can help:",
            "options": [
                {"id": 1, "text": "Getting started with the website"},
                {"id": 2, "text": "Specific features and how to use them"}
            ]
        })
    elif choice == 3:
        return jsonify({"message": "Let me know if you have any specific questions about the website or a different topic altogether. I'll do my best to assist you."})
    else:
        return jsonify({"error": "Invalid choice"})

# Function to provide follow-up options
def provide_follow_up():
    return jsonify({
        "message": "What would you like to do next?",
        "options": [
            {"id": 1, "text": "Okay, I understood."},
            {"id": 2, "text": "Request a Call (for more complex inquiries)"}
        ]
    })

@app.route('/', methods=['GET'])
def index():
    return eva_introduction()

@app.route('/handle_choice', methods=['POST'])
def handle_choice():
    data = request.get_json()
    choice = int(data['choice'])
    return handle_user_choice(choice)

@app.route('/follow_up', methods=['GET'])
def follow_up():
    return provide_follow_up()

if __name__ == '__main__':
    app.run(debug=True)
