# 🌦️ Weather Data ETL Pipeline Project

This project builds a complete end-to-end data pipeline that fetches real-time weather data, loads it into a PostgreSQL database, transforms it using dbt, and visualizes insights using Apache Superset. The entire workflow is orchestrated using Apache Airflow and containerized with Docker for easy deployment and reproducibility.

---

## 🚀 Tech Stack Used

- **Python** – for data fetching and ingestion logic  
- **PostgreSQL** – as the data warehouse  
- **Apache Airflow** – to orchestrate the ETL pipeline  
- **dbt (Data Build Tool)** – for transforming and cleaning data  
- **Apache Superset** – for interactive dashboards and visualizations  
- **Docker** – to containerize all services and enable isolated, consistent environments  

---

## 🛠️ Pipeline Architecture


<img width="900" height="1100" alt="image" src="https://github.com/user-attachments/assets/6bcaa030-97f4-4a25-acdf-a7e71080482e" />


---

## ⏱️ Airflow Scheduling & Orchestration

- **Airflow** schedules and triggers:
  - A **Python script** to fetch and insert weather data into PostgreSQL.
  - A **Dockerized dbt run** to transform the raw weather data.
- **Superset** connects directly to the transformed PostgreSQL tables to create dashboards.
- All services (Postgres, Airflow, dbt, Superset) are defined and orchestrated using **Docker Compose**.

---

## ⚠️ Challenges Faced

- Understanding the role and setup of **volumes** in Docker for data persistence and file sharing.
- Correctly referencing **Airflow** and **dbt** directories inside containers (`/opt/airflow`, `/usr/app`, etc.).
- Learning to write effective **dbt models** using Jinja templating.
- Handling environment-related compatibility issues when using **Airflow inside WSL** (Windows Subsystem for Linux).

---

## ✅ Highlights

- Real-time weather data ingestion every **minute** using Airflow DAGs.
- Modular, containerized architecture for **ingestion**, **transformation**, and **visualization**.
- Reproducible and scalable setup ideal for both **learning** and **production**.
- **Interactive dashboards** built using Superset for quick insights and analytics.

---

## 📂 Project Structure

- `api-request/` – Python script to fetch and load weather data.
- `airflowww/dags/` – Airflow DAGs for orchestration.
- `dbt/my_project/` – dbt models and configurations for data transformation.
- `superset/` – Superset setup scripts and configs.
- `docker-compose.yaml` – Defines all containerized services.

---

## 🧠 Future Improvements

- Integrate **CI/CD** for automated deployment.
- Add **alerting/reporting** for extreme weather conditions.
- Store **versioned dashboards** in Superset for historical analytics.
