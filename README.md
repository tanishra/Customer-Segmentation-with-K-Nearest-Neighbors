# 🛍️ Customer-Segmentation-with-K-Nearest-Neighbors


This project applies the **K-Nearest Neighbors (KNN)** classification algorithm to segment mall customers into value-based groups (Low, Medium, High). A **Streamlit web app** is included for real-time prediction based on user inputs like age, gender, income, and spending score.

---

## 📌 Project Highlights

- ✅ Supervised learning with **KNN**
- ✅ Hyperparameter tuning using **GridSearchCV**
- ✅ Feature preprocessing with **Label Encoding** and **StandardScaler**
- ✅ Interactive UI built using **Streamlit**
- ✅ Dataset: Mall Customers Dataset (publicly available)

---

## 📊 Dataset Information

**Dataset Name:** Mall Customers  
**Source:** Kaggle  
**Link:** [https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)

**Columns:**

| Column Name     | Description                                |
|------------------|--------------------------------------------|
| `CustomerID`     | Unique customer ID                         |
| `Gender`         | Gender of customer (Male/Female)           |
| `Age`            | Age of the customer                        |
| `Annual Income`  | Income in thousands of dollars             |
| `Spending Score` | Spending behavior score (1–100)            |

---

## 🧪 Data Preprocessing

1. **Dropped `CustomerID`** as it’s not a feature.
2. **Encoded `Gender`** using LabelEncoder: Female → 0, Male → 1
3. **Created labels (`Segment`)** based on heuristics:
   - Low-Value (0): Low income & low spending
   - Medium-Value (1): Mid-range profiles
   - High-Value (2): High income & high spending
4. **Features Standardized** using `StandardScaler`.

---

## 🧠 Model Building

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Hyperparameter Tuning:** `GridSearchCV` on `k` (1 to 20)
- **Evaluation Metrics:**
  - Accuracy
  - Classification Report
  - Confusion Matrix

---

## 💻 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Customer-Segmentation-With-K-Nearest-Neighbors.git
cd Customer-Segmentation-with-K-Nearest-Neighbors
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

### 3. Install dependencies
```bash
pip install -r streamlit_app/requirements.txt
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

---

# 🤝 Contributions
Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.