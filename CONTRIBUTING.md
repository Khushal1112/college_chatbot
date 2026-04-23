# Contributing to College Chatbot

First off, thank you for considering contributing to College Chatbot! It's people like you that make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

**Unacceptable behavior includes:**
- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

---

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

**Bug Report Template:**
```markdown
**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear description of what you expected to happen.

**Screenshots**
If applicable, add screenshots to help explain your problem.

**Environment:**
 - OS: [e.g. Windows 10, macOS 13, Ubuntu 22.04]
 - Python Version: [e.g. 3.11.0]
 - Browser: [e.g. Chrome 120, Firefox 121]
 - Version: [e.g. 1.0.0]

**Additional context**
Add any other context about the problem here.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

**Enhancement Template:**
```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is. Ex. I'm always frustrated when [...]

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
A clear description of any alternative solutions or features you've considered.

**Additional context**
Add any other context or screenshots about the feature request here.
```

### Your First Code Contribution

Unsure where to begin? You can start by looking through these issues:
- `good-first-issue` - Issues that should only require a few lines of code
- `help-wanted` - Issues that are a bit more involved

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Make sure your code follows the style guidelines
5. Issue that pull request!

---

## Development Setup

### Prerequisites
- Python 3.8+
- Git
- Virtual environment tool

### Setup Steps

1. **Fork and clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/college-chatbot.git
cd college-chatbot
```

2. **Create a virtual environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run tests**
```bash
python test_chatbot.py
```

5. **Start the development server**
```bash
python app.py
```

6. **Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

---

## Coding Standards

### Python Code Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

**Key Points:**
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Add docstrings to all functions and classes
- Use type hints where appropriate

**Example:**
```python
def get_response(self, user_input: str) -> dict:
    """
    Process user input and return a response.
    
    Args:
        user_input (str): The user's message
        
    Returns:
        dict: Response with 'response', 'tag', and 'confidence' keys
    """
    # Implementation here
    pass
```

### JavaScript Code Style

- Use 2 spaces for indentation
- Use `const` and `let`, avoid `var`
- Use semicolons
- Use meaningful variable names
- Add comments for complex logic

**Example:**
```javascript
const sendMessage = async (message) => {
  // Validate input
  if (!message.trim()) {
    return;
  }
  
  // Send to API
  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });
  
  return response.json();
};
```

### HTML/CSS Style

- Use 2 spaces for indentation
- Use semantic HTML5 elements
- Use BEM naming convention for CSS classes
- Keep CSS organized by component

**Example:**
```html
<section class="hero">
  <div class="hero__content">
    <h1 class="hero__title">Welcome</h1>
    <p class="hero__subtitle">Subtitle text</p>
  </div>
</section>
```

### File Organization

```
New files should follow this structure:
- Python files: app/, models/, utils/
- Templates: templates/
- Static files: static/css/, static/js/, static/images/
- Tests: tests/
- Documentation: docs/
```

---

## Commit Guidelines

### Commit Message Format

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that don't affect code meaning (formatting, etc.)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding or updating tests
- `chore`: Changes to build process or auxiliary tools

**Examples:**
```bash
feat(chatbot): add multi-language support

Add support for Hindi and Spanish languages in the chatbot.
Includes translation files and language detection.

Closes #123

---

fix(ui): correct modal positioning on mobile

The chatbot modal was not properly centered on mobile devices.
Updated CSS to use flexbox centering.

Fixes #456

---

docs(readme): update installation instructions

Added Docker deployment section and clarified Python version requirements.
```

### Commit Best Practices

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests after the first line
- Consider starting the commit message with an applicable emoji:
  - 🎨 `:art:` - Improve structure/format
  - ⚡️ `:zap:` - Improve performance
  - 🐛 `:bug:` - Fix a bug
  - ✨ `:sparkles:` - Introduce new features
  - 📝 `:memo:` - Add or update documentation
  - 🚀 `:rocket:` - Deploy stuff
  - ✅ `:white_check_mark:` - Add or update tests

---

## Pull Request Process

### Before Submitting

1. **Update documentation** - If you changed APIs, update the README
2. **Add tests** - Ensure your code is tested
3. **Run tests** - Make sure all tests pass
4. **Update CHANGELOG** - Add your changes to CHANGELOG.md
5. **Check code style** - Ensure your code follows our style guide

### PR Template

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## How Has This Been Tested?
Describe the tests you ran to verify your changes.

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Related Issues
Closes #(issue number)
```

### Review Process

1. **Automated checks** - CI/CD will run tests automatically
2. **Code review** - At least one maintainer will review your code
3. **Feedback** - Address any requested changes
4. **Approval** - Once approved, a maintainer will merge your PR

### After Your PR is Merged

- Delete your branch (if you want)
- Update your local repository
- Celebrate! 🎉 You've contributed to open source!

---

## Development Workflow

### Branching Strategy

We use a simplified Git Flow:

- `main` - Production-ready code
- `develop` - Integration branch for features
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Urgent production fixes

**Example:**
```bash
# Create a feature branch
git checkout -b feature/add-voice-support

# Make changes and commit
git add .
git commit -m "feat(chatbot): add voice input support"

# Push to your fork
git push origin feature/add-voice-support

# Create a pull request on GitHub
```

### Testing

**Run all tests:**
```bash
python test_chatbot.py
```

**Test specific functionality:**
```bash
python -c "from chatbot import CollegeChatbot; bot = CollegeChatbot(); print(bot.get_response('hello'))"
```

**Manual testing:**
1. Start the app: `python app.py`
2. Open http://localhost:5000
3. Test all features
4. Check console for errors

---

## Adding New Features

### Adding a New Intent

1. **Edit `Dataset/intents.json`:**
```json
{
  "intent": "library_hours",
  "text": [
    "when is the library open",
    "library timings",
    "library hours"
  ],
  "responses": [
    "The library is open from 8 AM to 10 PM on weekdays and 9 AM to 6 PM on weekends."
  ],
  "extension": {
    "function": "",
    "entities": false,
    "responses": []
  },
  "context": {
    "in": "",
    "out": "LibraryHours",
    "clear": true
  },
  "entityType": "NA",
  "entities": []
}
```

2. **Test the new intent:**
```bash
python -c "from chatbot import CollegeChatbot; bot = CollegeChatbot(); print(bot.get_response('library hours'))"
```

3. **Add to test suite** in `test_chatbot.py`

### Adding a New API Endpoint

1. **Add route in `app.py`:**
```python
@app.route("/api/feedback", methods=["POST"])
def submit_feedback():
    """Submit user feedback."""
    data = request.get_json()
    # Process feedback
    return jsonify({"status": "success"})
```

2. **Update API documentation** in README.md

3. **Add tests** for the new endpoint

---

## Questions?

If you have questions, you can:
- Open an issue with the `question` label
- Join our [Discord server](https://discord.gg/your-server)
- Email us at dev@yourproject.com

---

## Recognition

Contributors will be recognized in:
- README.md Contributors section
- CHANGELOG.md for each release
- GitHub Contributors page

Thank you for contributing! 🙏

---

<div align="center">

**Happy Coding! 💻**

</div>
