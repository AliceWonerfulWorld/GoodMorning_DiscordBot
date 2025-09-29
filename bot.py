import discord
from discord.ext import commands
import random
import asyncio
from datetime import datetime
import os

# ボットの設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# キャプテンファルコンのランチ占い結果データ
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

# ファルコンランチ占いの種類
falcon_lunch_types = [
    '今日のファルコンランチ',
    'ファルコン恋愛ランチ',
    'ファルコン仕事ランチ',
    'ファルコン金運ランチ',
    'ファルコン健康ランチ',
    'ファルコン学業ランチ',
    'ファルコン朝食',
    'ファルコン夕食',
    'ファルコンおやつ'
]

@bot.event
async def on_ready():
    print(f'{bot.user} がログインしました！')
    print('キャプテンファルコンのランチ占いボットが準備完了です！🦅')
    print('ファルコンのランチで運勢を占いましょう！')

@bot.command(name='ファルコン占い', aliases=['falcon', 'ファルコン', 'ランチ占い'])
async def falcon_lunch_fortune_telling(ctx, lunch_type: str = None):
    """キャプテンファルコンのランチ占い機能"""
    
    # ランチの種類が指定されていない場合はランダムに選択
    if not lunch_type:
        lunch_type = random.choice(falcon_lunch_types)
    
    # ファルコン運勢をランダムに選択（重み付けあり）
    weights = [0.05, 0.15, 0.25, 0.25, 0.20, 0.10]  # ファルコン大吉からファルコン凶の重み
    fortune_result = random.choices(
        list(falcon_lunch_fortune.keys()),
        weights=weights,
        k=1
    )[0]
    
    result = falcon_lunch_fortune[fortune_result]
    
    # 埋め込みメッセージを作成
    embed = discord.Embed(
        title=f"🦅 {lunch_type} 🦅",
        color=discord.Color.blue(),
        timestamp=datetime.now()
    )
    
    embed.add_field(
        name=f"{result['emoji']} {result['title']}",
        value=result['description'],
        inline=False
    )
    
    embed.add_field(
        name="🍽️ 今日のファルコンランチ",
        value=result['lunch_item'],
        inline=False
    )
    
    embed.add_field(
        name="🎨 ラッキーカラー",
        value=result['lucky_color'],
        inline=True
    )
    
    embed.add_field(
        name="🔢 ラッキーナンバー",
        value=str(result['lucky_number']),
        inline=True
    )
    
    embed.add_field(
        name="💡 ファルコンからのアドバイス",
        value=result['advice'],
        inline=False
    )
    
    embed.set_footer(text=f"{ctx.author.display_name} さんのファルコンランチ占い結果")
    
    # 画像ファイルを添付
    image_path = os.path.join('images', result['image'])
    if os.path.exists(image_path):
        file = discord.File(image_path, filename=result['image'])
        embed.set_image(url=f"attachment://{result['image']}")
        await ctx.send(embed=embed, file=file)
    else:
        await ctx.send(embed=embed)

@bot.command(name='ファルコン一覧', aliases=['falcon_list', 'ファルコンいちらん'])
async def falcon_lunch_list(ctx):
    """利用可能なファルコンランチ占いの種類を表示"""
    
    embed = discord.Embed(
        title="🦅 ファルコンランチ占いの種類一覧 🦅",
        color=discord.Color.blue(),
        description="以下の種類のファルコンランチ占いができます！"
    )
    
    for i, lunch_type in enumerate(falcon_lunch_types, 1):
        embed.add_field(
            name=f"{i}. {lunch_type}",
            value=f"`!ファルコン占い {lunch_type}` で占えます",
            inline=False
        )
    
    embed.add_field(
        name="💡 使い方",
        value="`!ファルコン占い` - ランダムなファルコンランチ占い\n`!ファルコン占い ファルコン恋愛ランチ` - 特定のランチを占う",
        inline=False
    )
    
    await ctx.send(embed=embed)

@bot.command(name='ファルコン統計', aliases=['falcon_stats', 'ファルコンとうけい'])
async def falcon_lunch_stats(ctx):
    """今日のファルコンランチ占い統計を表示"""
    
    # 簡単な統計情報（実際の実装ではデータベースを使用）
    embed = discord.Embed(
        title="📊 今日のファルコンランチ占い統計 📊",
        color=discord.Color.green(),
        description="今日のファルコンランチ占い結果の統計です"
    )
    
    embed.add_field(
        name="🦅 ファルコン大吉",
        value="5%",
        inline=True
    )
    embed.add_field(
        name="⚡ ファルコン中吉",
        value="15%",
        inline=True
    )
    embed.add_field(
        name="🍽️ ファルコン小吉",
        value="25%",
        inline=True
    )
    embed.add_field(
        name="🥪 ファルコン吉",
        value="25%",
        inline=True
    )
    embed.add_field(
        name="🌅 ファルコン末吉",
        value="20%",
        inline=True
    )
    embed.add_field(
        name="🌩️ ファルコン凶",
        value="10%",
        inline=True
    )
    
    await ctx.send(embed=embed)

@bot.command(name='ファルコンヘルプ', aliases=['falcon_help', 'ファルコンへるぷ'])
async def falcon_help_command(ctx):
    """ファルコンランチ占いボットのヘルプコマンド"""
    
    embed = discord.Embed(
        title="🦅 キャプテンファルコンランチ占いボット ヘルプ 🦅",
        color=discord.Color.gold(),
        description="このボットの使い方を説明します"
    )
    
    embed.add_field(
        name="🦅 ファルコン占いコマンド",
        value="`!ファルコン占い` - ランダムなファルコンランチ占い\n`!ファルコン占い ファルコン恋愛ランチ` - 特定のランチを占う",
        inline=False
    )
    
    embed.add_field(
        name="📋 その他のコマンド",
        value="`!ファルコン一覧` - ファルコンランチの種類を表示\n`!ファルコン統計` - 統計情報を表示\n`!ファルコンヘルプ` - このヘルプを表示",
        inline=False
    )
    
    embed.add_field(
        name="🍽️ ファルコンランチの種類",
        value="今日のファルコンランチ、ファルコン恋愛ランチ、ファルコン仕事ランチ、ファルコン金運ランチ、ファルコン健康ランチ、ファルコン学業ランチ、ファルコン朝食、ファルコン夕食、ファルコンおやつ",
        inline=False
    )
    
    await ctx.send(embed=embed)

# エラーハンドリング
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ そのコマンドは存在しません。`!ファルコンヘルプ` で利用可能なコマンドを確認してください。🦅")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ 必要な引数が不足しています。`!ファルコンヘルプ` で正しい使い方を確認してください。🦅")
    else:
        await ctx.send(f"❌ エラーが発生しました: {error} 🦅")

if __name__ == "__main__":
    # ボットを起動（トークンは環境変数から取得）
    import os
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        print("❌ DISCORD_BOT_TOKEN 環境変数が設定されていません。")
        print("Discord Developer Portal でボットのトークンを取得し、環境変数に設定してください。")
    else:
        bot.run(token)
