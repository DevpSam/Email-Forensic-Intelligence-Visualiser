# Email-Forensic-Intelligence-Visualiser

This project is an interactive, 3D Organizational Network Analysis (ONA) platform designed to visualize and analyze communication patterns within the Enron Email Dataset. It transforms raw metadata into a relational intelligence dashboard to identify knowledge silos and critical influencers within the corporate structure.

Overview

The dashboard utilizes a high-contrast visual interface to map the social and professional structures of the organization. By analyzing sender-recipient relationships, the system mathematically identifies "Bridges"—individuals who facilitate communication between disparate departments—and "Silos"—isolated groups at risk of operational fragmentation.

Technical Stack

Three.js / 3d-force-graph: Utilized for high-performance WebGL rendering of the 3D network.

Tailwind CSS: Implements a responsive user interface with glassmorphism design principles.

JavaScript (ES6+): Handles real-time data processing, graph heuristics, and interactive logic.

Problem Statement

Traditional organizational charts fail to represent how information actually propagates within an enterprise. In the case of Enron, lack of communication transparency was a primary failure point. This tool addresses the following:

Knowledge Silos: Detection of teams that have ceased external information sharing.

Information Bottlenecks: Identification of critical nodes whose absence would result in network collapse.

Strategic Visualization: Providing leadership with a transparent view of internal corporate culture and operational dependencies.

Installation and Usage

Acquire the Dataset:
Download the emails.csv file from the Kaggle Enron Dataset repository.

Data Pre-processing:
It is recommended to use the provided Python script to extract an edges.csv file containing only the "from" and "to" columns. This ensures optimal 3D rendering performance within the browser environment.

Launch the Dashboard:
Open index.html in a modern web browser and upload the processed CSV file.

Key Features

Interactive 3D Environment: Navigation through the corporate structure via rotation, zoom, and pan functions.

Entity Search System: Direct location of specific employees and their communication profiles.

Temporal Evolution: A timeline feature to observe the dynamic growth of the network.

Forensic Analysis Mode: A specialized view to highlight critical communication bridges and high-centrality nodes.

Developed for forensic data analysis and organizational strategy research.
