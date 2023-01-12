# inStan
A bot that stans its favorite influencers. This Instagram reposting selenium engine tags artists and reposts their content to a specified Instagram account at a specified random interval.
It basically curates an instagram account for you, allowing you more freedom to respond to your followers and interact with your community.

# Requirements
- Python 3.6+
- Selenium
- Chromedriver
- Instagram account

# Setup
1. Clone the repository
2. Install the requirements
3. Create a new Instagram account

# Usage
1. Run the script
2. Log into the Instagram account
3. Wait for the script to run

# Configuration
The configuration file is located in the `config` folder. The file is named `config.json`. The file is structured as follows:
```json
{
    "username": "username",
    "password": "password",
    "target": "target",
    "interval": {
        "min": 0,
        "max": 0
    },
    "tags": [
        "tag1",
        "tag2",
        "tag3"
    ]
}
```
- `username` is the username of the Instagram account that will be used to repost content
- `password` is the password of the Instagram account that will be used to repost content
- `target` is the username of the Instagram account that will be reposted
- `interval` is the interval in which the script will repost content
- `tags` is the list of tags that will be used to tag the reposted content

# Disclaimer
This script is for educational purposes only. I am not responsible for any misuse of this script. Use at your own risk. I am not responsible for any bans or suspensions that may occur from using this script.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details
