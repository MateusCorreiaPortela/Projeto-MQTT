# 📦 Projeto de Integração MQTT + RabbitMQ + MongoDB

Este projeto demonstra a integração entre MQTT, RabbitMQ e MongoDB, simulando um fluxo completo de mensagens entre publicadores e consumidores. A aplicação utiliza Docker Compose para facilitar a orquestração dos serviços.

##🐳 Subindo o Projeto
Para executar a aplicação, utilize o seguinte comando:

`docker compose up --build`

⚠️ Certifique-se de que o arquivo mosquitto.conf está na raiz do projeto. Ele é responsável por permitir a publicação de mensagens anônimas no broker MQTT.

##🔎 Acompanhamento e Visualização
Após subir os containers, acesse os seguintes serviços para acompanhar o fluxo das mensagens:

🐰 RabbitMQ: http://localhost:15673
Interface web para monitorar a chegada de mensagens nas filas.

🍃 Mongo Express: http://localhost:8081
Interface web para visualizar os bancos de dados e suas coleções no MongoDB.

##✉️ Publicando uma Mensagem
Para publicar uma mensagem via terminal, execute o comando abaixo:

```mosquitto_pub -h localhost -p 1884 -t "topico1" -m '{"ID": "123", "data": "2025-04-29", "relogio": 12, "vazao_instantanea": 3.14}'```

A mensagem deve ser um dicionário em formato de string JSON para passar pela validação e ser enviada ao banco de dados.

Você poderá acompanhar:

1-  A chegada da mensagem na fila via interface do RabbitMQ.

2 - A persistência da mensagem no banco "banco", na coleção "mensagens", via Mongo Express.

##⚙️ Configurações Opcionais
Alterar nome do banco de dados ou da coleção
No arquivo consumer_amqp.py:
`db = client["banco"]         # Nome do banco`
`colecao = db["mensagens"]    # Nome da coleção`

Alterar o tópico MQTT
No consumer_mqtt.py:
`client.subscribe('topico1')  # Altere para o tópico desejado`

❗ O tópico que você se inscrever deve ser exatamente o mesmo usado para publicar as mensagens. Caso contrário, o broker não encaminhará a mensagem ao consumidor.

##⚠️ Notas sobre Portas
Caso você não tenha o Mosquitto, RabbitMQ, MongoDB e Mongo Express instalados localmente, sinta-se à vontade para deixar as portas padrão no docker-compose.yml.
Padrão
`- "5672:5672"       # RabbitMQ`
`- "27017:27017"     # MongoDB`

##✅ Tecnologias Utilizadas

    Docker & Docker Compose

    Mosquitto (MQTT)

    RabbitMQ

    MongoDB

    Mongo Express

    Python


