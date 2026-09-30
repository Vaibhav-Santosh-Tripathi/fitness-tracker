# Problem Statement: Calisthenics and Macro Tracker

## Context
Many individuals struggle to maintain consistency in their fitness journeys because tracking diet and exercise often requires juggling multiple complex, subscription-based mobile applications. Furthermore, existing fitness trackers often prioritize weightlifting and cardio, lacking tailored tracking for calisthenics and bodyweight exercises (like static holds measured in seconds rather than reps). 

## Objective
The objective of this project is to develop a lightweight, unified Command Line Interface (CLI) application in Python that seamlessly integrates both bodyweight workout tracking and nutritional (macronutrient) logging. 

## Scope & Requirements
The proposed system, "Calisthenics and Macro Tracker," must fulfill the following criteria:
1. **User Personalization:** The system must capture biometric data (age, gender, height, weight) and fitness goals to automatically calculate scientifically sound BMR and daily macro targets.
2. **Exercise Tracking:** Allow users to log calisthenics specific exercises, tracking sets, reps, and hold times, while automatically calculating personal bests.
3. **Dietary Logging:** Provide a customizable food database where users can log meals by weight (grams) and automatically calculate the resulting caloric and macronutrient values.
4. **Data Persistence:** The application must save all user data, logs, and food databases locally without requiring a complex database server setup (using standard text files).
5. **Progress Visualization:** The system should provide easily readable feedback, including text-based progress bars for daily goals and graphical charts for weekly caloric adherence.