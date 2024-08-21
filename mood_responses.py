def mood_response(mood):
    responses = {
        "happy": "That's wonderful! Keep smiling!",
        "sad": "I'm sorry to hear that. I hope things get better soon.",
        "excited": "Awesome! It sounds like you have something fun going on.",
        "angry": "Take a deep breath. It's okay to feel this way sometimes.",
        "nervous": "Try to stay calm and take it one step at a time.",
        "tired": "Maybe some rest will help. Take care of yourself."
    }

    return responses.get(mood.lower(), "That's an interesting mood. I hope you have a great day!")