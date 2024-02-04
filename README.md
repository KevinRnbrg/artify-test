Follow the instructions to set up the project:
# XAMPP
1. Download XAMPP with default settings.
2. Start XAMPP.
3. In XAMPP, start Apache and MySQL.
4. Navigate to 'http://localhost/dashboard/' in your browser.
5. Open phpMyAdmin from the selection at the top of the page.
6. From the left sidebar, select 'New' to create a new database.
7. Name the new database 'artify_database'.
8. From the top tab, select 'Import', and add the database dump file to the 'File to import' window. Then, press 'Import' at the bottom of the page.
# Backend
1. Download Python 3.12 (if not already installed on your computer).
2. Install the repository zip and extract it.
3. Open the project in a code editor.
4. In /artify-test-main/project_files/backend/venv:
* Install Flask: pip install Flask
* Install Flask-MySQLdb: pip install Flask-MySQLdb
* Install Flask-SQLAlchemy: pip install Flask-SQLAlchemy
* Install Flask-Cors: pip install Flask-Cors
5. In /artify-test-main/project_files/backend/venv, run 'python app.py'.
# Frontend
1. In a new terminal in /artify-test-main/project_files/ (project root), run 'npm i' to install necessary packages.
2. Then run 'npm run dev' to start the developement server.

If there were no errors, the site will be working on http://127.0.0.1:5173/ or on another specified port in the terminal.
