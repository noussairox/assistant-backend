from flask import Flask, request, jsonify
from flask_cors import CORS
from personality import analyze_personality
from gpt_advice import get_gpt_advice
from questions import questions

app = Flask(__name__)
CORS(app)

@app.route('/api/advice', methods=['POST'])
def advice():
    data = request.json
    answers = data.get('answers', [])
    topic = data.get('topic', 'développement personnel')

    personality = analyze_personality(" ".join(answers))
    advice = get_gpt_advice(personality, topic)
    return jsonify({
        'personality': personality,
        'advice': advice
    })

@app.route('/api/custom', methods=['POST'])
def custom_advice():
    data = request.json
    personality = data.get('personality')
    user_prompt = data.get('prompt')

    full_prompt = f"""
    Je suis un coach pour un utilisateur de type MBTI {personality}.
    L'utilisateur me demande : {user_prompt}.
    Donne une réponse adaptée à ce type de personnalité.
    """
    advice = get_gpt_advice(personality, full_prompt)
    return jsonify({'response': advice})

@app.route('/api/questions', methods=['GET'])
def get_questions():
    return jsonify(questions)

if __name__ == '__main__':
    # Écoute sur localhost:5000 en debug
    app.run(host='0.0.0.0', port=5000, debug=True)
