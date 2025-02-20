from kafka import KafkaProducer
import json
import time

# Configurações
TOPIC_NAMES = ['classe', 'subclasse', 'estruturado']
BOOTSTRAP_SERVERS = 'localhost:9092'
MENSAGENS_POR_TOPICO = 5  # Quantidade de mensagens por tópico

# Inicializa o produtor Kafka
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print(f"🚀 Enviando {MENSAGENS_POR_TOPICO} mensagens para cada tópico: {', '.join(TOPIC_NAMES)}")
print(f"📦 Total esperado de mensagens: {MENSAGENS_POR_TOPICO * len(TOPIC_NAMES)}\n")

# Enviando mensagens para cada tópico
for i in range(MENSAGENS_POR_TOPICO):
    mensagem = {
        "id": f"msg_{i+1}",
        "nome_cliente": f"Cliente {i+1}",
        "valor_investido": 10000.0 + (i * 500),
        "MODULO_TXADM": f"ADM_{i+1:03}",
        "TX_ADM_TIPO_ATIVOS": f"ATIVO_{chr(65 + i)}",
        "TX_ADM_TIPO_ATIVO_PERCENTUAL": round(1.5 + (i * 0.5), 2),
        "CONTROLADOR_ES": "Banco XPTO",
        "CNPJ": "12.345.678/0001-99"
    }

    for topic in TOPIC_NAMES:
        producer.send(topic, mensagem)
        print(f"📤 [{i+1}/{MENSAGENS_POR_TOPICO}] Mensagem enviada para o tópico: {topic}")

    time.sleep(1)  # Simula envio a cada segundo

producer.flush()
producer.close()

print(f"\n✅ Envio de {MENSAGENS_POR_TOPICO * len(TOPIC_NAMES)} mensagens concluído com sucesso!")
