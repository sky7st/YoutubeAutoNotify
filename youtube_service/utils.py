import json
import re
import requests


def parse_YT_channel(channel_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept-Language": "zh-TW"
    }
    
    video_list = []
    
    url = f"https://www.youtube.com/channel/{channel_id}/videos?view=57&flow=grid"
    
    res = requests.get(url, headers=headers, verify=False)

    html = res.text
    
    if('window["ytInitialData"]' in html):
        pattern = r"window[\"ytInitialData\"] = (.*);"
    else:
        pattern = r">var ytInitialData = (.*?);</script>"
    
    # pattern = re.compile(pattern)
    matches = re.findall(pattern, html, re.MULTILINE)
    if len(matches) == 0:
        return None
    
    match = matches[0]
    js = json.loads(match)
    
    with open("test.json", "w+") as f:
        f.write(match)
    
    # for matchNum, match in enumerate(matches, start=1):
        
    #     print ("Match {matchNum} was found at {start}-{end}".format(matchNum = matchNum, start = match.start(), end = match.end()))
    # print(html)
    
    
if __name__ == "__main__":
    channel_id = "UC4Xs2rULr-dWKGSfVBWYdoQ"
    
    parse_YT_channel(channel_id)