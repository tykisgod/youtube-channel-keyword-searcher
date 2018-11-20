# youtube-channel-keyword-searcher
Search video info by give keywords and channel name.

# Prerequisites:
1. Install python 3.6 or higher version
2. Run the following commands to install the library using pip:

`pip install --upgrade google-api-python-client`

`pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2`

3. Put the file **client_secret.json** in the same directory of **youtube_video_info_searcher.py**. (Read 'Before you start' section in this [page](https://developers.google.com/youtube/v3/getting-started) if you want to use your own credentials instead of existing one)

# Quickstart
1. Create a CSV file in the format of **example.csv** which provides channel names and keywords (this file has no header). In this example, let's name it **example.csv**

     But you should notice that the channel name in the first column of this csv file should be the name in its url. Say, the channel name of UMG should be **universalmusicgroup** in the last part of the channel url: https://www.youtube.com/user/universalmusicgroup instead of the name 'Universal Music Group' shows in that page.

2. Run the command at the directory of **youtube_video_info_searcher.py**

`python youtube_video_info_searcher.py example.csv 2`

The first parameter **example.csv** indicates the file name which contains the channel and keywords information.

The second parameter **2** is the max page number (each page contains at most 50 results) which indicates the max number of results for each channel-keywords pair.

So in this case, we can get at most 2*50 results for each channel-keyword pair. We have 2 channel-keyword pairs in **example.csv**, so we will have at most 2\*2\*50 = 200 results in the output csv file.

3. The console will show a link like:

`Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=xxxx`

`Enter the authorization code:   `

4. Click the link (or copy and paste in the browser) and use your Google account to login.
5. Copy and paste the authorization code shows in browser to the console.
5. If it runs well, for each channel-keyword pair, a file named like **channel_universalmusicgroup_keyword_taylor_result_at_2018-11-20 12/56/58_.csv** will be generated in the current directory. The default order of the results is based on relevance