window.comp.choose = {};
window.comp.choose.answer = {};

window.comp.choose.check = function(comp_id) {
    var component = document.getElementById(comp_id);
    var svg_correct = document.getElementById(`${comp_id}-bg-correct`);
    var svg_wrong = document.getElementById(`${comp_id}-bg-wrong`);

    var answer = window.comp.choose.answer[comp_id];
    var userAnswer = [];

    document.getElementsByName(`${comp_id}-choice`).forEach((element) => {
        if (element.checked) {
            userAnswer.push(element.value);
        }
    });

    if (listeq(answer, userAnswer)) {
        component.style.backgroundColor = "#2ea04326";
        svg_correct.style.display = "block";
        svg_wrong.style.display = "none";
    } else {
        component.style.backgroundColor = "#ff000026";
        svg_correct.style.display = "none";
        svg_wrong.style.display = "block";
    }
}

function listeq(a, b) {
    if (a.length != b.length) {
        return false;
    }

    for (var i = 0; i < a.length; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }

    return true;
}