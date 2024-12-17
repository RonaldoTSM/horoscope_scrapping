Web Scraping Horóscopos
Este projeto extrai dados diários de horóscopos de um site e salva em um arquivo CSV. O processo de scraping é automatizado para rodar todos os dias.

Como usar
1. Clonar o repositório
bash
Copy code
git clone https://github.com/seuusuario/horoscope-web-scraping.git
cd horoscope-web-scraping
2. Criar e ativar um ambiente virtual
bash
Copy code
python -m venv venv
Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
3. Instalar as dependências
bash
Copy code
pip install -r requirements.txt
4. Rodar o script
Execute o script para coletar os dados:

bash
Copy code
python scraper.py
Os dados serão salvos em um arquivo horoscope_data.csv.

Automatizando o Scraping
Para rodar o scraping todos os dias automaticamente, use o script scheduler.py.

bash
Copy code
python scheduler.py
Estrutura do Projeto
bash
Copy code
horoscope-web-scraping/
│
├── scraper.py          # Script principal para o scraping
├── scheduler.py        # Script para agendar o scraping
├── requirements.txt    # Dependências
└── README.md           # Este arquivo
