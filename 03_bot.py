import pyautogui
import pyperclip
import time
from openai import OpenAI

def is_last_message_from_sender(chat_log, sender_name = "SENDER_NAME_HERE"):

    messages = chat_log.strip().split("2024]")[-1]
    if sender_name in messages:
        return True
    return False

client = OpenAI(
    api_key="YOU_OPENAI_KEY"
)
# Click at position (824, 1050)

pyautogui.click(824, 1050)

# Pause to ensure the click is registered
time.sleep(1)

while True:

    # Drag from position (673, 191) to (1885, 932)
    pyautogui.moveTo(673, 191)
    pyautogui.dragTo(1885, 932, duration=1, button='left')

    # Pause to ensure the drag is complete
    time.sleep(1)

    # Copy the selected content to the clipboard
    pyautogui.hotkey('ctrl', 'c')

    # Wait for clipboard data to be copied
    time.sleep(1)

    # Get the clipboard content
    chat_response = pyperclip.paste()
    pyautogui.click(695,225)

    # Output the clipboard content to the console
    print("Copied Content:")
    print(chat_response)

    if is_last_message_from_sender(chat_response):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            # Put your details to train the bot. So, it will be make the replies accordingly. 
            messages=[
                {"role": "system", "content": "YOUR_DETAILS_HERE"},
                {
                    "role": "user",
                    "content": chat_response
                }
            ]
        )

        gpt_response = completion.choices[0].message.content

        pyperclip.copy(gpt_response)

        # Click at position (1270, 988)
        pyautogui.click(1270, 988)

        # Pause to ensure the click is registered
        time.sleep(1)

        # Paste the message
        pyautogui.hotkey('ctrl', 'v')

        # Pause to ensure the message is pasted
        time.sleep(1)

        # Hit enter
        pyautogui.press('enter')



