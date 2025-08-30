# Project Architecture & Development Roadmap

## Introduction

This document details the architecture and evolution of the "Global Economic Impact Analysis" project. What began as a data analysis notebook has been engineered into a full-stack, portfolio-ready software application. The project's development followed a multi-phase roadmap, transforming the initial analysis into a robust, interactive, and deployed data product that showcases a wide range of modern software engineering and data science practices.

---

### Phase 1: Building a Solid Foundation

A robust software architecture is the bedrock of this project, ensuring the final application is maintainable, testable, and scalable.

- **Data Preprocessing Pipeline:** A dedicated data preprocessing pipeline was established in a standalone module. This pipeline cleans, validates, and prepares all incoming data, ensuring consistency and reliability while cleanly separating data preparation logic from the core analysis code.

- **Modularized Codebase:** The project transitioned from a monolithic notebook to a well-organized `src` directory. The codebase is broken down into logical modules for data loading, API services, analytical modeling, and visualization components, adhering to modern software design principles.

- **Object-Oriented Data Models:** Object-Oriented principles were applied by creating Python classes for the primary data sources (SIPRI, World Bank, Bloomberg). This approach encapsulates data and its associated methods, promoting code reusability and simplifying maintenance.

---

### Phase 2: Automating the Data Workflow

To ensure data integrity and complete reproducibility, the project incorporates a fully automated workflow.

- **Automated Data Pipeline Script:** A core script automates the end-to-end process of loading raw data, executing the preprocessing pipeline, and merging the disparate sources into analysis-ready datasets. This forms the reliable backbone of the application's data layer.

- **Integrated Build System:** A `Makefile` was implemented to automate and standardize common development tasks. Commands like `make build`, `make test`, and `make run` streamline the development workflow, making the project easy for any developer to set up and contribute to.

---

### Phase 3: Creating an Interactive User Experience

The analytical insights are delivered through a dynamic and interactive web application, built on a modern, decoupled architecture.

- **Interactive Dashboard Frontend:** A user-friendly dashboard was built using **Streamlit**, allowing users to dynamically explore the project's analysis. The interface provides interactive visualizations of global events' impact on economies and sectors, offering a rich experience not possible in a static notebook.

- **Decoupled REST API Backend:** The dashboard is powered by a high-performance REST API built with **FastAPI**. This decoupled backend serves the cleaned and processed data to the frontend, ensuring a clean separation of concerns, high efficiency, and the ability to scale the frontend and backend independently.

---

### Phase 4: Uncovering Deeper Insights with Advanced Analytics

Beyond data visualization, the project leverages advanced modeling to provide deeper, forward-looking insights.

- **Applied Statistical Modeling:** Advanced statistical models, including time-series decomposition, were applied to formally analyze the impact of global events and uncover the underlying trend, seasonal, and residual components of the economic data.

- **Integrated Predictive Modeling:** A predictive ARIMA (Autoregressive Integrated Moving Average) model was developed to forecast future trends in key economic indicators like World GDP. This adds a quantitative, forward-looking perspective to the analysis, accessible directly through the application.

---

### Phase 5: Ensuring a Professional Finish with Deployment and Documentation

To complete the development lifecycle, the application was packaged and deployed, making it globally accessible and fully reproducible.

- **Containerized Application:** The entire application stack (the FastAPI backend and the Dash frontend) is containerized using **Docker**. This guarantees a consistent and reliable environment, encapsulating all dependencies and simplifying deployment across any platform.

- **Cloud Deployment:** The containerized application is deployed on **Google Cloud Run**, a serverless platform that automatically scales based on traffic. This choice ensures the application is highly available, cost-efficient, and can handle a global audience without manual infrastructure management.

- **Comprehensive Documentation:** This project is documented in a detailed `README.md` file that serves as a central hub. It explains the project's purpose, outlines the system architecture, and provides clear instructions on how to set up the development environment and run the application locally.
