Projeto de Detecção de Objetos com Webcam

Descrição

Este projeto é uma aplicação em Python que utiliza a webcam do seu MacBook para detectar e rastrear objetos em tempo real. Utilizamos a biblioteca OpenCV para processamento de vídeo e a tecnologia de detecção de objetos YOLO (You Only Look Once) para identificar objetos específicos capturados pela câmera. Este projeto serve como uma base para aplicações de visão computacional, podendo ser expandido para vários usos, como monitoramento de segurança, análise de fluxo de pessoas, entre outros.

Funcionalidades

Captura de vídeo em tempo real usando a webcam do MacBook.
Detecção de objetos com YOLO, incluindo a capacidade de identificar diferentes categorias de objetos.
Exibição gráfica das detecções com caixas delimitadoras e rótulos.
Tecnologias Utilizadas

Python
OpenCV (Open Source Computer Vision Library)
YOLO (You Only Look Once)
Como Configurar

Pré-requisitos
Python 3.x
OpenCV-Python
YOLOv3 pré-treinado (ou outra versão, dependendo da necessidade)
Instalação
Clone o repositório para o seu ambiente local.
Baixe os arquivos yolov3.weights e yolov3.cfg do YOLOv3 e coloque-os no diretório yolo_cfg.
Baixe o arquivo coco.names e coloque-o também no diretório yolo_cfg.
Instale as dependências necessárias usando o arquivo requirements.txt:
Copy code
pip install -r requirements.txt

Vá para a página inicial do YOLO: YOLO website
Role para baixo até encontrar a seção para YOLOv3.
Lá, você encontrará um link para baixar os pesos do YOLOv3, geralmente com uma descrição como "YOLOv3-416" ou similar.
Clique no link para baixar o arquivo .weights.
Salve o arquivo na pasta yolo_cfg.


Como Usar

Execute o script main.py para iniciar a detecção de objetos em tempo real:

css
Copy code
python src/main.py
Contribuições

Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar este projeto, sinta-se à vontade para criar um pull request ou abrir uma issue.