<<<<<<< HEAD
# SemesterProject
=======
#ReadMe
I started my work from the work proposed by Samuel Tokheim provided in this link https://github.com/samtokheim/datamining-yelp-categories

To test the code in your local machine you have to download the Yelp Academic Dataset from the link here https://www.yelp.com/academic_dataset . Then, unzip it in the code directory.

I provided the list of 5000 most common words in english from http://www.wordfrequency.info/top5000.asp so you don't need to download it.

You have to install mrjob who lets you write MapReduce jobs in Python 2.6+ and run them on several platforms:  $ pip install mrjob.


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
>>>>>>> 8a2b0a1ef4dfcbe99535ea9cc9c08b9478975dff
