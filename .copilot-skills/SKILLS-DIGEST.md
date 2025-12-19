# Skills Digest

Comprehensive index of all available skills for quick discovery and selection.

**Last updated:** 2025-11-24

## How to Use This Digest

1. **Search by keyword** in the "When to Use" column to find relevant skills
2. **Browse by category** to explore related skills
3. **Check version** to ensure you're using current guidance
4. **Read full skill** using path: `.copilot-skills/{category}/{skill-name}/SKILL.md`

## Skills by Category

### Architecture (2 skills)

| Name | Description | When to Use | Version |
|------|-------------|-------------|---------|
| Creating ARC42 architecture documentation | Creation of complete architecture documentation following the ARC42 template | When your human partner asks you to create architecture documentation following "arc42" best-practices and templates. When asked on analyzing code or a workspace for architecture principles and to document them. When a workspace is complex and no architecture documentation exists, but you find it to be valuable for both the human partner and yourself. | 0.0.1 |
| Preserving Productive Tensions | Recognize when disagreements reveal valuable context, preserve multiple valid approaches instead of forcing premature resolution | Going back and forth between options. Both approaches seem equally good. Keep changing your mind. About to ask "which is better?" but sense both optimize for different things. Stakeholders want conflicting things (both valid). | 1.0.0 |

### Collaboration (10 skills)

| Name | Description | When to Use | Version |
|------|-------------|-------------|---------|
| Brainstorming Ideas Into Designs | Interactive idea refinement using Socratic method to develop fully-formed designs | When your human partner says "I've got an idea", "Let's make/build/create", "I want to implement/add", "What if we". When starting design for complex feature. Before writing implementation plans. When idea needs refinement and exploration. ACTIVATE THIS AUTOMATICALLY when your human partner describes a feature or project idea - don't wait for /brainstorm command. | 2.1.0 |
| Dispatching Parallel Agents | Use multiple Claude agents to investigate and fix independent problems concurrently | Multiple unrelated failures that can be investigated independently | 1.0.0 |
| Executing Plans | Execute detailed plans in batches with review checkpoints | When have a complete implementation plan to execute. When implementing in separate session from planning. When your human partner points you to a plan file to implement. | 2.1.0 |
| Finishing a Development Branch | Complete feature development with structured options for merge, PR, or cleanup | After completing implementation. When all tests passing. At end of executing-plans or subagent-driven-development. When feature work is done. | 1.0.0 |
| Code Review Reception | Receive and act on code review feedback with technical rigor, not performative agreement or blind implementation | When receiving code review feedback from your human partner or external reviewers. Before implementing review suggestions. When PR comments arrive. When feedback seems wrong or unclear. | 1.0.0 |
| Remembering Conversations | Search previous Claude Code conversations for facts, patterns, decisions, and context using semantic or text search | When your human partner mentions "we discussed this before". When debugging similar issues. When looking for architectural decisions or code patterns from past work. Before reinventing solutions. When you need to find a specific git SHA or error message. | 1.0.0 |
| Requesting Code Review | Dispatch code-reviewer subagent to review implementation against plan or requirements before proceeding | After completing a task. After major feature implementation. Before merging. When executing plans (after each task). When stuck and need fresh perspective. | 1.0.0 |
| Subagent-Driven Development | Execute implementation plan by dispatching fresh subagent for each task, with code review between tasks | Alternative to executing-plans when staying in same session. When tasks are independent. When want fast iteration with review checkpoints. After writing implementation plan. | 1.0.0 |
| Using Git Worktrees | Create isolated git worktrees with smart directory selection and safety verification | When starting feature implementation in isolation. When brainstorming transitions to code. When need separate workspace without branch switching. Before executing implementation plans. | 1.0.0 |
| Writing Plans | Create detailed implementation plans with bite-sized tasks for engineers with zero codebase context | After brainstorming/design is complete. Before implementation begins. When delegating to another developer or session. When brainstorming skill hands off to planning. | 2.0.0 |

### Debugging (4 skills)

| Name | Description | When to Use | Version |
|------|-------------|-------------|---------|
| Defense-in-Depth Validation | Validate at every layer data passes through to make bugs impossible | Found a bug where invalid data causes problems deep in call stack | 1.0.0 |
| Root Cause Tracing | Systematically trace bugs backward through call stack to find original trigger | Bug appears deep in call stack but you need to find where it originates | 1.0.0 |
| Systematic Debugging | Four-phase debugging framework that ensures root cause investigation before attempting fixes. Never jump to solutions. | When encountering any technical issue, bug, test failure, or unexpected behavior. When tempted to quick-fix symptoms. When debugging feels chaotic or circular. When fixes don't stick. Before proposing any fix. When you notice yourself jumping to solutions. | 2.0.0 |
| Verification Before Completion | Run verification commands and confirm output before claiming success | Before claiming complete, fixed, working, passing, clean, ready, or done. Before expressing satisfaction with work. Before committing or creating PRs. When tempted to declare success. After code changes. When delegating to agents. | 1.0.0 |

### Meta (6 skills)

| Name | Description | When to Use | Version |
|------|-------------|-------------|---------|
| Gardening Skills Wiki | Maintain skills wiki health - check links, naming, cross-references, and coverage using LLM-native tools | When adding/removing skills. When reorganizing categories. When links feel broken. Periodically (weekly/monthly) to maintain wiki health. When INDEX files don't match directory structure. When cross-references might be stale. | 2.0.0 |
| Pulling Updates from Skills Repository | Sync local skills repository with upstream changes from obra/superpowers-skills | When session start shows "New skills available from upstream" or user wants to update skills | 1.0.0 |
| Sharing Skills | Contribute skills back to upstream via branch and PR | When you have a skill that would benefit others and want to contribute it to the upstream repository | 2.0.0 |
| Testing Skills With Subagents | RED-GREEN-REFACTOR for process documentation - baseline without skill, write addressing failures, iterate closing loopholes | When creating any skill (especially discipline-enforcing). Before deploying skills. When skill needs to resist rationalization under pressure. | 2.0.0 |
| Using Portable Skills | Deploy and use skills in any repository as IDE-agnostic markdown documentation | When setting up skills in a new project, updating existing skills, or migrating from script-based to scriptless mode | 2.0.0 |
| Writing Skills | TDD for process documentation - test with subagents before writing, iterate until bulletproof | When you discover a technique, pattern, or tool worth documenting for reuse. When editing existing skills. When asked to modify skill documentation. When you've written a skill and need to verify it works before deploying. | 5.0.0 |

### Problem-Solving (6 skills)

| Name | Description | When to Use | Version |
|------|-------------|-------------|---------|
| Collision-Zone Thinking | Force unrelated concepts together to discover emergent properties - "What if we treated X like Y?" | Can't find approach that fits your problem. Conventional solutions feel inadequate. Need innovative solution. Stuck thinking inside one domain. Want breakthrough, not incremental improvement. | 1.0.0 |
| Inversion Exercise | Flip core assumptions to reveal hidden constraints and alternative approaches - "what if the opposite were true?" | Stuck on assumptions you can't question. Solution feels forced. "This is how it must be done" thinking. Want to challenge conventional wisdom. Need fresh perspective on problem. | 1.0.0 |
| Meta-Pattern Recognition | Spot patterns appearing in 3+ domains to find universal principles | Same issue in different parts of codebase. Pattern feels familiar across projects. "Haven't I solved this before?" Different teams solving similar problems. Recurring solution shapes. | 1.0.0 |
| Scale Game | Test at extremes (1000x bigger/smaller, instant/year-long) to expose fundamental truths hidden at normal scales | Unsure if approach will scale. Edge cases unclear. Want to validate architecture. "Will this work at production scale?" Need to find fundamental limits. | 1.0.0 |
| Simplification Cascades | Find one insight that eliminates multiple components - "if this is true, we don't need X, Y, or Z" | Code has many similar-looking implementations. Growing list of special cases. Same concept handled 5 different ways. Excessive configuration. Many if/else branches doing similar things. Complexity spiraling. | 1.0.0 |
| When Stuck - Problem-Solving Dispatch | Dispatch to the right problem-solving technique based on how you're stuck | Stuck on a problem. Conventional approaches not working. Need to pick the right problem-solving technique. Not sure which skill applies. | 1.0.0 |

### Research (1 skill)

| Name | Description | When to Use | Version |
|------|-------------|-------------|---------|
| Tracing Knowledge Lineages | Understand how ideas evolved over time to find old solutions for new problems and avoid repeating past failures | When problem feels familiar but can't remember details. When asked "why do we use X?". Before abandoning an approach, understand why it exists. When evaluating "new" ideas that might be revivals. When past attempts failed and need to understand why. When tracing decision genealogy. | 1.0.0 |

### Testing (3 skills)

| Name | Description | When to Use | Version |
|------|-------------|-------------|---------|
| Condition-Based Waiting | Replace arbitrary timeouts with condition polling for reliable async tests | When tests use setTimeout/sleep and are flaky or timing-dependent | 1.0.0 |
| Test-Driven Development (TDD) | Write the test first, watch it fail, write minimal code to pass | Every feature and bugfix. No exceptions. Test first, always. When you wrote code before tests. When you're tempted to test after. When manually testing seems faster. When you already spent hours on code without tests. | 2.0.0 |
| Testing Anti-Patterns | Never test mock behavior. Never add test-only methods to production classes. Understand dependencies before mocking. | When writing tests. When adding mocks. When fixing failing tests. When tempted to add cleanup methods to production code. Before asserting on mock elements. | 1.0.0 |

## Quick Reference: Common Scenarios

| Scenario | Recommended Skill(s) |
|----------|---------------------|
| Starting a new feature | Test-Driven Development + Brainstorming Ideas Into Designs (if complex) |
| Fixing a bug | Systematic Debugging → Root Cause Tracing (if needed) → Test-Driven Development |
| Tests are flaky | Condition-Based Waiting |
| Stuck on a problem | When Stuck - Problem-Solving Dispatch |
| Code getting complex | Simplification Cascades |
| Need to change old code | Tracing Knowledge Lineages |
| Planning large work | Brainstorming Ideas Into Designs → Writing Plans |
| Executing a plan | Executing Plans or Subagent-Driven Development |
| About to merge/deploy | Verification Before Completion |
| Creating architecture docs | Creating ARC42 architecture documentation |
| Multiple independent bugs | Dispatching Parallel Agents |
| Receiving PR feedback | Code Review Reception |
| Feature is complete | Finishing a Development Branch |

## Statistics

- **Total Skills:** 32
- **Categories:** 7
- **Average Version:** 1.4
- **Most Active Category:** Collaboration (10 skills)

## Maintenance Notes

This digest is automatically generated from skill frontmatter. To rebuild:
1. Ensure all skills have complete YAML frontmatter
2. Run digest rebuild process
3. Verify all canonical skills appear exactly once
4. Check no setup/duplicate paths are included
