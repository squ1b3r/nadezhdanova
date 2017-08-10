$(function() {
  $(".carousel").each(function() {
    var _this = this;
    $(this).carousel({
      interval: 0
    });
    $(this).find("img").on("click", function(event) {
      event.preventDefault();
      $(_this).carousel("next");
    });
    $(this).find("img").on("swipeleft", function(event) {
      event.preventDefault();
      $(_this).carousel("next");
    });
    $(this).find("img").on("swiperight", function(event) {
      event.preventDefault();
      $(_this).carousel("prev");
    });
  })
  $("#main-slider").find("figcaption").hover(
    function() {
      $(this).addClass("active");
      $("#main-slider").find(".carousel-control.left").hide();
    },
    function() {
      var _this = this;
      $(this).find(".description").addClass("transition");
      $(this).removeClass("active");
      setTimeout(function () {
        $(_this).find(".description").removeClass("transition");
      }, 100);
      $("#main-slider").find(".carousel-control.left").show();
    }
  );
});
