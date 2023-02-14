function btn() {
  ips = $("#ip").val();
  if (ips.length > 6 && ips.length < 16) {
    $.get("scann/" + ips, function (){
      window.location = "/network";
    });
  } else {
    alert("Error: Address wrong!\nTry again.")
  }
}
