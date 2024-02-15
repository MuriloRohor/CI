document.addEventListener('DOMContentLoaded', function () {
    var mensagem = lerCookie('mensagem');
    if (mensagem && mensagem !== "") {

        let toastHTML = `<span>${mensagem}</span><button class="btn-flat green-text toast-action" id="close-toast"><i class="material-icons">done</i></button>`;
        let toastInstance = M.toast({ html: toastHTML});

        document.getElementById('close-toast').addEventListener('click', function () {
            toastInstance.dismiss(); 
        });
        document.cookie = "mensagem=; Max-Age=-99999999;";
    }
});
function lerCookie(nome) {
    var nameEQ = nome + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) {
            // Decodifica o valor do cookie, que pode incluir caracteres codificados em percentual
            return decodeURIComponent(c.substring(nameEQ.length, c.length).replace(/\"/g, ''));
        }
    }
    return null;
}
