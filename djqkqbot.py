import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("어밥봇 도움말로 사용 가능한 명령어를 확인하세요.")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("어밥봇 안녕"):
        await message.channel.send(" > 안녕안녕안녕~~~~~~~")
    if message.content.startswith("어밥봇 바보 멍청이"):
         await message.channel.send(" > 아닌데~ 난 천재고 넌 바보야♡♡♡")
    if message.content.startswith("어밥봇 도움말"):
         await message.channel.send(" https://docs.google.com/document/d/11AxI7BdRXR2r-pjP4Vv2rP9QH4J4atsxqp_RREj9XTs/edit?usp=sharing ")
    if message.content.startswith("어밥봇 업데이트"):
         await message.channel.send(" ```업데이트가 없습니다```")
    if message.content.startswith("어밥봇 넌 해고야!"):
         await message.channel.send(" > 내가 왜 해고당하는지 구체적으로 설명좀, 에휴 쯧쯧 에휴 쯧쯧 ((속마음 : 흐흙휼ㄹㄱ 억울해ㅐ ㅠㅠㅠ")
    if message.content.startswith("어밥봇 맛있어"):
        await message.channel.send(" > 나 머거? 흑ㄹ흘규")
    if message.content.startswith("어밥봇 앉아"):
        await message.channel.send(" > 의자를 줘야...큽")     
    if message.content.startswith("어밥봇 일어서"):
        await message.channel.send(" > 난 지금 일어서 있어요~풉킼")    
    if message.content.startswith("어밥봇 지금 몇시야?"):
        await message.channel.send(" > 너 핸드폰 없냐 니가 보면 대지 왜 나한테 시키고 그러냐고... (따흐흑 고흐흑 바흐흑,,)")
    if message.content.startswith("어밥봇 지금 니 기분은?"):
        await message.channel.send(" > 니 기분~~~~~~~~////")                 
    if message.content.startswith("어밥봇 뚱이 알아?"):
        await message.channel.send(" > 아니유~? 어밥봇 인데융ㅇ~~~?~?~?")                                        
    if message.content.startswith("어밥봇 분리수거"):
        await message.channel.send(" > 전 분리수거 안댑니다 일반쓰레기고 아늬에여")                                         
    if message.content.startswith("어밥봇 욕 해봐"):
        await message.channel.send(" > 욕은 나빠용ㅋ 욕 하디마라^^^^^^^^ 적발대면 주근다^^^^^^^^")                                         
    if message.content.startswith("어밥봇 켜기"):
        await message.channel.send(" > 이미 켜져있은뎅7 흐하헤헤힣")                                         
    if message.content.startswith("어밥봇 뚱이 알아?"):
        await message.channel.send(" > 아니유~? 어밥봇 인데융ㅇ~~~?~?~?")                                         
    if message.content.startswith("어밥봇 돌아와"):
        await message.channel.send(" > 나 지금 여기 있는데엥???ㅋ")                                         
    if message.content.startswith("어밥봇 뛰어가"):
        await message.channel.send(" > 귀차나")
    if message.content.startswith("어밥봇 라면 후루룩"):
        await message.channel.send(" > 흑ㄹㄱ 먹혔다..")
    if message.content.startswith("어밥봇 라면 얼마야?"):
        await message.channel.send(" > 어밥봇라면이 뭔데여...흐...헤...ㅎ....")        
    if message.content.startswith("어밥봇 라면"):
       await message.channel.send(" > ㄴ...내가..ㄹ..라..ㅁ..면..ㅇ..이라..ㄴ..니...?")                               
    if message.content.startswith("어밥봇 죽어봐"):
        await message.channel.send(" > 너먼저 주거바 ㅋ크흫ㅎ켏")                                                
    if message.content.startswith("어밥봇 먹기"):
        await message.channel.send(" > 늬희희 날 먹겠다 이거지?흫ㅎ 받아라!!! 어밥빔!!! - - 삐용오오옹 - -")                                                         
    if message.content.startswith("어밥봇 잘했어"):
        await message.channel.send(" > 역시 나야 ♡♡♡♡흐헿흫ㅎ")                                                        
    if message.content.startswith("어밥봇 고생한다"):
        await message.channel.send(" > 맞아맞아 그럼 그래야지!@ (헥헥")                                                        
    if message.content.startswith("어밥봇 심심이 알아?"):
        await message.channel.send(" > 심심이는... 너무 무서우ㅓ요.ㅠㅠㅜㅠ  욕쟁이 심심이....!!!//")                                                        
    if message.content.startswith("어밥봇 시리 알아?"):
        await message.channel.send(" > 시리? 나보다 더 잘났다고 하는애? 참나 이름도 부르지 마라;")                                                        
    if message.content.startswith("어밥봇 어밥이 정체"):
        await message.channel.send(" > 어밥이 = 어밥봇 개발자/햇반이/확계 등!")                                                       
    if message.content.startswith("어밥봇 확퇴"):
        await message.channel.send(" > 우잉? 그럼 나도 퇴물이냐아?? ㅠㅠ")                                                      
    if message.content.startswith("어밥봇 해밥봇 알아?"):
        await message.channel.send(" > 이세상에 해밥봇은 없습니당ㅎ 호홓ㅎ홓")                                                      
    if message.content.startswith("어밥봇 끄기"):
        await message.channel.send(" > 안꺼줄거양 ㅎ히")                                                       
    if message.content.startswith("어밥봇 미육이 알아?"):
        await message.channel.send(" > 어밥봇은 미육이선배라고 불러요!!")

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
