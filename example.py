__author__ = 'Alexandre'
from crawler import Crawler

if __name__ == "__main__":
    #WARNING!!!!!!!!!
    #The following code runs a crawler that has the potential to download thousands
    #of files in a very short lapse of time. Let it run for a day and you will proba-
    #bly bust your ISP download limit for the month. Just saying... ;)

    #Instantiate a Crawler object using 50 spider processes and 20 document processing processes.
    #This crawler searches for jpg images to index. The do_not_crawl list could be used to specify
    #not to crawl *.google.*, but in this case we use a regex to restrict crawling to *.google.*
    myCrawler = Crawler(n_spiders=50,
        n_document_processors=20,
        seeds=['http://www.google.com'],
        indexable_content_types=[('jpg', 'image/jpg')],
        do_not_crawl=['^((?!(\.)(google)(\.)).)*$']
    )
    #For more Mime types, please refer to the following link:
    #http://reference.sitepoint.com/html/mime-types-full

    #Start the crawler
    myCrawler.start()

    raw_input("Press Enter to stop crawling...\n")

    #Stop the crawler
    myCrawler.stop()
