# youtube-channel-keyword-searcher
Search video info by give keywords and channel name.

# Prerequisites:
1. Install python 3.6 or higher version
2. Run the following commands to install the library using pip:

`pip install --upgrade google-api-python-client`

`pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2`

3. Put the file **client_secret.json** in the same directory of **youtube_video_info_searcher.py**

# Quickstart
1. Create a CSV file in the format of **example.csv** which provides channel names and keywords (this file has no header). In this example, let's name it **example.csv**
2. Run the command at the directory of **youtube_video_info_searcher.py**

`python youtube_video_info_searcher.py example.csv 100`

The first parameter **example.csv** indicates the file name which contains the channel and keywords information.

The second parameter **100** indicates the approximately max number of results for each channel-keywords pair. The actual number of results may be more or less than the number you expect.

3. The console will show a link like:

`Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=xxxx`

`Enter the authorization code:   `

4. Click the link (or copy and paste in the browser) and use your Google account to login.
5. Copy and paste the authorization code shows in browser to the console.
5. If it runs well, a file named like **search_result_Mon Nov 19 17/51/54 2018_.csv** will be generated in the current directory