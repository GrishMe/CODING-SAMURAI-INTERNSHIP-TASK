Stock & Crypto Price Prediction App
A Machine Learning + Deep Learning project for forecasting stock and cryptocurrency prices, complete with a Streamlit web application for interactive predictions.

🚀 Overview
This project predicts future stock and cryptocurrency prices using a combination of:
- Random Forest Regressor (Machine Learning)
- LSTM Neural Network (Deep Learning)
It includes:
- A Jupyter Notebook for data exploration, model training, and evaluation
- A Streamlit web app for real‑time predictions
- A Python backend (main.py) for model loading and inference
- A clean project structure suitable for portfolios and internships
This project was developed as part of the Coding Samurai Internship.

🧠 Features
- 📊 Stock price prediction
- 🪙 Crypto price prediction
- 🔍 Data preprocessing & visualization
- 🤖 Random Forest model
- 🧬 LSTM deep learning model
- 🌐 Streamlit web interface
- 📁 Organized project structure
- 📈 Interactive charts and predictions

🗂️ Project Structure
Stock_Prediction/
│
├── main.py
├── streamlit_app.py
├── stock_and_crypto_prediction.ipynb
├── requirements.txt
└── README.md


main.py
Handles model loading, preprocessing, and prediction logic.

streamlit_app.py
Interactive web app for users to input a stock/crypto symbol and view predictions.

stock_and_crypto_prediction.ipynb

Notebook containing:

- Data loading
- Cleaning & preprocessing
- Exploratory Data Analysis (EDA)
- Model training (Random Forest + LSTM)
- Evaluation metrics
- Visualization
  
requirements.txt
List of all Python dependencies needed to run the project.

🛠️ Tech Stack
- Python 3.x
- Pandas, NumPy
- Scikit‑learn
- TensorFlow / Keras
- Matplotlib, Seaborn
- Streamlit
- YFinance / Alpha Vantage (optional)

📥 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/<your-username>/Coding-Samurai.git


2️⃣ Navigate to the project folder
cd Coding-Samurai/Stock_Prediction


3️⃣ Install dependencies
pip install -r requirements.txt



▶️ Running the Streamlit App
Run the following command:
streamlit run streamlit_app.py


This will open the app in your browser.

📘 How It Works

1. Data Collection
Historical stock/crypto data is fetched using APIs such as Yahoo Finance.
2. Preprocessing
- Handling missing values
- Scaling
- Creating sequences for LSTM
- Train‑test split
3. Model Training
Two models are trained:
🔹 Random Forest
- Fast
- Good baseline
- Handles non‑linear patterns
🔹 LSTM
- Captures long‑term dependencies
- Ideal for time‑series forecasting
4. Prediction
The Streamlit app loads the trained model and predicts future prices based on recent data.

📊 Results
The notebook includes:
- Loss curves
- Actual vs Predicted charts
- Model comparison
- Performance metrics (MAE, RMSE, etc.)

🎥 Demo Video
A demonstration video is included in the repository (uploaded separately due to size limits).

🔮 Future Improvements
- Add Prophet model for comparison
- Deploy Streamlit app on cloud (Streamlit Cloud / Render)
- Add more cryptocurrencies
- Add sentiment analysis using news or tweets
- Improve UI/UX of the web app

👩‍💻 Author
Grishma
MSc Cybersecurity | Coding Samurai Intern
Focused on AI, ML, and practical project development.

📜 License
This project is for educational and internship purposes.


