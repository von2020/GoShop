$(document).ready(function() {

    // JQuery code to be added in here.
    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });

    // modal box
    $(".open").on("click", function(){
        $(".popup, .popup-content").addClass("active");
    });

    $(".close, .popup").on("click", function(){
        $(".popup, .popup-content").removeClass("active");
    });

    $("#hide-button").click(function(){ 
        $("#hide-button").addClass("active"); 
      });

    $("#close-button").click(function(){ 
        $("#hide-button").removeClass("active"); 
    });
    

    // $(".close, #hide-button").click(function(){ 
    //     $("#hide-button").removeClass("active"); 
    //   });

});

const countbtn = document.querySelector('.countbtn button');
let countNum = document.querySelector('.countNum h1');

countbtn.addEventListener('click', countUp);
function countUp(){
    countNum.innerHTML ++;
    }

function addone(){
    var foo = document.getElementById('thisone').innerHTML
    foo++;
    document.getElementById('thisone').innerHTML = foo;
}