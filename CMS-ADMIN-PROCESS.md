# MASTER CMS SETUP FOR CLUB WEBSITE

This single file contains the code and instructions to set up a free visual editor 
that uses GitHub Pull Requests (MRs) for approval and handles /YYYY/MM folders.

---

### STEP 1: CREATE THE ADMIN PAGE
Save this exact code as: `static/admin/index.html`

<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Club Content Manager</title>
</head>
<body>
  <script src="https://unpkg.com@^3.0.0/dist/decap-cms.js"></script>
</body>
</html>

---

### STEP 2: CREATE THE CONFIGURATION
Save this exact code as: `static/admin/config.yml`
(Note: Update 'repo' with your actual GitHub username and repository name)

backend:
  name: github
  repo: your-username/your-repo-name
  branch: main
  open_authoring: true 

publish_mode: editorial_workflow

media_folder: "static/images"
public_folder: "/images"

collections:
  - name: "articles"
    label: "Club Articles"
    folder: "content/articles"
    path: "{{year}}/{{month}}/{{slug}}" 
    create: true
    fields:
      - {label: "Title", name: "title", widget: "string"}
      - {label: "Publish Date", name: "date", widget: "datetime"}
      - {label: "Author", name: "author", widget: "string"}
      - {label: "Body", name: "body", widget: "markdown"}

  - name: "authors"
    label: "Author Profiles"
    folder: "content/authors"
    create: true
    fields:
      - {label: "Full Name", name: "title", widget: "string"}
      - {label: "Bio", name: "body", widget: "markdown"}

---

### STEP 3: WORKFLOW RULES
1. CMS USERS: Go to ://yoursite.com. Log in with GitHub. 
2. DRAFTS: Saving in the CMS creates a Pull Request (PR) on GitHub. 
3. FOLDERS: The CMS uses the 'date' field to build the /YYYY/MM path automatically.
4. GIT USERS: Continue using the CLI/Git as normal. Your PRs will coexist with CMS PRs.
5. ADMIN: You must merge the PRs on GitHub for content to be "official."

---

### STEP 4: FINAL REQUIREMENTS
- Members must be "Collaborators" on the GitHub repo.
- You must create a GitHub OAuth App in your GitHub Developer Settings.
- Callback URL for OAuth: https://netlify.com
