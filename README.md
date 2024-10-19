# Establishment Analysis in Eastern Saudi Arabia

This project processes and analyzes a dataset of 1,000+ establishments in Eastern Saudi Arabia using Scala, Apache Spark, Databricks, and AWS S3. The aim is to derive insights from the dataset based on ratings, types, and geographic locations of businesses, and to perform geospatial analysis for identifying commercial hubs and high-density business areas.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Data Pipeline](#data-pipeline)
- [Geospatial Analysis](#geospatial-analysis)
- [AWS S3 Integration](#aws-s3-integration)
- [Setup Instructions](#setup-instructions)
- [Results](#results)
- [License](#license)

## Project Overview

This project involves processing and analyzing establishment data in the Eastern Province of Saudi Arabia using big data tools. The dataset contains information on establishments' ratings, types, locations (longitude and latitude), and more. The goal is to extract meaningful insights about commercial areas and business hubs.

### Objectives:
- Clean and preprocess the dataset.
- Perform data transformation and analysis to extract insights based on types of businesses, ratings, and locations.
- Conduct geospatial clustering using latitude and longitude to identify high-density business areas.
- Deploy the pipeline on Databricks and store the processed data in AWS S3 for scalability and accessibility.

## Technologies Used
- **Programming Language:** Python, Scala
- **Framework:** Apache Spark
- **Platform:** Databricks
- **Cloud Storage:** AWS S3
- **Geospatial Analysis:** Spark SQL with geospatial functions

## Data Pipeline

The project consists of an end-to-end ETL pipeline built using Apache Spark:

1. **Extract**: Load the dataset of establishments from a CSV file.
2. **Transform**: 
   - Data cleaning (handling missing values, correcting data types, etc.).
   - Data transformation (normalizing business categories, analyzing ratings).
   - Geospatial transformation (clustering establishments by geographic coordinates).
3. **Load**: Save the processed data to AWS S3 for scalable cloud storage and future use.

## Geospatial Analysis

The geospatial analysis component of the project clusters businesses based on their latitude and longitude. Using Spark’s distributed processing capabilities, we identified key commercial hubs and areas with high business density in Eastern Saudi Arabia.

### Key Metrics:
- Number of establishments in each cluster.
- Average rating of businesses within each cluster.
- Types of businesses (restaurants, retail, etc.) predominant in each cluster.

## AWS S3 Integration

The processed and analyzed data is stored on AWS S3 to ensure accessibility and scalability. This integration allows for efficient data storage and retrieval from the cloud.

## Setup Instructions

### Prerequisites:
- Databricks account for running the pipeline.
- AWS S3 bucket for storing the processed data.
- Scala and Spark installed locally (if testing locally).

### Steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/ItsJettLag/establishments-analysis-saudi-arabia.git
