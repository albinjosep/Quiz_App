# Django Quiz App

A simple Django web application that allows a user to take a quiz, submit answers, and view results.

## Assumptions

- The app assumes that the database is already set up and the tables for `Question`, `UserSubmission`, and `QuizSession` exist.
- The app uses Django's default database settings (SQLite).
- The user interacts with the app through Postman or other API clients to start a quiz, get random questions, submit answers, and view results.
- The app is designed for a single user session (no authentication is implemented).

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/quiz-app.git


   ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

2. **Navigate into the project directory:**

bash
Copy code
cd quiz-app


3. **Create a virtual environment (optional but recommended):**

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

4. **Install dependencies:**

bash
Copy code
pip install -r requirements.txt

5. **Apply migrations to set up the database:**

bash
Copy code
python manage.py migrate

6. **Create some sample questions (optional but helpful for testing): You can add questions manually through Django Admin or use the Django shell to add sample questions.**

To open the Django shell:

bash
Copy code
python manage.py shell
Example to create a question:

python
Copy code
from quiz.models import Question
Question.objects.create(
    text="What is the capital of France?",
    option_a="Berlin", option_b="Madrid", option_c="Paris", option_d="Rome",
    correct_option="c"
)

7. **Run the development server:**

bash
Copy code
python manage.py runserver
Your app should now be accessible at http://127.0.0.1:8000/.

API Endpoints
GET /api/start/: Start a new quiz session.
GET /api/question/: Get a random question.
POST /api/submit/: Submit an answer for a question.
GET /api/results/: Get the results of the quiz session.
Testing with Postman
To interact with the API, you can use Postman or any other API client to test the following endpoints:

GET /api/start/: Start a new quiz session.
GET /api/question/: Retrieve a random question.
POST /api/submit/: Submit an answer with the parameters question_id and selected_option.
GET /api/results/: View the results of the quiz session.

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

Conclusion
This project demonstrates a simple Django API that allows a user to take a quiz, submit answers, and view results.

Feel free to make any changes or improvements to the app as you see fit.

css
Copy code

Make sure to adjust the repository URL, project details, and any assumptions according to your 
