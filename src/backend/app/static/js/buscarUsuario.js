document.getElementById('ci_filial').addEventListener('change', function() {
    var filialId = this.value;
    var colaboradoresSelect = document.getElementById('ci_colaborador');

    // Limpar colaboradores anteriores
    colaboradoresSelect.innerHTML = '<option value="">Selecione um Colaborador</option>';

    // Desabilitar o select enquanto a requisição está sendo feita
    colaboradoresSelect.disabled = true;

    if (filialId) {
        // Fazer uma chamada AJAX para buscar os colaboradores da filial selecionada
        fetch('/caminho/para/servidor?filialId=' + filialId)
            .then(response => response.json())
            .then(data => {
                // Atualizar o select de colaboradores com os novos dados
                data.colaboradores.forEach(function(colaborador) {
                    var option = new Option(colaborador.nome, colaborador.id);
                    colaboradoresSelect.add(option);
                });
                // Habilitar o select após atualizar os dados
                colaboradoresSelect.disabled = false;
            })
            .catch(error => {
                console.error('Erro ao buscar colaboradores:', error);
            });
    }
});
