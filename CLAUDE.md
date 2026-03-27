# AgentSkills Project Guidelines

This is the project-level CLAUDE.md for the AgentSkills repository.

---

## AI Native Skill Evaluation Standard

This repository uses a standardized 5-star rating system to evaluate Skill AI Native quality. **Every Skill modification MUST be evaluated using this standard.**

### Core Principle

> "Can AI complete the configuration without asking users or making guesses, solely based on the documentation?"

### Evaluation Dimensions (5 Dimensions)

| Dimension | Weight | Description |
|-----------|--------|-------------|
| **Instruction Clarity** | 25% | Can AI accurately understand what to do |
| **Execution Predictability** | 25% | Are AI execution results predictable and reproducible |
| **Error Handling Completeness** | 20% | Can AI handle problems correctly |
| **Cross-System Compatibility** | 15% | Can it run in different AI systems |
| **Efficiency Optimization** | 15% | Token usage efficiency, execution efficiency |

### Star Rating Standards

#### ⭐ (1/5) - Basic Description
- Has basic skill structure (frontmatter + content)
- Describes the task to be completed
- **Issues:** AI needs extensive guessing to execute
- **Typical Problems:**
  - Vague step descriptions ("configure it")
  - Missing specific commands/code
  - No error handling

#### ⭐⭐ (2/5) - Basically Usable
- Has clear step division
- Provides configuration examples
- **Issues:** Key details missing, prone to errors
- **Typical Problems:**
  - Unclear configuration formats (mixed usage across clients)
  - Missing detection logic ("auto-detect" but no method specified)
  - Simple error handling ("if it fails, please retry")

#### ⭐⭐⭐ (3/5) - Basically AI Native
- Steps are clear and executable
- Provides configuration templates
- Has basic troubleshooting
- **Issues:** Insufficient edge case handling
- **Typical Problems:**
  - Infinite retry on failure
  - Missing fallback strategies
  - Unoptimized token usage

#### ⭐⭐⭐⭐ (4/5) - Highly AI Native
- All instructions are clear and unambiguous
- Has explicit failure handling strategies
- Considers multiple execution paths
- **Issues:** Cross-system compatibility or minor details can be optimized
- **Typical Features:**
  - Clear detection logic
  - 3-attempt failure fallback mechanism
  - Structurally unified reference files

#### ⭐⭐⭐⭐⭐ (5/5) - Fully AI Native
- AI can execute completely by following instructions, no guessing needed
- Complete exception handling
- Reliable operation across multiple AI systems
- Token usage optimized
- **Typical Features:**
  - Visualized decision trees
  - Precise environment variable detection
  - Clear token optimization suggestions
  - Unified file structure

### Evaluation Checklist

**When modifying ANY Skill, you MUST complete this checklist:**

```markdown
## AI Native Evaluation Checklist

### Instruction Clarity (25 points)
- [ ] Each step has clear action verbs
- [ ] Conditional judgments have explicit check items (environment variables, file existence, etc.)
- [ ] Configuration formats have specific code examples
- [ ] Different scenarios have clear branches

### Execution Predictability (25 points)
- [ ] Has decision trees or flowcharts
- [ ] Success paths are explicit
- [ ] Failure paths are explicit
- [ ] Exit conditions are explicit

### Error Handling Completeness (20 points)
- [ ] Has retry mechanism (maximum attempts specified)
- [ ] Has fallback strategy (Plan B)
- [ ] Has final exit mechanism (prevents infinite loops)
- [ ] Troubleshooting covers common issues

### Cross-System Compatibility (15 points)
- [ ] Explicitly lists supported systems
- [ ] Configuration formats for different systems don't conflict
- [ ] Reference file structures are unified
- [ ] Has system detection logic

### Efficiency Optimization (15 points)
- [ ] Has token usage suggestions
- [ ] Avoids repeated reads
- [ ] Configuration examples are directly usable
- [ ] Has caching/state detection

**Total Score:** ___/100 → **Rating:** ___/5 stars
```

### Scoring Calculation

```
Total Score = Sum of all checked items (each item = 5 points)
Rating = Total Score / 20

- 0-20: ⭐
- 21-40: ⭐⭐
- 41-60: ⭐⭐⭐
- 61-80: ⭐⭐⭐⭐
- 81-100: ⭐⭐⭐⭐⭐
```

### Evaluation Report Template

**After completing Skill modifications, output this report:**

```markdown
## Skill Modification AI Native Evaluation Report

### Modified Files
- [List all modified files]

### Evaluation Score
| Dimension | Score | Notes |
|-----------|-------|-------|
| Instruction Clarity | __/25 | [Specific improvements] |
| Execution Predictability | __/25 | [Specific improvements] |
| Error Handling Completeness | __/20 | [Specific improvements] |
| Cross-System Compatibility | __/15 | [Specific improvements] |
| Efficiency Optimization | __/15 | [Specific improvements] |
| **Total** | **__/100** | |
| **Rating** | **__/5** | |

### Key Improvements
1. [Improvement 1]
2. [Improvement 2]
3. [Improvement 3]

### Remaining Issues
- [Issue 1]
- [Issue 2]

### Target AI Systems
- [ ] Claude Code
- [ ] Cursor
- [ ] VS Code Copilot
- [ ] Other: ___________

### Recommended Next Steps
- [Next optimization suggestions]
```

### Important Notes

1. **Mandatory Evaluation:** Every Skill modification MUST use this standard for evaluation
2. **Score Standards:**
   - Internal use skills: Minimum ⭐⭐⭐⭐ (80/100)
   - Open source/Shared skills: Must reach ⭐⭐⭐⭐⭐ (95/100)
3. **Cross-System Requirements:** If claiming support for multiple AI systems, must test in at least 2 different environments
4. **Documentation Updates:** After evaluation, update the docs/ directory with evaluation reports
5. **Continuous Improvement:** Lower-rated skills should have improvement plans
