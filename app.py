from flask import Flask 
app=Flask(__name__) #_name_ 代表目執行的模組

@app.route("/") #funtion 的裝飾(Decorator):funtion 為基礎提供附加的功能
def home():
    return "Hello Flask "

@app.route("/test") #代表我們要處理的網站路徑
def test():
    return "This is Test"

if __name__=="__main__": #如果以主程式執行
    app.run() #立刻啟動何服器

