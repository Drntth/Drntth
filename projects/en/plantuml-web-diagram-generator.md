# :file_folder: PlantUML Web Diagram Generator

---

## Project Name

**Repository:** `plantuml-web-diagram-generator`

## Description

A web application that allows users to upload or enter PlantUML text descriptions and automatically generates UML diagrams on the backend. The backend uses PlantUML (via Docker) to render diagrams, and the frontend provides an intuitive interface for users to interact with the system.

## Technologies Used

- JavaScript (frontend)
- Node.js (backend)
- PlantUML
- Docker
- HTML5, CSS3

## Features

- Upload or paste PlantUML text to generate diagrams
- Download generated diagrams as images (PNG/SVG)
- REST API for diagram generation
- User-friendly web interface
- Dockerized backend for easy deployment

## Installation

Clone the repository and run the following commands:

```bash
# Clone the repository
 git clone https://github.com/yourusername/plantuml-web-diagram-generator.git
 cd plantuml-web-diagram-generator

# Build and run the backend with Docker
 docker-compose up --build

# (Optional) Install frontend dependencies and start development server
 cd frontend
 npm install
 npm start
```

## Usage

1. Open the web interface in your browser.
2. Paste or upload your PlantUML text description.
3. Click "Generate" to view and download the UML diagram.

Example API usage:
```bash
curl -X POST -F 'uml=@diagram.puml' http://localhost:3000/api/generate
```

## Screenshots

_Add screenshots or architecture diagrams here._

## License

MIT License
