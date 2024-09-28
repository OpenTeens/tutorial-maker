def process(sections, comp_id):
    choices = [(c[6:], c[3] == '*') for c in sections[1].split('\n')]
    answers = [c[0] for c in choices if c[1]]
    choose_type = "radio" if len(answers) == 1 else "checkbox"

    return {
        "question": sections[0],
        "choices": choices,
        "answers": answers,
        "choose_type": choose_type
    }
