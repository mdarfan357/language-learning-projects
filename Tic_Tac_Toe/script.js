let btnRef = document.querySelectorAll(".button-option");
let popupRef = document.querySelector(".popup");
let popupBackgroundRef = document.getElementsByClassName("popup");
// console.log(popupBackgroundRef.body.style.background)
let bodyBackgroudRef = document.body.style.background = "linear-gradient(0deg, rgba(34,193,195,1) 0%, rgba(10,39,64,1) 100%)";

let newgameBtn = document.getElementById("new-game");
let restartBtn = document.getElementById("restart");
let msgRef = document.getElementById("message");
// winning pattern array
let winningPatten = [
    [0,1,2],
    [0,3,6],
    [2,5,8],
    [6,7,8],
    [3,4,5],
    [1,4,7],
    [0,4,8],
    [2,4,6]
];
let xTurn = true;
let count = 0;

// change colour 

const changeColor = (xTurn) => {
    if (xTurn){
        bodyBackgroudRef = document.body.style.background = "linear-gradient(0deg, rgba(34,193,195,1) 0%, rgba(10,39,64,1) 100%)";
    }else{
        bodyBackgroudRef = document.body.style.background = "linear-gradient(0deg, rgba(195,34,34,1) 21%, rgba(107,23,23,1) 84%)";
    }
}


// disable all buttons
const disableButtons = () => {
    btnRef.forEach((element) => (element.disabled = true));
    // enable popup
    popupRef.classList.remove("hide");
    popupBackgroundRef[0].style.background = document.body.style.background;
};

// Enable all buttons (For New game and Restart)
const enableButtons = () => {
    btnRef.forEach(element => {
        element.innerText = "";
        element.disabled = false;
    });
    popupRef.classList.add("hide");
};

// New Game
newgameBtn.addEventListener("click",() => {
    count = 0;
    enableButtons();
    xTurn = true;
    document.body.style.background = "linear-gradient(0deg, rgba(34,193,195,1) 0%, rgba(10,39,64,1) 100%)";

});
restartBtn.addEventListener("click",() => {
    count = 0;
    enableButtons();
    xTurn = true;
    document.body.style.background = "linear-gradient(0deg, rgba(34,193,195,1) 0%, rgba(10,39,64,1) 100%)";

});

// This function is executed when the player wins

const winner = (letter) => {
    disableButtons();
    if (letter == "X"){
        popupBackgroundRef[0].style.background = "linear-gradient(0deg, rgba(34,193,195,1) 0%, rgba(10,39,64,1) 100%)";
        msgRef.innerHTML = "&#x1F389; <br> X  Wins";
    }else{
        popupBackgroundRef[0].style.background = "linear-gradient(0deg, rgba(195,34,34,1) 21%, rgba(107,23,23,1) 84%)";
        msgRef.innerHTML = "&#x1F389; <br> O  Wins";
    }
};

// Function for draw
const noWinner = () => {
    bodyBackgroudRef = document.body.style.background = "radial-gradient(circle, rgba(251,63,133,1) 0%, rgba(92,76,201,1) 83%, rgba(29,8,221,1) 100%)";
    disableButtons();
    
    msgRef.innerHTML = "&#x1F60E; <br> Its a Draw";
    
};

// Win logic
const winChecker = () => {
    for (let i of winningPatten){
        let[element1,element2,element3]=[
            btnRef[i[0]].innerText,
            btnRef[i[1]].innerText,
            btnRef[i[2]].innerText,
        ];
        // Check if elements are filled
        // 3 empty elements are same and would give win 
        if (element1 != "" && element2 != "" && element3 != ""){
            if (element1 == element2 && element2 == element3 ){
                //  if all 3 buttons have same values then pass the value as winner
                winner(element1);
            }
        }
    }
};

// Display X/0 on click
btnRef.forEach((element) => {
    element.addEventListener("click",() =>{
        if (xTurn){
            xTurn = false;
            element.innerText = "X";
            element.disabled = true;
            bodyBackgroudRef = document.body.style.background = "linear-gradient(0deg, rgba(195,34,34,1) 21%, rgba(107,23,23,1) 84%)";
            
            
        }
        else{
            xTurn = true;
            element.innerText = "O";
            element.disabled = true;
            bodyBackgroudRef = document.body.style.background = "linear-gradient(0deg, rgba(34,193,195,1) 0%, rgba(10,39,64,1) 100%)";
        }

        // Increment count on each click
        count += 1;
        if (count == 9){
            // Its a draw        
            noWinner();
        }
        // Check for win on every click 
        winChecker();
    }); 
});
// Enable Buttons and disable pop up on page load
window.onload = enableButtons;
