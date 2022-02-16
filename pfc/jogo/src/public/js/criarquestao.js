var criarquestao = document.getElementById('criarquestao')

criarquestao.addEventListener('click', validarquestao());

function validarquestao() {
    var tituloquestao = document.getElementById('tituloquestao').value;
    var resposta1 = document.getElementById('resposta1').value;
    var resposta2 = document.getElementById('resposta2').value;
    var resposta3 = document.getElementById('resposta3').value;

    if(tituloquestao == ""){
        document.getElementById('erro-tituloquestao').innerHTML = "Informe o título da questão!"
        return false;
    }else{
        document.getElementById('erro-tituloquestao').innerHTML = "";
    }

    if(resposta1 == ""){
        document.getElementById('erro-resposta1').innerHTML = "Informe a 1º resposta!"
        return false;
    }else{
        document.getElementById('erro-resposta1').innerHTML = "";
    }

    if(resposta2 == ""){
        document.getElementById('erro-resposta2').innerHTML = "Informe a 2º resposta!"
        return false;
    }else{
        document.getElementById('erro-resposta2').innerHTML = "";
    }

    if(resposta3 == ""){
        document.getElementById('erro-resposta3').innerHTML = "Informe a 3º resposta!"
        return false;
    }else{
        document.getElementById('erro-resposta3').innerHTML = "";
    }

}