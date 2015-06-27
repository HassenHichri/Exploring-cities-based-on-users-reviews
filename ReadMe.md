
# SemesterProject
=======

This work is part of 3cixty project (www.3cixty.com).

In this project, we aim to identify sub-categories for predefined top categories for businesses in the 3cixty dataset using data mining techniques on review text contents.

We started the work with the yelp academic dataset (www.yelp.com/academic_dataset) and we get inspired from topics tackled by teams in the Yelp Dataset Challenge (www.yelp.com/dataset_challenge).

I provided the list of 5000 most common words in english from http://www.wordfrequency.info/top5000.asp so you don't need to download it.

You have to install mrjob who lets you write MapReduce jobs in Python 2.6+ and run them on several platforms:  $ pip install mrjob.

The 3cixty dataset can be downloaded from www.3city.eurecom.fr/sparql by running this sparql query:

 					select distinct ?s ?o1 as ?review ?id ?top where {
 					 ?s a schema:Review;
 					 schema:reviewBody ?o1;
 					 schema:itemReviewed ?o.
 					 ?o owl:sameAs ?id;
 					 locationOnt:businessTypeTop ?top .
 					 FILTER ( lang(?o1) = "en" || lang(?o1) = "en-tr" )
 					}

PS: You can use 3cixty_dataset_top.json that you find in this repository. It respects the formatting for loading it with python.

The Yelp Academic Dataset is available via this link: www.yelp.com/academic_dataset. Once downloaded, you have to create two sub-datasets (one for reviews and one for businesses). To do so, run this shell commands on your terminal:

		grep 'type": "business' yelp_academic_dataset.json > yelp_businesses.json
		grep 'type": "review' yelp_academic_dataset.json > review_set.json 

#How to run the code?

1. Clone the content of the SemesterProject repository
2. Navigate to the directory
3. Run: $ python get_reviews_data.py
4. At the prompt type 3cixty or yelp to choose which dataset you will work with.
5. At the prompt type in a 3cixty or a yelp category of your choice
6. The results will be output to ‘reviews_data.[category].json’
7. if you chose Yelp, run: $ python business_sim_yelp.py < reviews_data.[category].json > [category].txt
   if you chose 3cixty, run: $ python business_sim_cixty.py < reviews_data.[category].json > [category].txt
8. Run: $ agglom_clusters.py
9. When asked for the input file choose the output file of the step 7. ( [category].txt )
10. Enter the tokheim-baker coefficient and wait for clusters to be formed. 

#References

This work was inspired by the work done by Ryan Baker and Sam Tokheim from UC Berkley School of Information (http://www.ischool.berkeley.edu/courses/i290-dma) and "Generating Recommendation Dialogs by Extracting Information from User Reviews" done by Dan Jurafsky, Adam Vogel and Kevin Reschke from Stanford University (http://nlp.stanford.edu/projects/yelp.shtml)

