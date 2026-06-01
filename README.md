# 🚀 NASA Meteorite Analytics Platform
NASA Meteorite Analytics Platform is an end-to-end Data Engineering project focused on collecting, processing, and analyzing NASA Near-Earth Object (NEO) data.
The platform extracts asteroid and close-approach data from NASA APIs, stores raw datasets in a Bronze layer, applies transformations through a Medallion Architecture (Bronze, Silver, Gold), and delivers analytical insights using Databricks, PySpark, Delta Lake, and SQL.

## Key Features
☄️ Near-Earth Object (NEO) monitoring
🌍 Earth close-approach analysis
⚠️ Potentially hazardous asteroid tracking
📏 Asteroid size and magnitude analysis
🚀 Velocity and distance analytics
📊 Interactive Databricks dashboards
🔄 Automated ingestion pipelines
🏗️ Medallion Architecture implementation

## Tech Stack
* Python
* Databricks
* PySpark
* Delta Lake
* SQL
* Pandas
* Git & GitHub

## Architecture
NASA API
    ↓
Python Ingestion Jobs
    ↓
Cloud Storage (Bronze)
    ↓
Databricks
        ↓
    Bronze
        ↓
    Silver
        ↓
    Gold
        ↓
    Dashboard

## Project Objectives
* Demonstrate modern Data Engineering practices
* Build an end-to-end analytics platform
* Implement a Medallion Architecture
* Showcase Databricks and Delta Lake expertise
* Develop automated ingestion pipelines
* Analyze Near-Earth Objects and potential Earth impact risks

<!-- ## Current Progress

### ✅ Completed
* NASA API integration
* Environment configuration management (.env)
* Raw JSON ingestion
* Bronze layer generation
* GitHub integration
* Project structure setup

### 🚧 In Progress
* Databricks Bronze ingestion
* Silver layer transformations
* Data quality checks

### 📅 Planned
* Gold analytical tables
* Threat scoring model
* Interactive dashboards
* Automated pipeline scheduling
* Historical trend analysis -->