from kafka import KafkaConsumer
import json
import time

# Configurações
TOPIC_NAMES = ['classe', 'subclasse', 'estruturado']
BOOTSTRAP_SERVERS = 'localhost:9092'

# Inicializa o consumidor Kafka
consumer = KafkaConsumer(
    *TOPIC_NAMES,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',  # Lê desde o início do tópico
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=10000  # Fecha após 10 segundos sem novas mensagens
)

print(f"📥 Consumindo mensagens dos tópicos: {', '.join(TOPIC_NAMES)}...\n")

# Contadores
total_recebidas = 0
inicio = time.time()

try:
    for mensagem in consumer:
        total_recebidas += 1
        dados = mensagem.value
        topico = mensagem.topic

        print(f"\n📬 Mensagem recebida do tópico: {topico}")
        print(f"🔑 ID: {dados.get('id', 'N/A')}")
        print(f"👤 Nome do Cliente: {dados.get('nome_cliente', 'N/A')}")
        print(f"💰 Valor Investido: {dados.get('valor_investido', 0.0)}")
        print(f"🏢 Módulo TXADM: {dados.get('MODULO_TXADM', 'N/A')}")
        print(f"📊 Tipo de Ativos: {dados.get('TX_ADM_TIPO_ATIVOS', 'N/A')}")
        print(f"📈 Percentual do Ativo: {dados.get('TX_ADM_TIPO_ATIVO_PERCENTUAL', 0.0)}%")
        print(f"🏦 Controlador: {dados.get('CONTROLADOR_ES', 'N/A')}")
        print(f"🆔 CNPJ: {dados.get('CNPJ', 'N/A')}")
        print(f"🕒 Offset: {mensagem.offset}")

except KeyboardInterrupt:
    print("\n🚪 Interrompido pelo usuário.")

finally:
    consumer.close()
    duracao = time.time() - inicio

    print("\n✅ Processamento concluído!")
    print(f"📊 Total de mensagens recebidas: {total_recebidas}")
    print(f"⏱️ Tempo total de execução: {duracao:.2f} segundos")
    print(f"🚀 Taxa de processamento: {total_recebidas / duracao:.2f} msgs/seg" if total_recebidas > 0 else "Nenhuma mensagem processada.")
