import os
import streamlit as st
from groq import Groq
import requests
from dotenv import load_dotenv

# Groq API setup
client = Groq(api_key="your groq api")

# Title and Introduction
st.title("Recipe Recommendation System")
st.write("Welcome to your personalized recipe assistant. Enter your preferences, and we'll recommend recipes with calorie details.")

# User Input Section
st.header("Find a Recipe")
ingredients = st.text_input("Enter ingredients you have (comma-separated):", placeholder="e.g., tomato, eggs, cheese")
max_calories = st.number_input("Maximum calorie limit:", min_value=50, step=50, value=1000)
dietary_preference = st.selectbox("Select dietary preference:", options=["None", "Vegan", "Vegetarian", "Keto", "Gluten-Free"])

# Chatbot for Personalized Assistance
st.header("Chat with the Recipe Assistant")
user_query = st.text_input("Ask for a recipe or get advice:", placeholder="e.g., Suggest a low-carb breakfast recipe.")

if st.button("Ask Assistant"):
    if user_query:
        # Query Groq API using LLM
        chat_response = client.chat.completions.create(
            messages=[{"role": "user", "content": user_query}],
            model="llama3-8b-8192",
        )
        st.write("Assistant Response:")
        st.success(chat_response.choices[0].message.content)
    else:
        st.warning("Please enter a query for the assistant.")

# Fetch Recipe Recommendations


# Directly assign the API key (not secure, only for testing purposes)
spoonacular_api_key = "your spoonacular api key"  # Replace with your actual API key

if st.button("Get Recipe Recommendations"):
    if ingredients:
        try:
            # Check if API key exists
            if not spoonacular_api_key:
                st.error("Spoonacular API key is missing. Please provide the API key.")
            else:
                api_url = f"https://api.spoonacular.com/recipes/findByIngredients"
                params = {
                    "ingredients": ingredients,
                    "number": 10,
                    "ranking": 1-3,
                    "apiKey": spoonacular_api_key,
                }

                response = requests.get(api_url, params=params)

                if response.status_code == 200:
                    recipes = response.json()
                    if recipes:
                        st.subheader("Recommended Recipes")
                        for recipe in recipes:
                            st.write(f"**{recipe['title']}**")
                            st.image(recipe.get("image"), width=300)
                            st.write(f"Ingredients: {', '.join([i['name'] for i in recipe.get('missedIngredients', [])])}")
                    else:
                        st.warning("No recipes found for the given ingredients.")
                else:
                    st.error(f"Failed to fetch recipes. API returned status: {response.status_code}. Error: {response.text}")
        except Exception as e:
            st.error(f"Error fetching recipes: {str(e)}")
    else:
        st.warning("Please enter ingredients to get recipe recommendations.")


# Calorie Calculation using Groq API
if st.button("Calculate Calories"):
    if ingredients:
        try:
            calorie_response = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": f"Calculate the calories for ingredients: {ingredients}",
                }],
                model="llama3-8b-8192",
            )
            st.subheader("Calorie Calculation")
            st.success(calorie_response.choices[0].message.content)
        except Exception as e:
            st.error(f"Error calculating calories: {str(e)}")
    else:
        st.warning("Please enter ingredients to calculate calories.")

# Display Footer
st.write("Thank you for using the Recipe Recommendation System! 🍽️")
