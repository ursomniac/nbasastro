---
title: "Submit by Pull Request"
date: 2026-05-03
layout: "members"
weight: 1
---

# Submit by Pull Request

Used by Pathway 1. You submit your article as a feature branch on GitHub,
which the site administrator reviews and merges.

---

## Branch Naming

Every article must be submitted on its own branch. Use this naming convention:

{{< highlight bash >}}
username-YYYYMMDD-article-slug
{{< /highlight >}}

For example: `jsmith-20260503-m42-orion-nebula`

- One article per branch — do not combine multiple articles on one branch
- The date prevents collisions if you submit more than one article on the same day
- The slug identifies the article in the PR list

---

## Method 1: GitHub Desktop

### First Time Only

1. Download and install [GitHub Desktop](https://desktop.github.com)
2. Sign in with your GitHub account
3. Go to **File → Clone Repository**
4. Find `ursomniac/nbasastro` and clone it to your local machine

### Each Article

**1. Make sure you're on main and up to date:**

In GitHub Desktop, select the `main` branch from the branch dropdown.
Click **Fetch origin**, then **Pull origin** if updates are available.

**2. Create a new branch:**

Click the branch dropdown and choose **New Branch**.
Name it using the convention above: `jsmith-20260503-m42-orion-nebula`

**3. Add your article:**

Copy your completed article directory into:

{{< highlight bash >}}
content/articles/YYYY/MM/your-article-name/
{{< /highlight >}}

**4. Commit your changes:**

GitHub Desktop will show your new files in the left panel.
Enter a short commit message (e.g. `Add M42 observation article`) and
click **Commit to your-branch-name**.

**5. Push and open a Pull Request:**

Click **Publish branch** (or **Push origin** if you've pushed before).
Then click **Create Pull Request** — this opens GitHub in your browser.
Add a brief description and click **Create pull request**.

---

## Method 2: Command Line

### First Time Only

{{< highlight bash >}}
cd ~/Documents/Projects/NBAS
git clone https://github.com/ursomniac/nbasastro.git
cd nbasastro
{{< /highlight >}}

### Each Article

**1. Make sure you're on main and up to date:**

{{< highlight bash >}}
git checkout main
git pull origin main
{{< /highlight >}}

**2. Create a new branch:**

{{< highlight bash >}}
git checkout -b jsmith-20260503-m42-orion-nebula
{{< /highlight >}}

**3. Add your article directory:**

Copy your completed article directory into `content/articles/YYYY/MM/`.

**4. Commit your changes:**

{{< highlight bash >}}
git add content/articles/2026/05/my-article-name/
git commit -m "Add M42 observation article"
{{< /highlight >}}

**5. Push and open a Pull Request:**

{{< highlight bash >}}
git push origin jsmith-20260503-m42-orion-nebula
{{< /highlight >}}

Then go to the [repository on GitHub](https://github.com/ursomniac/nbasastro),
where you will see a prompt to open a Pull Request for your branch.
Click **Compare & pull request**, add a brief description, and click
**Create pull request**.

---

## After Submission

See [After Submission](/members/submission/after-submission/) for what
happens next and how long to expect before your article goes live.
