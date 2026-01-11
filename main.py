try:
            user_answer = int(user_input)
            if user_answer == correct_answer:
                score += 1
                print(f"Correct! 🎉 Score: {score}")
            else:
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            # This happens if you type letters instead of a number
            print("Please enter a number or type 'exit'!")

if name == "main":
    math_game()