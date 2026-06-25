# Docker Notes App

A simple Notes Application built with Flask, PostgreSQL, Docker, and Docker Compose.

This project demonstrates how multiple containers communicate using Docker networking while storing persistent data using Docker volumes.

## Features

* Create and save notes
* Store notes in PostgreSQL database
* Responsive web interface
* Persistent storage using Docker Volumes
* Containerized application using Docker
* Multi-container deployment using Docker Compose

---

## Tech Stack

### Backend

* Flask
* Flask-SQLAlchemy
* PostgreSQL

### DevOps

* Docker
* Docker Compose
* Docker Networking
* Docker Volumes

---

## Project Architecture

```text
User Browser
      |
      v
Flask Container
      |
      v
PostgreSQL Container
      |
      v
Docker Volume
```

---

## Project Structure

```text
flask-notes-app/

├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Docker Concepts Used

### Docker Image

The Flask application is packaged into a Docker image using a Dockerfile.

### Docker Container

The Flask application and PostgreSQL database run as separate containers.

### Docker Networking

Docker Compose automatically creates a network that allows containers to communicate using service names.

Example:

```python
postgresql://admin:password@db:5432/notesdb
```

The Flask container connects to PostgreSQL using the service name `db` instead of an IP address.

### Docker Volumes

A Docker volume is used to persist PostgreSQL data.

```yaml
volumes:
  - postgres_data:/var/lib/postgresql/data
```

This ensures notes remain available even if the database container is recreated.

---

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd flask-notes-app
```

### Build and Start Containers

```bash
docker compose up --build -d
```

### Verify Running Containers

```bash
docker ps
```

Expected output:

```text
flask-app
postgres-db
```

---

## Access Application

Open:

```text
http://localhost:5000
```

Or:

```text
http://SERVER-IP:5000
```

---

## Useful Docker Commands

### View Running Containers

```bash
docker ps
```

### View Logs

```bash
docker logs flask-app
```

### Enter Flask Container

```bash
docker exec -it flask-app bash
```

### Enter PostgreSQL Container

```bash
docker exec -it postgres-db psql -U admin -d notesdb
```

### Stop Containers

```bash
docker compose down
```

### Remove Containers and Volumes

```bash
docker compose down -v
```

---

## Database Verification

Connect to PostgreSQL:

```bash
docker exec -it postgres-db psql -U admin -d notesdb
```

Show tables:

```sql
\dt
```

Display stored notes:

```sql
SELECT * FROM note;
```

---

## Troubleshooting

### Database Connection Error

Check database container:

```bash
docker ps
```

Start database if stopped:

```bash
docker start postgres-db
```

---

### Application Not Accessible

Verify port mapping:

```bash
docker ps
```

Expected:

```text
0.0.0.0:5000->5000/tcp
```

---

### Check Container Logs

```bash
docker logs flask-app
```

```bash
docker logs postgres-db
```

---

## Future Improvements

* Edit Notes
* Delete Notes
* Bootstrap UI
* Nginx Reverse Proxy
* Environment Variables using .env
* Health Checks
* CI/CD with GitHub Actions
* Automated PostgreSQL Backups

---

## Learning Outcomes

Through this project I learned:

* Docker Images
* Docker Containers
* Docker Networking
* Docker DNS
* Docker Volumes
* Docker Compose
* PostgreSQL Integration
* Multi-Container Application Deployment

---

## Author

Vaishnav Chavan

Aspiring DevOps Engineer | Cloud & Infrastructure Enthusiast
