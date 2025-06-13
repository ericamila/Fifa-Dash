# Etapa 1: Imagem Base com Python 3.13
FROM python:3.13-slim

# Define variáveis de ambiente para o Rust
# Isso garante que o Rust seja instalado em um local conhecido e adicionado ao PATH
ENV RUSTUP_HOME=/usr/local/rustup \
    CARGO_HOME=/usr/local/cargo \
    PATH=/usr/local/cargo/bin:$PATH

# Etapa 2: Instalar dependências do sistema e a Toolchain do Rust
# - build-essential: Compiladores C/C++ essenciais
# - curl: Necessário para baixar o instalador do Rust
# - pkg-config & libssl-dev: Dependências comuns para compilar pacotes Rust
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    pkg-config \
    libssl-dev \
    # Instala o Rust de forma não-interativa
    && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain stable \
    # Limpa o cache do apt para manter a imagem final menor
    && rm -rf /var/lib/apt/lists/*

# Etapa 3: Configurar o diretório da aplicação
WORKDIR /app

# Etapa 4: Instalar as dependências Python
# Copia primeiro apenas o requirements.txt para aproveitar o cache do Docker
COPY requirements.txt ./

# Instala os pacotes. Agora, o pip poderá compilar pacotes baseados em Rust.
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 5: Copiar o código da aplicação
# Copia o restante dos arquivos do seu projeto para o contêiner
COPY . .

# Etapa 6: Comando para iniciar a aplicação Streamlit
# Inclui os parâmetros recomendados para rodar atrás do proxy do Coolify
CMD ["streamlit", "run", "1_🏠_home.py", "--server.headless=true", "--server.port=8501", "--server.enableCORS=false"]