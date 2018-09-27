class PrintReviews():

    def __init__(self):
        self = self


    def print_reviews(self, array, number_of_items):
        for review in array[:number_of_items]:
            print(review.title)
            print(review.score)
            print(review.review)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
