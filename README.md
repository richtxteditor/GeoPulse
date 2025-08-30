# GeoPulse: A Full-Stack Global Economic Impact Analysis Application

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Powered-blue)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**This project transforms a data analysis notebook into a full-stack, interactive web application for analyzing the economic effects of global events on financial markets.**

It leverages data from the World Bank, SIPRI, and Bloomberg Intelligence, served via a robust backend API and visualized in a dynamic frontend dashboard. This repository showcases a complete workflow from raw data processing to a containerized, multi-service application.

---

## Demo & Screenshots

_(**Recommendation:** Create a short GIF of you interacting with the dashboard and API docs. It's the best way to showcase your work. Tools like LICEcap or Giphy Capture are great for this. Replace the placeholder below with your GIF.)_

![Application Demo GIF](https://your-link-to-demo.gif)

---

## Key Features

- **Interactive Dashboard:** A web-based frontend built with **Streamlit** for dynamic visualization of economic indicators, arms trade, and aerospace industry data.
- **Decoupled REST API:** A high-performance backend built with **FastAPI** serves clean, processed data, ensuring a scalable and maintainable architecture with automated documentation.
- **Predictive Forecasting:** Integrates an **ARIMA time-series model** to forecast future trends in key indicators like World GDP.
- **Automated Data Pipeline:** A reproducible data pipeline, orchestrated by `make`, handles data loading, cleaning, and preparation from raw source files.
- **Containerized Environment:** The entire application stack is containerized with **Docker** and managed with `docker-compose`, guaranteeing a secure, one-command setup for any development environment.

## Architecture & Tech Stack

The project uses a modern, decoupled architecture, separating the frontend interface from the backend data and logic layers for scalability and maintainability.

```text
+------------------+      +---------------------------+      +---------------------+      +-----------------+
|   User Browser   | <--> | Streamlit Frontend Service| <--> | FastAPI API Service | <--> | Data Pipeline   |
+------------------+      +---------------------------+      +---------------------+      +-----------------+
       (HTTP)                   (Docker Container)             (Docker Container)        (Python Scripts)
```

**Technologies Used:**

- **Backend:** FastAPI, Uvicorn
- **Frontend:** Streamlit, Plotly
- **Data Science:** Pandas, Statsmodels, NumPy
- **DevOps & Tools:** Docker, Docker Compose, Makefile, Python 3.9

---

## Getting Started: Running Locally

This application is designed to be run with a single command using Docker and Make.

### Prerequisites

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/products/docker-desktop/) & Docker Compose
- [Make](https://www.gnu.org/software/make/) (usually pre-installed on Linux/macOS)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/GeoPulse.git
cd GeoPulse
```

### 2. Set Up Data

The data pipeline requires the raw source files. Due to their size, they are not included in this repository.

1. Create the necessary directory structure:

   ```bash
   mkdir -p data/raw/bloomberg data/raw/sipri data/raw/world_bank
   ```

2. Place your raw `.csv` files into their corresponding folders within `data/raw/`.

### 3. Build and Run the Application

Use the provided `Makefile` to process the data, build the secure Docker images, and launch the services.

```bash
# This single command handles the entire process.
make run
```

The first build may take a few minutes. Subsequent launches will be much faster due to Docker's caching.

### 4. Access the Application

Once the containers are running, you can access the services in your browser:

- **Interactive Dashboard:** **[http://localhost:8501](http://localhost:8501)**
- **API Documentation (Swagger UI):** **[http://localhost:8000/docs](http://localhost:8000/docs)**

### 5. Managing the Application

- **To stop the application:**

  ```bash
  make stop
  ```

- **To view live logs from all services:**

  ```bash
  make logs
  ```

- **To clean processed data and force a pipeline rerun:**

  ```bash
  make clean
  ```

---

## Project Documentation

- **[Architecture Overview](ARCHITECTURE.md):** For a detailed breakdown of the project's evolution, design choices, and multi-phase development roadmap. _(Recommendation: Rename `roadmap.md` to `ARCHITECTURE.md`)_
- **[Data Analysis Notebook](notebooks/):** The original Jupyter Notebook containing the exploratory data analysis that inspired this full-stack application.

## Next Steps

While the application is fully functional locally, future enhancements could include:

- **Cloud Deployment:** Deploy the containerized application to a serverless platform like Google Cloud Run or AWS App Runner.
- **CI/CD Pipeline:** Implement a GitHub Actions workflow to automate testing and deployment.
- **Enhanced Analytics:** Incorporate more advanced models to explore cross-dataset correlations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
