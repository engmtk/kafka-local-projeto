Projeto Kafka Local - Produtor e Consumidor
Estava com umas duvidas sobre como atuar num projeto profissional e resolvi colocar a mão na massa gastando umas horas da madrugada fazendo essa brincadeira aqui, mais com o objetivo de aprender e aprofundar mais o conhecimento sobre construção, envio e consumo de informações via tópico Kafka. 

Este projeto demonstra como configurar um ambiente Kafka local para enviar e consumir mensagens de forma simples e eficiente. A aplicação inclui um produtor que envia mensagens para três tópicos (classe, subclasse e estruturado) e um consumidor que lê e processa essas mensagens.

Visão Geral

Este projeto tem como objetivo:
Enviar mensagens Kafka para múltiplos tópicos (classe, subclasse e estruturado).
Consumir as mensagens enviadas e exibir os dados processados.
Monitorar a quantidade de mensagens enviadas, recebidas e a taxa de processamento.

As mensagens contêm dados como ID, nome do cliente, valor investido, tipo de ativo e outras informações relevantes para o cenário de investimento.

Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em seu ambiente local:

1.	Python 3.10+ – Instalar Python
2.	Kafka Local – Apache Kafka
3.	Bibliotecas Python:

pip install kafka-python
Instalação e Configuração

1.	Clone o Repositório:

git clone https://github.com/seu-usuario/kafka-local-projeto.git

cd kafka-local-projeto

2.	Inicie o Kafka Local:
Se estiver usando Kafka instalado localmente:
Suba o Zookeeper e o Kafka

bin/zookeeper-server-start.sh config/zookeeper.properties

bin/kafka-server-start.sh config/server.properties

3.	Crie os tópicos:
bin/kafka-topics.sh --create --topic classe --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
bin/kafka-topics.sh --create --topic subclasse --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
bin/kafka-topics.sh --create --topic estruturado --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

Estrutura do Projeto
kafka-local-projeto/
├── produtor.py      # Envia mensagens para os tópicos
├── consumidor.py    # Lê as mensagens dos tópicos
├── README.md        # Documentação do projeto
└── requirements.txt # Dependências do projeto

Execução
1.	Iniciar o Produtor:
python produtor.py
2.	Iniciar o Consumidor:
python consumidor.py
3.	Monitorar os Tópicos:
bin/kafka-console-consumer.sh --topic classe --bootstrap-server localhost:9092 --from-beginning

Exemplo de Mensagem
O produtor envia mensagens com a seguinte estrutura JSON:
{
  "id": "msg_1",
  "nome_cliente": "Cliente 1",
  "valor_investido": 10000.0,
  "MODULO_TXADM": "ADM_001",
  "TX_ADM_TIPO_ATIVOS": "ATIVO_A",
  "TX_ADM_TIPO_ATIVO_PERCENTUAL": 1.5,
  "CONTROLADOR_ES": "Banco XPTO",
  "CNPJ": "12.345.678/0001-99"
}

 Resultados Esperados
Ao executar o projeto, você verá algo como:
 Enviando 5 mensagens para cada tópico: classe, subclasse, estruturado
 Total esperado de mensagens: 15

 [1/5] Mensagem enviada para o tópico: classe
 [1/5] Mensagem enviada para o tópico: subclasse
 [1/5] Mensagem enviada para o tópico: estruturado
 Consumindo mensagens dos tópicos: classe, subclasse, estruturado...

 Mensagem recebida do tópico: classe
 ID: msg_1
 Nome do Cliente: Cliente 1
 Valor Investido: 10000.0
 Módulo TXADM: ADM_001
 Tipo de Ativos: ATIVO_A
 Percentual do Ativo: 1.5%
 Controlador: Banco XPTO
 CNPJ: 12.345.678/0001-99

Sinta-se à vontade para contribuir com este projeto! Se encontrar problemas ou quiser sugerir melhorias:
1.	Faça um fork do repositório.
2.	Crie um branch para sua feature (git checkout -b feature/nova-feature).
3.	Faça o commit das suas mudanças (git commit -m 'Adiciona nova feature').
4.	Envie um pull request.

Dúvidas? Sugestões? Entre em contato pelo GitHub ou envie um e-mail para o e-mail:
alexandre.zero11@gmail.com
