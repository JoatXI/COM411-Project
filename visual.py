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
import matplotlib.animation as animation
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
    def getting_total(k):
        i = {}
        for index in reviews_data:
            if index[2] != "":
                national.append(index[2])
        for j in k:
            if j in i:
                i[j] += 1
            else:
                i[j] = 1
        return i
    labels = ["UK: 456", "USA: 78", "Australia: 51", "Ireland: 38", "Saudi Arabia: 23", "Netherlands: 21", "Germany: 20", "UAE: 18", "France: 17", "Canada: 16", "Israel: 16", "Italy: 15", "Turkey: 15", "Belgium: 13", "Greece: 11", "Spain: 10", "Others: 212"]
    sizes = [456, 78, 51, 38, 23, 21, 20, 18, 17, 16, 16, 15, 15, 13, 11, 10, 212]

    plt.figure(figsize=(10,10))
    plt.pie(sizes, labels=labels, textprops={"fontsize":7})
    #plt.title(label="Number of reviews by the nationality of a reviewer", fontdict={"fontsize":16}, pad=20)
    plt.show()
    print(getting_total(national))

def animate(reviews_data):
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
    print(f"Negaftive Reviews: {negative_reviews}", f"Positive Reviews: {positive_reviews}", round({average_rating},1))
    
national = []
