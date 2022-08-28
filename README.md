# subreddit-collector-script
This script allows users to collect specified number of hot reddit posts from the specified subreddit. The data collected from the posts can be accessed via a csv file created by the script. It requires the use of a reddit account to acquire access to the reddit api. I plan to use this to collect data for some of my personal NLP projects.

### Configuration
1. Clone this repository
2. Install required libraries: `pip install pandas praw`
3. Add a `.env` file with the following environment variables:
    - CLIENT_ID : can be obtained from https://www.reddit.com/prefs/apps with a valid reddit account
    - CLIENT_SECRET: can be obtained from https://www.reddit.com/prefs/apps with a valid reddit account
    - REDDIT_USERNAME: username for the reddit account used to get the CLIENT_ID and CLIENT_SECRET
    - PASSWORD: password for the reddit account used to get the CLIENT_ID and CLIENT_SECRET
    
### Usage
The script can be called from the CLI by providing the subreddit name and number of hot posts.
Example: `python subreddit_collector.py github 1000` can be used to get 1000 hot posts from the github subreddit.
