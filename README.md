Projeto Kafka Local - Produtor e Consumidor
Estava com umas duvidas sobre como atuar num projeto profissional e resolvi colocar a mão na massa gastando umas horas da madrugada fazendo essa brincadeira aqui, mais com o objetivo de aprender me familiarizar e aprofundar mais o conhecimento sobre como proceder para a construção e atendimento da demanda, que consistia em envio e consumo de informações via tópico Kafka. 

O projeto demonstra como configurar um ambiente Kafka local para enviar e consumir mensagens de forma simples e eficiente. A aplicação inclui um produtor que envia mensagens para três tópicos (classe, subclasse e estruturado) e um consumidor que lê e processa essas mensagens.

Visão Geral

Este projeto tem como objetivo:
Enviar mensagens Kafka para múltiplos tópicos (classe, subclasse e estruturado).
Consumir as mensagens enviadas e exibir os dados processados.
Monitorar a quantidade de mensagens enviadas, recebidas e a taxa de processamento.

As mensagens contêm dados como ID, nome do cliente, valor investido, tipo de ativo e outras informações relevantes para o cenário de investimento.

Pré-requisitos

Antes de iniciar, certifique-se de ter instalado em seu ambiente local:

✅ Pré-requisitos

✅ Java JDK 8+ instalado e configurado no PATH

✅ Kafka (ex: kafka_2.12-3.1.1) baixado e extraído em uma pasta local

✅ Python 3.10 ou superior

✅ Pip + kafka-python ou confluent-kafka instalado

pip install kafka-python
Instalação e Configuração

1.	Clone o Repositório:

git clone https://github.com/seu-usuario/kafka-local-projeto.git

cd kafka-local-projeto

2.	Inicie o Kafka Local:
Se estiver usando Kafka instalado localmente:
Suba o Zookeeper primeiro e depois o Kafka

bin/zookeeper-server-start.sh config/zookeeper.properties
![{0F8EF3B9-43E1-4F78-8221-031EE1EF355B}](https://github.com/user-attachments/assets/bbae71ad-67dc-4aac-834b-278152da174a)

Zookeeper no ar:
![{009B8CF5-9B7D-4594-B8A9-C0130AF9FC3E}](https://github.com/user-attachments/assets/7200e06f-1cc2-44f3-a7c3-8ddde2ac2f83)

Agora o Kafka local:
![{435B4199-67AD-489B-8168-E6D56D483B46}](https://github.com/user-attachments/assets/60794b73-a374-4207-bdee-bf9a357768be)

bin/kafka-server-start.sh config/server.properties

Kafka no ar:
![{77017270-3F5C-47C8-91AF-86C70F9E2C86}](https://github.com/user-attachments/assets/4fcad5b4-8d3e-467f-97bd-abfa0436b89d)


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
![{1CF60948-0AC2-413A-9EE1-FE58A86BC98B}](https://github.com/user-attachments/assets/c9d6b693-d487-4193-93de-4cc924ed1c9f)

3.	Iniciar o Consumidor:
python consumidor.py

![{4C284AFE-A49D-4D1C-B801-ED7EE9CC9429}](https://github.com/user-attachments/assets/f479ffba-2db8-4d6b-b9a5-0319b86c41e8)

4.	Monitorar os Tópicos:
bin/kafka-console-consumer.sh --topic classe --bootstrap-server localhost:9092 --from-beginning

![{20117176-3BE7-47A8-B6E0-EAF9C1EAA25A}](https://github.com/user-attachments/assets/a974f666-264a-499b-a846-d16537914b6d)


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
