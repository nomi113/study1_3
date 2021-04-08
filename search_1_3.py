
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
# csv読み込み



### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    ### ここに検索ロジックを書く
    import csv
    with open('kimetsu.csv','r')as csv_file:
        reader=csv.reader(csv_file)
        for source in reader:
            print(source)

        
    if word in source:
        print("{}が見つかりした".format(word))
        
    else:
        print('存在しません')
        source.append(word)
        
        print(source)

if __name__ == "__main__":
    search()