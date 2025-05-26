import threading
import queue
import requests

# Tạo queue chứa proxy
q = queue.Queue()
valid_proxies = []

# Đọc proxy từ file
with open("proxy_list.txt", "r") as f:
    proxies = f.read().splitlines()

    for p in proxies:
        if p.strip():
            q.put(p.strip())

# Hàm kiểm tra proxy
def check_proxies():
    global q
    while not q.empty():
        proxy = q.get()
        try:
            res = requests.get("https://www.facebook.com/", proxies={
                "http": proxy,
                "https": proxy
            }, timeout=5)  # timeout giúp bỏ qua proxy chết nhanh hơn
            if res.status_code == 200:
                print(f"[LIVE] {proxy}")
                valid_proxies.append(proxy)
        except:
            print(f"[DEAD] {proxy}")
        finally:
            q.task_done()  # đánh dấu task đã hoàn thành

# Tạo và khởi chạy thread
num_threads = 10
for _ in range(num_threads):
    t = threading.Thread(target=check_proxies)
    t.daemon = True  # tự dừng khi main thread kết thúc
    t.start()

q.join()  # Đợi đến khi tất cả proxy được kiểm tra xong

# Ghi proxy sống vào file
with open("valid_proxies.txt", "w") as f:
    for p in valid_proxies:
        f.write(p + "\n")

print("\n Hoàn tất kiểm tra proxy.")
