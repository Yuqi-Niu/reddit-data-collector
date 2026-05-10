# Reddit Data Collector

A simple Python project for collecting Reddit posts and comments using the Reddit API and PRAW.

This project is designed for:

- Academic research
- Social media analysis
- Reddit data collection experiments
- NLP / multimodal research
- Meme and privacy studies

---

# Features

- Collect posts from one or more subreddits
- Optionally collect comments
- Save results as CSV files
- Record readable UTC timestamps
- Support multiple sorting methods
- Support keyword search
- Easy configuration through `config.py`
- Compatible with both Windows and macOS

---

# Project Structure

```text
reddit-data-collector/
├── reddit_collector.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Requirements

- Python 3.9+
- Reddit API credentials

---

# Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/reddit-data-collector.git
cd reddit-data-collector
```

Replace:

```text
YOUR_USERNAME
```

with your GitHub username.

---

# Step 2: Create a Virtual Environment

Using a virtual environment is recommended to avoid dependency conflicts.

## Windows

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

If successful, you should see:

```text
(.venv)
```

at the beginning of the terminal.

---

## macOS

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate:

```bash
source .venv/bin/activate
```

If successful, you should see:

```text
(.venv)
```

at the beginning of the terminal.

---

# Step 3: Install Dependencies

## Windows

```bash
pip install -r requirements.txt
```

## macOS

```bash
pip3 install -r requirements.txt
```

---

# Step 4: Create Reddit API Credentials

Go to:

```text
https://www.reddit.com/prefs/apps
```

Click:

```text
Create App
```

Use the following settings:

```text
name: reddit-data-collector
type: script
redirect uri: http://localhost:8080
```

After creating the app, copy:

- client_id
- client_secret

---

# Step 5: Configure API Credentials

Open:

```text
config.py
```

Edit:

```python
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"
USER_AGENT = "reddit data collector by u/your_reddit_username"
```

---

# Step 6: Configure Collection Settings

In `config.py`, you can customize:

## Subreddits

```python
SUBREDDITS = ["privacy", "AskReddit"]
```

---

## Post Limit

```python
POST_LIMIT = 20
```

---

## Collect Comments

```python
COLLECT_COMMENTS = True
```

Disable comment collection:

```python
COLLECT_COMMENTS = False
```

---

## Comment Limit Per Post

```python
COMMENT_LIMIT_PER_POST = 10
```

---

## Sorting Method

```python
SORT_TYPE = "new"
```

Available options:

- `"new"`
- `"hot"`
- `"top"`
- `"rising"`
- `"controversial"`

---

## Keyword Search

Disable keyword filtering:

```python
KEYWORD = None
```

Enable keyword search:

```python
KEYWORD = "privacy"
```

---

# Step 7: Run the Script

## Windows

```bash
python reddit_collector.py
```

## macOS

```bash
python3 reddit_collector.py
```

---

# Output Files

The script generates:

```text
reddit_posts.csv
reddit_comments.csv
```

These files contain:

## Posts

- post id
- title
- text
- score
- subreddit
- timestamps
- URLs
- metadata

## Comments

- comment id
- post id
- body
- score
- timestamps
- metadata

---

# Example Output

```text
Collecting posts from r/privacy...

Collecting comments for post: abc123

Saved 20 posts to reddit_posts.csv
Saved 200 comments to reddit_comments.csv

Done!
```

---

# Notes on Research Ethics

This project is intended for academic and research purposes.

Please:

- Follow Reddit API Terms of Service
- Avoid collecting unnecessary personal information
- Respect subreddit community rules
- Anonymize user information when necessary

---

# Dependencies

```text
praw
pandas
```

Install manually:

```bash
pip install praw pandas
```

---

# Future Improvements

Possible future features include:

- JSON / JSONL export
- Async collection
- Image downloading
- Pushshift integration
- Time range filtering
- CLI arguments
- Docker support
- Automatic anonymization
- Database storage
- Sentiment analysis

---

# License

MIT License
