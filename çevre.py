import discord
import os
import random
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def çokiyi(ctx):
    await ctx.send(f'evet ben harikayım')
    
@bot.command()
async def harikasın(ctx):
    await ctx.send(f'evet ben harikayım')

@bot.command()
async def harika(ctx):
    await ctx.send(f'harikalar yaratıyorum')

@bot.command()
async def naber(ctx):
    await ctx.send(f'iyi sen')

@bot.command()
async def bendeiyiyim(ctx):
    await ctx.send(f'güzel')

@bot.command()
async def iyimisin(ctx):
    await ctx.send(f'iyi sen')

@bot.command()
async def iyigeçiyor(ctx):
    await ctx.send(f'çok sevindim')

@bot.command()
async def okullarınaçılmasınanekadarkaldı(ctx):
    await ctx.send(f'çok az')

@bot.command()
async def of(ctx):
    await ctx.send(f'evet haklısın')

@bot.command()
async def neyemeyiseversin(ctx):
    await ctx.send(f'ben bir discord botuyum yemek yiyemem')

@bot.command()
async def nasılsın(ctx):
    await ctx.send(f'iyi sen')

@bot.command()
async def neyapmayıseversin(ctx):
    await ctx.send(f'discorddan çıkmayı ve enderman doğramayı')

@bot.command()
async def haklısınendermankesmekeğlenceliamatehlikeli(ctx):
    await ctx.send(f'doğru')

@bot.command()
async def watsappniger(ctx):
    await ctx.send(f'meow meow niger')

@bot.command()
async def yardımedermisin(ctx):
    await ctx.send(f'ne konu da yardımcı olabilirim')

@bot.command()
async def bunusakla105ty(ctx):
    await ctx.send(f'tamam saklıyorum, sakladım')

@bot.command()
async def sakladığınısöyle(ctx):
    await ctx.send(f'105ty')

@bot.command()
async def aptalbot(ctx):
    await ctx.send(f'sensin o')

@bot.command()
async def aptal(ctx):
    await ctx.send(f'sensin o')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'hey, selam, ben bot 1')

@bot.command()
async def selam(ctx):
    await ctx.send(f'selam')

@bot.command()
async def neyapmakistersin(ctx):
    await ctx.send(f'hiçbirb şey')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def çevre(ctx):
    await ctx.send("çevre canlıların yaşadığı doğal ortamdır")


@bot.command()
async def kirlilik(ctx):
    await ctx.send("insanların yere veya doğaya bıraktığı atıklardır")


@bot.command()
async def çevrefest(ctx,):
    await ctx.send("insanların çevreyi temizlemek için kurduğu bir dernektir")


@bot.command()
async def nasılevimdekiçopleriazaltırım(ctx):
    await ctx.send("evindeki çopleri daha az harcayarak azaltabilirsin mesala kullandığın kağıdın arkasınıda kullana bilirsin.")


@bot.command()
async def doğalçevre(ctx):
    await ctx.send("insan eli değmeden, doğanın kendi kendine, yani doğal yollarla meydana getirdiği tüm canlı ve cansız varlıkların bir arada bulunduğu bütünsel ortamdır")


@bot.command()
async def doğa(ctx,):
    await ctx.send("insan eliyle yapılmamış, kendiliğinden var olan ve sürekli değişen canlı ile cansız varlıkların tümüdür")

@bot.command()
async def toprak(ctx,):
    await ctx.send("üstüne çiçek,ağaç ,ev,bina olan yer")

@bot.command()
async def deniz(ctx):
    await ctx.send("bize su balık kum deniz bitkisi ve hava veren büyük su parçası")

@bot.command()
async def canlılar(ctx,):
    await ctx.send("yaşayan hareket eden varlık")


@bot.command()
async def elktronikatıknedir(ctx):
    await ctx.send("doğaya bırakılan atıkların elektronik halidir")

@bot.command()
async def geri_dönüşüm(ctx,):
    await ctx.send("bir şeyi başka bir şeye dödürmek")

@bot.command()
async def atmosver(ctx,):
    await ctx.send("oksijenin olduğu yer")



async def mem(ctx):
    files = os.listdir('images')
    selected = random.choice(files)
    with open(f'images/{selected}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run("")
