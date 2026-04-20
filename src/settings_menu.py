import logging
import sys
import yaml
import questionary
import os
import src.config_loader as config_loader

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    config = config_loader.load_config()
    while True:
        keys = list(vars(config).keys())
        keys.append("Back")
        logging.debug("asking user what parameter to change")
        choice = questionary.select(
            "Which setting do you want to change",
            choices=keys
        ).ask()
        logging.debug(f"user choose to change {choice}")

        if choice == "Back":
            break

        current_value = getattr(config, choice)

        if isinstance(current_value, bool):
            new_value = questionary.confirm(
                f"{choice}: {current_value}").ask()
            logging.debug(f"changed from {current_value} to {new_value}")

        elif isinstance(current_value, int):
            new_value = int(questionary.text(f"{choice}: {current_value}").ask())
            logging.debug(f"changed from {current_value} to {new_value}")

        elif isinstance(current_value, float):
            new_value = float(questionary.text(f"{choice}: {current_value}").ask())
            logging.debug(f"changed from {current_value} to {new_value}")
            
        elif isinstance(current_value, str):
            if "path" in choice:
                new_value = questionary.path(f"{choice}: {current_value}").ask()
                logging.debug(f"changed from {current_value} to {new_value}") 
            else:
                new_value = questionary.text(f"{choice}: {current_value}").ask()
                logging.debug(f"changed from {current_value} to {new_value}")

        setattr(config, choice, new_value)
        config_loader.save_config(config)