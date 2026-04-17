import src.housey_logging
src.housey_logging.configure()

import sys
import src.twitch_dj_clipper
import logging
import os
import questionary
import yaml


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def settings_menu():
    while True:
        clear_screen()
        config = src.config_loader.load_config()
        choice = questionary.select(
            "=== Settings menu ===",
            choices=[
                f"Change bot name: {config.bot_name}",
                f"Change oath token: {config.oath_token}",
                f"Change target channel: {config.channel}",
                f"Change twitch api id: {config.twitch_api_id}",
                f"Change twitch api secret: {config.twitch_api_secret}",
                f"Change clip start before timestamp: {config.clip_start_before_timestamp}",
                f"Change max total clip duration: {config.total_clip_duration}",
                f"Change metadata artist: {config.metadata_artist}",
                f"Change folder path of VOD's: {config.vod_folder_path}",
                f"Change if bot responds in chat: {config.quiet}",
                f"Change extra parameters: {config.extra_params}",
                "Back",
            ]
        ).ask()

        if choice is None or choice == "Back":
            break

def main_menu():
    return questionary.select(
        "=== Main Menu ===",
        choices=[
            questionary.Choice("Start clipper", value="1"),
            questionary.Choice("Test mode", value="2"),
            questionary.Choice("Settings", value="3"),
            questionary.Choice("Exit", value="exit"),
        ]
    ).ask()


def main():
    while True:
        clear_screen()
        menu_choice = main_menu()

        if menu_choice == "1":
            logging.info("starting twitch_dj_clipper twitch chatbot")
            logging.info("only errors will be displayed unless otherwise configured")
            src.twitch_dj_clipper.main()
        
        elif menu_choice == "2":
            pass #need to make a test mode

        elif menu_choice == "3":
            settings_menu()

        elif menu_choice == "exit" or menu_choice is None:
            break


if __name__ == "__main__":
    sys.excepthook = src.housey_logging.log_exception
    main()
