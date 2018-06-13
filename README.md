# Trending-Social-media-celebrity-bot
Language: Python
Dependencies: requests ($ pip install requests)
              pandas ($ pip install pandas)
              json ($ pip install simplejson)
              operator ($ pip install operator)

INPUT:
  A List(or array or dataFrame)of celebraties.
  Example:["beyonce","taylor swift","cristiano ronaldo","Roger Federer"]
  Input can be of any size.
  note:spaces are not encouraged in names.
     example- "Christiano ronaldo" ---> "Christianoronaldo" 
  
PROCESS:
  Computes Facebook,Instagram and Twitter scores of each celebrity. 
  Social_media_score = Facebook_score + Instagram_score + Twitter_score
  Ranking is given based on Social_media_score

OUTPUT:
  rank              name  Social media score
     1       taylorswift            13906499
     2           beyonce            12173563
     3  cristianoronaldo             3507576
     4      rogerfederer              411846
