# ism2411

ISM2411 — Python for Business

## Student
Sandeep Senthilkumar

## Course Information
- **Course**: ISM2411 (Python for Business)
- - **Semester**: Fall 2026
 
  - ## Repository Structure
  - This repository contains coursework for ISM2411, organized by module:
 
  - - `week07/` - Module 7: Functions, exercises, and self-assessment
   
    - ## Module 7 Reflection & Self-Assessment
   
    - ### Question 1: Bug Identification
    - I located the first bug – `total = sale` – from the print statement. I printed the result of what total was after the loop (or after being incremented inside it) and I received 90, not 715, which told me something wasn't right. Then I spent some time looking at the code and found that I was replacing total, instead of appending to it. I could see at once that something was wrong when I was trying to use the program as it didn't contain a colon and gave me an error on start up.
   
    - ### Question 2: Discount Function Understanding
    - When applying a discount, the input is an object called price (a number such as 200), and another called tier (a string such as "gold", "silver", "bronze" or "none"). The function prints the discounted price. If tier is "gold" it returns 85% of the price. It will return 90% if it is "silver". If it is "bronze", it will return 95%. It will return the full price if it's something else. One of my colleagues might be able to use it without bothering to read the code, only be told they should be using those tier names and it will return a price discounted by that tier.
   
    - ### Question 3: Debugging Tools & Methodology
    - Claude AI was used in Explainer mode to learn what the IndexError traceback indicates. I was not calling for any code changes. Print statements and rubber ducking were used to find the bugs.
