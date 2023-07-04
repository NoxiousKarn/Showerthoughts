# ShowerThoughts Plugin

This plugin displays random shower thoughts headlines on your pwnagotchi when the device is waiting.

## Installation

1. Clone or download this repository to your pwnagotchi device.
2. Copy the `Showerthoughts.py` file to the `plugins` directory.
3. Edit the `config.toml` file and add the lines from `showerthoughts_config`
4. Save and reboot.

## Configuration
The following options can be configured in the config.toml file:

`enable`: Whether or not the plugin is enabled. (default: true)

`rss_url`: The URL of the RSS feed that the plugin should download. (default:"https://www.reddit.com/r/showerthoughts.rss")

`saved_rss`: The file where the plugin should save the downloaded RSS feed. (default:"/root/showerthoughts.rss")

`max_title_length`: The maximum length of a headline that the plugin will display. (default: 68)

## Usage
The plugin will automatically start displaying random shower thoughts headlines when the device is waiting.
You can edit the RSS you pull remember to also update the save location in `saved_rss` field

## Troubleshooting
If you are having problems with the plugin, please check the following:

1. Make sure that the plugin is installed correctly.
2. Make sure that the RSS feed URL is correct.
3. Make sure that the saved_rss file exists and is writable.
4. Make sure that the max_title_length value is not too low.

## Contributing
If you would like to contribute to the plugin, please fork the repository and submit a pull request.

## License
The plugin is licensed under the GPLv3 license.
