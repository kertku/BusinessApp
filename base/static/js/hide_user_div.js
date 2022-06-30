 function hide_business_user(radio_button) {
   if (radio_button.checked) {
     document.getElementById("business_user_form").style.visibility = "hidden";
     document.getElementById("user_form").style.visibility = "visible";
   }
 }

 function hide_user(radio_button) {
   if (radio_button.checked) {
     document.getElementById("user_form").style.visibility = "hidden";
     document.getElementById("business_user_form").style.visibility = "visible";
   }
 }