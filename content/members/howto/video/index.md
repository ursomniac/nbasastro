---
title: "How-To: Show a YouTube Video"
date: 2026-04-22
layout: "members"
---

## How do I put a YouTube video in my article?"

This is easy with the custom "nbas-video" partial!

### Steps:

1. Go to the video on YouTube.
2. Find the code at the end of the URL
3. Use this snippet of template code in your index.md file:

```
{{</* nbas-video
    src="https://youtube.com/embed/PUT_THE_CODE_HERE"
    title="OPTIONAL TITLE GOES HERE"
    caption="OPTIONAL CAPTION AT THE BOTTOM GOES HERE"
*/>}}
```

Parameters:

* **src** (Required): The YouTube embed link. 
  Must follow the format: `https://youtube.com/embed/ID`
* **title** (Optional): Sets the title attribute for the iframe 
  (accessibility). Defaults to "NBAS Video" if omitted.
* **caption** (Optional):  Generates a <figcaption> element below the video.


Here's an example of what it looks like (using ID: "LFToko-ksWI"):

   {{< nbas-video
       src="https://youtube.com/embed/LFToko-ksWI"
       title="Tour of the Moon"
       caption="A high-resolution tour of the lunar surface, courtesy of NASA."
   >}}

