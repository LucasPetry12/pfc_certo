var cadastro = document.getElementById("cadastro");

cadastro.addEventListener("click", validarcadastro);

function validarcadastro(){
    var nome = document.getElementById('nome').value;
    var email = document.getElementById('email').value;
    var senha = document.getElementById('senha').value;
    var confirmasenha = document.getElementById('confirmasenha').value;

    if(nome == ""){ 
        document.getElementById('erro-nome').innerHTML = "Informe seu nome completo!"
        return false;
    }else{
        document.getElementById('erro-nome').innerHTML = "";
    }

    if(email == "" || email.indexOf('@') == -1){
        document.getElementById('erro-email').innerHTML = "Informe seu e-mail!"
        return false;
    }else{
        document.getElementById('erro-email').innerHTML = "";
    }

    if(senha == ""){
        document.getElementById('erro-senha').innerHTML = "Informe sua senha!"
        return false;
    }else{
        document.getElementById('erro-senha').innerHTML = "";
        if(confirmasenha == ""){
            document.getElementById('erro-confirma-senha').innerHTML = "Informe sua senha para confirmar!";
            return false;
        }else{
            document.getElementById('erro-confirma-senha').innerHTML = "";
            if(senha != confirmasenha){
                document.getElementById('senhas-diferentes').removeAttribute('hidden');
            }else{
                document.getElementById('senhas-diferentes').setAttribute('hidden', 'true');
            }
        }
    }

    if(senha.length <= 5){
        document.getElementById('erro-senha').innerHTML = "Informe uma senha forte!"
        return false;
    }
}
