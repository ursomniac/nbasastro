---
title: "Pathway 2 — Local Preview"
date: 2026-05-03
layout: "members"
weight: 2
---

# Pathway 2 — Local Preview

You write and preview your article locally using Hugo, then submit it as
a ZIP file by email. No git branching or pull requests required.

**You will need:**
- Hugo installed locally
- A copy of the NBAS repository on your machine

---

## First Time Only

Complete these steps once to set up your local environment.

**1. Install Hugo**

See [Install/Setup](/members/docs/install/) for Mac and Windows instructions.

**2. Clone the repository**

*Command line (Mac):*
{{< highlight bash >}}
cd ~/Documents/Projects/NBAS
git clone https://github.com/ursomniac/nbasastro.git
cd nbasastro
{{< /highlight >}}

*Command line (Windows PowerShell):*
{{< highlight bash >}}
New-Item -Path "$HOME\Documents\Projects\NBAS" -ItemType Directory -Force
Set-Location -Path "$HOME\Documents\Projects\NBAS"
git clone https://github.com/ursomniac/nbasastro.git
Set-Location -Path ".\nbasastro"
{{< /highlight >}}

Alternatively, use [GitHub Desktop](https://desktop.github.com) —
go to **File → Clone Repository** and find `ursomniac/nbasastro`.

---

## Each Article

Follow these steps each time you write a new article.

**1. Update your local copy**

Before starting, make sure your local copy is up to date.

*Command line:*
{{< highlight bash >}}
git checkout main
git pull origin main
{{< /highlight >}}

*GitHub Desktop:*
Select the `main` branch. Click **Fetch origin**, then **Pull origin**.

**2. Create your article directory**

See [Creating Your Article Directory](/members/articles/create-article-directory/)
for naming rules and instructions.

**3. Generate your index.md**

Use the [Article Builder](/members/article-builder/) to generate your
starting `index.md` file. Move it into your article directory.

**4. Write your article**

Open `index.md` in a plain text editor and write your content below the
front matter. See:

- [Markdown Basics](/members/reference/markdown-basics/)
- [Widgets & Shortcodes](/members/widgets/)
- [Front Matter Reference](/members/reference/front-matter/)

**5. Add your media**

Copy your image files into the article directory.
See [Media Guidelines](/members/media/guidelines/) for size and naming rules.

**6. Preview locally**

Start the Hugo server:

{{< highlight bash >}}
hugo server -D
{{< /highlight >}}

Open [http://localhost:1313](http://localhost:1313) in your browser and
navigate to your article. Check that:

- The article appears correctly in listings
- Images and media render as expected
- Front matter metadata is correct

Stop the server when done with **Ctrl+C**.

**7. Submit**

See [Submit by ZIP](/members/submission/submit-zip/) for instructions on
packaging and emailing your article directory.

---

## After Submission

See [After Submission](/members/submission/after-submission/) for the
review process and timeline.
