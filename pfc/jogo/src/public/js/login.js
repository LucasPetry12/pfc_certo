var login = document.getElementById("login");

login.addEventListener("click", validarlogin());

function validarlogin(){
    var email = document.getElementById('email-login').value;
    var senha = document.getElementById('senha-login').value;

    if(email == "" || email.indexOf('@') == -1){
        document.getElementById('erro-email-login').innerHTML = "Iforme seu e-mail de login!";
        return false;
    }else{
        document.getElementById('erro-email-login').innerHTML = "";
    }

    if(senha == ""){
        document.getElementById('erro-senha-login').innerHTML = "Informe sua senha de login!"
        return false;
    }else{
        document.getElementById('erro-senha-login').innerHTML = "";
    }
}