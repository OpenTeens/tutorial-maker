window.comp.choose = {};
window.comp.choose.answer = {};

window.comp.choose.check = function(id) {
    var comp_id = `comp-choose-${id}`;
    component = document.getElementById(comp_id);

    var answer = window.comp.choose.answer[id];
    var userAnswer = [];

    document.getElementsByName(`${comp_id}-choice`).forEach((element) => {
        if (element.checked) {
            userAnswer.push(element.value);
        }
    });

    if (listeq(answer, userAnswer)) {
        component.style.backgroundColor = "#2ea04326";
    } else {
        component.style.backgroundColor = "#ff000026";
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