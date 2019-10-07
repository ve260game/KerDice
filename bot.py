import discord
from discord.ext import commands
import json
import random

with open('KerDice\setting.json', mode='r', encoding='UTF-8') as jfile: 
    jdata = json.load(jfile) #jdata等於setting文件

bot = commands.Bot(command_prefix= '/rk ') 

roll_WildMagicSurge = ['在接下來的一分鐘內，你每個行動輪開始時，重投此檢定。在後續的檢定中無視本結果。','在接下來的一分鐘內，只要有視覺線，你就可以看到隱形生物。','一隻魔冢（ＤＭ指定並控制）出現在你身邊５尺內一個未被佔據的方格，１分鐘後消失。','你施展第三環效果的火球術  (以你自己為爆心)','你施展第五環效果的魔法飛彈。','投一個ｄ１０，這是你身高改變的英寸數。奇數變矮，偶數長高。','你以自己為中心施展困惑術。','	下一分鐘內，每當你的行動輪開始，你回復５點ＨＰ。','你的臉上長出大把的羽毛。一旦你打了噴嚏，這些羽毛會從你的臉上炸開。','你以自己為中心施展油膩術。','你在下一分鐘內施展的第一個需要豁免檢定的法術，其目標生物的豁免獲得劣勢。','你的皮膚變成藍色。移除詛咒法術可結束此效果。','你的前額長出第三只眼，存在１分鐘。下一分鐘內你所有基於視覺的感知（察覺）檢定獲得優勢。','下一分鐘內，你可用一個附贈動作施展任何施法時間為１動作的法術。','指定一個距你６０尺內，未被佔據且你可以看到的格子，你傳送到那裡。','你被傳送到星界，並在你的下一個行動輪結束時返回原位。如果那個格子被佔據，你出現在最近的未被佔據的格子內。','你在下一分鐘內施展的下一個傷害法術所有傷害骰取滿。','投一個ｄ１０，這是你年齡改變的年份數。奇數變年輕，偶數變衰老。',
'１ｄ６只ＤＭ控制的飛天意面怪（Flumph）出現在你６０尺內未被佔據的格子，並因你而陷入恐慌。它們將在１分鐘後消失。','你回復２ｄ１０點ＨＰ。','你變成一棵盆栽，直至你的下個行動輪開始。在盆栽狀態下，你處於乏力，並對所有傷害易傷。如果你的ＨＰ下降至０，你的花盆被打碎，你恢復原形。','接下來一分鐘內，在你的行動輪中，你可以用一個附贈動作傳送２０尺。','	你對自己施展浮空術。','	一只ＤＭ控制的獨角獸出現在你身邊５尺以內，並在１分鐘後消失。','	在１分鐘內你無法說話。你一張嘴就會吐出粉色的泡泡。','	一面靈能盾牌掩護著你，為你提供＋２ＡＣ加值，並使你免疫魔法飛彈，持續１分鐘。','在接下來５ｄ６天內，你免疫醉酒。','你的頭發掉光，２４小時後恢復。','	在接下來１分鐘內，你接觸的任何沒有被人穿戴或攜帶的可燃物都會被點燃。','你回復你已用法術位中環數最低的那些。','	在１分鐘內，你說話時只能喊叫。','你以自身為中心施展隱霧術。','你指定最多３個距離你３０尺內的生物，使之承受４ｄ１０電擊傷害。','	你因最近的生物而恐慌，直至你的下一個行動輪結束。','你身邊３０尺內所有生物在下一分鐘內隱形。一旦施法或攻擊則隱形結束。','	下一分鐘內你對所有傷害獲得抗力。','距離你６０尺內的一個隨機生物中毒１ｄ４小時。','	你發出３０尺輻射的亮光。結束其行動輪時距離你５尺內的生物目盲，直至其下一個行動輪結束。','你對自己施展變形術。如果豁免失敗，你被變成綿羊。'
,'下一分鐘內，你身邊１０尺范圍不斷出現虛幻的蝴蝶和花瓣。','你立刻獲得一個動作。','距離你３０尺內的所有生物承受１ｄ１０暗蝕傷害。你回復ＨＰ，數值等於傷害值的總和。','你施展鏡影術。','你對６０尺內隨機生物施展飛行術。','你在下一分鐘內隱形，且其他生物無法聽到你。一旦施法或攻擊則隱形結束。','如果你在下一分鐘內死亡，你立刻復活，如同被施展轉生術。','在下一分鐘內你的體型暫時變大一級。','	下一分鐘內，你和你身邊３０尺內所有生物獲得穿刺易傷。','	下一分鐘內，你被虛無縹緲的音樂環繞。','你回復全部術法點。']
roll_uncommon = ['搜魔魔杖 [Wand of Magic Detection]','探秘魔杖 [Wand of Secrets]','蛛網魔杖 [Wand of Web]','魔法飛彈魔杖 [Wand of Magic Missiles]','戰法師魔杖 Wand of The War Mage+1','蝰蛇法杖 [Staff of The Adder]','巨蟒法杖 [Staff of The Python]','魅惑法杖 [Staff of Charming]','叢林法杖 [Staff of The Woodlands]','治癒法杖 [Staff of Healing]','蟲群法杖 [Staff of Swarming Insects]','雕零法杖 [Staff of Withering]','火焰法杖 [Staff of Fire]','威力法杖 [Staff of Power]','冰霜法杖 [Staff of Frost]','強襲法杖 [Staff of Striking]','雷霆法杖 [Staff of Thunder And Lightning]','不動權杖 [Immovable Rod]']
roll_rare = ['定身魔杖 [Wand of Binding]','火球魔杖 [Wand of Fireballs]','閃電束魔杖 [Wand of Lightning Bolts]','驚異魔杖 [Wand of Wonder]','搜敵魔杖 [Wand of Enemy Detection]','恐懼魔杖 [Wand of Fear]','麻痹魔杖 [Wand of Paralysis]','支配權杖 [Rod of Rulership]','觸手權杖 [Tentacle Rod]']
roll_veryrare = ['變形魔杖 [Wand of Polymorph]','吸收權杖 [Rod of Absorption]','警示權杖 [Rod of Alertness]','庇護權杖 [Rod of Security]']
roll_legend = ['賢者法杖 [Staff of The Magi]','王者權杖 [Rod of Lordly Might]','復活權杖 [Rod of Resurrection]']



@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.event
async def on_member_join(member):
    channel =bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(menber):
    channel =bot.get_channel(int(jdata['Welcome_channel']))
    await channel.send(f'{member} leave!')

@bot.command()
async def command(ctx):
    await ctx.send('/rk WMS 骰狂野魔法浪潮 Wild Magic Surge\n/rk uncommon 從對應稀有度(uncommon、rare、veryrare、legend)魔杖、法杖、權杖骰一把')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)} ms')


@bot.command()
async def Hi(ctx):
      await ctx.send('hello')


@bot.command()
async def uncommon(ctx):
    randice = random.randint(0,len(roll_uncommon)-1)
    await ctx.send(f'{roll_uncommon[randice]} ')    

@bot.command()
async def rare(ctx):
    randice = random.randint(0,len(roll_rare)-1)
    await ctx.send(f'{roll_rare[randice]} ')    
    
@bot.command()
async def veryrare(ctx):
    randice = random.randint(0,len(roll_veryrare)-1)
    await ctx.send(f'{roll_veryrare[randice]} ')    

@bot.command()
async def legend(ctx):
    randice = random.randint(0,len(roll_legend)-1)
    await ctx.send(f'{roll_legend[randice]} ')    

@bot.command()
async def WMS(ctx):
    randice = random.randint(0,len(roll_WildMagicSurge)-1)
    await ctx.send(f'{roll_WildMagicSurge[randice]} ')    

bot.run(jdata['TOKEN'])