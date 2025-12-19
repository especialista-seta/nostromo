---
name: Using Portable Skills
description: Deploy and use skills in any repository as IDE-agnostic markdown documentation
when_to_use: When setting up skills in a new project, updating existing skills, or migrating from script-based to scriptless mode
version: 2.0.0
---

# Using Portable Skills

## Overview

Deploy the skills system to any repository as pure markdown files. Works with any IDE that has AI assistant integration (VS Code, IntelliJ IDEA, etc.).

**No scripts required** - skills are read directly by LLMs using native tools.

**Workflow:** Copy skills → Configure IDE integration → Use skills → Update as needed

## When to Use

**Use copy mode when:**
- Starting out with skills
- Want project-specific skill customizations
- Working on a personal/small project

**Use submodule mode when:**
- Want to version-control skills
- Need to update skills across multiple projects
- Working on a team (everyone gets same skills)
- Want to contribute skills back upstream

## Initial Setup

See **[GETTING_STARTED.md](../../../GETTING_STARTED.md)** for detailed setup instructions.

**Quick summary:**

1. Copy skills directory to your project
2. Copy IDE-specific integration files from `.setup/{ide}/`
3. Reload IDE to activate

**No bash scripts required** - all operations use IDE-native tools.

### Setup Paths by IDE

**VS Code + GitHub Copilot:**
```
.setup/vscode/README.md              → Setup instructions
.setup/vscode/copilot-instructions.md → Copy to .github/
```

**IntelliJ IDEA + AI Assistant:**
```
.setup/intellij/README.md → Setup instructions
```

## Updating Skills

### In Copy Mode

**Manual update:**
```bash
# Pull latest from source
cd /path/to/superpowers-skills-vscode
git pull

# Copy to your project
cp -r skills /path/to/your-project/superpowers-skills/

# Update IDE integration if changed
cp .setup/vscode/copilot-instructions.md /path/to/your-project/.github/
```

### In Submodule Mode

```bash
# In your project root
cd superpowers-skills
git pull origin main
cd ..

# Commit the update
git add superpowers-skills
git commit -m "chore: update skills"
```

## Migrating Copy → Submodule

```bash
# 1. Remove copied version
rm -rf superpowers-skills/

# 2. Remove from git if committed
git rm -rf superpowers-skills/
git commit -m "chore: prepare for skills submodule"

# 3. Add as submodule
git submodule add https://github.com/your-org/superpowers-skills-vscode superpowers-skills

# 4. Commit
git add superpowers-skills .gitmodules
git commit -m "chore: migrate skills to submodule"

# 5. IDE integration already configured, no changes needed
```

## Migrating from Script-Based (Old) → Scriptless (New)

**If you have the old `.vscode-skills/` with bootstrap.sh:**

1. **Remove old scripts:**
   ```bash
   rm -rf .vscode-skills/
   git rm -rf .vscode-skills/ .vscode/settings.json
   ```

2. **Follow new setup:**
   See [GETTING_STARTED.md](../../../GETTING_STARTED.md)

3. **Clean up .gitignore:**
   Remove lines referencing `.vscode-skills/`

## How IDE Integration Works

**VS Code + Copilot:**
- Copilot reads `.github/copilot-instructions.md`
- Instructions tell Copilot to read `skills/SKILLS-DIGEST.md` first
- Copilot uses `file_search`, `grep_search`, `read_file` to access skills
- **No environment variables or PATH manipulation**

**IntelliJ + AI Assistant:**
- Manually configure AI Assistant to reference skills directory
- AI reads skill files directly as markdown
- Uses native IDE search capabilities

## Troubleshooting

### Copilot Not Using Skills

1. **Verify file exists:** `.github/copilot-instructions.md`
2. **Check it references skills directory correctly**
3. **Reload VS Code window** (Copilot loads instructions on startup)
4. **Verify skills directory copied:** `ls -la superpowers-skills/skills/`

### AI Can't Find Specific Skill

Ask AI: "Search for skills about [topic]"

AI should use:
- `file_search(query: "skills/**/SKILL.md")` to list all skills
- `grep_search` to search within skills
- `read_file(skills/SKILLS-DIGEST.md)` for quick overview

### Update Not Reflected

**In copy mode:**
- Did you copy the latest files?
- Did you overwrite IDE integration files?

**In submodule mode:**
- Did you `git pull` inside the submodule directory?
- Did you commit the submodule pointer update?

## Related Skills

- **skills/meta/sharing-skills** - Contributing skills back to upstream
- **skills/meta/writing-skills** - Creating new skills
- **skills/collaboration/using-git-worktrees** - Isolated development environments
- **skills/meta/pulling-updates-from-skills-repository** - Keeping skills current
