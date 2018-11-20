# youtube-channel-keyword-searcher
Search video info by give keywords and channel name.

# Prerequisites:
1. Install python 3.6 or higher version
2. Run the following commands to install the library using pip:

`pip install --upgrade google-api-python-client`

`pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2`

3. Put the file **client_secret.json** in the same directory of **youtube_video_info_searcher.py**

# Quickstart
1. Create a CSV file in the format of example.csv which provides channel names and keywords (this file has no header). In this example, let's name it **example_keywords.csv**
2. Run the command at the directory of **youtube_video_info_searcher.py**

`python youtube_video_info_searcher.py example_keywords.csv`

3. If it runs well, a file named like **search_result_Mon Nov 19 17/51/54 2018_.csv** will be generated in the current directory