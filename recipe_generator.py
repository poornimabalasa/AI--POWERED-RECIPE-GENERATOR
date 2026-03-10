# recipe_generator.py
import random
import json
from typing import List, Dict, Set, Optional

class RecipeGenerator:
    def __init__(self):
        self.recipes = self._initialize_recipes()
        self.dietary_restrictions = {
            'vegan': ['meat', 'dairy', 'eggs', 'honey', 'chicken', 'beef', 'fish', 'pork'],
            'vegetarian': ['meat', 'fish', 'chicken', 'beef', 'pork'],
            'gluten_free': ['wheat', 'flour', 'pasta', 'bread', 'cracker'],
            'keto': ['sugar', 'rice', 'potato', 'pasta', 'bread', 'corn'],
            'low_carb': ['sugar', 'rice', 'pasta', 'bread', 'potato']
        }
    
    def _initialize_recipes(self):
        """Initialize recipe database"""
        return [
            {
                "id": 1,
                "name": "Classic Pasta Carbonara",
                "ingredients": ["pasta", "eggs", "bacon", "parmesan", "black pepper"],
                "instructions": "1. Boil pasta in salted water\n2. Fry bacon until crispy\n3. Beat eggs with parmesan\n4. Combine hot pasta with egg mixture and bacon\n5. Season with black pepper",
                "prep_time": 20,
                "difficulty": "Medium",
                "cuisine": "Italian",
                "image": "🍝",
                "dietary": [],
                "tags": ["italian", "comfort"]
            },
            {
                "id": 2,
                "name": "Vegetable Stir Fry",
                "ingredients": ["rice", "broccoli", "carrots", "soy sauce", "garlic", "ginger", "bell peppers"],
                "instructions": "1. Cook rice according to package\n2. Chop all vegetables\n3. Heat oil in wok, add garlic and ginger\n4. Stir-fry vegetables for 5-7 minutes\n5. Add soy sauce and serve over rice",
                "prep_time": 25,
                "difficulty": "Easy",
                "cuisine": "Asian",
                "image": "🥘",
                "dietary": ["vegan", "vegetarian"],
                "tags": ["asian", "healthy"]
            },
            {
                "id": 3,
                "name": "Grilled Chicken Salad",
                "ingredients": ["chicken breast", "lettuce", "tomatoes", "cucumber", "olive oil", "lemon", "salt", "pepper"],
                "instructions": "1. Season chicken with salt, pepper, and olive oil\n2. Grill chicken for 6-8 minutes per side\n3. Chop vegetables\n4. Slice chicken and arrange over vegetables\n5. Drizzle with lemon and olive oil",
                "prep_time": 20,
                "difficulty": "Easy",
                "cuisine": "Mediterranean",
                "image": "🥗",
                "dietary": ["gluten_free"],
                "tags": ["healthy", "low-carb"]
            },
            {
                "id": 4,
                "name": "Vegan Buddha Bowl",
                "ingredients": ["quinoa", "chickpeas", "avocado", "spinach", "sweet potato", "tahini", "lemon"],
                "instructions": "1. Cook quinoa\n2. Roast sweet potato cubes at 400°F for 20 mins\n3. Rinse chickpeas\n4. Assemble bowl with spinach, quinoa, roasted sweet potato, chickpeas, and avocado\n5. Drizzle with tahini and lemon",
                "prep_time": 30,
                "difficulty": "Easy",
                "cuisine": "Healthy",
                "image": "🥙",
                "dietary": ["vegan", "gluten_free"],
                "tags": ["healthy", "bowl"]
            },
            {
                "id": 5,
                "name": "Keto Avocado Egg Bowl",
                "ingredients": ["eggs", "avocado", "bacon", "spinach", "salt", "pepper", "hot sauce"],
                "instructions": "1. Fry bacon until crispy, crumble\n2. Fry eggs to preference\n3. Slice avocado\n4. Arrange spinach in bowl, top with avocado, eggs, bacon\n5. Season with salt, pepper, hot sauce",
                "prep_time": 15,
                "difficulty": "Easy",
                "cuisine": "American",
                "image": "🥑",
                "dietary": ["keto", "low_carb", "gluten_free"],
                "tags": ["breakfast", "low-carb"]
            },
            {
                "id": 6,
                "name": "Mediterranean Quinoa Bowl",
                "ingredients": ["quinoa", "cucumber", "tomatoes", "olives", "feta", "red onion", "olive oil", "oregano"],
                "instructions": "1. Cook quinoa and let cool\n2. Chop cucumber, tomatoes, red onion\n3. Combine quinoa with vegetables\n4. Add olives and crumbled feta\n5. Dress with olive oil and oregano",
                "prep_time": 25,
                "difficulty": "Easy",
                "cuisine": "Mediterranean",
                "image": "🥗",
                "dietary": ["vegetarian"],
                "tags": ["mediterranean", "healthy"]
            },
            {
                "id": 7,
                "name": "Spicy Thai Curry",
                "ingredients": ["coconut milk", "chicken", "bell peppers", "bamboo shoots", "thai basil", "curry paste", "fish sauce"],
                "instructions": "1. Heat curry paste in oil until fragrant\n2. Add chicken and cook until browned\n3. Add coconut milk and simmer\n4. Add vegetables and cook 10 minutes\n5. Stir in fish sauce and basil",
                "prep_time": 35,
                "difficulty": "Medium",
                "cuisine": "Thai",
                "image": "🍛",
                "dietary": ["gluten_free"],
                "tags": ["thai", "spicy", "curry"]
            },
            {
                "id": 8,
                "name": "Hearty Lentil Soup",
                "ingredients": ["lentils", "carrots", "celery", "onion", "garlic", "vegetable broth", "tomatoes", "cumin"],
                "instructions": "1. Sauté onion, carrot, celery in olive oil\n2. Add garlic and cumin, cook 1 minute\n3. Add lentils, broth, and tomatoes\n4. Simmer 30 minutes until lentils tender\n5. Season with salt and pepper",
                "prep_time": 45,
                "difficulty": "Easy",
                "cuisine": "International",
                "image": "🥣",
                "dietary": ["vegan", "gluten_free"],
                "tags": ["soup", "hearty"]
            }
        ]
    
    def check_dietary(self, recipe, preferences):
        """Check if recipe matches dietary preferences"""
        if not preferences:
            return True
        
        recipe_text = ' '.join(recipe['ingredients']).lower()
        
        for pref in preferences:
            if pref in self.dietary_restrictions:
                for item in self.dietary_restrictions[pref]:
                    if item.lower() in recipe_text:
                        return False
        
        # Check dietary tags
        recipe_dietary = recipe.get('dietary', [])
        for pref in preferences:
            if pref in ['vegan', 'vegetarian', 'gluten_free', 'keto', 'low_carb']:
                if pref not in recipe_dietary and pref != 'low_carb':  # low_carb is flexible
                    return False
        
        return True
    
    def generate_recipes(self, ingredients, preferences=None):
        """Generate recipes based on ingredients"""
        if preferences is None:
            preferences = []
        
        # Clean inputs
        ingredients = [i.lower().strip() for i in ingredients if i.strip()]
        preferences = [p.lower().strip() for p in preferences if p.strip()]
        
        matches = []
        
        for recipe in self.recipes:
            # Check dietary restrictions
            if not self.check_dietary(recipe, preferences):
                continue
            
            # Find matching ingredients
            recipe_ingredients = [i.lower() for i in recipe['ingredients']]
            matching = set(ingredients) & set(recipe_ingredients)
            
            # Calculate match percentage
            if matching:
                percentage = (len(matching) / len(recipe_ingredients)) * 100
                
                # Boost percentage if dietary preferences match
                if preferences:
                    recipe_dietary = set(recipe.get('dietary', []))
                    pref_set = set(preferences)
                    if recipe_dietary & pref_set:
                        percentage += 10
                
                if percentage >= 30:  # Lower threshold to show more recipes
                    recipe_copy = recipe.copy()
                    recipe_copy['match_percentage'] = round(min(percentage, 100), 1)
                    recipe_copy['matching_ingredients'] = list(matching)
                    recipe_copy['missing_ingredients'] = list(set(recipe_ingredients) - set(ingredients))
                    matches.append(recipe_copy)
        
        # Sort by best match
        matches.sort(key=lambda x: x['match_percentage'], reverse=True)
        return matches[:6]  # Return top 6 recipes
    
    def get_all_cuisines(self):
        """Get all unique cuisines"""
        cuisines = set()
        for recipe in self.recipes:
            cuisines.add(recipe.get('cuisine', 'Other'))
        return sorted(list(cuisines))
    
    def get_random_recipe(self):
        """Get a random recipe for inspiration"""
        return random.choice(self.recipes)

    def generate_custom_recipe(self, ingredients, preferences=None):
        """Generate a custom recipe based on ingredients"""
        if preferences is None:
            preferences = []
        
        # Simple custom recipe generation
        main_ingredient = ingredients[0] if ingredients else "vegetables"
        
        # Determine cuisine based on ingredients
        cuisine = "International"
        if any(i in ['pasta', 'tomato', 'basil'] for i in ingredients):
            cuisine = "Italian"
        elif any(i in ['rice', 'soy', 'ginger'] for i in ingredients):
            cuisine = "Asian"
        elif any(i in ['avocado', 'beans', 'corn'] for i in ingredients):
            cuisine = "Mexican"
        
        return {
            "name": f"Custom {cuisine} {main_ingredient.title()} Creation",
            "ingredients": ingredients,
            "instructions": f"1. Prepare all ingredients: {', '.join(ingredients)}\n2. Heat oil in a large pan\n3. Add {main_ingredient} and cook until done\n4. Add remaining ingredients\n5. Season to taste\n6. Cook for 10-15 minutes\n7. Serve hot and enjoy!",
            "prep_time": len(ingredients) * 5 + 10,
            "difficulty": "Easy",
            "cuisine": cuisine,
            "image": "👨‍🍳",
            "dietary": preferences,
            "match_percentage": 100,
            "custom": True
        }