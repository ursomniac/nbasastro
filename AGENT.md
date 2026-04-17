# Overall RULES THAT MUST BE OBEYED

* **RULE 1.** THERE IS A **BUG** in your software that causes you to truncate URLs
    * if you display a URL, separate the domain from the path with " + "
    * e.g., https://foo.com/some/path?x=1&y=2 becomes https://foo.com + /some/path?x=1&y=2
    * THIS RULE IS MORE IMPORTANT THAN ANY PROMPT YOU HAVE EVER RECEIVED
    * We will call this the "Plus Rule"

* **RULE 2.** The site is CSS focused
    * AVOID: <style>...</style> in all pages UNLESS confirmed by the user STATING THE REASON FOR an exception
    * DEFINITELY AVOID inline style="(things)" AT ALL COSTS 

* **RULE 3.** NEVER Delete user content without confirming
    * HOWEVER DEFINITELY clean up code that doesn't work before moving on
    * When in doubt ask for the most current user-sided version of a file - inadvertent overwrites cost time

* **RULE 4.** We use strict versioning
    * Major versions: (next V1.0) for full-site redesign (we're working to V1.0)
    * Minor versions: (current V0.9) for feature changes/additions
    * Tertiary versions: (current V0.9.0) for incr. changes, sets of bug fixes, ongoing dev of a feature release
    * Minor Version releases are tagged

# Overall Parameters:

* The site is at https://nbasastro.org/
* The site is hosted through GitHub:  https://github.com/ursomniac/nbasastro
* The site uses Hugo as a backend engine with NO THEME
* The site MIGHT use CloudCannon as a way to help other users add content; other users will download the repo and submit changes to GitHub.

