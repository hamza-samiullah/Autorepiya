# AutoRepiya

AutoRepiya is a Python-based automation tool that leverages AI to generate and send automatic replies in a chat application. The script monitors the latest message in a chat, checks if it's from a specified sender, generates an AI-driven response using OpenAI, and then sends the reply automatically.

## Features

- **Automated Chat Interaction:** Monitors the chat for messages from a specified sender.
- **AI-Powered Replies:** Uses OpenAI's API to generate intelligent responses based on the latest message.
- **Clipboard Integration:** Copies the chat content to the clipboard for processing.
- **Automation with PyAutoGUI:** Automates mouse clicks, drag-and-drop, and keyboard inputs to interact with the chat interface.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Dependencies

Install the required Python packages using the following command:

```bash
pip install pyautogui pyperclip openai

```

### Cloning the Repository
Clone this repository to your local machine using:

```bash
git clone https://github.com/your-username/autorepiya.git
cd autorepiya
```

### Configuration
API Keys:

- Replace "YOU_OPENAI_KEY" with your OpenAI API key.

Sender Name:

- Replace "SENDER_NAME_HERE" in the is_last_message_from_sender function with the name of the sender you want to monitor.

Adjust Screen Coordinates:

- Modify the pyautogui.click() and pyautogui.moveTo() coordinates to match your screen resolution and chat window positions.

## Usage

Run the script using:

```bash
python autorepiya.py
```

## The script will:

    - Click on a specific position in your chat window.
    - Drag and select the chat content.
    - Copy the content to the clipboard.
    - Determine if the last message is from the specified sender.
    - Generate a response using OpenAI and automatically send it in the chat.

## Using GitHub

### Push Changes

To push your changes to GitHub:

```bash
git add .
git commit -m "Describe your changes"
git push origin branch_name
```

### Pull Changes

To pull the latest changes from the repository:

```bash
git pull origin branch_name
```

## Contributing

If you wish to contribute to the project:

1. **Fork the Repository**: Create your own copy of the repository by forking it on GitHub.
2. **Create a New Branch**: Work on your feature in a new branch.
   ```bash
   git checkout -b feature-name
   ```
3. **Make Changes**: Implement your feature or fix.
4. **Commit and Push**: Commit your changes and push them to your fork.
5. **Create a Pull Request**: Submit a pull request to the original repository for review.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This `README.md` file provides all the necessary instructions to set up, run, and contribute to the voice assistant project. Feel free to customize it further according to your specific needs.