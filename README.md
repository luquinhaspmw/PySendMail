# PyMailSend 🚀

**PyMailSend** é uma ferramenta inicial para envio automatizado de e-mails com Python. Com suporte à personalização de mensagens e integração com planilhas Excel, é ideal para quem quer automatizar o envio de e-mails de forma prática.

---

## 🧩 Como funciona?

O **PyMailSend** permite:  
- Enviar e-mails personalizados para múltiplos destinatários com base em dados de uma planilha.  
- Personalizar mensagens com placeholders substituídos dinamicamente (ex.: nome, data, horário).  
- Adicionar imagens incorporadas no corpo do e-mail.  
- Suporte ao formato HTML para mensagens mais atrativas.

---

## ⚙️ Pré-requisitos

1. **Python** (versão 3.8 ou superior).
2. Instale as dependências necessárias com:
   ```bash
   pip install -r requirements.txt 

3. Configure as variáveis de ambiente no arquivo .env:
    ```env
    SMTP_SERVER=smtp.gmail.com
    SMTP_PORT=587
    GMAIL_USER=seuemail@gmail.com
    GMAIL_PASS_APP=senha-do-app
 
 ### <strong>Para usar o Gmail, é necessário configurar uma senha de app na sua conta, use esse video abaixo como guia para criar seu GMAIL_PASS_APP</strong>

 # link do video <a href='https://www.youtube.com/watch?v=vaZ_XV5yvf4'>aqui</a>

---

## 🚀 Como usar

### Configuração inicial
1. Certifique-se de que a planilha contém as colunas:

- <strong>Nome:</strong> Nome dos destinatários.
- <strong>Email:</strong> Endereço de e-mail dos destinatários.

#### Salve a planilha no formato .xlsx e coloque-a no mesmo diretório do script.

2. ## Execução do script

### Inicie o script principal:
``` bash
    python pymailsend.py 
```
Siga as instruções para:
- Digitar o nome da planilha.
- Inserir o assunto do e-mail.
- Confirmar os dados pré-configurados, como data, horário e endereço da empresa.

O script enviará os e-mails para cada destinatário listado na planilha.