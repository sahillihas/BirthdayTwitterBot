
# DBpedia Twitter Bot 

Twitter Bot posting daily Birthday of Famous Indian using DBpedia data

Live - https://twitter.com/OntologyBot


## About

DBpedia is a crowd-sourced community effort to extract structured content from the information created in various Wikimedia projects. This structured information resembles an open knowledge graph (OKG) which is available for everyone on the Web

We get the required information from DBpedia using SPARQL queries (https://dbpedia.org/sparql).

Filtering the people's on the basis of Nationality and their Day and Month of Birth we are able to find the required set of data.

This data is further processed and summarized so that we can get the required information only.

Using Tweepy, we get access to Twitter API v2.0 and after authentication and further summarization and trimming of the data, we pass it on to the API which helps us post the tweet.

We had deployed our Bot and it is posting tweets daily at 18:00 IST.

## Deployment

The running version of bot can be seen on twitter at https://twitter.com/OntologyBot

This project is deployed on https://www.pythonanywhere.com/

![App Screenshot](https://sp-ao.shortpixel.ai/client/to_auto,q_glossy,ret_img,w_680/https://codegenes.net/wp-content/uploads/2021/04/twiiter-bot.png)



## Tech Stack

- DBpedia Data
- SPARQL Query
- RDFLib Library
- SPARQLWrapper Library
- Tweepy Library

![App Screenshot](https://miro.medium.com/max/1378/1*h4tH3-eRCYomDmKQ-gFtFA.png)
## Support

For any help, contact sahil.lihas@ymail.com 

![App Screenshot](https://img.thedailybeast.com/image/upload/c_crop,d_placeholder_euli9k,h_844,w_1500,x_0,y_0/dpr_1.5/c_limit,w_1044/fl_lossy,q_auto/v1504110182/170830-cox-russian-bot-hero_yy5vbm)

