"""
This module is responsible for visualising the data using Matplotlib.
"""

"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.

Each function should visualise the data using Matplotlib.
"""
import matplotlib.pyplot as plt
import tui

def pie_chart(reviews_data):
    get_name = tui.hotel_name()
    negative = 0
    positive = 0

    for index in reviews_data:
        if get_name in index:
            if index[3] != "No Negative":
                negative += 1
            if index[4] != "No Positive":
                positive += 1
                
    print(f"{negative} {positive}")
    labels = [f"Positive Reviews: {positive}", f"Negative Reviews: {negative}"]
    sizes = [positive, negative]

    plt.pie(sizes, labels=labels)
    plt.show()

def num_of_reviews(reviews_data):
    pass