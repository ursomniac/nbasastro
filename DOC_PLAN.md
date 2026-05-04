# NBAS website - documentation pass

- All the documentation is under the /members part of the site
   - This is not public-facing
- We need to be able to show Markdown code for examples as well as rendered examples (screen shots are ok)
   - But we should have the files available as templates

## Pathways

Because the members who will be writing articles have a wide range of technical expertise, 
we want to make it possible for any of them to feel confident about making articles.

Thus I have 3 "pathways" to do this:

### Pathway 1.  Git workflow - submitting content as a feature branch
Prerequisites:
   1. User installs the repo locally
   2. User spins up local site with hugo on localhost:1313
Article Creation:
   1. User pulls main
   2. User cuts a branch from main:  username-YYMMDD
   3. User creates a new article directory under /content/articles/YYYY/MM/(new-directory)
   4. User generates an index.md file
   5. User writes the article and tests it locally
      - User adds media to the directory
   6. When finished user makes a push request via git

This has several potential issues, esp. surrounding git workflows.  We have to be very careful that the instructions don't lead to unforseen situations.

### Pathway 2.  semi-Git workflow - only pull submit article directories ZIP through email
Prerequisites:
   1. User installs the repo locally
   2. User spins up local site with hugo on localhost:1313
Article Creation:
   1. User pulls main
   2. User creates a new article directory under /content/articles/YYYY/MM/(new-directory)
   3. User generates an index.md file
   4. User writes the article and tests it locally
      - User adds media to the directory
   5. When finished, user creates a ZIP file from the new directory and emails it for approval

### Pathway 3.  No technical expertise - submit article content in any form, ZIP + email
Prerequisites: None
Article Creation:
   1. User writes an article in a preferred format in a directory
      - User adds media to the directory
   2. User creates a ZIP file of the directory and emails is for approval

## Issues surrounding articles
   1. Markdown templates can be constructed from the Article Builder (already written)
   2. Adjustments to metadata CAN be made (with caveats)
      - We need to be able to instruct them how to change the metadata if the generated file doesn't have everything: e.g., if they want to add another Messier object, etc.
   3. Media might have to be adjusted (we don't want very large files), so instructions for how to do that (in general, e.g., the "sips" command on Mac OS Terminal)


