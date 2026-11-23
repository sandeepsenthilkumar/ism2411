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
    - The first error I found was in the line total = sale. When I printed the value of total after the loop (or increment in loop) had been completed, the value was 90 rather than 715. I looked through my code carefully and realised that rather than adding to the variable, total was being reassigned. Additionally, when I attempted to run the program I could immediately see there was an issue. There was no colon in the code and so I got an error as soon as the program started.
    - ### Question 2: Discount Function Understanding
    - Takes a price (number) and tier (string) as inputs, and outputs discounted prices. If the tier is gold, the output will be 0.85price. If it is silver, it will be 0.9price. If it is bronze, it will be 0.95price. Otherwise, it will just be the original price. My colleague may be able to use this function by just knowing what to write into ‘tier’ without understanding the code. They just need to know that it should be one of these words, and it will give them a discounted price depending on which one they choose.


   
    - ### Question 3: Debugging Tools & Methodology
    - In explainer mode, I used Claude AI to understand what the index error trace back meant. As no code adjustments were being made, print statements and rubber ducking were used to identify the errors.
