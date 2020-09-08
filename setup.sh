# mkdir -p ~/.streamlit/
# echo "\
# [general]\n\
# email = \"divyamkhanna13@gmail.com\"\n\
# " > ~/.streamlit/credentials.toml
# echo "\
# [server]\n\
# headless = true\n\
# enableCORS=false\n\
# port = $PORT\n\

mkdir -p ~/.streamlit/
echo "[general]
email = \"divyamkhanna13@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml