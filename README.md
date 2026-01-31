# BD Taka Detection API (Dockerized)

A **FastAPI-based object detection API** for detecting **Bangladeshi Taka notes** using a trained model. The project is fully **Dockerized** for easy setup and deployment.

---

## 📁 Project Structure

```
bd_taka_detection_api_and_docker/
├── app/
│   ├── main.py        # FastAPI entry point
│   ├── model.py       # Model loading & inference logic
│   ├── schma.py       # Pydantic schemas
│   └── images/        # Sample / test images
├── model/             # Trained model files
├── Dockerfile         # Docker build configuration
├── docker-compose.yml # Multi-container setup
├── requirements.txt   # Python dependencies
├── .gitignore
└── README.md
```

---

## ✨ Features

* 💵 Detects Bangladeshi currency notes
* ⚡ FastAPI-based REST API
* 🧠 Modular model loading & inference
* 🐳 Fully Dockerized (Docker & Docker Compose)
* 📦 Clean project structure

---

## 📥 Installation (Local)

1. **Clone the repository**

```
git clone https://github.com/codebysajed/bd_taka_detection_api_and_docker.git
cd bd_taka_detection_api_and_docker
```

2. **Create virtual environment (optional)**

```
python -m venv venv
venv\\Scripts\\activate   # Windows
# source venv/bin/activate # Linux/Mac
```

3. **Install dependencies**

```
pip install -r requirements.txt
```

4. **Run the API**

```
uvicorn app.main:app --reload
```

---

## 🐳 Run with Docker

### Build & run using Docker Compose

```
docker-compose up --build
```

API will be available at:

```
http://localhost:8000
```

---

## 📡 API Usage

* **POST** `/predict`
* Input: Image file (`.jpg`, `.png`, `.jpeg`)
* Output: Detected Taka note class & confidence

---

## 📌 Notes 

This project is designed for detecting Bangladeshi currency notes

Docker makes it easy to run on any machine without environment issues

Being an API, it can be easily integrated with frontend or mobile applications
---

Made with ❤️ for real-world ML deployment
