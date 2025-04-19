# 🛍️ FastAPI Social API example

## 🚀 Features

- 🔐 Authentication & Registration
- 👤 User's profile
- 🙋‍♂️ Followers & Following system
- 📱 Functionality with posts (create, like, unlike, delete, update)
- ✉️ Functionality with comments (create, like, unlike, delete)
- 🔔 Simple notification system
- 🔁 Password reset via email
- ⛔ Simple reporting system
- ▶️ Bookmarks

## 🧱 Tech Stack

- Python 3.11+
- FastAPI
- Pydantic
- SQLAlchemy (using PostgreSQL)
- JWT
- aiohttp
- Redis
- Kafka
- Docker

## 📦 Installation

Clone repo:
```bash
git clone https://github.com/linwexEU/gab.git
```

Docker:
```bash
cd src

docker compose build 
docker compose up -d
```

Run consumers for kafka: 
```bash
docker compose exec -it gab bash 

python3 -m broker.kafka.consumer email_topic
python3 -m broker.kafka.consumer notification_topic
```


