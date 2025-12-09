import random
import tornado.ioloop
import tornado.web
import tornado.websocket

# Quản lý các kết nối WebSocket
class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set() # Lưu danh sách các client đang kết nối

    def open(self):
        WebSocketServer.clients.add(self)
        print("WebSocket opened")

    def on_close(self):
        WebSocketServer.clients.remove(self)
        print("WebSocket closed")

    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            try:
                client.write_message(message)
            except:
                pass

# Class chọn từ ngẫu nhiên
class RandomWordSelector:
    def __init__(self, word_list):
        self.word_list = word_list

    def sample(self):
        return random.choice(self.word_list)

def main():
    # Danh sách trái cây để gửi
    word_selector = RandomWordSelector(['apple', 'banana', 'orange', 'grape', 'melon'])
    
    # Cấu hình ứng dụng Web
    app = tornado.web.Application(
        [(r"/websocket/", WebSocketServer)],
        websocket_ping_interval=10,
        websocket_ping_timeout=30
    )
    
    app.listen(8888)
    print("Server is listening on port 8888...")
    
    io_loop = tornado.ioloop.IOLoop.current()
    
    # Tạo callback chạy mỗi 3000ms (3 giây)
    periodic_callback = tornado.ioloop.PeriodicCallback(
        lambda: WebSocketServer.send_message(word_selector.sample()), 
        3000
    )
    periodic_callback.start()
    
    io_loop.start()

if __name__ == "__main__":
    main()