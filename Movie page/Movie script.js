let stars = Array.from(document.querySelectorAll("i"));

stars.forEach((element) => {
    element.addEventlistener("click" , (e) => {
        rate(element);
    });

    element.addEventlistener("mouseover" ,(e) => {
        rate(element);
    });
});

function rate(Element) {
    stars.forEach((el) => {
        el.classList.remove("selected");
    });
    selectedRating = stars.indexOf(Element);
    for (let i = 0; i <= selectedRating; i++) {
        allstars[i].classList.add("selected");
    }
}