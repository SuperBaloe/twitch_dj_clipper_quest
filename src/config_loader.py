import os
import yaml
import logging

default_config = {
    "bot_name": '',
    "oath_token": '',
    "channel": '',
    "twitch_api_id": "",
    "twitch_api_secret": "" ,
    "clip_start_before_timestamp": 30,
    "total_clip_duration": 60,
    "metadata_artist": "twitch_dj_clipper",
    "vod_folder_path": "path/to/thingie",
    "quiet": False,
    "extra_params": ""
}
def create_config_if_missing():
    if not os.path.exists("config/config.yaml"):
        with open("config/config.yaml", "w") as file:
            yaml.safe_dump(default_config, file, indent=4)


# loads config from file
def load_config() -> dict:
    with open("config/config.yaml") as config_file:
        config_yaml = yaml.safe_load(config_file)
        merged_config = config_object({**default_config, **config_yaml})
    logging.debug("succesfully loaded config")       
    return(merged_config)

#saves config to file
def save_config(config) -> None:
    config_dict = config.__dict__
    with open("config/config.yaml", "w") as config_file:
        yaml.safe_dump(config_dict, config_file, default_flow_style=False, sort_keys=False)
    logging.debug("succesfully saved config")


class config_object:
    def __init__(self, d=None):
        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)
