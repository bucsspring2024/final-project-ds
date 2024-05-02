[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14588688&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Cookie Clicker
## CS110 Final Project  Spring Semester, 2024

## Team Members

Andrew Li

***

## Project Description

I will be creating a cookie clicker game with 3 upgrades: autoclicker, better clicks, and better chance for super cookies. The goal is to reach 1,000,000 Jojobills.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start screen
2. Goal screen
3. Various cookies
4. Shop
5. End screen

### Classes

- Sprite
  - This class will create various sprites for my Controller class to use.
- Controller
  - This will handle the code of the entire game.

## ATP

<!-- | Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      | -->

# Test #1
- Step 1: Start Game
    - Go to main.py, then open terminal to type:
      ```py
        python3 main.py
    - Click the Start button
- **Expected Outcome**
  - The starting screen disappears
  - The goal screen appears for 3 seconds
  - The main game screen appears
  - Jojobill counter starts at 0

# Test #2
- Step 2: Description Box
    - Hover cursor over any of the 3 shop upgrades and move off each sprite
- **Expected Outcome**
  - The description box should appear for each upgrade
  - Description box disappears if cursor leaves the upgrade sprite

# Test #3
- Step 3: Click
    - Click on the realistic chocolate chip cookie on the left
- **Expected Outcome**
  - The Jojobill increases by 1 (clicking power)
  - There is a 10% chance to make the sugar cookie appear on the left half of the screen
- Step 4:
  - Keep on clicking the realistic cookie until a sugar cookie appears
- **Expected Outcome**
  - Jojobill increases by 100 times the clicking power
  - Sugar cookie moves off screen ("disappears")

# Test #4
- Step 5: Autoclicker Upgrade
  - Click on autoclicker upgrade when Jojobills are greater than or equal to the purchase price (first sprite)
- **Expected Outcomes**
  - Jojobill decreases by the purchase price
  - Jojobill increases by 1 per second (initially)
    - Next purchase multiplies that rate by 5
- Step 6: Click Upgrade
  - Click on click upgrade when Jojobills are greater than or equal to the purchase price (second sprite)
- **Expected Outcomes**
  - Jojobill decreases by the purchase price 
  - Click power multiplies by 5
- Step 7: Sugar Cookie Upgrade
  - Click on sugar cookie upgrade when Jojobills are greater than or equal to the purchase price (third sprite)
- **Expected Outcomes**
  - Jojobill decreases by the purchase price 
  - Cookies appear more frequently

# Test #5
- Step 6:
  - Repeat Steps 3-7 in any order until Jojobill counter reaches 1,000,000
- **Expected Outcome**
    - The end screen appears

