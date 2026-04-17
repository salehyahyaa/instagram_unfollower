# Instagram Unfollower

Automated Instagram unfollow tracker that detects when mutual followers unfollow you and automatically unfollows them back. Runs once daily and sends a native Mac desktop notification with who got removed.

## Features

* Detects when a mutual unfollows you
* Automatically unfollows them back
* Saves daily snapshots of followers, following, and mutuals to a local PostgreSQL database
* Native Mac desktop notifications
* Session management to avoid repeated logins

## Flow

```
Login → Load Session
        ↓
Get Followers + Following
        ↓
Calculate Mutuals (followers & following)
        ↓
Compare with Yesterday's Mutuals (from db)
        ↓
Detect Unfollowers → Auto Unfollow → Notify
        ↓
Save Today's Snapshot to DB
```

## Project Structure

```
instagram_unfollower/
│
├── src/
│   ├── main.py
│   ├── authUser.py
│   ├── followerAuditing.py
│   ├── notifyUser.py
│   └── database/
│       ├── __init__.py
│       └── connection.py
│
├── documentation/
│   ├── schema.sql
│   └── diagram
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository

```
git clone https://github.com/salehyahyaa/instagram_unfollower.git
cd instagram_unfollower
```

2. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory

```
IG_USERNAME=your_instagram_username
IG_PASSWORD=your_instagram_password
DB_URL=postgresql://your_user@localhost:5432/instaAuditor
```

5. Set up the database — see `documentation/` for the schema and diagram

## How to Run

```
cd src
python3 main.py
```

The program will run automatically every day at 6:30pm. Keep the terminal open or run it as a background process.

## License
This project is licensed under the MIT License - see the LICENSE file for details.