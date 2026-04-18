# Reorganizing the Article structure

## PROBLEM: 
* There are 88 constellations
* There are 110 Messier objects
* There are 109 Caldwell objects
* There are thousands of asteroids
* There are thousands of comets

You get the picture.  The point is tagging for these isn't going to work - the tag
list will be overwhelmed quickly.

## PROPOSAL: Create a new section of metadata in Articles

### CASE 1: T Corona Borealis Page

object_sections: 
  constellation: "Corona Borealis"

### CASE 2: M 87 page

object_sections:
  constellation: "Virgo"
  messier: 87

### CASE 3: Something about Comet C2026/A1

object_sections:
  comet: C2026/A1

### CASE 4: One of the Constellation PDF pages converted to an Article

object_sections:
  constellation: "Orion"
  messier_objects: ["42", "43", "78"]
  other_objects: ["NGC 2024", "NGC 1980", "Cr 70"]

### CASE 5: Article on the Great Red Spot

object_sections:
  planet: "Jupiter"

## What's in the object_sections:

1. Constellation - now we can have an Articles by Constellation page
2. Messier - now we can have an Articles on Messier Objects page
3. Caldwell - (ditto, for Caldwell Objects)
(repeat for other catalogs, maybe)

## On the Site
* Remembering that "Library" will probably go away before long", the top nav will get lonely
* This completely changes the top nav, because aside from Home, everything else is related to slices of the Articles set:
* "Articles by:" <--- reverse, not clicked, follows by clickable
  1. "Recent" (what "Articles" is now)
  2. ADD ada a section for "Club" which can combine
      * Newsletters
      * Events
      * Announcements / News
  3. "Series" (from the modal)
  4. "Tag" (from the model - adding these eliminates "Explore Topics"
  5. Add "by Constellation"
  6. Add a dropdown for "by Catalog" (for DSOs)
       * This would further drill down to "Messier", "Caldwell" and others as needed
  7. Add a dropdown for "Solar System"
       * Similarly "Planet", "Comet", "Small Bodies", "the Moon", "the Sun", "Earth"
       * this DOES get a little hairy because, "Asteroids", "Dwarf Planets", "Meteor Showers", and so on...  

So it'll look kind of like:

Home | [Club ⬇️ ] | _ARTICLES by:_  Recent | Series | Tag | Constellation | [Catalog ⬇️  ] | [Solar System ⬇️  ]

Where things in [] are dropdowns

Catalog: Messier, Caldwell, Other
Solar System (see list above)

## the pages

* the Constellation page would list all the articles by constellation
* the Catalog page would list all of the object for a given catalog in numerical order
* the Solar System page would list all the objects by their object catagory


