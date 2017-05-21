#Measuring User Engagement with Stochastic Processes

The following plots depict the distributions of mean user-response times once they have entered a conversation with another user on the given subreddits. The elements of the histogram represent a user's mean response time, and the distribution is meant to reflect the general distribution of users.

##Histograms showing distribution results of popular subreddits:

###/r/math:

![/r/math distribution plot](https://github.com/alextairbekov/CSE392_Final_Project/tree/master/images/r_math.png)

Mean: 9860 s
Standard Deviation: 17783.27 s
Entries: 162 (over 100 posts)

###/r/books:

![/r/books distribution plot](https://github.com/alextairbekov/CSE392_Final_Project/tree/master/images/r_books.png)

Mean: 8198.1 s
Standard Deviation: 14456.28 s
Entries: 372 (over 100 posts)

###/r/programming:

![/r/programming distribution plot](https://github.com/alextairbekov/CSE392_Final_Project/tree/master/images/r_programming.png)

Mean: 4798 s
Standard Deviation: 6380.354 s
Entries: 151 (over 100 posts)

###/r/cpp (C++):

![/r/cpp distribution plot](https://github.com/alextairbekov/CSE392_Final_Project/tree/master/images/r_cpp.png)

Mean: 15999.5 s
Standard Deviation: 24059.69 s
Entries: 168 (over 100 posts)

###/r/Python:

![/r/Python distribution plot](https://github.com/alextairbekov/CSE392_Final_Project/tree/master/images/r_python.png)

Mean: 8124 s
Standard Deviation: 11568.83 s
Entries: 86 (over 100 posts)

##Interpretation

The shape of the following distributions imply that they could be gamma-distributed, as shown by the high frequency in response times within roughly 3 hours, with diminishing tails for responses after that. Popular non-technical subreddits like /r/books attract a lot of attention and thus, in our computations, have a record of 372 distinct conversations within 100 posts. 

###Further Investigation:

Our next steps would be to determine the distributions of response times as determined by the popuarity of a subreddit and how that would affect the Gamma-Distribution model for these mean-response times. Also, we intend to use the stochastic models developed by each user to see the user's change in activity by time (as some users are more active at different times of day, perhaps because they live in different time zones).

The purpose of this would be to determine the best time and location to post a query or inquiry, in order to determine a quick response. This did not take into account user popularity or how a post was rated, just the frequency with which a conversation could be made between two different users. The frequency of response times is clearly important and should be considered when making a post. 
