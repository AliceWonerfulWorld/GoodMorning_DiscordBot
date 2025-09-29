#!/usr/bin/env python3
"""
キャプテンファルコンランチ占い機能のテストスクリプト
実際のDiscordボットを起動せずにファルコンランチ占い機能をテストできます
"""

import random
from datetime import datetime

# キャプテンファルコンのランチ占い結果データ（bot.pyからコピー）
falcon_lunch_fortune = {
    'ファルコン大吉': {
        'emoji': '🦅',
        'title': 'ファルコン大吉！',
        'description': 'キャプテンファルコンのランチが最高に美味しい日です！',
        'lunch_item': 'ファルコン特製ランチ',
        'lucky_color': 'ファルコンカラー（青と白）',
        'lucky_number': random.randint(1, 100),
        'advice': '今日はファルコンのように高く飛び、新しい挑戦をしてみてください！',
        'image': 'falcon-lunch.jpg'
    },
    'ファルコン中吉': {
        'emoji': '⚡',
        'title': 'ファルコン中吉！',
        'description': 'ファルコンのランチが美味しく、パワーがみなぎる日です！',
        'lunch_item': 'ファルコン風サンドイッチ',
        'lucky_color': '雷の色（黄色）',
        'lucky_number': random.randint(1, 100),
        'advice': 'ファルコンのように素早く行動し、目標に向かって突き進んでください！',
        'image': 'falcon-lunch.jpg'
    },
    'ファルコン小吉': {
        'emoji': '🍽️',
        'title': 'ファルコン小吉！',
        'description': 'ファルコンのランチが美味しく、少しずつ運が向いてきます！',
        'lunch_item': 'ファルコン風サラダ',
        'lucky_color': '緑色（健康の色）',
        'lucky_number': random.randint(1, 100),
        'advice': 'ファルコンのように着実に前進し、健康に気をつけてください！',
        'image': 'falcon-lunch.jpg'
    },
    'ファルコン吉': {
        'emoji': '🥪',
        'title': 'ファルコン吉！',
        'description': 'ファルコンのランチが美味しく、安定した一日になりそうです！',
        'lunch_item': 'ファルコン風パン',
        'lucky_color': '茶色（安定の色）',
        'lucky_number': random.randint(1, 100),
        'advice': 'ファルコンのように安定して飛び、今の状況を大切にしてください！',
        'image': 'falcon-lunch.jpg'
    },
    'ファルコン末吉': {
        'emoji': '🌅',
        'title': 'ファルコン末吉！',
        'description': 'ファルコンのランチは控えめですが、後で良いことがあります！',
        'lunch_item': 'ファルコン風軽食',
        'lucky_color': 'オレンジ色（希望の色）',
        'lucky_number': random.randint(1, 100),
        'advice': 'ファルコンのように忍耐強く待ち、朝日のように希望を持ってください！',
        'image': 'falcon-lunch.jpg'
    },
    'ファルコン凶': {
        'emoji': '🌩️',
        'title': 'ファルコン凶！',
        'description': 'ファルコンのランチが少し物足りない日ですが、明日は良い日です！',
        'lunch_item': 'ファルコン風スープ',
        'lucky_color': 'グレー色（慎重の色）',
        'lucky_number': random.randint(1, 100),
        'advice': 'ファルコンのように慎重に行動し、嵐が過ぎるのを待ってください！',
        'image': 'falcon-lunch.jpg'
    }
}

def test_falcon_fortune():
    """ファルコンランチ占い機能をテストする"""
    print("🦅 ファルコンランチ占い機能テスト 🦅")
    print("=" * 50)
    
    # 10回ファルコン占いを実行して結果を確認
    results = {}
    for i in range(10):
        # ファルコン運勢をランダムに選択（重み付けあり）
        weights = [0.05, 0.15, 0.25, 0.25, 0.20, 0.10]  # ファルコン大吉からファルコン凶の重み
        fortune_result = random.choices(
            list(falcon_lunch_fortune.keys()),
            weights=weights,
            k=1
        )[0]
        
        if fortune_result in results:
            results[fortune_result] += 1
        else:
            results[fortune_result] = 1
        
        result = falcon_lunch_fortune[fortune_result]
        print(f"{i+1:2d}. {result['emoji']} {result['title']}: {result['description']}")
        print(f"    ランチ: {result['lunch_item']}")
    
    print("\n📊 ファルコンランチ占い結果統計:")
    for fortune, count in results.items():
        percentage = (count / 10) * 100
        print(f"  {fortune}: {count}回 ({percentage:.1f}%)")
    
    print("\n✅ ファルコンランチ占い機能のテストが完了しました！")

def test_specific_falcon_fortune():
    """特定のファルコンランチ占いをテストする"""
    print("\n🎯 特定のファルコンランチ占いテスト")
    print("=" * 40)
    
    falcon_lunch_types = ['今日のファルコンランチ', 'ファルコン恋愛ランチ', 'ファルコン仕事ランチ', 'ファルコン金運ランチ', 'ファルコン健康ランチ', 'ファルコン学業ランチ']
    
    for lunch_type in falcon_lunch_types:
        # ファルコン運勢をランダムに選択
        fortune_result = random.choice(list(falcon_lunch_fortune.keys()))
        result = falcon_lunch_fortune[fortune_result]
        
        print(f"\n🦅 {lunch_type}")
        print(f"結果: {result['emoji']} {result['title']}")
        print(f"説明: {result['description']}")
        print(f"ランチ: {result['lunch_item']}")
        print(f"ラッキーカラー: {result['lucky_color']}")
        print(f"ラッキーナンバー: {result['lucky_number']}")
        print(f"アドバイス: {result['advice']}")

if __name__ == "__main__":
    test_falcon_fortune()
    test_specific_falcon_fortune()
    print("\n🎉 すべてのファルコンランチ占いテストが完了しました！")
