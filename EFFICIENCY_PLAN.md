# Increasing disk use/image size efficiency

The issue:
1. content/ is the largest disk/image usage (expected)
2. A given article can be up to 20MB+
3. Likely causes:
  - article images are bloated more than they need to be
  - images not used are present and should be removed

## WHAT I WANT:
- a script that I can run on any directory that:
   1. analyzes the content versus what's in the index.md file
   2. reports on inefficient usage:
      - media that should be made smaller
         - this would be based on what is necessary for a WEBSITE
         - I know that the present nbas-image allows for clicking on an image to make it larger and sometimes we WILL want to do that.   But even so, we have to be understanding that we have limitations and it might not be practical to have a 2000px image rendered to 900px (or whatever the fullwidth size it in the CSS/rendering).   
      - media that is not necessary

The script should also have a --fix flag that:
   - runs sips (or does anything internal) to create the appropriate file
   - converts files from an inefficient file format to one that will use less space
   - updates the index.md file to point to the correct file (if it is replaced)
   - cleans up 
   - reports on savings

## GOALS:

1. Any given article directory should be < 2 MB, ideally ~1 MB
   - this might not be practical for EVERY article, of course



