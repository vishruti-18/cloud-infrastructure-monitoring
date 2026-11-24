
from pathlib import Path
from datetime import datetime

# Define alert log file
alert_file = Path("logs/alerts.log")

# Create logs directory
alert_file.parent.mkdir(parents=True, exist_ok=True)


def send_alert(resource, usage, threshold):

    timestamp = datetime.now()

    message = (
        f"{timestamp} - CRITICAL - "
        f"{resource} usage is {usage}%. "
        f"Threshold is {threshold}%."
    )

    print("\nALERT GENERATED!")
    print(message)

    # Save alert to a separate file
    with alert_file.open("a", encoding="utf-8") as file:
        file.write(message + "\n")
