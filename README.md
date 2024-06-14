# Chat_Bot

Chat_Bot is a project that uses Flask and a machine learning model to create a simple web interface where users can ask questions and get answers from the model.

## Table of Contents

- [Installation](#installation)
- [Running](#running)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Continuing On](#continuing-on)
- [Uninstalling Chat_Bot](#uninstalling-chat_bot)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Installation

### Requirements

- Docker
- Docker Compose

### Installation Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/IvanEfimenko1/Chat_Bot.git
    cd Chat_Bot
    ```

2. Build the Docker container:

    ```bash
    docker-compose build
    ```

## Running

To run the application, use the following command:

```bash
docker-compose up
```

The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Usage

1. Open a browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).
2. Enter your question in the text field and press the "Ask" button.
3. The model's response will be displayed below your question on the page.

## Project Structure

- `.dockerignore`: Specifies files and directories to be ignored by Docker.
- `app.py`: Main Flask application file.
- `Chat_Bot_Proj.code-workspace`: VS Code workspace configuration.
- `docker-compose.yml`: Docker Compose file for managing multi-container Docker applications.
- `Dockerfile`: Instructions for building the Docker image.
- `README.md`: This file, provides information about the project.
- `requirements.txt`: List of project dependencies.
- `templates/`: Directory containing HTML templates for Flask.

## Testing

You can test the project by following these steps:

1. Run the container:

    ```bash
    docker-compose up
    ```

2. Go to [http://127.0.0.1:5000](http://127.0.0.1:5000) and test the functionality by entering questions and receiving answers.

## Continuing On

Once you've finished with the project, you can use your new knowledge to develop your own projects or contribute to this one.

## Uninstalling Chat_Bot

If you want to remove Chat_Bot from your system, follow these steps:

1. Remove the project folder:

    ```bash
    rm -rf Chat_Bot
    ```

2. Stop and remove Docker containers:

    ```bash
    docker-compose down
    ```

