# Site Facets

## 1. Knowns

* the central "unit" of content is the Article
* Articles are stored in content/articles/(section)/(YEAR)/(MONTH)/(article-directory)
* We have detail pages (the Article page itself)
* We want LISTING pages (subsets of Articles, selected and ordered by rules)

### 1.1 The Article Universe

For a typical article, it could appear in a number of lists (subsets) of articles:

* If it's recent it might make it to the Home Page
    * This is basically a subset of Articles across the entire article "space"
      ordered newest first to some limit (which we haven't dealt with yet)
    * (let's ignore pagination for the moment, unless incorporating it at this
      juncture is strategically beneficial)
* If it's under the "historical" section then it might show up on an Article listing
    page with all the other "historical" articles

However, there are other facets:

* If it's tagged "galaxy" or "constellation: orion" then there might be pages generated
    for all the "galaxy" articles or the "constellation: orion" articles
* Search results create a custom subset

### 1.2 The Problem

1. While SOME of these facets are structural (you can pull the list from the structure
    of the /content/articles/ directory), others:
2. Might be programmatic (all the articles from 2026-05-12 to 2026-05-18 as a 
   "this week's articles" subset.
3. Still others might cross sections (via tags)

We don't want to hard-code "article listing pages" - but we want a way to define
how to generate a subset, and then display it the results.

This has the advantage of course, that aside from the core article list metadata 
(to get a proper Title for the list), that we only need one template for every list
that could ever be generated.

HOWEVER - this might not work on a static site, in which case we DO have to curate
and manage list definitions and their rules.

### 1.3 The other problems

1. We have to somehow come up with a design and navigation that is VERY EASY for the
user to comprehend.

2. We don't REALLY know the scope of the facets until we encounter them as "can we
do it THIS way"

3. We haven't discussed a search engine;  I don't even know if that's possible 
with a static page site.

## 2. The payoff

What this means is that as long as authors include things in the article headers
that mention some of the key terms that subset generators look for, and if we 
have a (nearly) unified templating, then the usefulness of the site increases
dramatically.  If the resultant listing page has a consistent URL, then those can
be shared as well "All the NBAS Events for 2027" - which ALSO MEANS that targeted
promotions are as easy as "assemble these articles and share".


