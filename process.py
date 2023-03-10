"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""
import tui

def total_retrieval(reviews_data):
    tui.total_reviews(len(reviews_data))
    
def name_retrieval(reviews_data):
    user_name = tui.hotel_name()
    for line in reviews_data:
        if user_name in line:
            print(line)
         
def dates_retrieval(reviews_data):
    user_date = tui.review_dates()
    i = [x[0] for x in reviews_data]
    if user_date in i:
        for x in range(0,len(reviews_data)):
            if user_date == reviews_data[x][0]:
                print(reviews_data[x])
    
def nationality_retrieval(reviews_data):
    tui.display_reviews(reviews_data, 2)
    
def summary(reviews_data):
    negative_reviews =  0
    positive_reviews = 0
    average = []
    
    for index in reviews_data:
        if index[5] != "":
            average.append(float(index[5]))
        if index[3] != "No Negative":
            negative_reviews += 1
        if index[4] != "No Positive":
            positive_reviews += 1
            
    average_rating = sum(average)/len(average)
    return negative_reviews, positive_reviews, round(average_rating,1)