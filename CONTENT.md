# NBAS content structure

## 1. Articles

* Articles should include
  * Title (required)
  * Author (optional)
  * Byline (optional - but useful for digestifying in lists of articles)
  * Tags (optional - but useful for finding similar articles across the site)
  * Feature (optional, but ideally MOST articles should be under some Feature)
    * we'll need a way to manage the set of features
  * Publish Date (default "today")
    * Ideally we should be able to set a future date for this and the page won't go live until that date
  * content (of course)
    * content can include images (formatted properly)
    * content might include other media
    * content can have links (external and internal)
    * content can be formatted
* Features should have a listing page  (ordered by date, descending)

* Provisional list of Features
  * News
    * This could be internal news OR reporting on external news
  * General Article
  * Astronomy Explained
  * Tech
  * Event
  * Constellation Highlight
    * this might be "... of the month"
  * Object (DSO or SSO) Highlight
    * this might be "... of the month"
  * Advice / How-To
  * Imaging
  * Gallery
  * Observing Report
    * this will likely have a gallery IN it.

## 2. Widgets --- THIS IS DONE as of V0.5.

NOTE: none of these are fleshed out and will have to be developed over time.

* Current skymap (for the date)
  * Ideally show position of the Moon and Planets up mid-evening
  * constellations and stick figures
  * names of the brighter stars
  * downloadable and printable
  * (I have Python code that can do this, but it would be several hundred lines)
  * links to a page where you can see a larger view and download/print it.
* Weather forecasting for the general N. Adams area - astronomy focused (clear skies, etc.)
* Calendar
  * internal: meetings, public events, local events
  * astronomical: moon phase, season data, appulses, oppositions, etc.
  * external: TBD
* Almanac
  * sunrise/sunset
  * moonrise/moonset
  * lunar phase
  * astronomical twilight begin and end
  * (this should update daily without having to do anything manually)
* Merchandise - we plan to have a store site (externally hosted), but showing an item from the store.

## 3. Utility pages
* about us
* contact
(see PLAN_260414.md for additions to this list)
