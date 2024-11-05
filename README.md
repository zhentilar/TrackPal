# TrackPal: Your Personal Calorie Tracker
#### Video Demo: [TrackPal Video](<URL HERE>)
#### Description:

TrackPal is a web-based application designed to help users monitor their daily calorie intake. Built with Flask and designed to have a clean and minimal aesthetic, TrackPal provides an intuitive and visually appealing platform for users to track their calorie goals and food entries dairy. This project was developed as part of the CS50 web project assignment, focusing on responsive design, visual clarity, and essential functionality.

### Project Overview

The core objective of TrackPal is to simplify calorie tracking and make it a more accessible and engaging process. Users can set target calorie goals, add daily food entries, and visualize their progress through interactive progress bars. The application also provides easy navigation options for adding new entries, updating targets, and viewing progress in real-time.

The application features:
1. **User Registration and Login**: Users can create an account, set initial calorie goals, and log in to access personalized data.
2. **Calorie Tracking Dashboard**: Users can view their current progress toward calorie goals and add new food entries.
3. **Responsive Design**: The interface is fully responsive and adapts to various device sizes to enhance user experience.
4. **Minimalist Aesthetic**: The application is designed with a clean, visually appealing layout, prioritizing simplicity and functionality.

### Project Structure and Files

- `app.py`: This is the main Python file where the Flask application is defined. It includes routes for the homepage, user registration, login, food entry addition, and target updating. Each route connects to a corresponding HTML template and handles both GET and POST requests.
- `models.py`: Defines the database schema for storing user details, calorie targets, and food entries. It includes tables for `User`, `FoodEntry`, and `CalorieTarget`, each with attributes necessary for tracking user progress.
- `templates/`: This folder contains all HTML templates used in TrackPal. Key files include:
  - `home.html`: The main dashboard displaying current progress, total calories consumed, and a list of food entries.
  - `add_food.html`: The form for users to add a new food entry with calorie information.
  - `login.html` and `register.html`: Templates for user authentication, allowing users to log in and register.
  - `update_target.html`: A page for users to update their calorie target.
- `static/style.css`: This is the custom stylesheet that provides the clean styling across all templates. The style file includes responsive layouts, progress bar designs, and color themes that give the app its unique look.

### Design Choices and Reasoning

A primary design consideration was creating a minimalist interface that feels engaging without overwhelming the user with too much information. TrackPal’s layout relies on white space, a simple color palette, and clear progress visuals to create a seamless user experience. The progress bars use CSS-based animations, making it easy for users to visualize their achievements.

Additionally, I used Flask’s Jinja templating engine to keep HTML templates dynamic and reusable. For example, components such as the header and navigation links are consistent across all pages, ensuring a smooth user experience.

Some additional design considerations included:
- **Database Schema**: To ensure accurate tracking, I created separate tables for `FoodEntry` and `CalorieTarget`. This structure supports users setting new goals without losing previous progress records, allowing for flexibility in how calorie goals are updated over time.
  
### How to Run the Project

To run TrackPal locally:
1. Clone the repository to your local machine.
2. Navigate to the project folder and install the required dependencies listed.
3. Start the Flask server with `flask run`.
4. Access the application through your browser at `http://127.0.0.1`.

TrackPal is a project that reflects thoughtful design and a commitment to user experience, making it easy to track, set, and meet daily calorie goals in an approachable way.
