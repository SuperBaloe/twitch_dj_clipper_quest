import src.housey_logging
src.housey_logging.configure()

import sys
import src.settings_menu
import src.twitch_dj_clipper
import logging


def is_user_facing():
    return sys.stdin.isatty() and sys.stdout.isatty()


def main():

    if is_user_facing():
        logging.debug("Program is opend in user facing terminal")
        logging.info("Loading config menu")
        src.config_loader.create_config_if_missing()
        src.settings_menu.menu()

    else:
        logging.info("starting twitch_dj_clipper twitch chatbot")
        logging.info("only errors will be displayed unless otherwise configured")
        src.twitch_dj_clipper.main()


if __name__ == "__main__":
    sys.excepthook = src.housey_logging.log_exception
    main()
