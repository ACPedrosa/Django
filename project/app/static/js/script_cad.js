document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('cadastro-form').addEventListener('submit', function(event) {
        event.preventDefault();

        // Coletar os dados do formulário
        const primeiroNome = document.getElementById('firstname').value;
        const sobrenome = document.getElementById('lastname').value;
        const email = document.getElementById('email').value;
        const celular = document.getElementById('number').value;
        const cpf = document.getElementById('cpf').value;
        const senha = document.getElementById('password').value;
        const confirmarSenha = document.getElementById('confirmPassword').value;
        const genero = document.querySelector('input[name="gender"]:checked');

        console.log(cpf);
        // Coletar URL de sucesso
        const successUrl = document.body.getAttribute('data-success-url');
        console.log("Redirecionando para:", successUrl);

        // Validações adicionais
        if (!validarCPF(cpf)) {
            alert("CPF inválido!");
            return;
        }

        if (!genero) {
            alert('Por favor, selecione um gênero.');
            return;
        }

        // Verificação da senha (exemplo de validação mais forte)
        if (senha.length !== 12 || !/[A-Za-z]/.test(senha) || !/\d/.test(senha)) {
            alert('A senha deve ter 12 caracteres, incluindo pelo menos uma letra e um número!');
            return;
        }

        // Verifica se as senhas coincidem
        if (senha !== confirmarSenha) {
            alert('As senhas não coincidem!');
            return;
        }

        // Dados a serem enviados
        const data = {
            usuario: {
                nome: `${primeiroNome} ${sobrenome}`,
                email: email,
                telefone: celular,
                cpf: cpf,
                senha: senha,
                sexo: genero.value,  // Valor selecionado do gênero
            }
        };

        // Exibir no console os dados enviados (para debugging)
        console.log('Dados enviados:', JSON.stringify(data));

        // Enviar os dados para o backend
        fetch('/participantes/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('input[name="csrfmiddlewaretoken"]').value,  // CSRF token
            },
            body: JSON.stringify(data),
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => {
                    throw new Error(err.message || 'Erro no cadastro');
                });
            }
            return response.json();
        })
        .then(data => {
            alert('Cadastro realizado com sucesso!');  // Notifica o usuário
            document.getElementById('cadastro-form').reset();  // Limpar o formulário após sucesso
            setTimeout(() => {
                window.location.href = successUrl;  // Redirecionar após 1 segundo
            }, 1000); // Atraso de 1000 milissegundos (1 segundo)
        })
        .catch(error => {
            alert('Erro: ' + error.message);
        });
    });
});

function validarCPF(cpf) {
    // Remover caracteres não numéricos
    cpf = cpf.replace(/\D/g, '');

    // Verificar se o CPF possui 11 dígitos
    if (cpf.length !== 11) {
        return false;
    }

    // Impedir CPFs com números repetidos (ex: 111.111.111-11)
    if (/^(\d)\1{10}$/.test(cpf)) {
        return false;
    }

    // Validar os dois últimos dígitos (dígitos verificadores)
    let soma = 0;
    let resto;

    // Validação do 1º dígito
    for (let i = 0; i < 9; i++) {
        soma += parseInt(cpf.charAt(i)) * (10 - i);
    }
    resto = soma % 11;
    if (resto < 2) {
        resto = 0;
    } else {
        resto = 11 - resto;
    }
    if (parseInt(cpf.charAt(9)) !== resto) {
        return false;
    }

    // Validação do 2º dígito
    soma = 0;
    for (let i = 0; i < 10; i++) {
        soma += parseInt(cpf.charAt(i)) * (11 - i);
    }
    resto = soma % 11;
    if (resto < 2) {
        resto = 0;
    } else {
        resto = 11 - resto;
    }
    if (parseInt(cpf.charAt(10)) !== resto) {
        return false;
    }

    return true;
}
