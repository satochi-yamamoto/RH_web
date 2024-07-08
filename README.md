# Sistema de Controle de RH

Este é um sistema de controle de RH que inclui funcionalidades para gestão de funcionários, acesso a holerites, banco de horas, férias e controle de ponto para equipes home office através de leitura facial.

## Tecnologias Utilizadas
- Python
- Flask
- MySQL
- HTML/CSS/JavaScript

## Funcionalidades
- Gestão de funcionários
- Acesso a holerites
- Banco de horas
- Controle de férias
- Sistema de ponto com leitura facial

## Configuração e Execução
1. Clone o repositório
2. Configure o banco de dados MySQL e ajuste a URI no arquivo `config.py`
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Execute a aplicação:
    ```bash
    python run.py
    ```

## API Endpoints
- `GET /employees`
- `POST /employees`
- `GET /payroll`
- `POST /payroll`
- `GET /timesheet`
- `POST /timesheet`
- `GET /vacations`
- `POST /vacations`
