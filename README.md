# Chrome Audible Auto Add-to-Library

This Python script uses Selenium to automatically click all visible **"Add to Library"** buttons on an Audible (or similar) web page that’s open in an existing Chrome session.

## 🚀 How It Works
- Connects to a running Chrome window started with remote debugging (`--remote-debugging-port=9222`)
- Finds all visible "Add to Library" buttons
- Clicks each one safely (handling dynamic pages and avoiding stale element errors)
- Stops when no more buttons are found

## 🧠 Requirements
- Python 3.8+
- Google Chrome
- Chrome Driver for your version of chrome, found here (https://googlechromelabs.github.io/chrome-for-testing/)
- Selenium for Python  
Install it with:
  ```bash
  pip install selenium
  ```

⚙️ Setup
1.	Start Chrome with remote debugging enabled.
Open a new terminal window and run:
  ```bash
  /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/tmp/chrome-debug"
  ```

2.	Navigate to the Audible page you want to automate. Be sure to be logged in to your account.

3.	Run the script:
  ```bash
  python add_books.py
  ```

📝 Notes
•	The script connects to your existing Chrome session, so you stay logged in.
•	It’s safe to stop and restart — only visible “Add to Library” buttons are clicked.
•	Don't enter anything else in the Terminal Shell that is running your chrome session once you've launched chrome. You will know it is running chrome when you see a line towards the top that says: "DevTools listening on ws://127.0.0.1:9222/devtools/browser/<some-long-id>"
•	When you are done just terminate the terminal shell and it will close the chrome session.
