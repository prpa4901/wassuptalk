# Chatbot Tool with Hugging Face Models

This project provides an easy-to-use chatbot interface powered by Hugging Face models, such as Falcon, Mistral, and Phi-2. The chatbot runs in a Dockerized environment and includes a Makefile for streamlined setup and management.

## Features

- Chatbot interface with **user and bot images**.
- Models powered by Hugging Face APIs (e.g., Falcon, Mistral, Phi-2).
- Dockerized environment for portability and ease of use.
- Simple one-step commands using the `Makefile`.

---

## Prerequisites

1. Install **Docker** and **Docker Compose**:
   - [Docker Installation Guide](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

2. Install `make`:
   - On Ubuntu/Debian:
     ```bash
     sudo apt install make
     ```
   - On macOS:
     ```bash
     xcode-select --install
     ```
   - On Windows: Use [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm) or a compatible environment like WSL.

---

## Getting Started

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

### Step 2: Build and Run the Application
Use the `Makefile` to simplify setup and usage.

#### Commands:

1. **Build and Run the Application**:
   ```bash
   make build-and-run
   ```

2. **Start the Application** (without rebuilding):
   ```bash
   make up
   ```

3. **Stop and Remove Containers**:
   ```bash
   make down
   ```

4. **View Logs**:
   ```bash
   make logs
   ```

5. **Clean Up Unused Docker Objects**:
   ```bash
   make clean
   ```

---

## Accessing the Chatbot

1. Open your web browser and navigate to:

   ```
   http://localhost:8501
   ```

2. Enter your Hugging Face API token in the chatbot interface:
   - **Don't have a token yet?** [Create one here](https://huggingface.co/settings/tokens).

3. Select a model (e.g., Falcon, Mistral, Phi-2) and start chatting!

---

## Project Structure

```
├── Dockerfile              # Docker configuration for the app
├── docker-compose.yml      # Docker Compose configuration
├── Makefile                # Simplified commands for setup and management
├── run.sh                  # Alternative shell script for running the app
├── app/                    # Main application code
│   ├── constants.py        # Constants (model names, etc.)
│   ├── main.py             # Streamlit app code
│   └── requirements.txt    # Python dependencies
├── README.md               # Project documentation
└── assets/                 # Images and other assets
```

---

## Models Supported

| Model Name                 | Description                                  |
|----------------------------|----------------------------------------------|
| `tiiuae/falcon-7b`         | Falcon 7B, medium-sized powerful model.     |
| `mlx-community/phi-2`      | Phi-2, lightweight model for general use.   |
| `mistralai/Mistral-7B-v0.1`| Mistral 7B, latest medium-sized model.      |
| `gpt2`                     | GPT-2, general-purpose model.               |

---

## Customization

### Add Your Own Profile Image
- Replace the default user image (`path_to_user_image.png`) in the `assets/` folder.
- Replace the bot image (`path_to_bot_image.png`) in the same folder.

---

## Contributing

Feel free to submit issues or pull requests for any bugs, enhancements, or new features you'd like to see!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
