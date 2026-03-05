# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

Name: Rayed Jawad

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

    The visual UI and look of the game looked good without any bugs but once you started playing, thats when you would immediately notice the many bugs in the program. The game would say a number is higher when in reality the number was lower and vice versa. The "New Game" button also doesnt work it only works to restart if you refresh the entire page which is inefficient. The difficulties of the game is also bugged as the hardest difficulty is guessing numbers from 1 - 50 while the normal difficulty is guessing numbers from 1 - 100 which doesnt make any sense in terms of difficulty. Normal also has 7 attempts while easy difficulty only has 5.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  I utilized Anthropic's Claude Code for this project. AI helped me correctly identify the type switching bug in check_guess. This was where when even-numbered attempts converted the secret number to a string before comparison. I correctly verified this by reading the original code and confirming in lines 158-161. Then I played the game manually to fully confirm if the hints were functional and factual.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

  I play tested the game thoroughly with a specific bug in mine and tested specifically that feature multiple times to make sure they are working properly with various different kinds of attempts. I ran the test after refactoring logic_utils.py and all three of those tests failed. The AI helped me by suggesting writing three new tests that sprcifically targetted the difficulty range bug. It showed me how to write a test that locks in a specific fixed value so the same bug can never silently come back. 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

  Basically the secret number kept changing because everytime you clicked the submit button, the streamlit reran the enmtire python script all over again from top to bottom. The code "random.randint()" was outside of any session state check which is why it generated a brand new number on every rerun. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  One habit I will continue to reuse is to always run the existing tests before and after making changes. The test caught the broken starter tests immediately and saved me from committing code that looked fine but was actually wrong. But next time, I definetly would run and be sure to verify every AI generated test right away instead of assuming that they work. Since this project had styarter tests with a bug in them from the start. I used to think the correctness of AI generated code was easy to spot. This project showed to me that bugs can be very subtle and even hidden in logic that looks completely normal at a first glance. So I will always test AI code before fully trusting it. 