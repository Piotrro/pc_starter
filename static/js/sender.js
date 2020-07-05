var counter = 0

$(document).on('click', '#the_button', function(e) {
    var mac = document.getElementById("mac_input").value;
    var passwd = document.getElementById("passwd_input").value;
    document.getElementById("passwd_input").value = "";
    var encrypted = CryptoJS.AES.encrypt(mac, passwd);
    $.ajax({
        type: 'POST',
        url:  "http://localhost:5000/run_pc",
        data: JSON.stringify({"MAC": encrypted.toString()}),
        contentType: "application/json",
        success:function(response){
            counter += 1;
            $('#response_div').html("Magic Packet was sent. ".concat(counter.toString()));
        }
    });
});