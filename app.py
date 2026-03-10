# app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from recipe_generator import RecipeGenerator
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize recipe generator
generator = RecipeGenerator()

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate_recipes():
    """API endpoint to generate recipes"""
    try:
        data = request.json
        ingredients = data.get('ingredients', [])
        preferences = data.get('preferences', [])
        
        # Generate recipes
        recipes = generator.generate_recipes(ingredients, preferences)
        
        return jsonify({
            'success': True,
            'recipes': recipes,
            'count': len(recipes)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/custom', methods=['POST'])
def generate_custom():
    """Generate a custom recipe"""
    try:
        data = request.json
        ingredients = data.get('ingredients', [])
        preferences = data.get('preferences', [])
        
        recipe = generator.generate_custom_recipe(ingredients, preferences)
        
        return jsonify({
            'success': True,
            'recipe': recipe
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/random', methods=['GET'])
def random_recipe():
    """Get a random recipe"""
    try:
        recipe = generator.get_random_recipe()
        return jsonify({
            'success': True,
            'recipe': recipe
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/cuisines', methods=['GET'])
def get_cuisines():
    """Get all available cuisines"""
    try:
        cuisines = generator.get_all_cuisines()
        return jsonify({
            'success': True,
            'cuisines': cuisines
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 AI RECIPE GENERATOR WEB APP")
    print("="*60)
    print("📱 Local URL: http://127.0.0.1:5000")
    print("🌐 Network URL: http://localhost:5000")
    print("="*60)
    print("\n✨ Press CTRL+C to stop the server\n")
    app.run(debug=True, host='0.0.0.0', port=5000)