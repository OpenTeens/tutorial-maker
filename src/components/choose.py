def parse(sections: list[str], component_id) -> None:
    choices = [(value[4:], value[1] == "*") for value in sections[1].split("\n")]
    answers = [option[0] for option in choices if option[1]]

    res = f"""
    <div class='component card choose' id='comp-choose-{component_id}'>
        <div class='choose_header'>
            {sections[0]}
        </div>
        <div class='choose_options'>
            {gen_options(choices, answers, component_id)}
        </div>
        <div class='choose_footer'>
            <button class='submit choose_submit' onclick="comp.choose.check('{component_id}')">Submit</button>
        </div>
        <script>
            window.comp.choose.answer['{component_id}'] = {answers};
        </script>
    </div>
    """.replace(
        "\n    ", "\n"
    )

    return res


def gen_single_choice(choice, choose_id):
    text, is_answer = choice
    return f"""
    <div class='choose_option'>
        <input type='radio' id='comp-choose-{choose_id}-choice-{text}' name='comp-choose-{choose_id}-choice' value='{text}'>
        <label for='comp-choose-{choose_id}-choice-{text}'>{text}</label>
    </div>
    """

def gen_multiple_choice(choice, choose_id):
    text, is_answer = choice
    return f"""
    <div class='choose_option'>
        <input type='checkbox' id='comp-choose-{choose_id}-choice-{text}' name='comp-choose-{choose_id}-choice' value='{text}'>
        <label for='comp-choose-{choose_id}-choice-{text}'>{text}</label>
    </div>
    """


def gen_options(choices, answers, choose_id):
    if len(answers) == 1:
        return "\n".join([gen_single_choice(choice, choose_id) for choice in choices])
    elif len(answers) > 1:
        return "\n".join([gen_multiple_choice(choice, choose_id) for choice in choices])

