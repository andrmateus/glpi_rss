import rfeed

class generateFeedRss:
    def create(self, dataFrame):
        items = []
        for val in dataFrame.index:
            items.append(
                rfeed.Item(
                    title="{} - {} - {}".format(dataFrame['id'][val], dataFrame['last_update'][val], dataFrame['user'][val]),
                    link=str(dataFrame['url'][val]),
                    description="Ticket GLPI"
                )
            )

        feed = rfeed.Feed(
            title="GLPI TICKETS", 
            link="links", 
            description="description",
            items=items
        )
        return(feed.rss())