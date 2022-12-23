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
    user_date = tui.review_dates
    return user_date
    
def nationality_retrieval(reviews_data):
    tui.display_reviews
    
def summary():
    pass

my_list = ["10/08/2016,K K Hotel George,United Kingdom,The bed mattress was too hard without the mattress topper on which we removed because it made us hot The mattress was orthopaedic firm,Staff were very helpful,7.9,1,[' Leisure trip ', ' Couple ', ' Classic Double Room ', ' Stayed 2 nights ', ' Submitted from a mobile device '],299 day", "04/05/2017,Apex Temple Court Hotel,United Kingdom,A few more little milks maybe as I drink a lot of tea but I was given a little jug of milk when I asked,The bathroom was light pleasant and very clean The wardrobe space was good and there were tea making facilities The bed was comfortable,10,2,[' Leisure trip ', ' Couple ', ' City King Room ', ' Stayed 4 nights ', ' Submitted from a mobile device '],120 day", "01/04/2017,Apex Temple Court Hotel,United Kingdom,No Negative,Large bathroom with great elemis toiletries comfortable and king size bed,9.2,4,[' Leisure trip ', ' Solo traveler ', ' Superior King Room with Balcony ', ' Stayed 1 night '],211 day"]