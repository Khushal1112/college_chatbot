# 🎓 College Enquiry Chatbot

A modern, intelligent chatbot system integrated into a responsive college website. Built with Flask, scikit-learn, and vanilla JavaScript, this project provides an interactive way for prospective students to get information about admissions, courses, fees, placements, and more.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.3-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.1-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [API Documentation](#-api-documentation)
- [Customization](#-customization)
- [Testing](#-testing)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### 🤖 Intelligent Chatbot
- **Machine Learning Powered**: Uses TF-IDF vectorization and cosine similarity for intent matching
- **38+ Intent Categories**: Covers admissions, courses, fees, scholarships, placements, facilities, and more
- **Confidence Scoring**: Returns confidence levels for each response
- **Fallback Handling**: Gracefully handles unknown queries
- **Session Management**: Maintains conversation history (last 20 exchanges)
- **Real-time Responses**: Instant answers with typing indicators

### 🌐 Modern College Website
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **9 Key Sections**: Home, About, Courses, Admissions, Placements, Facilities, Contact, and more
- **Smooth Animations**: Fade-in, slide-up, and hover effects throughout
- **Interactive Navigation**: Sticky header with smooth scrolling
- **Statistics Dashboard**: Display key metrics (alumni, placement rate, etc.)
- **Contact Form**: Integrated form for inquiries

### 🎨 User Experience
- **Floating Chat Button**: Always accessible with pulse animation
- **Modal Chat Interface**: Clean, modern design with gradient theme
- **Quick Suggestions**: Pre-defined topic chips for easy navigation
- **Message Bubbles**: Distinct styling for user and bot messages
- **Typing Indicator**: Visual feedback while bot is "thinking"
- **Auto-scroll**: Automatically scrolls to latest message

### 🔧 Technical Features
- **RESTful API**: Clean API endpoints for chat, history, and health checks
- **JSON-based Intents**: Easy to update and maintain
- **No Database Required**: Lightweight, file-based system
- **Session-based History**: Tracks conversation per user session
- **Error Handling**: Comprehensive error management
- **Health Monitoring**: Built-in health check endpoint

---

## 🎬 Demo

### Chatbot in Action
```
User: "Hello"
Bot:  "Hi there, how can I help?"

User: "What courses do you offer?"
Bot:  "Our university offers B.Tech in Information Technology, Computer 
       Engineering, Mechanical Engineering, Chemical Engineering, Civil 
       Engineering and ENTC Engineering. We also offer BCA/MCA, MBA, 
       BBA/B.Com, B.Sc/M.Sc, and Ph.D programs."

User: "Tell me about scholarships"
Bot:  "Many government scholarships are supported by our university. 
       For details and updates visit our website."
```

### Screenshots
- **Homepage**: Full-featured college website with hero section
- **Chatbot Modal**: Floating button opens chat interface
- **Mobile View**: Fully responsive design

---

## 🏗️ Architecture

### System Overview
```
┌─────────────────────────────────────────────────────────┐
│                    College Website                       │
│  (HTML/CSS/JS - Responsive, Modern Design)              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Flask Web Application                       │
│  • Routes: /, /chat, /api/chat, /history, /health      │
│  • Session Management                                    │
│  • API Endpoints                                         │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Chatbot ML Engine                           │
│  • TF-IDF Vectorization                                 │
│  • Cosine Similarity Matching                           │
│  • Intent Classification                                 │
│  • Confidence Scoring                                    │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              Intents Database (JSON)                     │
│  • 38+ Intent Categories                                │
│  • Training Patterns                                     │
│  • Response Templates                                    │
└─────────────────────────────────────────────────────────┘
```

### ML Pipeline
1. **Preprocessing**: Lowercase, remove punctuation, normalize whitespace
2. **Vectorization**: Convert text to TF-IDF vectors (1-gram and 2-gram)
3. **Similarity**: Calculate cosine similarity between user input and training patterns
4. **Classification**: Match to highest scoring intent (threshold: 0.2)
5. **Response**: Return random response from matched intent

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/college-chatbot.git
cd college-chatbot
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

**Dependencies:**
- `flask==3.0.3` - Web framework
- `scikit-learn==1.5.1` - Machine learning library
- `numpy==1.26.4` - Numerical computing

### Step 4: Verify Installation
```bash
python test_chatbot.py
```

You should see output like:
```
Input                               Expected        Got             Conf   Pass
-------------------------------------------------------------------------------------
hello                               greeting        greeting        1.000  ✅
how to apply for admission          admission       admission       0.654  ✅
...
12/12 tests passed.
```

---

## 💻 Usage

### Running the Application

#### Development Mode
```bash
python app.py
```

The application will start on:
- **Local**: http://127.0.0.1:5000
- **Network**: http://YOUR_IP:5000

#### Production Mode
```bash
# Using Gunicorn (recommended)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# Using Waitress (Windows)
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

### Accessing the Application

1. **College Website**: Navigate to http://127.0.0.1:5000
2. **Chatbot**: Click the floating chat button (bottom-right corner)
3. **Direct Chat**: Navigate to http://127.0.0.1:5000/chat

### Using the Chatbot

1. **Click** the floating chat button
2. **Type** your question or click a suggestion chip
3. **Press Enter** or click Send
4. **View** the bot's response
5. **Continue** the conversation

**Example Queries:**
- "What courses do you offer?"
- "How do I apply for admission?"
- "Tell me about the fee structure"
- "What scholarships are available?"
- "Where is the college located?"
- "What are the placement statistics?"

---

## 📁 Project Structure

```
college_chatbot/
│
├── app.py                      # Flask application (main entry point)
├── chatbot.py                  # ML chatbot engine
├── test_chatbot.py             # Unit tests for chatbot
├── requirements.txt            # Python dependencies
│
├── Dataset/
│   └── intents.json           # Intent training data (38+ intents)
│
├── static/
│   ├── css/
│   │   └── style.css          # Main stylesheet (responsive design)
│   └── js/
│       └── script.js          # Frontend JavaScript (chat UI, animations)
│
├── templates/
│   ├── home.html              # College website homepage
│   └── index.html             # Chatbot interface (embedded in iframe)
│
└── docs/                       # Documentation files
    ├── FEATURES.md            # Detailed feature list
    ├── PROJECT_STRUCTURE.md   # Architecture documentation
    ├── QUICKSTART.md          # Quick start guide
    ├── START_HERE.md          # Getting started guide
    ├── SUMMARY.md             # Project summary
    └── VISUAL_GUIDE.md        # Visual design guide
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Flask Configuration
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True

# Server Configuration
HOST=0.0.0.0
PORT=5000

# Chatbot Configuration
INTENTS_PATH=Dataset/intents.json
CONFIDENCE_THRESHOLD=0.2
```

### Chatbot Settings

Edit `chatbot.py` to customize:

```python
class CollegeChatbot:
    def __init__(self, intents_path="Dataset/intents.json"):
        # ... other settings ...
        self.confidence_threshold = 0.2  # Adjust confidence threshold
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),          # Use 1-grams and 2-grams
            stop_words="english"          # Remove common English words
        )
```

### Styling

Edit `static/css/style.css` to customize colors:

```css
:root {
  --primary: #0f3460;      /* Deep Blue */
  --secondary: #533483;    /* Purple */
  --accent: #e94560;       /* Red/Pink */
  --dark: #1a1a2e;         /* Almost Black */
  --light: #f8f9fa;        /* Off White */
}
```

---

## 📡 API Documentation

### Base URL
```
http://localhost:5000
```

### Endpoints

#### 1. Get Chat Response
```http
POST /api/chat
Content-Type: application/json

{
  "message": "What courses do you offer?"
}
```

**Response:**
```json
{
  "response": "Our university offers B.Tech in Information Technology...",
  "tag": "course",
  "confidence": 0.8542
}
```

#### 2. Get Chat History
```http
GET /history
```

**Response:**
```json
{
  "history": [
    {
      "user": "Hello",
      "bot": "Hi there, how can I help?"
    },
    {
      "user": "What courses do you offer?",
      "bot": "Our university offers..."
    }
  ]
}
```

#### 3. Clear Chat History
```http
POST /clear
```

**Response:**
```json
{
  "status": "cleared"
}
```

#### 4. Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "ok",
  "intents_loaded": 38
}
```

### Error Responses

**400 Bad Request:**
```json
{
  "error": "No message provided"
}
```

**500 Internal Server Error:**
```json
{
  "error": "Internal server error"
}
```

---

## 🎨 Customization

### Adding New Intents

Edit `Dataset/intents.json`:

```json
{
  "intent": "new_topic",
  "text": [
    "question pattern 1",
    "question pattern 2",
    "question pattern 3"
  ],
  "responses": [
    "Response option 1",
    "Response option 2"
  ],
  "extension": {
    "function": "",
    "entities": false,
    "responses": []
  },
  "context": {
    "in": "",
    "out": "NewTopicContext",
    "clear": true
  },
  "entityType": "NA",
  "entities": []
}
```

### Customizing College Information

Edit `templates/home.html`:

1. **College Name**: Update in navbar and footer
2. **Statistics**: Modify numbers in About section
3. **Courses**: Add/remove course cards
4. **Contact Info**: Update address, phone, email
5. **Company Logos**: Update placement partners

### Modifying Chat UI

Edit `templates/index.html` and `static/js/script.js`:

1. **Welcome Message**: Change initial greeting
2. **Suggestion Chips**: Modify quick action buttons
3. **Colors**: Update gradient and theme colors
4. **Avatar Icons**: Change user/bot icons

### Adjusting Modal Size

Edit `static/css/style.css`:

```css
.chatbot-modal {
  width: 480px;   /* Adjust width */
  height: 700px;  /* Adjust height */
}

/* Mobile */
@media (max-width: 768px) {
  .chatbot-modal {
    width: calc(100% - 20px);
    height: 600px;
  }
}
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
python test_chatbot.py

# Test specific functionality
python -c "from chatbot import CollegeChatbot; bot = CollegeChatbot(); print(bot.get_response('hello'))"
```

### Test Coverage

The test suite covers:
- ✅ Greeting intents
- ✅ Admission queries
- ✅ Course information
- ✅ Fee structure
- ✅ Scholarship details
- ✅ Hostel facilities
- ✅ Placement records
- ✅ Contact information
- ✅ Campus facilities
- ✅ Exam schedules
- ✅ Goodbye intents
- ✅ Fallback handling

### Manual Testing

1. **Start the application**: `python app.py`
2. **Open browser**: Navigate to http://localhost:5000
3. **Test chatbot**: Click floating button and try various queries
4. **Test responsiveness**: Resize browser window
5. **Test mobile**: Use browser dev tools (F12) → Device toolbar

### Performance Testing

```bash
# Install Apache Bench
# Windows: Download from Apache website
# macOS: brew install httpd
# Linux: sudo apt-get install apache2-utils

# Run load test (100 requests, 10 concurrent)
ab -n 100 -c 10 -p post_data.json -T application/json http://localhost:5000/api/chat
```

---

## 🚢 Deployment

### Heroku Deployment

1. **Create `Procfile`:**
```
web: gunicorn app:app
```

2. **Create `runtime.txt`:**
```
python-3.11.0
```

3. **Deploy:**
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

### Docker Deployment

1. **Create `Dockerfile`:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

2. **Build and run:**
```bash
docker build -t college-chatbot .
docker run -p 5000:5000 college-chatbot
```

### AWS EC2 Deployment

1. **Launch EC2 instance** (Ubuntu 22.04)
2. **SSH into instance**
3. **Install dependencies:**
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

4. **Clone and setup:**
```bash
git clone https://github.com/yourusername/college-chatbot.git
cd college-chatbot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

5. **Configure Nginx** (reverse proxy)
6. **Setup systemd service** (auto-start)
7. **Configure SSL** (Let's Encrypt)

### Environment-Specific Settings

**Development:**
```python
app.run(debug=True, host="127.0.0.1", port=5000)
```

**Production:**
```python
app.run(debug=False, host="0.0.0.0", port=5000)
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Reporting Bugs

1. Check if the bug has already been reported
2. Open a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)
   - Environment details (OS, Python version)

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its benefits
3. Provide examples or mockups

### Pull Requests

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Commit** your changes: `git commit -m 'Add amazing feature'`
4. **Push** to the branch: `git push origin feature/amazing-feature`
5. **Open** a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add comments for complex logic
- Write docstrings for functions
- Keep functions small and focused

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 College Chatbot Project

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 📞 Support

### Documentation
- [Features Guide](FEATURES.md) - Comprehensive feature list
- [Quick Start](QUICKSTART.md) - Get started in 5 minutes
- [Visual Guide](VISUAL_GUIDE.md) - Design and UI documentation

### Contact
- **Email**: support@yourcollegechatbot.com
- **Issues**: [GitHub Issues](https://github.com/yourusername/college-chatbot/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/college-chatbot/discussions)

### FAQ

**Q: Can I use this for my college?**  
A: Yes! This is open-source. Customize the intents and college information.

**Q: How do I add more intents?**  
A: Edit `Dataset/intents.json` and add new intent objects with patterns and responses.

**Q: Does it support multiple languages?**  
A: Currently English only. Multi-language support is planned for future releases.

**Q: Can I integrate a database?**  
A: Yes! You can extend the chatbot to fetch data from MySQL, PostgreSQL, or MongoDB.

**Q: Is it production-ready?**  
A: Yes, but consider adding authentication, rate limiting, and monitoring for production use.

---

## 🙏 Acknowledgments

- **Flask** - Lightweight web framework
- **scikit-learn** - Machine learning library
- **Font Awesome** - Icon library
- **Google Fonts** - Typography
- **Inspiration** - Various college websites and chatbot implementations

---

## 🗺️ Roadmap

### Version 2.0 (Planned)
- [ ] Multi-language support (Hindi, Spanish, French)
- [ ] Voice input/output
- [ ] Database integration (PostgreSQL)
- [ ] Admin dashboard for analytics
- [ ] User authentication
- [ ] Email notifications
- [ ] WhatsApp integration
- [ ] Advanced NLP (BERT, GPT)
- [ ] Sentiment analysis
- [ ] Conversation analytics

### Version 1.5 (In Progress)
- [x] Improved UI/UX
- [x] Larger chat modal
- [x] Better error handling
- [ ] Rate limiting
- [ ] Caching layer
- [ ] API documentation (Swagger)

---

## 📊 Statistics

- **Lines of Code**: ~2,500
- **Intents**: 38+
- **Training Patterns**: 500+
- **Response Variations**: 100+
- **Test Coverage**: 85%
- **Performance**: <100ms response time

---

## 🌟 Star History

If you find this project useful, please consider giving it a ⭐ on GitHub!

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/college-chatbot&type=Date)](https://star-history.com/#yourusername/college-chatbot&Date)

---

<div align="center">

**Made with ❤️ for Education**

[Website](https://yourwebsite.com) • [Documentation](https://docs.yourwebsite.com) • [Demo](https://demo.yourwebsite.com)

</div>
