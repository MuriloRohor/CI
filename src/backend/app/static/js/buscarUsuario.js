document.addEventListener("DOMContentLoaded", function () {
    let form = document.getElementById("form_search_usuarios");
    if (form) { // Verifica se o form existe
        form.addEventListener("submit", function (e) {
            e.preventDefault();

            // Captura os valores dos campos
            let formData = new FormData(form);
            let filial = formData.get("filial_usuario_modal");
            let nome = formData.get("nome_usuario_modal");

            let filialInt = parseInt(filial, 10);

            console.log("filial: ", filial, "Nome: ", nome);

            let dataToSend = {
                page: 1,
                cod_filial: filialInt,
                nome_usuario: nome,
                
                
            };
            console.log(dataToSend)
            

            axios.post('http://localhost:8000/user/filtrar-por-filial', dataToSend)
                .then(function (response) {
                    console.log(response.data);
                    var list_user = document.getElementById("lista_user_cadastrar");
                    
                    list_user.innerHTML = ""
                    response.data.forEach(user => {
                        let row = 
                        `   
                        <li class="collection-item avatar">
                        <i class="material-icons circle red">person</i>
                        <span class="title">${user.nome}</span>
                        <p>
                            Matricula ${user.cod_matricula} <br>
                            Filial ${user.filial.nome}
                        </p>
                        <a href="#!" class="secondary-content"><i class="material-icons">arrow_forward</i></a>
                        </li>
                        `;

                        list_user.innerHTML += row;
                    
                    });
    
                })
                .catch(error => {
                    if (error.response) {
                      // O servidor respondeu com um status fora do intervalo 2xx
                      console.log("Dados do erro:", error.response.data);
                      console.log("Status do erro:", error.response.status);
                      console.log("Cabeçalhos do erro:", error.response.headers);
                    } else if (error.request) {
                      // A solicitação foi feita, mas não houve resposta
                      console.log("Erro na solicitação:", error.request);
                    } else {
                      // Algo aconteceu na configuração da solicitação que acionou um erro
                      console.log('Erro:', error.message);
                    }
                  });
        });
    }
});
