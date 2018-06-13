from instagram.client import InstagramAPI
import json, math
import requests
from operator import itemgetter
import pandas as pd

class tag_recommender(object):

    def __init__(self, parameters):
        self.access_token = parameters.get("access_token","ACCESS_TOKEN")
        self.client_secret = parameters.get("client_secret","CLIENT_SECRET")
        self.limit = parameters.get("limit",50)
        self.searchType = parameters.get("search_type","breadth")
        self.no_of_days_before = parameters.get("days_before",1)
        self.api = InstagramAPI(access_token=self.access_token, client_secret=self.client_secret)

    def tag_score(self,multiple_tags):
        complete_data = []
        rank=0
        for tag in multiple_tags:
            response = requests.get('https://api.instagram.com/v1/tags/'+tag+'?'+'access_token='+self.access_token)
            if response.status_code ==200:
                response_json_data = json.loads(response.text)
                tagname_and_mediacount = response_json_data['data']
                complete_data.append(tagname_and_mediacount)
        complete_data = sorted(complete_data, key=itemgetter('media_count'),reverse=True)
        df = pd.DataFrame(complete_data)
        df['rank'] = df['media_count'].rank(ascending=False).astype(int)
        df.rename(columns={'media_count':'Social media score'},inplace=True)
        return(df[df.columns[::-1]].to_string(index=False))

if __name__ == "__main__":
    parameters = {}
    obj = tag_recommender(parameters)
    tags = ["india",'pakisthan']
    result = obj.multiple_insta_tag(tags)
    print(result)
