# Version Control Safety and Rollback Guide
## Protocols for Preserving Author Word Documents and Instant Reversion

This guide outlines the exact, step-by-step procedures to recover earlier versions of your Microsoft Word documents and establishes a bulletproof Git version control protocol to prevent accidental overwrites or unwanted content injections.

---

## Part 1: How to Recover Your Previous Word Document Versions Right Now

Because your repository is hosted inside your Embry-Riddle OneDrive (`CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity`), **OneDrive automatically records every version saved throughout the day**. Your work is preserved in OneDrive cloud revision history and in local backups.

### Method 1: Using Microsoft Word's Built-in Version History (Fastest)
1. Open the file in question (e.g., `ChpIII v2.docx`) in **Microsoft Word for Mac**.
2. In the top macOS menu bar, click **File > Browse Version History**  
   *(or click the document title in the top title bar of Word and select **Version History**)*.
3. A **Version History** panel will open on the right side of the screen.
4. You will see a chronological list of every auto-save and manual save from today with exact timestamps and authors.
5. Click on the version from earlier today (prior to the injection). Word will open that version in a side-by-side window.
6. Click **Restore** to roll back the document, or **Save a Copy** to save it under a new name (e.g., `ChpIII_v2_Restored.docx`).

### Method 2: Using OneDrive in Finder
1. Open **Finder** and navigate to:  
   `OneDrive - Embry-Riddle Aeronautical University > final-thesis > thesis_docs > manuscripts`.
2. Right-click (or control-click) the `.docx` file (e.g., `ChpIII v2.docx`).
3. In the context menu, select **Version History** (provided by the OneDrive sync client).
4. A window will display every timestamped cloud revision.
5. Click the three dots `...` next to the timestamp you want, then choose **Restore** or **Download**.

### Method 3: Using OneDrive on the Web
1. Log into your university portal at [portal.office.com](https://portal.office.com) or [onedrive.live.com](https://onedrive.live.com) using your Embry-Riddle credentials.
2. Navigate to `final-thesis > thesis_docs > manuscripts`.
3. Hover over the document, click the three vertical dots `...`, and select **Version history**.
4. You will see every historical version saved over the past 30–90 days.
5. Select the version saved earlier today and click **Restore**.

### Method 4: Local Consolidated Thesis Backup on Your Desktop
A master thesis document saved today at **1:53 PM** is located on your local drive:
* **Path**: `/Users/leilagleich/Desktop/700B Wk9/Gleich-Thesis_v1.docx`
* **Contents**: 456 total paragraphs containing Chapter I, Chapter II, Chapter III (paragraphs 72–188, 117 paragraphs total with your formatting and indents), Chapter IV, and Chapter V.
* You can open this file immediately in Word to copy or extract your updated sections.

---

## Part 2: Git Version Control Protocol to Prevent Future Issues

To ensure you can always branch, commit, and roll back changes without risk, follow this standard Git workflow.

### 1. Dedicated Author Snapshot Branch
Never let automated scripts or AI assistants operate on the same branch where you keep active uncommitted Word drafts.

To create and switch to a personal safety branch:
```bash
# 1. Create and switch to a personal working branch
git checkout -b author-safe-drafts

# 2. Stage your current Word documents
git add thesis_docs/manuscripts/*.docx

# 3. Commit with a clear, timestamped message
git commit -m "checkpoint: author manual edits prior to assistant tasks"
```

### 2. Creating a Rollback Checkpoint (Tag)
Before starting any significant automated task or AI conversation, create a local Git tag:
```bash
# Create an immutable checkpoint tag
git tag -a checkpoint-before-work -m "Restore point before session"
```

If anything goes wrong, you can return to that exact snapshot with one command:
```bash
git checkout checkpoint-before-work
```

### 3. How to Restore an Individual File Without Touching Anything Else
If an individual file was changed and you want to restore it from an earlier commit or branch:
```bash
# Restore a single file from a previous commit
git checkout <commit_hash> -- "thesis_docs/manuscripts/ChpIII v2.docx"

# Or discard all local modifications to a specific file
git restore "thesis_docs/manuscripts/ChpIII v2.docx"
```

### 4. How to Compare Revisions of Any Word Document
Because `.docx` files are binary zip archives, you can inspect their internal paragraph counts across git commits using Python:
```bash
python3 -c "
import subprocess, io, docx
data = subprocess.check_output(['git', 'show', 'HEAD:thesis_docs/manuscripts/ChpIII v2.docx'])
doc = docx.Document(io.BytesIO(data))
print('Paragraphs:', len(doc.paragraphs))
"
```

---

## Part 3: Golden Operational Rules for AI Assistance

1. **Policy 1.1 Enforcement**: The AI assistant must never create, modify, overwrite, convert, or delete any `.docx` file in the repository.
2. **Pre-Task Git Status Verification**: Before any tool makes a file edit, the agent must check `git status` and verify that no author Word documents are in an uncommitted or dirty state.
3. **Manuscripts in Markdown Only**: All agent drafts and recommendations must be written exclusively to Markdown (`.md`) files in `thesis_docs/recommendations/` or `thesis_docs/notes/`, never directly into active manuscript files until explicitly reviewed and approved by the author.
