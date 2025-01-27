from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load dish dataset
with open('dishes.json', 'r') as f:
    dishes= json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recipes")
def recipe_page():
    return render_template("recipe.html", dishes=dishes)

@app.route("/dish/<dish_name>")
def dish_detail(dish_name):
    dish = next((dish for dish in dishes if dish["name"].lower() == dish_name.lower()), None)
    if dish:
        return jsonify(dish)
    else:
        return jsonify({"error": "Dish not found"}), 404

@app.route("/meal-plan")
def meal_plan():
    return render_template("meal_plan.html")

@app.route("/Fast")
def Fast():
    return render_template("Fast.html")

if __name__ == "__main__":
    app.run(debug=True)