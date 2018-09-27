import requests
from review import Review
from printReviews import PrintReviews
from BeautifulSoup import BeautifulSoup

l = []
baseUrl = "https://www.dealerrater.com"
url = "https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/#link"
try:
    for page in range(0,5):
        response = requests.get(url)
        html = response.content
        soup = BeautifulSoup(html)
        reviews = soup.find(id="reviews")
        reviewEntries = reviews.div.div.findAll("div", "review-entry")

        for review in reviewEntries:
            rating = review.find("div", "dealership-rating").find("div", "rating-static")['class'][53:55]
            title = review.find("div", "review-wrapper").find("h3").text
            customerreview = review.find("div", "review-wrapper").find("p").text

            r = Review(title, rating, customerreview)
            r.score_review()
            l.append(r)


        nextpage = soup.find("div", "next").a['href']
        url = baseUrl + nextpage

except IOError:
    print("Error in processing the request. Please Try again")

l.sort(key=lambda x: x.score, reverse=True)

PrintReviews().print_reviews(l, 3)
print(len(l))
