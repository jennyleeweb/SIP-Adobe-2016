window.onload = function() {
    alert('Welcome to my site (:');
}


// $(".homepic").fadeIn("slow", "swing");
// $(".homepic").fadeOut("slow", "swing");
// $(".homepic").fadeToggle("slow");

$('.homepic').click(function(){
    $("#homepic1").fadeIn();
    $("#homepic2").fadeIn("slow");
    $("#homepic3").fadeIn(3000);
});