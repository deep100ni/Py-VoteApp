# VoteApp

**VoteApp** is a simple and secure desktop-based voting application developed using **Python** and **Tkinter**. It is designed for use in school-level elections such as Head Boy and Head Girl selection.

This app ensures **one vote per student** by validating admission numbers, preventing duplicate voting, and securely storing vote counts.

---

## Key Features

- **User Authentication** using Admission Number
- **Candidate-Based Voting** for Multiple Posts
- **Real-Time Vote Recording**
- **Prevention of Duplicate Votes**
- **Dynamic GUI Navigation** (Previous, Next, Submit)
- **Thanks Screen** after successful voting
- **Data Persistence** using JSON files

---

## How It Works

1. User enters their **Admission Number**.
2. App checks if the user has already voted.
3. For each post (e.g., Head Boy, Head Girl), user selects one candidate.
4. Once all posts are voted, user can **Submit** their choices.
5. Votes are saved in `votes.json`, and the user's admission number is saved in `adm_nos.json`.

---

## Project Structure

- `main.py` - The main script to launch the application.
- `candidates.json` - Stores all the candidates mapped to their respective posts.
- `votes.json` - Stores vote counts for each candidate.
- `adm_nos.json` - Stores admission numbers of students who have already voted.

---
