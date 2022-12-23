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
from statistics import mean

def total_retrieval(reviews_data):
    tui.total_reviews(len(reviews_data))
    
def name_retrieval(reviews_data):
    user_name = tui.hotel_name()
    for user_name in reviews_data:
        print(f"{user_name}")
         
def dates_retrieval(reviews_data):
    user_date = tui.review_dates()
    for user_date in reviews_data:
        return user_date
    
def nationality_retrieval(reviews_data):
    tui.display_reviews(reviews_data, 2)
    
def summary(reviews_data):
    index1 = 3
    index2 = 4
    index3 = 5
    sum_review = {"negative_reviews": 0, "positive_reviews": 0, "average_rating": ""}
    for review in reviews_data:
        count = review[index1]
        count2 = review[index2]
        count3 = review[index3]
        if count in reviews_data:
            sum_review["negative_reviews"] += 1
        elif count2 in reviews_data:
            sum_review["positive_reviews"] += 1
        elif count3 in reviews_data:
            sum_review["average_rating"] = mean(count3)
    tui.total_reviews(sum_review)