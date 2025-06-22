from flask import Flask, request, jsonify
from flask_cors import CORS
from skincare import wiki_agent, crawl_agent, search_agent, router

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Skincare Agent API is running."

@app.route("/ask", methods = ["POST"])
def ask_agent():
    user_input = request.json.get("query", "")
    if not user_input:
        return jsonify({"error": "Query is required,"}), 400
    
    try:
        response = router.run(user_input)
        
        if hasattr(response, "content"):
            return jsonify({"response": str(response.content)})
        else:
            return jsonify({"error": "No valid content received"}), 500
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)