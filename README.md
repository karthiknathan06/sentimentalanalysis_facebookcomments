Sentimental Analysis for Facebook data

Problem statement:
“Public opinion in this country is everything”
-	Abraham Lincoln
The public opinion can have various effects on how policy is made or viewed by the government. It also makes the people to acquire trust from the government. Lack of trust comprises the willingness of citizens and business to respond to public policies and contribute to a sustainable economic recovery. The result will be healthy governance. As of now the only way to acquire public opinion is by conducting elections. Government is unable to get the voice of the normal people in their day to day activities/programs executed by them. 

Proposed solution:
As of the first quarter of 2018, Facebook had 2.19 billion monthly active users. And surprisingly India claimed the first place with 270 million users. Nowadays facebook is used by all sorts of people. Even a common man can easily access  social media. Nowadays government depends on some third party statistical analysis of finding people’s opinion. Their result brings a wide range of effects towards the government. Instead of depending on the other third parties, a page can be managed in the government website in which they can acquire public’s opinion in various ways.

Project Idea
By taking these point, that frequency of the usage and percentage of users of this social media.We are going to create a web portal which is governed by the state government, that give them provision to post their recent program or activity or an act or something that for people. These things are posted in facebook by the government. A proper time is given to the people for responding to their post. After processing these comments are extracted using graph API and then using python sentiment analysis using natural language processing toolkit, we can classify whether the comment is positive or negative or neutral. And we can provide as many insights from these comments.

Use Case
From this the government can understand whether this program will be useful or successful among those people. They can implement that program with the people moral support in a healthy way. And they can easily express their thoughts to their government. This increases trust of people to their government. This leads to a perfect way for a democratic nation.

Future Improvements

We can extend this project,

By providing live status by big data analytics.
By  extending this to different social media and based on the number of users we can come up with a result.
By using local language dataset and provide analysis result for specific language in that city.

Code explanation:

Libraries Used:
Flask framework 
Pandas: Data analysis tool
Requests:
Json: processing json files
nltk: The Natural Language Toolkit (NLTK) is a platform used for building Python programs that work with human language data for applying in statistical natural language processing (NLP). It contains text processing libraries for tokenization, parsing, classification, stemming, tagging and semantic reasoning.
	
	Vader: VADER (Valence Aware Dictionary for sEntiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity (strength) of emotion

Data Gathering:
The data set is gathered from facebook graph API by using testing authority. Still we didn’t deploy the project we are given limited access in the basis of time.

The data is gathered as a .Json file format and processed as dataframe in pandas using python as intermediate language.

Data processing:
The initial data is gathered and modified effectively for our convenience for analysis.

In facebook it is difficult to clean data since those comments are not appropriate.
They mention their name in their comments and it is not necessary for our decision making.
Hence this can be removed by use Pos tagging in python.
Pos tagging:  The process of classifying words into their parts of speech and labelling them accordingly is known as part-of-speech tagging, POS-tagging or simply tagging. Parts of speech are also known as word classes or lexical categories. 

And empty comments are not processed hence removed
 
This is our result where sentiments of each comments are listed.Since the prediction score is less as compared to vader lexicon, we have implemented our module using vader lexicon using flask framework in python


