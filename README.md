# Calisthenics and Macro Tracker

A command-line Python application designed to help users track their calisthenics workouts and daily nutritional intake (macros). The app supports multiple user profiles and uses local text files to store data, ensuring progress is saved between sessions.

## Features
- **User Profiles:** Create and switch between multiple user profiles. Calculates basal metabolic rate (BMR), total daily energy expenditure (TDEE), and macro targets based on height, weight, activity level, and goals (cut, maintain, bulk).
- **Workout Logging:** Log calisthenics exercises (reps, sets, or seconds for static holds). The app automatically tracks your personal bests.
- **Nutrition Tracking:** Log meals (breakfast, lunch, dinner, snacks) using a pre-loaded food database. Users can also add custom foods.
- **Daily Summaries:** View progress bars for daily calories, protein, carbs, and fats.
- **Weekly Analytics:** View a 7-day summary of workouts and generate a bar chart of your calorie intake versus your target (requires `matplotlib`).

## Prerequisites
- Python 3.x
- `matplotlib` (Optional, but required for generating weekly calorie charts)
  ```bash
  pip install matplotlib
  ```

## How to Run
1. Ensure the main script `fitness_tracker_final_version.py` is in your project directory.
2. Open your terminal or command prompt.
3. Run the script:
   ```bash
   python fitness_tracker_final_version.py
   ```

## File Structure
The application will automatically generate and read from the following text files in the same directory:
- `users.txt`: Stores user profile data and goals.
- `workouts.txt`: Stores all logged workout sets and dates.
- `meals.txt`: Stores logged food intake and portion sizes.
- `difffoods.txt`: Stores the database of foods and their macronutrient values per 100g.
- `calorie_chart.png`: Generated automatically when viewing the weekly summary (if matplotlib is installed).