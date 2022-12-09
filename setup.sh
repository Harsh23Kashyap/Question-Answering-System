mkdir -p ~/.streamlit/
echo "[general]
email = \"harsh.kashyap2001@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml