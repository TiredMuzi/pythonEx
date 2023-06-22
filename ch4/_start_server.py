import server

app = server.create_app()
app.run(debug=True, host='0.0.0.0', port=7777)

# 아래의 내용은 플라스크 서버의 상태를 보여주는 내용임 ...
# WARNING: This is a development server. Do not use it in a production deployment.
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.