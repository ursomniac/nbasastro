---
title: "Pathway 1 — Full Git"
date: 2026-05-03
layout: "members"
weight: 1
---

# Pathway 1 — Full Git

You write and preview your article locally, then submit it as a pull request
on GitHub. This is the most technically involved pathway but gives you the
most control.

**You will need:**
- Git and Hugo installed locally
- A GitHub account with access to the NBAS repository

---

## First Time Only

Complete these steps once to set up your local environment.

**1. Install Hugo**

See [Install/Setup](/members/docs/install/) for Mac and Windows instructions.

**2. Install GitHub Desktop or use the command line**

[GitHub Desktop](https://desktop.github.com) is recommended if you are
not already comfortable with git on the command line.

**3. Clone the repository**

*GitHub Desktop:*
Go to **File → Clone Repository**, find `ursomniac/nbasastro`, and clone
it to your local machine.

*Command line:*
{{< highlight bash >}}
cd ~/Documents/Projects/NBAS
git clone https://github.com/ursomniac/nbasastro.git
cd nbasastro
{{< /highlight >}}

---

## Each Article

Follow these steps each time you write a new article.

**1. Update main**

*GitHub Desktop:*
Select the `main` branch. Click **Fetch origin**, then **Pull origin**.

*Command line:*
{{< highlight bash >}}
git checkout main
git pull origin main
{{< /highlight >}}

**2. Create a new branch**

Name your branch using this convention: `username-YYYYMMDD-article-slug`

For example: `jsmith-20260503-m42-orion-nebula`

*GitHub Desktop:*
Click the branch dropdown and choose **New Branch**. Enter your branch name.

*Command line:*
{{< highlight bash >}}
git checkout -b jsmith-20260503-m42-orion-nebula
{{< /highlight >}}

**3. Create your article directory**

See [Creating Your Article Directory](/members/articles/create-article-directory/)
for naming rules and instructions.

**4. Generate your index.md**

Use the [Article Builder](/members/article-builder/) to generate your
starting `index.md` file. Move it into your article directory.

**5. Write your article**

Open `index.md` in a plain text editor and write your content below the
front matter. See:

- [Markdown Basics](/members/reference/markdown-basics/)
- [Widgets & Shortcodes](/members/widgets/)
- [Front Matter Reference](/members/reference/front-matter/)

**6. Add your media**

Copy your image files into the article directory.
See [Media Guidelines](/members/media/guidelines/) for size and naming rules.

**7. Preview locally**

Start the Hugo server:

{{< highlight bash >}}
hugo server -D
{{< /highlight >}}

Open [http://localhost:1313](http://localhost:1313) in your browser and
navigate to your article. Check that:

- The article appears correctly in listings
- Images and media render as expected
- Front matter metadata is correct

**8. Commit your changes**

*GitHub Desktop:*
Your new files appear in the left panel. Enter a short commit message
(e.g. `Add M42 observation article`) and click **Commit to your-branch-name**.

*Command line:*
{{< highlight bash >}}
git add content/articles/2026/05/my-article-name/
git commit -m "Add M42 observation article"
{{< /highlight >}}

**9. Push and open a Pull Request**

See [Submit by Pull Request](/members/submission/submit-pr/) for full
instructions on pushing your branch and opening a PR on GitHub.

---

## After Submission

See [After Submission](/members/submission/after-submission/) for the
review process and timeline.
