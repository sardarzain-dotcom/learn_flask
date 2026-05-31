# Anti-AI Writing Style Guide

## Avoid These AI-Generated Writing Patterns

### 1. Overly Formal and Robotic Language
**Don't:** "I would be happy to assist you in the implementation of this feature."
**Do:** "Let's build this feature together."

### 2. Excessive Use of Transition Words
**Don't:** "Furthermore, additionally, moreover, it is important to note that..."
**Do:** Use transitions sparingly and naturally.

### 3. Repetitive Sentence Structures
**Don't:** Starting every paragraph with "It is important to..." or "One should consider..."
**Do:** Vary your sentence beginnings and structures.

### 4. Generic, Non-Committal Statements
**Don't:** "This approach may potentially offer some benefits that could be useful."
**Do:** "This approach works well because..."

### 5. Overuse of Qualifying Language
**Don't:** "It seems that this might possibly be a good solution, perhaps."
**Do:** "This is a solid solution."

## Write Like a Human

### Use Personal Voice
- Include personal opinions and preferences
- Share specific experiences or anecdotes
- Use contractions (don't, won't, can't)
- Express genuine emotions and reactions

### Be Concise and Direct
- Get to the point quickly
- Use active voice
- Cut unnecessary words
- Make bold statements when appropriate

### Include Imperfections
- Use incomplete thoughts occasionally
- Include minor tangents
- Allow for some informality
- Don't over-explain everything

### Show Personality
- Use humor when appropriate
- Include cultural references
- Express preferences and biases
- Use colloquial expressions

### Specific Examples Over Generic Advice
**Don't:** "There are many benefits to this approach."
**Do:** "I saved 3 hours last week using this method."

### Natural Flow and Rhythm
- Read your writing aloud
- Vary sentence length
- Use natural pauses and breaks
- Trust your instincts

## Red Flags of AI Writing

Watch out for these telltale signs:
- Lists that always have exactly 3, 5, or 10 items
- Excessive use of "comprehensive," "robust," "seamless"
- Every paragraph ending with a summary statement
- Overly balanced perspectives on controversial topics
- Lack of specific, personal details
- Perfect grammar with no colloquialisms

## Most Common AI Words and Phrases to Avoid

### Overused Adjectives
- Comprehensive
- Robust
- Seamless
- Optimal
- Innovative
- Cutting-edge
- State-of-the-art
- Revolutionary
- Game-changing
- Powerful
- Efficient
- Effective
- Sophisticated
- Advanced
- Enhanced
- Streamlined
- Dynamic
- Versatile
- Scalable
- User-friendly

### Filler Phrases
- "It's worth noting that..."
- "It's important to understand that..."
- "In today's fast-paced world..."
- "As we move forward..."
- "In conclusion..."
- "To sum up..."
- "At the end of the day..."
- "When it comes to..."
- "In terms of..."
- "With that being said..."
- "However, it's crucial to remember..."
- "On the other hand..."
- "Furthermore..."
- "Moreover..."
- "Additionally..."

### Hedging Language
- Potentially
- Possibly
- Perhaps
- Might
- Could
- May
- Seems to
- Appears to
- Tends to
- Generally speaking
- In most cases
- Typically
- Usually
- Often
- Frequently

### Business Jargon Favorites
- Leverage
- Utilize
- Facilitate
- Implement
- Optimize
- Maximize
- Minimize
- Transform
- Revolutionize
- Disrupt
- Paradigm shift
- Synergy
- Best practices
- Core competencies
- Value proposition
- Strategic initiative
- Deliverables
- Stakeholders
- Touch base
- Circle back

### Generic Conclusion Starters
- "In summary..."
- "To conclude..."
- "In closing..."
- "All things considered..."
- "Taking everything into account..."
- "Ultimately..."
- "At the end of the day..."
- "In the final analysis..."

**Human Alternative:** Just end with your actual point or a call to action.

## Quick Test: The Human Check

Ask yourself:
1. Would I actually say this to a friend?
2. Does this sound like my natural speaking voice?
3. Am I being too diplomatic about my opinions?
4. Have I included any personal touches or experiences?

Remember: Good writing feels effortless, even when it takes effort to create.

## Targeted Writing Modes

### Academic Style
- Prefer precise claims over emotional language.
- Define key terms early and use them consistently.
- Favor evidence-based phrasing: "The data indicates..." not "This proves..."
- Keep tone formal but readable.

### Scientific Style
- Report methods and results clearly before interpretation.
- Avoid overclaiming causality unless your design supports it.
- Use domain terms accurately; remove vague intensifiers.
- Prioritize reproducibility language: assumptions, limitations, uncertainty.

### Resume + ATS Style
- Use standard section headings: Summary, Experience, Skills, Education, Projects.
- Start bullets with action verbs (Built, Led, Reduced, Automated, Delivered).
- Add measurable outcomes in bullets (%, $, time saved, throughput, scale).
- Mirror job-description keywords naturally in skills and experience.
- Avoid graphics-heavy formatting and unusual section names.

## Local Style Filter Script

Use this helper to flag and reduce common AI-sounding words/phrases in your own drafts.

```bash
python3 ai_style_filter.py your-draft.md
```

Academic profile:

```bash
python3 ai_style_filter.py your-draft.md --profile academic
```

Scientific profile:

```bash
python3 ai_style_filter.py your-draft.md --profile scientific
```

Resume + ATS profile (includes ATS quality checks):

```bash
python3 ai_style_filter.py your-resume.md --profile resume-ats
```

Rewrite to a new file:

```bash
python3 ai_style_filter.py your-draft.md --profile academic --output cleaned.md
```

Rewrite in-place:

```bash
python3 ai_style_filter.py your-draft.md --profile scientific --write
```

Note: This improves style and clarity. It is not a bypass tool for AI-detection systems.