📦 Projeto de Integração MQTT + RabbitMQ + MongoDB

Este projeto demonstra a integração entre MQTT, RabbitMQ e MongoDB, simulando um fluxo de mensagens entre publicadores e consumidores. A aplicação está configurada 


Para a apliacção funcionar é necessário subir o docker compose (comando: docker compose up --build)

Observação: o comando mosquito.conf necessita de estar na raiz do projeto pois é ele que possibilita a entrada de mensagens anonimas no home broker

Ao subir o projeto, pode seguir os seguintes passos para melhor compreensão:
entrar nas seguintes abas na web com as devidas portas: 
localhost:15673 - Visualizador do RabbitMQ - Observar a chegada de mensagens na fila
localhost:8081 - Mongo Express - Vizualiza os bancos de dados e suas respectivas coleções

Vá no terminal e publique uma mensagem, a mensagem tem que ser um dícionário em formato de string, para passar pela validação e conseguir ser enviada para o banco:
mosquitto_pub -h localhost -p 1884 -t "topico1" -m '{"ID": "123", "data": "2025-04-29", "relogio": 12, "vazao_instantanea": 3.14}'

no vizualizador do rabbit vai poder observar a entrada de dados.

depois basta consultar o mongo express e verá o Banco de dados chamado "banco"

entre na coleção "mensagens" para poder ver as mensagens enviadas."

Caso queira trocar o nome do banco ou coleção, basta ir no arquivo consumer_amqp.py:
Alterar nome do banco de dados = altere db = client["banco"] para db = client["nome_do_banco_desejado"]
Alterar nome da coleção = altere colecao = db["mensagens"] para colecao = db["nome_da_colecao_desejada"]

Para alterar o tópico que ira receber as mensagens:
Altere a client.subscribe('topico1') para client.subscribe('topico_desejado')
OBS: O tópico que você inscrever o client DEVE OBRIGATÓRIAMENTE ser o mesmo que você vai enviar a mensagem, caso seja diferente o 
home broker não enviará a mensagem pro client