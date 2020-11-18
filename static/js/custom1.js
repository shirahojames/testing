$(document).ready(function(){
/*$(".dateinput").datepicker({changeYear: true,changeMonth: true});*/

  var age= "";
  $(".dateinput").datepicker({
    onSelect: function (value, ui){
      var today = new Date();
      age = today.getFullYear() - ui.selectedYear;
      $("#age").val(age);
      document.getElementById("age").value = age;
    },
    changeYear: true,
    changeMonth: true
});




});
