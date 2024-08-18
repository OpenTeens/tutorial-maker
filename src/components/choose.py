def parse(sections: list[str]) -> None:
    choices = [
        (value[4:], value[1] == '*') for value in sections[1].split("\n")
    ]
    answers = [option[0] for option in choices if option[1]]

    choose_class = ""
    if len(answers) > 1:
        choose_class = "choose_multiple"
    else:
        choose_class = "choose_single"

    res = f"""
    <div class='component card choose {choose_class}'>
        <div class='choose_header'>
            {sections[0]}
        </div>
        <div class='choose_options'>
            {"".join([f"<div class='choose_option' data-is-answer='{int(option[1])}'>{option[0]}</div>" for option in choices])}
        </div>
    </div>
    """.replace("\n    ", "\n")

    return res
