# 🎬 Advanced Movie Recommendation System

A full-stack intelligent recommendation system that delivers personalized movie suggestions using **Cold Start, Content-Based Filtering, and Hybrid Recommendation techniques**, built with a scalable backend and an interactive Streamlit frontend.

---

## 🚀 Project Overview

This system simulates a real-world recommendation engine (similar to Netflix/Amazon) by adapting to user behavior over time.

It handles:

* New users with no history (**Cold Start**)
* Users with limited interactions (**Content-Based Filtering**)
* Active users with rich behavior (**Hybrid Recommendation**)

The system continuously improves as users interact through **search, clicks, watchlist, and ratings**.

---

## 🧠 Key Features

### 🔹 Intelligent Recommendation Pipeline

* **Cold Start** → Based on demographics (age, gender, language)
* **Content-Based Filtering** → Uses movie metadata similarity (TF-IDF + Cosine Similarity)
* **Hybrid Model** → Combines content relevance with popularity & ratings

---

### 🔹 Dynamic User Interaction Tracking

* Tracks:

  * Search behavior
  * Movie clicks
  * Watchlist additions
  * Ratings
* Stores all interactions in a database for future personalization

---

### 🔹 Interactive UI (Streamlit)

* User authentication (Login/Signup)
* Personalized recommendations on login
* Search functionality with smart matching
* Clickable movie titles → detailed movie view
* Movie detail page includes:

  * Cast
  * Director
  * Genres
  * Overview
  * Rating system
  * Watchlist feature

---

### 🔹 Real-Time Personalization

* Recommendations evolve based on:

  * User interactions
  * Watchlist behavior
  * Ratings

---

## 🏗️ System Architecture

```text id="arch1"
User → Streamlit UI
        ↓
Backend (Python + SQLite)
        ↓
Recommendation Engine
   ├── Cold Start
   ├── Content-Based Model
   └── Hybrid Model
        ↓
Database (Users, Movies, Ratings, Interactions)
```

---

## 🗂️ Project Structure

```text id="arch2"
├── backend/
│   ├── auth.py              # User authentication
│   ├── db.py                # Database connection
│   ├── interactions.py      # User activity tracking
│   ├── ratings.py           # Ratings logic
│   ├── movie_search.py      # Search functionality
│   └── movie_details.py     # Movie metadata retrieval
│
├── recommender/
│   ├── cold_start.py        # Cold start recommendations
│   ├── content_model.py     # Content-based filtering
│   └── hybrid_model.py      # Hybrid recommendation logic
│
├── frontend/
│   └── app.py               # Streamlit application
│
├── data/
│   └── processed/           # Preprocessed datasets
│
├── evaluation/
│   └── evaluate.py          # Evaluation logic (future use)
│
└── README.md
```

---

## ⚙️ Technologies Used

* **Python**
* **Streamlit** (Frontend UI)
* **SQLite** (Database)
* **Pandas, NumPy**
* **Scikit-learn**

  * TF-IDF Vectorization
  * Cosine Similarity
* **Git & GitHub**

---

## 🧪 How It Works

1. User logs in / signs up
2. System checks interaction history
3. Based on user stage:

   * New → Cold Start
   * Few interactions → Content-Based
   * Active → Hybrid
4. User interacts (search, click, rate, watchlist)
5. Data stored → recommendations improve over time

---

## ▶️ Running the Project

```bash id="run1"
git clone https://github.com/your-username/your-repo.git
cd your-repo

pip install -r requirements.txt

streamlit run frontend/app.py
```

---

## 📌 Future Improvements

* Add evaluation metrics:

  * Precision@K
  * Recall@K
  * NDCG
* Track real-world metrics:

  * Click Through Rate (CTR)
  * Watchlist Rate
  * User Engagement
* Poster-based UI (Netflix-style cards)
* Collaborative Filtering using real user ratings
* Deep Learning-based recommendation models
* Real-time analytics dashboard
* Cloud deployment (Streamlit Cloud / AWS)

---

## 💡 Key Learnings

* Built a **multi-stage recommendation system**
* Designed a system that adapts based on user behavior
* Implemented **interaction-driven personalization**
* Applied **machine learning concepts in a real-world system**
* Developed a full-stack ML application with scalable architecture

---
