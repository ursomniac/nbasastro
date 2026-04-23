---
title: "Website Concepts"
date: 2026-04-22
layout: "members"
---

# How the Site is Laid Out

Welcome to the NBAS Website!   

This site has the potential for being an incredible resource.  It has some fundamental
features:

1. It is RESPONSIVE: it works on desktops, tablets, and phone
2. It is STATIC: all content is generated at public time - this make it fast and less prone to run-time errors
3. It is COLLABORATIVE: it is design for members to be able to contribure content, either one-off articles, or articles in a Series.   

## 1. Articles

The fundamental building block of the entire site is the **Article**.  
Basically it's a page.  And pages can include text, and media 
(images, video, audio, PDF pages, etc.).

Articles contain **Metadata** (also called "the front matter") at the top.  This is 
where you set all the parameters that Hugo uses to generate the page and link it to
other pages - for the most part this all happens "behind the scenes":  aside from 
setting the metadata, everything else is content.

## 2. Site Sections

On the site things are built in sections.  Some sections are lists of Articles
(like the Utility pages in the footer).  Mostly they're all collections of Articles
filter and arranged in certain ways.  Again - you don't have to do any of that, aside
from telling Hugo in the Metadata all the things you want to associate with your
Article.

Let's look at the Navbar - some of the links are sections:

    * All Articles - this is a paginated list of all the published articles on the site,
paginated.  

    * Tags - this organizes all the articles by the **Tags** that were assigned.  You can
define new Tags as you need them - there's no setup for "add a new Tag" - just use it
(it's defined in the Metadata) and the page for that Tag just appears.

    * DSO Catalog - this organizes all the articles related to one or more DSOs.  We've subdivided it into four subgroups: "Messier", "Caldwell", "NGC", and "Other" - so if you
want to find all the Articles on M 33, they'll all be grouped there.

    * Solar System - similar but for SSOs:  Sun, Moon, Planets, Comets, Asteroids, and Meteors. 

## 3. Series 

The other organizational structure is the **Series* - basically an Article _can_ be part of a series (it doesn't have to - many won't).   The NBAS monthly newsletter?  That's a **Series**.  So are NBAS Events pages, and Announcements.   So are the monthly "Constellation Highlights".   Series Articles don't have to come out regularly or on a schedule - they're just lumped together.   

Creating a new Series is as simple as defining it in your Article's metadata: if you're 
expecting to be creating a series of articles on "News about Smart Telescopes" that might
an Article every now and then, start a "Smart Telescope" Series and then it will be 
easy for users to find all of them conveniently.

In lists of Articles, each Article's "card" shows the Series it belongs to (if it does).

## 4. Tags

We mentioned Tags above.   Tags are great because you can link articles on the same 
topic together without having to worry about setting anything up on the site.  

Example: say you've observed a recent supernova in M 101.   You write an article about
it, showing your cool image.  You can Tag the article "Supernova" or "Extragalactic 
Supernova" and then it'll have links to any _other_ article that has the same tag.

(Note that in this case, you'd ALSO want to put the DSO reference to M 101 too so it'll 
show up on the "DSO Catalog - Messier" page as well!  And of course it'll be in 
"All Articles" AND on the Home page for a while.)

