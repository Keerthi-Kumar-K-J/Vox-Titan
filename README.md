# VoxTitan Backend

VoxTitan is a voice-enabled AI chatbot powered by Together.ai's advanced language models. This repository contains the backend code for VoxTitan, built using Flask and deployed on Render.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
  - [Environment Variables](#environment-variables)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
  - [Render](#render)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

## Features
- **AI-Powered Chat**: Integrates with Together.ai's API for natural language processing.
- **Voice Integration**: Supports voice-based interactions (via frontend integration).
- **RESTful API**: Provides a simple and scalable API for the frontend.
- **CORS Support**: Enables cross-origin requests for seamless frontend-backend communication.

## Technologies Used
- **Python**: Primary programming language.
- **Flask**: Web framework for building the backend.
- **Together.ai**: AI model provider for generating responses.
- **Render**: Cloud platform for hosting the backend.
- **Flask-CORS**: Enables Cross-Origin Resource Sharing (CORS).

## Setup
### Prerequisites
Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **pip**: Python package manager (comes with Python).
- **Git**: [Download Git](https://git-scm.com/downloads)

### Installation
#### Clone the Repository:
```sh
git clone https://github.com/your-username/Vox-Titan.git
cd Vox-Titan
```

#### Create a Virtual Environment:
```sh
python -m venv venv
```

#### Activate the Virtual Environment:
**On Windows:**
```sh
venv\Scripts\activate
```
**On macOS/Linux:**
```sh
source venv/bin/activate
```

#### Install Dependencies:
```sh
pip install -r requirements.txt
```

## Configuration
### Environment Variables
Create a `.env` file in the root directory and add the following variables:
```sh
TOGETHER_API_KEY=your_together_api_key
```
- `TOGETHER_API_KEY`: Your Together.ai API key. [Get it from Together.ai](https://together.ai/).

## API Endpoints
### `POST /chat`
**Description**: Sends a user message to the AI and returns the response.

**Request Body:**
```json
{
  "message": "Hello"
}
```

**Response:**
```json
{
  "response": "Hello! How can I assist you today?"
}
```

## Deployment
### Render
#### Sign Up:
- Create an account on [Render](https://render.com/).

#### Create a New Web Service:
1. Connect your GitHub repository.
2. Select the branch to deploy (e.g., `main`).

#### Configure Environment Variables:
- Add `TOGETHER_API_KEY` with your Together.ai API key.

#### Deploy:
- Render will automatically build and deploy your backend.

## Contributing
We welcome contributions! Here’s how you can help:

#### Fork the Repository:
```sh
git clone https://github.com/your-username/Vox-Titan.git
```

#### Create a Branch:
```sh
git checkout -b feature/your-feature-name
```

#### Commit Your Changes:
```sh
git commit -m "Add your feature"
```

#### Push to the Branch:
```sh
git push origin feature/your-feature-name
```

#### Open a Pull Request:
- Describe your changes and submit the PR.

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **Together.ai**: For providing the AI models.
- **Flask**: For the lightweight and flexible web framework.
- **Render**: For seamless deployment and hosting.

## Contact
For questions or feedback, feel free to reach out:

- **Email**: 24ec069@kpriet.ac.in
- **GitHub**: [Keerthi-Kumar-K-J](https://github.com/Keerthi-Kumar-K-J)
