from services import ws

if __name__ == '__main__':
    #ws.run()
    print("wsgi running")
    ws.run(host='0.0.0.0', port=5000)
