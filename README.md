# The Course Catalog API Cache
## Overview/FAQs
- What is a "course catalog API"?
    - The [course catalog API](https://github.com/sandboxnu/course-catalog-api) is an API to access Northeastern University's course catalog (containing section, class, and employee data).
- So what's a "course catalog API cache"?
    - Read the documentation [here](https://apidocs.searchneu.com/#/getting-started/stored-cache). If this link is dead, we may have changed the doc structure, so just go to [apidocs.searchneu.com](https://apidocs.searchneu.com) and search for "cache".
    - Long story short - it caches our scrapers' network requests to Banner, Northeastern's official course catalog. Our calls are rate-limited, so for development purposes, we cache those requests to make it easier for devs.
- How can I use this?
    - See the documentation link above
- How can I combine caches?
    - Run them one by one (ie. import one cache, run `yarn scrape`, delete the cache, and import the next). Every time you run `yarn scrape`, the data in your database will be updated with the new data (but will keep the old data as well).