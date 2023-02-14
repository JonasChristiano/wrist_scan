function openModal(nm) {
  let modal = document.getElementById(nm);
  if (typeof modal === 'undefined' || modal === null)
    return;
  modal.style.display = 'Block'
}

function closeModal(nm) {
  let modal = document.getElementById(nm);
  if (typeof modal === 'undefined' || modal === null)
    return;
  modal.style.display = 'none'
}
// configurar o status do checkbox para ser diferentes e desabilitar a caixa de texto
function checkbox() {
  if ($("#all_ports").is(":checked")) {
    $('#ports').prop('checked', false);
    $("#port_value").attr('disabled', true);
    $("#all_ports").prop('checked', true);
  } else {
    $('#ports').prop('checked', true);
    $("#port_value").attr('disabled', false);
    $("#all_ports").prop('checked', false);
  }
};

$(document).ready(function (){
  checkbox()  
});


function get_ip(ip){
  sessionStorage.setItem("ip", ip)
}

$(document).ready(function(){
  $("#home").after('<li id="network"><a href="/network"><span class="mif-books icon"></span>network</a></li>')
});

$(document).ready(function() {
  closeModal('load')
  $("#submit").click(function () {
    console.log()
    openModal('load')
    if ($("#all_ports").is(":checked")){
      $.post("/port_scann", {"ip": sessionStorage.getItem("ip"), "ports": "all_ports"});
    } else if ($("#ports").is(":checked") && $("#port_value").val() !== "") {
      $.post("/port_scann", {"ip": sessionStorage.getItem("ip"), "ports": $('#port_value').val()})
    } else {
      alert("Error: Select the ports.\nTry again!")
      closeModal('load')
    }
    
  });
});
