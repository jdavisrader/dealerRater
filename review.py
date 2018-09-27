class Review(object):
    score = 0

    def __init__(self, title, rating, review):
      self.title = title
      self.rating = int(rating)
      self.review = review


    def score_review(self):
        self.score = (self.review.count("wonderful") * 3) + (self.review.count("painless") * 2) + (self.review.count("fantastic") * 3) + (self.review.count("thank you") * 4) + (self.review.count("perfect") * 4) + (self.review.count("hassle free") * 2) + (self.review.count("pleasure") * 3) + (self.review.count("appreciate") * 4) + (self.review.count("knowledgable") * 3) + (self.review.count("patient") * 2) + (self.review.count("excellent") * 3)
        positiveWordCount = self.review.count("painless") + self.review.count("fantastic") + self.review.count("thank you") + self.review.count("perfect") + self.review.count("hassle free") + self.review.count("pleasure") + self.review.count("appreciate") + self.review.count("knowledgable") + self.review.count("patient") + self.review.count("excellent")

        ratio = int(float(positiveWordCount)/float(len(self.review.split())) * 1000)

        if ratio > 50:
            self.score += 5
        elif ratio > 40:
            self.score += 4
        elif ratio > 30:
            self.score += 3
        elif ratio > 10:
            self.score += 1
        else:
            self.score += 0

        if self.rating > 30:
            self.score += 0
        elif self.rating < 41:
            self.score += 1
        elif self.rating < 46:
            self.score += 4
        elif self.rating < 48:
            self.score += 5
        else:
            self.score += 7
