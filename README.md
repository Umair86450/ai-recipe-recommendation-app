# 🧠 AI Recipe Recommendation App 🍽️

Welcome to the **AI Recipe Recommendation App**, a smart cooking assistant built using **Streamlit**, **Groq's LLM**, and the **Spoonacular API**. This app helps you:

- Get personalized recipe suggestions based on ingredients.
- Estimate calories using AI.
- Chat with a smart assistant for cooking advice.

---

## 🚀 Features

- 🔍 **Search Recipes** by ingredients
- 🧮 **Estimate Calories** using AI
- 🤖 **Chatbot Assistant** for meal ideas
- ⚙️ Powered by **Groq LLM (LLaMA3)** and **Spoonacular API**

---

## 🛠️ Tools & Technologies Used

| Tool / Tech        | Purpose                                   |
|--------------------|-------------------------------------------|
| **Streamlit**      | Frontend for the web interface            |
| **Groq API**       | Access to LLaMA3 LLM for AI responses     |
| **Spoonacular API**| To fetch real recipe data & images        |
| **Python**         | Core programming language                 |
| **Requests**       | API calls to Spoonacular                  |
| **dotenv**         | Load secret API keys securely             |

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/ai-recipe-recommendation-app.git
cd ai-recipe-recommendation-app
````

### 2. Create and Activate Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

In the root directory, create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key_here
SPOONACULAR_API_KEY=your_spoonacular_api_key_here
```

---

## 🔑 How to Get API Keys

### ▶️ **Groq API Key**

1. Visit: [https://console.groq.com/keys](https://console.groq.com/keys)
2. Sign in and generate an API key.

### ▶️ **Spoonacular API Key**

1. Go to: [https://spoonacular.com/food-api](https://spoonacular.com/food-api)
2. Sign up and get a free API key.

---

## 💡 How It Works

### 🔹 Recipe Recommendation

* You enter ingredients like `eggs, tomatoes, cheese`.
* The app sends a request to **Spoonacular API**.
* It returns matching recipes with:

  * Title
  * Image
  * Missing ingredients

### 🔹 Calorie Calculation

* You click **"Calculate Calories"**.
* A prompt is sent to **Groq's LLaMA3 model** to estimate calories from the ingredients.
* It returns a breakdown or total calories.

### 🔹 AI Chat Assistant

* You ask questions like:

  * *"Suggest a high-protein vegan lunch"*
* The prompt goes to **Groq LLM**, which gives personalized suggestions.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the local URL (usually `http://localhost:8501`) in your browser.
