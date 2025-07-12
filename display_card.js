var other_experience = document.getElementById("other_experience");
var card = document.getElementById("card");
var cancel = document.getElementById("cancel_card")
var background = document.getElementById("black_background")



other_experience.addEventListener('click', () => {
        card.style.display="block";
        other_experience.style.color= "blueviolet";
        background.style.display ="block"
})

cancel.addEventListener('click', () => {
        card.style.display="none";
        other_experience.style.color= "grey";
        background.style.display = "none"
})

