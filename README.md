
# SemesterProject
=======
#ReadMe
I started my work from the work proposed by Samuel Tokheim provided in this link https://github.com/samtokheim/datamining-yelp-categories

To test the code in your local machine you have to download the Yelp Academic Dataset from the link here https://www.yelp.com/academic_dataset . Then, unzip it in the code directory.

I provided the list of 5000 most common words in english from http://www.wordfrequency.info/top5000.asp so you don't need to download it.

You have to install mrjob who lets you write MapReduce jobs in Python 2.6+ and run them on several platforms:  $ pip install mrjob.

From the Academic Dataset you have to create some sub-datasets:
 * yelp_business.json - extracted all business listings from yelp_academic_dataset:
    grep 'type": "business' yelp_academic_dataset.json > yelp_businesses.json
 * review_set25000.json - manageable sized set of reviews:
    grep -m 25000 'type": "review' yelp_academic_dataset.json > review_set25000.json    
 * review_set.json - huge file of all the reviews. use if you have a powerful processor.    

#How to run the code?

1. Clone the content of the SemesterProject repository
2. Navigate to the directory
3. Run: $ python get_reviews_data.py
4. At the prompt type in a Yelp category of your choice
5. The results will be output to ‘reviews_data.[category].json’
6. Run: $ python business_sim.py < reviews_data.[category].json > [category].txt
7. Run: $ agglom_clusters.py
8. When asked for the input file choose the output file of the step 7. ( [category].txt )
9. Enter the tokheim-baker coefficient and wait for clusters to be formed. 

