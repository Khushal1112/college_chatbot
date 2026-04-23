# 🚀 Quick Start Guide

## Installation & Running

### Step 1: Install Dependencies
```bash
cd college_chatbot
pip install -r requirements.txt
```

### Step 2: Start the Server
```bash
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### Step 3: Open in Browser
Navigate to: **http://localhost:5000**

## What You'll See

### 1. College Website
- Beautiful homepage with hero section
- Navigation menu (Home, About, Courses, Admissions, Placements, Facilities, Contact)
- Smooth scrolling between sections
- Responsive design (works on mobile too!)

### 2. Floating Chatbot Button
- Look at the **bottom-right corner**
- You'll see a **blue circular button** with a chat icon
- It has a "Ask me!" badge and pulse animation

### 3. Using the Chatbot
1. **Click the floating button**
2. A chatbot modal will open
3. Try these quick suggestions:
   - 📋 Admissions
   - 📚 Courses
   - 💰 Fees
   - 💼 Placements
   - 🏠 Hostel
4. Or type your own question like:
   - "What courses do you offer?"
   - "How do I apply?"
   - "Tell me about scholarships"
5. Click the **X** to close the chatbot

## Testing the Chatbot Engine

Run the test suite:
```bash
python test_chatbot.py
```

Expected output:
```
12/12 tests passed.
```

## Customization Quick Tips

### Change College Name
Edit `templates/home.html`, line ~15:
```html
<span>Your College Name</span>
```

### Change Colors
Edit `static/css/style.css`, lines 13-20:
```css
:root {
  --primary: #0f3460;    /* Main blue */
  --secondary: #533483;  /* Purple */
  --accent: #e94560;     /* Red/Pink */
}
```

### Add New Chatbot Intent
Edit `intents.json`, add:
```json
{
  "tag": "your_topic",
  "patterns": ["question 1", "question 2"],
  "responses": ["Answer here"]
}
```

Restart the server to see changes.

## Troubleshooting

### Port Already in Use
```bash
# Kill process on port 5000 (Windows)
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Or use a different port
# Edit app.py, last line:
app.run(debug=True, host="0.0.0.0", port=5001)
```

### Chatbot Not Responding
1. Check browser console (F12) for errors
2. Verify `/api/chat` endpoint:
   ```bash
   curl -X POST http://localhost:5000/api/chat \
     -H "Content-Type: application/json" \
     -d '{"message": "hello"}'
   ```

### Styles Not Loading
1. Clear browser cache (Ctrl+Shift+R)
2. Check `static/css/style.css` exists
3. Verify Flask is serving static files

## Next Steps

✅ Explore all website sections  
✅ Test different chatbot queries  
✅ Customize content for your college  
✅ Add your own intents  
✅ Deploy to production (Heroku, AWS, etc.)  

## Need Help?

Check the main **README.md** for detailed documentation.

---

**Enjoy your new college website with AI chatbot! 🎓**
