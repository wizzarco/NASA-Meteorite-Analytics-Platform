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
Python Ingestion Layer
    ↓
Azure Blob Storage OR Local Storage
        ↓
    Bronze Layer
        ├── delta/
        └── full/
    ↓
Databricks
    ↓
Silver Layer
    ↓
Gold Layer
    ↓
Analytics Dashboard (Power BI or Databricks Dashboard or Both)

## Project Objectives
* Demonstrate modern Data Engineering practices
* Build an end-to-end analytics platform
* Implement a Medallion Architecture
* Showcase Databricks and Delta Lake expertise
* Develop automated ingestion pipelines
* Analyze Near-Earth Objects and potential Earth impact risks