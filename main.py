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
                f"Toggle if bot responds in chat: {config.quiet}",
                f"Change extra parameters: {config.extra_params}",
                "Back",
            ]
        ).ask()

        if choice is None or choice == "Back":
            break

        if choice.startswith("Change bot name"):
            new_bot = questionary.text(
                "Enter new bot name: ",
                default=config.bot_name
            ).ask()

            if new_bot:
                config.bot_name = new_bot
                src.config_loader.save_config(config)
                logging.debug("succesfully changed bot name config")

        elif choice.startswith("Change oath token"):
            new_oath = questionary.text(
                "Enter new oath token: ",
                default=config.oath_token
            ).ask()

            if new_oath:
                config.oath_token = new_oath
                src.config_loader.save_config(config)
                logging.debug("succesfully changed oath token config")

        elif choice.startswith("Change target channel"):
            new_channel = questionary.text(
                "Enter new target channel: ",
                default=config.channel
            ).ask()

            if new_channel:
                config.channel = new_channel
                src.config_loader.save_config(config)
                logging.debug("succesfully changed channel config")

        elif choice.startswith("Change twitch api id"):
            new_api = questionary.text(
                "Enter new twitch api id: ",
                default=config.twitch_api_id
            ).ask()

            if new_api:
                config.twitch_api_id = new_api
                src.config_loader.save_config(config)
                logging.debug("succesfully changed twitch api id config")

        elif choice.startswith("Change twitch api secret"):
            new_secret = questionary.text(
                "Enter new twitch api secret: ",
                default=config.twitch_api_secret
            ).ask()

            if new_secret:
                config.twitch_api_secret = new_secret
                src.config_loader.save_config(config)
                logging.debug("succesfully changed twitch api secret config")

        elif choice.startswith("Change clip start before timestamp"):
            new_before = questionary.text(
                "Enter clip start in seconds: ",
                default=str(config.clip_start_before_timestamp)
            ).ask()

            if new_before and new_before.isdigit():
                config.clip_start_before_timestamp = int(new_before)
                src.config_loader.save_config(config)
                logging.debug("succesfully changed timestamp before clip")
            else:
                print("Invalid number")
                logging.debug("wrongly enterd timestamp before clip")

        elif choice.startswith("Change max total clip duration"):
            new_max = questionary.text(
                "Enter max clip duration in seconds: ",
                default=str(config.total_clip_duration)
            ).ask()

            if new_max and new_max.isdigit():
                config.total_clip_duration = int(new_max)
                src.config_loader.save_config(config)
                logging.debug("succesfully changed duration of clip")
            
            else:
                print("Invalid number")
                logging.debug("wrongly enterd number for duration of clip")

        elif choice.startswith("Change metadata artist"):
            new_meta = questionary.text(
                "enter name of metadata artist",
                default=config.metadata_artist
            ).ask()

            if new_meta:
                config.metadata_artist = new_meta
                src.config_loader.save_config(config)
                logging.debug("succesfully changed metadata artist config")

        elif choice.startswith("Change folder path of VOD's"):
            new_location = questionary.path(
                "enter location of VOD's: ",
                default=config.vod_folder_path
            ).ask()

            if new_location:
                config.vod_folder_path = new_location
                src.config_loader.save_config(config)
                logging.debug("succesfully changed location of VOD's in config")

        elif choice.startswith("Toggle if bot responds in chat"):
            config.quiet = not config.quiet
            src.config_loader.save_config(config)
            print("Bot respons is now ", config.quiet)
            logging.debug("succesfully changed state of bot response")

        elif choice.startswith("Change extra parameters"):
            new_para = questionary.text(
                "Enter extra parameters: ",
                default=config.extra_params
            ).ask()

            if new_para:
                config.extra_params = new_para
                src.config_loader.save_config(config)
                logging.debug("succesfully changed extra parameters in config")


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
            clear_screen()
            break


if __name__ == "__main__":
    sys.excepthook = src.housey_logging.log_exception
    main()
