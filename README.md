# Selenium ReCaptcha V2 Solver

Este projeto é uma automação desenvolvida em **Python** utilizando **Selenium WebDriver** para resolver desafios **ReCaptcha V2** de forma programática.

Diferente de automações que tentam simular cliques nas imagens (o que é lento e propenso a falhas), este script utiliza a API do **AntiCaptcha** para obter o token de validação e o injeta diretamente no DOM da página, simulando uma resolução humana legítima.

##  Funcionalidades

- **Extração Dinâmica:** Localiza a `sitekey` do ReCaptcha automaticamente no HTML.
- **Injeção de Token via JS:** Insere a resposta da API diretamente no campo oculto `g-recaptcha-response`.
- **Segurança:** Utiliza variáveis de ambiente (`.env`) para proteger a API Key.
- **Gerenciamento de Driver:** Configuração automática do ChromeDriver via `webdriver-manager` (ou Selenium Manager nativo).

## Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)
- [Selenium WebDriver](https://www.selenium.dev/)
- [AntiCaptcha Official](https://github.com/AdminAnticaptcha/anticaptcha-python)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)

##  Nota de Ética e Responsabilidade

**Este código foi desenvolvido estritamente para fins educacionais e de QA (Quality Assurance).**

O objetivo deste projeto é demonstrar como interagir com elementos ocultos do DOM e testar formulários protegidos em ambientes de desenvolvimento ou demonstração (como o [Google ReCaptcha Demo](https://google.com/recaptcha/api2/demo)). O uso de automação para burlar sistemas de terceiros sem autorização pode violar Termos de Uso e leis vigentes. Utilize com responsabilidade.

##  Configuração e Instalação

### 1. Clone o repositório
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio
```

### 2. Crie um ambiente virtual (Opcional, mas recomendado)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependência
```bash
pip install selenium anticaptchaofficial webdriver-manager python-dotenv
```

### 4. Configure as Variáveis de Ambiente
Crie um arquivo chamado .env na raiz do projeto e adicione sua chave da API do AntiCaptcha:
```bash
API_KEY=sua_chave_aqui_sem_aspas
```
Nota: O arquivo .env já está listado no .gitignore para garantir que sua chave não seja enviada para o repositório público.

## Como Executar
Com as dependências instaladas e o arquivo .env configurado, execute o script principal:
```bash
python apicaptcha.py
```

##O que vai acontecer:
- O navegador Chrome será aberto na página de demonstração do ReCaptcha.
- O script identificará a chave do site.
- tarefa será enviada para o serviço de resolução.
- Ao receber o token, o script preencherá o campo oculto e clicará no botão "Submit".
- Você verá a mensagem de sucesso na tela.

## Contribuição
Sinta-se à vontade para abrir Issues ou enviar Pull Requests para melhorias no código, como suporte a outros tipos de Captcha ou implementação de navegadores Headless.

Desenvolvido por Vitória
