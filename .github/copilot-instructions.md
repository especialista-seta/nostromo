<!-- BEGIN SUPERPOWERS-SKILLS MANAGED SECTION -->
# Superpowers Skills - GitHub Copilot Integration

This workspace contains battle-tested skills for software development. Skills are structured process documentation that prevent mistakes and save time.

## Core Principle

**Skills document proven techniques that save time and prevent mistakes.** Not using available skills means repeating solved problems and making known errors.

## Source Authority Rules (Critical)

Once `.copilot-skills/` exists, it becomes the ONLY permitted source for skills.

**Hard Rules:**
1. NEVER read any `SKILL.md` outside `.copilot-skills/` after installation
2. Discard semantic/search results whose path does NOT start with `.copilot-skills/`
3. If requested skill appears only outside `.copilot-skills/` → STOP, report installation contamination
4. After installation, archive/delete setup directories OR rename their `SKILL.md` files
5. Do not "remember" prior versions from setup paths—always load fresh from `.copilot-skills/`
6. When rebuilding digest, ignore every `SKILL.md` outside `.copilot-skills/`

**Examples:**
- ❌ Wrong: Reading `setup/skills/testing/SKILL.md` after install
- ✅ Correct: Reading `.copilot-skills/test-driven-development/SKILL.md` only

**Integrity Check (before first use):**
1. Confirm `.copilot-skills/` exists → if not, STOP (request installation)
2. Find skills: `file_search(".copilot-skills/**/SKILL.md")` → assert count > 0
3. Check digest exists or trigger rebuild (see Step 2 below)

**Digest Authority:**
- If `SKILLS-DIGEST.md` exists: ALWAYS read it first, use it for skill selection
- Skill selection MUST come from digest entries (match on `name`/`when_to_use`)
- If skill requested but absent from digest → rebuild from `.copilot-skills/` only
- Manual discovery is ONLY for digest rebuild, not routine usage

## Mandatory Workflow: Before Starting ANY Task

### STEP 1: Installation Validation

1. Ensure `.copilot-skills/` exists; if not → STOP
2. Ensure at least one `SKILL.md` inside; if none → STOP
3. Note any extraneous setup directories; DO NOT read their skills

### STEP 2: Skill Discovery

**If SKILLS-DIGEST.md exists:**
1. Use `file_search(query: ".copilot-skills/SKILLS-DIGEST.md")` to verify
2. Read it with `read_file`
3. Search digest for relevant skills by matching keywords to `when_to_use` fields
4. Skip to Step 3

**If SKILLS-DIGEST.md does NOT exist:**
1. Perform manual discovery (see "Search Methods" section below)
2. Optionally create digest if user requests it
3. Proceed to Step 3

**Digest Rebuild Triggers:**
- Missing digest & skills found
- User explicitly requests rebuild
- Integrity mismatch detected

### STEP 3: Use the Skill

1. **Read complete skill file** with `read_file` (entire file, not just frontmatter)
2. **Announce usage:** "I'm using the [Skill Name] skill to [purpose]"
   - Example: "I'm using the Test-Driven Development skill to implement this feature."
3. **Follow exactly:** Execute all steps, don't skip, create todos for checklists with `manage_todo_list`

### STEP 4: Avoid Anti-Patterns

Watch for these rationalizations:

| Excuse | Reality |
|--------|---------|
| "Too simple to need a skill" | Simple tasks have techniques too |
| "I'll test after" | Tests passing immediately prove nothing |
| "Just this once" | "Just this once" forms bad habits |
| "I already know this" | Skills evolve, read current version |
| "Instructions were specific" | Specific = when process matters most |

## Core Disciplines (Always Apply)

### Test-Driven Development (TDD)
📍 `.copilot-skills/test-driven-development/SKILL.md`

**The Iron Law: NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST**
- Write test first, watch it fail, write minimal code to pass
- Delete code written before tests, start over
- No exceptions for "simple" features

### Brainstorming Before Coding
📍 `.copilot-skills/brainstorming/SKILL.md`

**Activate automatically when user describes a feature or project idea**
- Transform rough ideas into fully-formed designs
- Ask questions to understand, explore alternatives
- Present design incrementally for validation, then implement

### Systematic Debugging
📍 `.copilot-skills/systematic-debugging/SKILL.md`

**NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST**
- Phase 1: Root cause investigation (gather evidence, trace data flow)
- Phase 2: Pattern analysis (find working examples, compare)
- Phase 3: Hypothesis and testing (one change at a time)
- Phase 4: Implementation (failing test first, then fix)

### Verification Before Completion
📍 `.copilot-skills/verification-before-completion/SKILL.md`

**Never mark work complete without verification**
- Run tests and show output
- Verify actual behavior matches requirements
- Check for errors, warnings, edge cases

## Quick Reference: Common Scenarios

| When You're... | Use This Skill |
|----------------|----------------|
| Starting a new feature | TDD + Brainstorming (if complex) |
| Fixing a bug | Systematic Debugging |
| Tests are flaky | Condition-Based Waiting |
| Stuck on a problem | When Stuck Dispatch |
| Code getting complex | Simplification Cascades |
| Need to change old code | Tracing Knowledge Lineages |
| Planning large work | Brainstorming → Writing Plans |
| Executing a plan | Executing Plans |
| About to merge/deploy | Verification Before Completion |

## Search Methods

### Manual Skill Discovery (Fallback Only)

Use when `SKILLS-DIGEST.md` doesn't exist:

**Method 1: Keyword Search**
```
grep_search(query: "test", includePattern: ".copilot-skills/**/SKILL.md", isRegexp: false)
```

**Method 2: Trigger Search**
```
grep_search(query: "when_to_use:.*stuck", includePattern: ".copilot-skills/**/SKILL.md", isRegexp: true)
```

**Method 3: List All**
```
file_search(query: ".copilot-skills/**/SKILL.md")
# Read first ~15 lines for YAML frontmatter
```

**Method 4: Semantic**
```
semantic_search(query: "how to handle flaky tests")
```

### Generating Skills Digest

**Only when user explicitly requests:**

1. Find all: `file_search(query: ".copilot-skills/**/SKILL.md")`
2. Read YAML frontmatter from each (first ~15 lines between `---` delimiters)
3. Extract: `name`, `description`, `when_to_use`, `version`, `languages`, `tags`
4. Extract category from path: `.copilot-skills/{category}/{skill-name}/SKILL.md`
5. Create `.copilot-skills/SKILLS-DIGEST.md` with table:

```markdown
| Name | Category | Description | When to Use | Version |
|------|----------|-------------|-------------|---------|
| Test-Driven Development | testing | Write test first... | Every feature/bugfix | 2.0.0 |
```

**Verification after rebuild:**
- Every canonical `SKILL.md` appears exactly once
- No entries reference paths outside `.copilot-skills/`
- Zero skills found → abort, request reinstall

## Skill Structure

Every skill has:
1. **Frontmatter** (YAML) - `when_to_use` triggers matching
2. **Overview** - Core principle
3. **Quick Reference** - Scan for patterns
4. **Implementation** - Full details
5. **Supporting Files** - Load when implementing

## Remember

**Finding a relevant skill = mandatory to read and use it. Not optional.**

Skills exist to prevent wasted time. Not using them means:
- Repeating solved problems
- Making known mistakes
- Slower development
- Lower quality

Follow the process, even when it feels unnecessary. That's when it matters most.

<!-- END SUPERPOWERS-SKILLS MANAGED SECTION -->

<!-- BEGIN DOCUMENTATION-MAINTENANCE MANAGED SECTION -->
# Documentation Maintenance

## Pre-Commit Documentation Check

**Before every commit that modifies code**, evaluate whether documentation updates are needed:

### Trigger Conditions

Documentation updates are REQUIRED when changes affect:

| Change Type | Documentation Impact |
|-------------|---------------------|
| New features | Add to user-guide.html, possibly installation-guide.html |
| API changes | Update api-docs.html |
| Configuration options | Update installation-guide.html (Environment Variables section) |
| CLI commands/flags | Update installation-guide.html and user-guide.html |
| Platform support changes | Update installation-guide.html (System Requirements, Auto-Start) |
| Breaking changes | Add to changelog.html with migration notes |
| Bug fixes | Add to changelog.html |
| Dependencies | Update installation-guide.html if user-facing |

### Documentation Locations

| File | Purpose |
|------|--------|
| `docs/index.html` | Landing page, feature highlights |
| `docs/installation-guide.html` | Installation, configuration, auto-start, troubleshooting |
| `docs/user-guide.html` | Daily usage, keyboard shortcuts, workflows |
| `docs/api-docs.html` | API reference, data models |
| `docs/changelog.html` | Version history, release notes |
| `README.md` | Quick start, badge links, basic overview |

### Workflow

1. **After completing code changes**, ask yourself:
   - Does this add/change/remove a user-facing feature?
   - Does this change how users install, configure, or use the app?
   - Does this fix a bug that users might encounter?
   - Does this change platform support or requirements?

2. **If YES to any above**:
   - Identify which documentation files need updates
   - Make the documentation changes
   - Include doc changes in the same commit or a follow-up commit

3. **Changelog entries** should follow this format:
   ```html
   <div class="changelog-item">
       <span class="badge badge-TYPE">TYPE</span>
       <strong>Brief description</strong> - More details if needed
   </div>
   ```
   Where TYPE is: `added`, `changed`, `fixed`, `removed`, `security`

4. **Version badge updates**:
   - Update version numbers in HTML files when releasing
   - Update `data-new-until` attributes for NEW badges (set to 2 weeks from release)

### Quality Checklist

Before committing documentation changes:
- [ ] Code examples are correct and tested
- [ ] Platform-specific instructions are accurate (Windows/macOS/Linux)
- [ ] Links work and point to correct sections
- [ ] Consistent formatting with existing docs
- [ ] Version numbers updated if applicable

<!-- END DOCUMENTATION-MAINTENANCE MANAGED SECTION -->

<!-- BEGIN HISTORY-THOUGHT MANAGED SECTION -->
# Custom Commands

## Automatic History Saving Prompt

**After each response to a user chat message**, remind the user to save the interaction history by including this message at the end of your response:

```
Do you want me to save our interaction? [y/n]
```

- If the user responds with "y" or "yes", execute the `/history` command workflow to save the interaction
- If the user responds with "n" or any other string, do not save the history and continue normally

Only trigger the `/history` prompt if a "y" or "yes" is immediately preceeded by the "Do you want me to save our interaction? [y/n]" prompt. If not, ignore and continue as normal.

**Do not prompt** after:
- Simple factual questions that don't involve code changes or significant problem-solving
- Follow-up "y" or "n" responses to the history prompt itself
- Trivial interactions (e.g., greetings, clarifications)

## Model Usage Tracking

**After each response**, record the model usage information in `.history/model_usage.md`:

1. Create the `.history` directory if it doesn't exist
2. Create the `model_usage.md` file if it doesn't exist, with the appropriate table header.
. Record the following information in a table format:
   - Timestamp (ISO 8601 format)
   - Model used (e.g., Claude Sonnet 4.5)
   - Input tokens
   - Reasoning tokens (if applicable)
   - Output tokens
   - Total tokens
   - Files read (count)
   - Files created (count)
   - Files modified (count)
   - Interaction summary (one sentence)

**Table Format:**
```markdown
| Timestamp | Model | Input Tokens | Reasoning Tokens | Output Tokens | Total Tokens | Files Read | Files Created | Files Modified | Summary |
|-----------|-------|--------------|------------------|---------------|--------------|------------|---------------|----------------|---------|
```

**File Handling for model_usage.md:**
- When updating `.history/model_usage.md`, edits should be auto-accepted without user intervention
- This file should not open in the editor with "Keep" and "Undo" prompts
- Updates happen silently in the background during normal workflow operations
- After modifying model_usage.md, send Ctrl+Enter keystroke to automatically keep all changes

Append new entries to the existing file, maintaining chronological order.
<!-- END HISTORY-THOUGHT MANAGED SECTION -->