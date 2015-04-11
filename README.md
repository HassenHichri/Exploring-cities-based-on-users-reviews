#ReadMe
I started from the code proposed by Samuel Tokheim provided in this link https://github.com/samtokheim/datamining-yelp-categories

To test the code in your local machine you have to download the Yelp Challenge Dataset from the link here http://www.yelp.com/dataset_challenge. Then, unzip it in same directory with the code: we will use yelp_academic_dataset_business.json and yelp_academic_dataset_reviews.json .

I provided the list of 5000 most common words in english from http://www.wordfrequency.info/top5000.asp so you don't need to download it.

You have to install mrjob who lets you write MapReduce jobs in Python 2.6+ and run them on several platforms:  $ pip install mrjob.


#How to run the code?

1. Clone the content of the SemesterProject repository
2. Navigate to the directory
3. Run: $ python get_reviews_data.py
4. At the prompt type in a Yelp category of your choosing
5. The results will be output to ‘reviews_data.[category].json’
6. Run: $ python business_sim.py < reviews_data.[category].json > biz_results.[category].txt
7. Run: $ agglom_clusters.py
