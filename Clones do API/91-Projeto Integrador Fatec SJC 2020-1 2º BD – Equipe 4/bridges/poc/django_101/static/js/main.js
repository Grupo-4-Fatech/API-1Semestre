$(".toogle-menu").click(function() {
  var largura = $("#sidebar-wrapper").width() + 5;
  // var largura = 185;
  if ($(".menu").is(":hidden")) {
    $(".menu").css("display", "block");
    $(this).css("left", largura + "px");
  } else {
    $(".menu").css("display", "none");
    $(this).css("left", "10px");
  }
});

// $('.nav a[href^="#"], #down-arrow').on('click', function(e) {
// 	e.preventDefault();
// 	var id = $(this).attr('href'),
// 			targetOffset = $(id).offset().top;

// 	$('html, body').animate({
// 		scrollTop: targetOffset - 100
// 	}, 500);
// });
