---
name: Gardening Skills Wiki
description: Maintain skills wiki health - check links, naming, cross-references, and coverage using LLM-native tools
when_to_use: When adding/removing skills. When reorganizing categories. When links feel broken. Periodically (weekly/monthly) to maintain wiki health. When INDEX files don't match directory structure. When cross-references might be stale.
version: 2.0.0
---

# Gardening Skills Wiki

## Overview

The skills wiki needs regular maintenance to stay healthy: links break, skills get orphaned, naming drifts, INDEX files fall out of sync.

**Core principle:** Use LLM-native tools (file_search, grep_search, read_file) to maintain wiki quality.

## When to Use

**Run gardening after:**
- Adding new skills
- Removing or renaming skills
- Reorganizing categories
- Updating cross-references
- Suspicious that links are broken

**Periodic maintenance:**
- Weekly during active development
- Monthly during stable periods

## Quick Health Check (LLM-Native)

When asked to "check skills health" or "garden skills", execute these procedures:

### Procedure 1: Check Links

**Step 1: Find all markdown files**
```yaml
tool: file_search
query: "skills/**/*.md"
purpose: "Get list of all skill markdown files"
```

**Step 2: Extract links from each file**
```yaml
tool: grep_search
query: "\\[.*\\]\\(.*\\)|@skills/|skills/"
includePattern: "skills/**/*.md"
isRegexp: true
purpose: "Find all markdown links and skill references"
```

**Step 3: Verify each skill reference**

For each found reference:
- If starts with `skills/`: Extract path and verify file exists
- Use `file_search` to check if target SKILL.md exists
- Document broken links

**Step 4: Report results**

Create list of:
- ✅ Valid internal links
- ❌ Broken internal links (file not found)
- ⚠️ Orphaned skills (SKILL.md exists but not referenced)

### Procedure 2: Check Naming Conventions

**Step 1: List all skill directories**
```yaml
tool: file_search
query: "skills/**/SKILL.md"
purpose: "Find all skills"
```

**Step 2: Extract directory names**

Parse paths to get directory names (e.g., `test-driven-development` from `skills/testing/test-driven-development/SKILL.md`)

**Step 3: Check naming patterns**

For each directory name:
- ✅ All lowercase
- ✅ Words separated by hyphens (kebab-case)
- ✅ Descriptive (not abbreviations)
- ❌ Flag violations (mixed case, underscores, etc.)

**Step 4: Check frontmatter**

For each SKILL.md:
- Read first ~15 lines (YAML frontmatter)
- Verify required fields present: `name`, `description`, `when_to_use`, `version`
- ❌ Flag missing fields

### Procedure 3: Check INDEX Coverage

**Step 1: Find all SKILL.md files**
```yaml
tool: file_search
query: "skills/**/SKILL.md"
exclude: "INDEX.md"
```

**Step 2: Find all INDEX.md files**
```yaml
tool: file_search
query: "skills/**/INDEX.md"
```

**Step 3: For each SKILL.md, verify it's in an INDEX**

```yaml
tool: grep_search
query: "<skill-name>"
includePattern: "skills/**/INDEX.md"
isRegexp: false
purpose: "Check if skill is indexed"
```

**Step 4: Report orphaned skills**

List skills not found in any INDEX.md file.

## What Gets Checked

### 1. Link Validation

**Checks:**
- Backtick-wrapped `@` links - backticks disable resolution
- Relative paths like skills/ or skills/gardening-skills-wiki/~/ - should use skills/ absolute paths
- All `skills/` references resolve to existing files
- Skills referenced in INDEX files exist
- Orphaned skills (not in any INDEX)

**Fixes:**
- Remove backticks from @ references
- Convert skills/ and skills/gardening-skills-wiki/~/ relative paths to skills/ absolute paths
- Update broken skills/ references to correct paths
- Add orphaned skills to their category INDEX
- Remove references to deleted skills

### 2. Naming Consistency

**Checks:**
- Directory names are kebab-case
- No uppercase or underscores in directory names
- Frontmatter fields present (name, description, when_to_use, version, type)
- Skill names use active voice (not "How to...")
- Empty directories

**Fixes:**
- Rename directories to kebab-case
- Add missing frontmatter fields
- Remove empty directories
- Rephrase names to active voice

### 3. INDEX Coverage

**Checks:**
- All skills listed in their category INDEX
- All category INDEX files linked from main INDEX
- Skills have descriptions in INDEX entries

**Fixes:**
- Add missing skills to INDEX files
- Add category links to main INDEX
- Add descriptions for INDEX entries

## Common Issues and Fixes

### Broken Links

When you find: `skills/debugging/old-skill` referenced but file doesn't exist

**Fix using LLM tools:**
1. Search for the reference: `grep_search(query: "old-skill", isRegexp: false)`
2. Find correct path: `file_search(query: "**/SKILL.md")` and match by name
3. Update references: `replace_string_in_file` with correct path

### Orphaned Skills

When SKILL.md exists but not in any INDEX.md

**Fix:**
1. Identify category from path (e.g., `skills/testing/my-skill` → testing category)
2. Read category INDEX: `read_file("skills/testing/INDEX.md")`
3. Add skill to INDEX: `replace_string_in_file` to append entry

```markdown
- skills/testing/my-skill - Description of what this skill does
```

### Naming Issues

When directory name violates conventions (e.g., `TestingPatterns` instead of `testing-patterns`)

**Fix:**
1. Create properly named directory
2. Move files using file operations
3. Update all references in other skills
4. Remove old directory

**LLM approach:**
```yaml
# This requires manual git operations
tool: run_in_terminal
command: "git mv skills/category/OldName skills/category/new-name"
explanation: "Rename directory to kebab-case"
```

Then update references:
```yaml
tool: grep_search
query: "OldName"
includePattern: "skills/**/*.md"
isRegexp: false
purpose: "Find all references to old name"
```

### Missing Frontmatter

When SKILL.md lacks required fields

**Fix using replace_string_in_file:**
1. Read current frontmatter
2. Add missing fields between `---` delimiters
3. Ensure all required fields present: `name`, `description`, `when_to_use`, `version`

## Naming Conventions

### Directory Names

- **Format:** kebab-case (lowercase with hyphens)
- **Process skills:** Use gerunds when appropriate (`creating-skills`, `testing-skills`)
- **Pattern skills:** Use core concept (`flatten-with-flags`, `test-invariants`)
- **Avoid:** Mixed case, underscores, passive voice starters ("how-to-")

### Frontmatter Requirements

**Required fields:**
- `name`: Human-readable name
- `description`: One-line summary
- `when_to_use`: Symptoms and situations
- `version`: Semantic version

**Optional fields:**
- `languages`: Applicable languages
- `dependencies`: Required tools

## LLM Workflow for Gardening

### When Adding New Skill

**Step 1: Create skill file**
```yaml
tool: create_file
filePath: "skills/category/new-skill/SKILL.md"
content: |
  ---
  name: New Skill
  description: One-line description
  when_to_use: When situation occurs
  version: 1.0.0
  ---
  
  # New Skill
  
  ## Overview
  ...
```

**Step 2: Add to category INDEX**
```yaml
tool: read_file
filePath: "skills/category/INDEX.md"
purpose: "Get current INDEX content"
```

```yaml
tool: replace_string_in_file
filePath: "skills/category/INDEX.md"
operation: append or insert
content: "- skills/category/new-skill - Description"
```

**Step 3: Verify health**
Run Procedure 1, 2, and 3 from "Quick Health Check" above

### When Reorganizing

**Step 1: Move skill files** (use git mv if in git repo)

**Step 2: Find all references**
```yaml
tool: grep_search
query: "old-category/skill-name"
includePattern: "skills/**/*.md"
isRegexp: false
```

**Step 3: Update each reference**
```yaml
tool: replace_string_in_file
filePath: "{each file from step 2}"
oldString: "old-category/skill-name"
newString: "new-category/skill-name"
```

**Step 4: Verify health**
Run link checking procedure

### Periodic Maintenance

**Monthly: Run full health check**

Execute all three procedures:
1. Check Links
2. Check Naming Conventions  
3. Check INDEX Coverage

**Review and fix:**
- ❌ errors (broken links, missing skills)
- ⚠️ warnings (naming, empty dirs)

## Quick Reference

| Issue | LLM Tool | Fix |
|-------|----------|-----|
| Broken links | `grep_search` + `file_search` | Find and update references |
| Orphaned skills | `file_search` + `grep_search` | Add to INDEX.md |
| Naming issues | `file_search` | Use git mv to rename |
| Empty dirs | `list_dir` | Remove with git rm |
| Missing from INDEX | `read_file` + `replace_string_in_file` | Add to INDEX.md |
| No description | `read_file` + `replace_string_in_file` | Update INDEX entry |
| Missing frontmatter | `read_file` + `replace_string_in_file` | Add required fields |

## Output Symbols

- ✅ **Pass** - Item is correct
- ❌ **Error** - Must fix (broken link, missing skill)
- ⚠️ **Warning** - Should fix (naming, empty dir)
- ℹ️ **Info** - Informational (no action needed)

## Integration with Workflow

**Before committing skill changes:**

Ask LLM: "Check skills health" or "Garden the skills wiki"

LLM will execute the three procedures and report:
- ❌ errors to fix
- ⚠️ warnings to consider
- ✅ passing checks

**When links feel suspicious:**

Ask LLM: "Check skill links" - executes Procedure 1

**When INDEX seems incomplete:**

Ask LLM: "Check skill INDEX coverage" - executes Procedure 3

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Will check links manually" | LLM can check all links in seconds |
| "INDEX probably fine" | Orphaned skills happen - always verify |
| "Naming doesn't matter" | Consistency aids discovery and maintenance |
| "Empty dir harmless" | Clutter confuses future maintainers |
| "Can skip periodic checks" | Issues compound - regular maintenance prevents big cleanups |

## Real-World Impact

**Without gardening:**
- Broken links discovered during urgent tasks
- Orphaned skills never found
- Naming drifts over time
- INDEX files fall out of sync

**With gardening:**
- LLM checks health in seconds
- Automated validation prevents manual inspection
- Consistent structure aids discovery
- Wiki stays maintainable

## The Bottom Line

**Don't manually inspect - ask LLM to check.**

Ask "garden the skills" after changes and periodically. Fix ❌ errors immediately, address ⚠️ warnings when convenient.

Maintained wiki = findable skills = reusable knowledge.
