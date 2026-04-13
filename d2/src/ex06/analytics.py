import os
import logging
import requests
import config
from random import randint

logging.basicConfig(
    filename=config.log_file,
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class Research:
    def __init__(self, path):
        self.path = path
        logging.debug(f"Research initialized with path: {path}")

    def file_reader(self, has_header=True):
        logging.debug("Reading file...")
        with open(self.path, 'r') as file:
            content = file.readlines()

        if has_header:
            header = content[0].strip().split(',')
            if len(header) != 2 or not header[0].isalpha() or not header[1].isalpha():
                logging.error("Incorrect header in file")
                raise ValueError('Incorrect Header in file')
            content = content[1:]

        data = []
        for line in content:
            first, second = line.strip().split(',')
            if int(first) not in (0, 1) or int(second) not in (0, 1) or first == second:
                logging.error("Incorrect data in file")
                raise ValueError('Incorrect data in file')
            data.append([int(first), int(second)])

        logging.debug(f"File successfully read with {len(data)} records")
        return data

    def send_to_telegram(self, message):
        logging.debug("Sending message to Telegram...")
        try:
            payload = {
                "chat_id": config.telegram_chat_id,
                "text": message
            }
            response = requests.post(config.telegram_url, json=payload)
            if response.status_code == 200:
                logging.debug("Message successfully sent to Telegram")
            else:
                logging.error(f"Telegram error: {response.status_code} {response.text}")
        except Exception as e:
            logging.error(f"Failed to send message to Telegram: {e}")

    class Calculations:
        def __init__(self, data):
            self.data = data
            logging.debug("Calculations initialized")

        def counts(self):
            logging.debug("Calculating the counts of heads and tails")
            heads = sum(row[0] for row in self.data)
            tails = sum(row[1] for row in self.data)
            return heads, tails

        def fractions(self, heads, tails):
            logging.debug("Calculating fractions")
            total = heads + tails
            return heads / total * 100, tails / total * 100

    class Analytics(Calculations):
        def predict_random(self, steps):
            logging.debug(f"Generating {steps} random predictions")
            result = []
            for _ in range(steps):
                if randint(0, 1) == 0:
                    result.append([0, 1])
                else:
                    result.append([1, 0])
            return result

        def predict_last(self):
            logging.debug("Returning last observation")
            return self.data[-1]

        def save_file(self, data, filename, ext):
            logging.debug(f"Saving data to {filename}.{ext}")
            if not isinstance(data, str):
                logging.error("Data must be a string")
                raise ValueError("Data for saving must be a string")
            path = f"{filename}.{ext}"
            with open(path, "w") as f:
                f.write(data)
            logging.debug("File saved successfully")
            return os.path.abspath(path)
