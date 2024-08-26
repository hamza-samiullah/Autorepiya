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
Cloning the Repository
Clone this repository to your local machine using:

bash
Copy code
git clone https://github.com/your-username/autorepiya.git
cd autorepiya
Configuration
API Keys:

Replace "YOU_OPENAI_KEY" with your OpenAI API key.
Sender Name:

Replace "SENDER_NAME_HERE" in the is_last_message_from_sender function with the name of the sender you want to monitor.
Adjust Screen Coordinates:

Modify the pyautogui.click() and pyautogui.moveTo() coordinates to match your screen resolution and chat window positions.
Usage
Run the script using:

bash
Copy code
python autorepiya.py
The script will:

Click on a specific position in your chat window.
Drag and select the chat content.
Copy the content to the clipboard.
Determine if the last message is from the specified sender.
Generate a response using OpenAI and automatically send it in the chat.
Contributing
If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -m 'Add new feature').
Push to the branch (git push origin feature-branch).
Open a Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.





