import json 
import re



# Create array of common stop words
stop_words  = set(['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your'])

cw = open('5kcommonwords.csv','rb')
# Create array of 5000 most common English words
common_words = []
for line in cw.readlines():
    a = line.split(',')
    word = a[1]
    word = word.lower()
    common_words.append(word)
cw.close()

# Instantiate set for storing business ids
biz_ids = set()
 
# This function looks for businesses that have a category that matches the user input.
def get_reviews_3cixty(business_data, review_data, category, filename):

    #Open file that will be used to store reviews data
    r = open(filename,'w')

    print('Looking for '+category.lower()+' businesses...')

    #Go through each line and if the category matches the user input add it to the biz_ids set 
    for line in review_data:
        line = json.loads(line)
        categ = re.split('\/',line['top']['value'])
        if category.lower() == categ[-1].lower():
            biz_id = re.split('\/',line['id']['value'])
            biz_ids.add(biz_id[-1])
    
    #Go through the data again, this time looking for reviews. If the review business id matches an id
    #found in biz_ids, write the line to the text file
    for line in review_data:
        line = json.loads(line)
        bis_id = re.split('\/',line['id']['value'])
        if bis_id[-1] in biz_ids:
            review_words = line['review']['value'].split()
            

            #Create new array that will replace the existing one found at line['text']
            cleaned_review_words = []

            #Iterate through each word in each review, lower the word, and remove any non-word characters
            for word in review_words:
                word = word.lower()
                word = re.sub(r'\W','', word)
                word = re.sub(r'^[0-9]+$','', word)
                
                #Check to see if the word is either a stop word or a common word. If it is, exclude it
                if word != '' and word not in common_words and word not in stop_words:
                    cleaned_review_words.append(word)
                

            #Update the line with the new truncated list of words   
            line['review']['value'] = cleaned_review_words

            #Write out the line in JSON format
            r.write(json.dumps(line))
            r.write('\n')
            
    if len(biz_ids)==0:
        return False
    else:
        return True

    r.close()    

# This function looks for businesses that have a category that matches the user input.
def get_reviews_yelp(business_data, review_data, category, filename):

    #Open file that will be used to store reviews data
    r = open(filename,'w')

    print('Looking for '+category.lower()+' businesses...')

    #Go through each line and if the category matches the user input add it to the biz_ids set 
    for line in business_data:
        line = json.loads(line)
        if line['type'] == 'business':
            categories = [w.lower() for w in list(line['categories'])]
            if category.lower() in categories:
                biz_ids.add(line['business_id'])        

    #Go through the data again, this time looking for reviews. If the review business id matches an id
    #found in biz_ids, write the line to the text file
    for line in review_data:
        line = json.loads(line)
        if line['type'] == 'review' and line['business_id'] in biz_ids:
            review_words = line['text'].split()

            #Create new array that will replace the existing one found at line['text']
            cleaned_review_words = []

            #Iterate through each word in each review, lower the word, and remove any non-word characters
            for word in review_words:
                word = word.lower()
                word = re.sub(r'\W','', word)
                word = re.sub(r'^[0-9]+$','', word)
                
                #Check to see if the word is either a stop word or a common word. If it is, exclude it
                if word != '' and word not in common_words and word not in stop_words:
                    cleaned_review_words.append(word)

            #Update the line with the new truncated list of words   
            line['text'] = cleaned_review_words

            #Write out the line in JSON format
            r.write(json.dumps(line))
            r.write('\n')
            
    if len(biz_ids)==0:
        return False
    else:
        return True

    r.close()    


       
#Menu that takes user input for the choice
def choose(makeAchoice,resultsFound):

    while makeAchoice == False:
        myChoice = raw_input('choose yelp or 3cixty dataset: ')
        myChoice = str(myChoice)
        myChoice_str = myChoice.replace(" ", "_").lower()
        if myChoice_str == 'yelp':
            print('you choose '+myChoice_str)
            makeAchoice = True
            f = open('yelp_business.json', 'rb')
            g = open('review_set.json', 'rb')
            business_data = f.readlines()
            review_data = g.readlines()
            f.close()
            g.close()
            while resultsFound == False:
                category = raw_input('Type in a business category (e.g. indian, massage): ')
                category = str(category)
                category_str = category.replace(" ", "_").lower()
                filename = "reviews_data." + category_str + ".json"
                resultsFound=get_reviews_yelp(business_data,review_data,category,filename)
                if resultsFound == False:
                    print('No results found for '+ category+ ', please try again: ')
            print(str(len(biz_ids))+' businesses found. Your data was output to ' + str(filename))
        
        elif myChoice_str == '3cixty':
            print('you choose '+myChoice_str)
            makeAchoice = True
            f = open('3cixty_dataset_top.json', 'rb')
            g = open('3cixty_dataset_top.json', 'rb')
            business_data = f.readlines()
            review_data = g.readlines()
            f.close()
            g.close()
            while resultsFound == False:
                category = raw_input('Type in a business top category (e.g. food, shopservice ...): ')
                category = str(category)
                category_str = category.replace(" ", "_").lower()
                filename = "reviews_data." + category_str + ".json"
                resultsFound=get_reviews_3cixty(business_data,review_data,category,filename)
                if resultsFound == False:
                    print('No results found for '+ category+ ', please try again: ')
            print(str(len(biz_ids))+' businesses found. Your data was output to ' + str(filename))
        else:
            print('Please make the choice between yelp and 3cixty!')
            makeAchoice = False
    
choose(False,False)    
    



   

    

