# GeminiApi

O projeto GeminiApi é uma aplicação de backend em Python que utiliza a API Gemini de IA generativa do Google para criar um sistema de chat interativo. Este modelo de linguagem, conhecido por sua capacidade de gerar textos coerentes e contextualmente apropriados, permite aos usuários interagir de maneira fluida e natural.

## Funcionalidades

- **Sessão de Chat Dinâmica**: Os usuários podem iniciar um chat interativo com o modelo Gemini, recebendo respostas em tempo real que simulam uma conversa humana.
- **Formatação em Markdown**: As respostas do modelo são formatadas em Markdown para melhor apresentação em interfaces que suportam esta formatação, como Jupyter Notebooks.
- **Controles de Segurança**: O projeto implementa configurações de segurança personalizáveis para garantir que o conteúdo gerado respeite normas éticas e regulamentações vigentes, prevenindo a geração de conteúdo ofensivo ou inadequado.
- **Ciclo Interativo de Respostas**: A aplicação mantém um ciclo interativo de entrada e resposta, proporcionando uma experiência de chat contínua até que o usuário escolha encerrar a conversa.

## Tecnologias Utilizadas

- **Python**: Utilizado para desenvolver a lógica de backend e gerenciar a interação com a API do Google.
- **API Gemini do Google**: Fornece acesso ao modelo de linguagem avançado para geração de texto e interações de chat.
- **IPython**: Facilita a execução e visualização interativa dentro de ambientes como Jupyter Notebooks.

## Contexto do Modelo Gemini

O modelo Gemini, parte das ofertas de IA generativa do Google, é projetado para aplicações que exigem respostas rápidas e contextuais, ideal para sistemas de chatbots, assistentes virtuais, e outras aplicações que necessitam de compreensão e geração de linguagem natural em nível avançado.

## Agradecimentos

- **Google Cloud**: Pela disponibilização das APIs de IA generativa, que são fundamentais para o funcionamento deste projeto.
- **Comunidade de Desenvolvedores Python**: Pelo suporte contínuo e evolução das ferramentas de desenvolvimento que tornam projetos como este possíveis.

---

### Como Executar

1. **Configuração do Ambiente**:
   - Assegure-se de que Python e IPython estão instalados.
   - Instale as bibliotecas necessárias, incluindo aquelas para integração com a API do Google.
2. **Configuração de API**:
   - Configure a chave de API necessária para autenticar o uso do modelo Gemini do Google.
   - Pegue sua API gratuitamente através do link:
   - Cole sua api no campo indicado dentro do script. Vá para lá: https://github.com/Eng-LeonardoH/GeminiApi/blob/907f4080063da81f0159aff87cc53e4a8ce2386b/main.py#L12
3. **Execução**:
   - Execute o script no IPython ou Jupyter Notebook.
   - Interaja com o sistema de chat enviando perguntas ou comentários e receba respostas do modelo Gemini.

Este projeto exemplifica a aplicação de tecnologias de ponta em IA para criar interfaces de comunicação avançadas e acessíveis.
