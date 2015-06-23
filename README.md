
# SemesterProject
=======

This work is part of 3cixty project (www.3cixty.com).

In this project, we aim to identify sub-categories for predefined categories for restaurants in the 3cixty dataset using data mining techniques on review text contents.

I provided the list of 5000 most common words in english from http://www.wordfrequency.info/top5000.asp so you don't need to download it.

You have to install mrjob who lets you write MapReduce jobs in Python 2.6+ and run them on several platforms:  $ pip install mrjob.

The 3cixty dataset can be downloaded from www.3city.eurecom.fr/sparql by running this sparql query:

 select distinct ?s ?o1 as ?review ?id ?category ?top where {
  ?s a schema:Review;
  schema:reviewBody ?o1;
  schema:itemReviewed ?o.
  ?o owl:sameAs ?id;
  locationOnt:businessType ?category;
  locationOnt:businessTypeTop ?top .
  FILTER ( lang(?o1) = "en" || lang(?o1) = "en-tr" )
 }
PS: You can use 3cixty_dataset.json that you find in this repository

#How to run the code?

1. Clone the content of the SemesterProject repository
2. Navigate to the directory
3. Run: $ python get_reviews_data.py
4. At the prompt type in a 3cixty category of your choice
5. The results will be output to ‘reviews_data.[category].json’
6. Run: $ python business_sim.py < reviews_data.[category].json > [category].txt
7. Run: $ agglom_clusters.py
8. When asked for the input file choose the output file of the step 7. ( [category].txt )
9. Enter the tokheim-baker coefficient and wait for clusters to be formed. 

#References

This work was inspired by the work done by Ryan Baker and Sam Tokheim from UC Berkley School of Information (http://www.ischool.berkeley.edu/courses/i290-dma)

