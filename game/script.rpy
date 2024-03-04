# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define e = Character('???', image="me", color="#c8ffc8")
define g = Character('신', image="god", color="#FFFF33")
define l1 = Character('아크룩스', image="ak", color="#FFFF33")
define l2 = Character('폴라리스', image="po", color="#FFFF33")
define l3 = Character('클라우드', image="cl", color="#FFFF33")
define l4 = Character('카리오트', color="#FFFF33")
define l5 = Character('말라리', color="#e71010")
define cha = Character('차현준(개발자)', color = "#c8ffc8")
define name = "주인공"
define c = Character("name", dynamic = True, color="#FFFF33")
define a = Character(None, kind=nvl)
define prophecy1 = Character(None, kind=nvl)
define bogo = Character(None, kind=nvl)
define rightCharacter = Position(xalign = 0.8, yallign = 0.0)
image logo = "backgrounds/logo.png"
image background_heaven = "backgrounds/천국.jpg"
image background_black = "backgrounds/black.jpg"
image background_forest = "backgrounds/forest.jpg"
image background_main = "backgrounds/main.jpg"
image background_ruin = "backgrounds/ruin.jpg"
image background_sun = "backgrounds/sun.jpg"
image background_star = "backgrounds/star.jpg"
image background_moon = "backgrounds/moon.jpg"
image background_hill = "backgrounds/언덕.jpg"
image background_supermoon = "backgrounds/슈퍼문.jpg"
image background_park = "backgrounds/공원.jpg"
image background_ending = "backgrounds/엔딩.jpg"
image background_backmo = "backgrounds/뒷산.jpg"
image background_bedroom = "backgrounds/침실.jpg"
image cg_ak1 = "backgrounds/아크룩스흥칫뿡.jpg"
image cg_cl1 = "backgrounds/클라우드쉿.jpg"
image cg_po1 = "backgrounds/폴라리스하하.jpg"
image cg_po2 = "backgrounds/폴라리스흑화.jpg"
image country1 = "characters/포코우넨.png"
image country2 = "characters/샤키란틴.png"
image country3 = "characters/클린스타클.png"
image country4 = "characters/무쇼.png"
image maps = "characters/지도.png"
image religion = "characters/3교.png"
image religion1 = "characters/슈퍼노바.png"
image religion2 = "characters/이클립스.png"
image religion3 = "characters/아스트라.png"
image god = "characters/신.png"
image me = "characters/주인공.png"
image ak std = "characters/아크룩스-기본.png"
image ak awk = "characters/아크룩스-당황.png"
image ak hmm = "characters/아크룩스-흠.png"
image ak wow = "characters/아크룩스-놀람.png"
image ak mad = "characters/아크룩스-화남.png"
image ak ha = "characters/아크룩스-웃음.png"
image ak haha = "characters/아크룩스-큰웃음.png"
image ak eh = "characters/아크룩스-머뭇.png"
image ak sad = "characters/아크룩스-슬픔.png"
image ak no = "characters/아크룩스-짜증.png"
image ak gal = "characters/아크룩스-갈.png"
image po std = "characters/폴라리스-기본.png"
image po wow = "characters/폴라리스-놀람.png"
image po hmm = "characters/폴라리스-무표정.png"
image po sad = "characters/폴라리스-슬픔.png"
image po ang = "characters/폴라리스-엥.png"
image po mad = "characters/폴라리스-화남.png"
image po haha = "characters/폴라리스-큰웃음.png"
image po dead = "characters/폴라리스-죽은눈.png"
image po gal = "characters/폴라리스-죽은갈.png"
image po ssha = "characters/폴라리스-썩소.png"
image po ho = "characters/폴라리스-호오.png"
image cl std = "characters/클라우드-기본.png"
image cl awk = "characters/클라우드-당황.png"
image cl awkmoo = "characters/클라우드-당황무표정.png"
image cl doki = "characters/클라우드-두근.png"
image cl moo = "characters/클라우드-무표정.png"
image cl haha = "characters/클라우드-아하하.png"
image cl no = "characters/클라우드-절망.png"
image cl dead = "characters/클라우드-죽은눈.png"
image cl hmm = "characters/클라우드-흠.png"
image cl hcb = "characters/클라우드-흥칫뿡.png"
image cl gal = "characters/클라우드-갈.png"
image cl ssha = "characters/클라우드-썩소.png"
image ka std = "characters/카리오트-기본.png"
image ka mad = "characters/카리오트-빡침.png"
image ka hah = "characters/카리오트-못마땅.png"
image ka haha = "characters/카리오트-웃음.png"
image ka dead = "characters/카리오트-죽은눈.png"
image ka deadha = "characters/카리오트-죽은눈웃음.png"
image ka hmm = "characters/카리오트-흠.png"
image ka seri = "characters/카리오트-진중.png"
image ka cham = "characters/카리오트-참나.png"
image ka deepmad = "characters/카리오트-개빡침.png"
image ka deepdeepmad = "characters/카리오트-개레전드빡침.png"
image ka ssha = "characters/카리오트-썩소.png"
image ka ssha2 = "characters/카리오트-썩소아우라.png"
image ka real = "characters/카리오트-가면벗음.png"
image dev = "characters/개발자.png"
define analysis = 0 #예언 해석도 변수
define supernovapower = 0 #슈퍼노바 신앙도 변수 
define eclipsepower = 0 #이클립스 신앙도 변수
define astrapower = 0 #아스트라 신앙도 변수
define reason1 = 40 #슈퍼노바 이성 변수
define reason2 = 40 #이클립스 이성 변수
define reason3 = 40 #아스트라 이성 변수
define dday = 5 #남은 날 수
define time = "오전" #시간대
define count = 0 #활동용 변수
define yebecount = 0 #예배 변수
define persistent.temcount1 = 0 #히든엔딩용 유적지 변수
define temcount = 0 #유적지 변수
define suncount = 0 #태양 관측 변수
define starcount = 0 #별자리 관측 변수
define mooncount = 0 #달 관측 변수
define restcount = 0 #여가활동 변수
define confessioncount1 = 0 #아크룩스 고해성사 변수
define confessioncount2 = 0 #폴라리스 고해성사 변수
define confessioncount3 = 0 #클라우드 고해성사 변수
define persistent.clear = 0 # 클리어 여부
define persistent.goodending1 = 0 # 클리어 여부
define persistent.goodending2 = 0 # 클리어 여부
define persistent.goodending3 = 0 # 클리어 여부
define persistent.normalending = 0 # 클리어 여부
define persistent.badending1 = 0 # 클리어 여부
define persistent.badending2 = 0 # 클리어 여부
define persistent.badending3 = 0 # 클리어 여부
define persistent.badending4 = 0 # 클리어 여부
define persistent.badending5 = 0 # 클리어 여부
define persistent.hiddenending = 0 # 클리어 여부
define persistent.hiddenendingkey = 0 #히든엔딩 트리거

label splashscreen:
    scene black
    $ renpy.pause(1, hard = True)
    play sound "audio/alarm.mp3"
    show logo with dissolve
    $ renpy.pause(2, hard = True)
    hide logo with dissolve
    show text "이 작품에서 등장한 모든 이름, 인물, 사건들은 허구입니다. \n실존하는 인물, 장소, 건물, 제품과는 일절 관련이 없습니다." with dissolve
    $ renpy.pause(2, hard = True)

    hide text with dissolve

    return
            

label reset:
    $ analysis = 0 #예언 해석도 변수
    $ supernovapower = 0 #슈퍼노바 신앙도 변수 
    $ eclipsepower = 0 #이클립스 신앙도 변수
    $ astrapower = 0 #아스트라 신앙도 변수
    $ reason1 = 40 #슈퍼노바 이성 변수
    $ reason2 = 40 #이클립스 이성 변수
    $ reason3 = 40 #아스트라 이성 변수
    $ dday = 5 #남은 날 수
    $ time = "오전" #시간대
    $ count = 0 #활동용 변수
    $ yebecount = 0 #예배 변수
    $ temcount = 0 #유적지 변수
    $ suncount = 0 #태양 관측 변수
    $ starcount = 0 #별자리 관측 변수
    $ mooncount = 0 #달 관측 변수
    $ restcount = 0 #여가활동 변수
    $ confessioncount1 = 0 #아크룩스 고해성사 변수
    $ confessioncount2 = 0 #폴라리스 고해성사 변수
    $ confessioncount3 = 0 #클라우드 고해성사 변수
return

init:
    screen stat_reason:
        frame:
            padding (15, 15)
            background "#2a76c780"
            align (0.0, 0.0) 
            xmaximum 500
            ymaximum 1000
            
            vbox:
                text  "                              예언까지   {color=#e71010}D - [dday] 일{/color}" size 20 
                text " " size 3
                text "현재 시간:{space=15}[time]" size 16
                text " " size 3
                text "아크룩스 이성:{space=15}[reason1]" size 16
                bar:
                    value reason1
                    range 100
                    style "fixed_bar"
                text " " size 3   
                text "폴라리스 이성:{space=15}[reason2]" size 16
                bar:
                    value reason2
                    range 100
                    style "fixed_bar"
                text " " size 3
                text "클라우드 이성:{space=15}[reason3]" size 16
                bar:
                    value reason3
                    range 100
                    style "fixed_bar"

init:    
    screen stat_overlay:        
        # 호감도 창        
        frame:            
            # 호감도 창 테두리와 컨텐츠와의 간격            
            padding (15, 15)            
            # 호감도 배경 (반투명 - 뒤 2자리 코드가 투명도)            
            background "#2a76c780"            
            # x, y축 정렬            
            align (1.0, 0.0)            
            # 호감도 창 크기            
            xmaximum 500            
            ymaximum 1000          
            # 텍스트와 호감도 바가 수직으로 배치됨            
            vbox:
                text "예언 해석도:{space=15}[analysis]" size 16                
                bar:                    
                    value analysis                   
                    # 호감도 바 범위                    
                    range 100                                        
                    # 아래 지정한 fixed_bar 스타일을 따름
                    style "fixed_bar"                                    
                # 다음 캐릭터의 바와 이전 캐릭터 텍스트 사이의 간격                
                # padding을 쓸 경우, 바, 텍스트 간격 모두 동일하게 적용됨                
                text " " size 3                 
                text "슈퍼노바 신앙도:{space=15}[supernovapower]" size 16                 
                bar:                    
                    value supernovapower                  
                    range 100                    
                    xalign 0.0                    
                    style "fixed_bar"                 
                text " " size 3                 
                text "이클립스 신앙도:{space=15}[eclipsepower]" size 16                 
                bar:                    
                    value eclipsepower                   
                    range 100                    
                    xalign 0.5
                    style "fixed_bar"                     
                text " " size 3                 
                text "아스트라 신앙도:{space=15}[astrapower]" size 16                 
                bar:                    
                    value astrapower                  
                    range 100                    
                    xalign 1.0                 
                    style "fixed_bar"
                    

init -5 python:    
        # 호감도 바 스타일    
        style.fixed_bar = Style(style.default)        
        # bar width    
        style.fixed_bar.xmaximum = 400        
        # bar height    
        style.fixed_bar.ymaximum = 30       
        # bar의 gutter 부분 간격; 5로 지정할 시 5만큼 색이 칠해져있음    
        style.fixed_bar.left_gutter = 0     
        style.fixed_bar.right_gutter = 0        
        style.fixed_bar.left_bar = Frame("images/bar_full.png", 0, 0)    
        style.fixed_bar.right_bar = Frame("images/bar_empty.png", 0, 0) 




# 여기에서부터 게임이 시작합니다.
label start:
    # $ config.rollback_enabled = False (나중에 #지우기)
    call reset from _call_reset
    hide screen stat_overlay
    hide screen stat_reason
    scene background_black
    if (persistent.goodending1 == 1 and persistent.goodending2 == 1 and persistent.goodending3 == 1 and persistent.normalending == 1 and persistent.badending1 == 1 and persistent.badending2 == 1 and persistent.badending3 == 1 and persistent.badending4 == 1 and persistent.badending5 == 1 and persistent.hiddenending == 1):
        play music "audio/omake.mp3"
        show dev
        cha "헉!!!!!!!!!!!!!!"
        cha "모든 엔딩을 해금하셨군요!!!!"
        cha "정말 열심히 해주셔서 감사합니다!!!!!"
        cha "이번 게임도 어쩌다보니 1인 개발하게 되었는데요.."
        cha "혼자서 그림도 그리고.. 코딩도 하고.. 전부 다 하려다 보니"
        cha "진~짜 죽을맛이였습니다ㅏㅏㅏ..."
        cha "렌파이 엔진 자체도 처음 써보는거라 많이 엉성하고요.."
        cha "거기다 도중에 역류성 식도염도 오고.."
        cha "감기도 한번 시원하게 걸려주고...."
        cha "몸이 정말 다방면에서 고통받았던 것 같습니다."
        cha "그래도 정말 열심히 개발했습니다!!!!!"
        cha "그리고 그렇게 열심히 만든 게임을 \n이렇게 완벽하게 끝까지 즐겨주셔서.."
        cha "진심으로 감사드립니다!!!!"
        cha "여기까지 오셨다면 정말로 더이상 볼 컨텐츠가 없습니다!!!"
        cha "혹시라도 제가 차후에 추가 패치를 \n하는 게 아닌 이상에는요......"
        cha "아! 그리고.."
        cha "실례가 되지 않는다면..\n저에게 피드백을 보내주신다면 \n정말로 큰 기쁨이 될 것 같습니다...."
        cha "분량은 적당했는지.. 시나리오는 납득 가능했는지...\n히든 엔딩 해금 조건이 혹시라도 괴랄하지는 않았는지.."
        cha "염치불구하고 오네가이시마스!!!!!!!!!!!!!!!"
        cha "아무쪼록 즐거운 경험을 제공해드렸길 바랍니다."
        cha "이 스크립트를 넘기면 다시 원래 게임으로 돌아갑니다!"
        hide dev
        stop music

    if (persistent.clear != 0):
        "이전에 클리어한 기록이 존재합니다."
        "플레이 시 스토리에 영향을 미칠 수 있습니다."
        "처음부터 플레이를 원하시는 경우 \n클리어 데이터를 지우시는 것을 추천드립니다."
        "모든 엔딩 해금에 도전하시는 경우 \n그대로 진행하시는 것을 추천드립니다."
        menu:
            "클리어 데이터를 지울까요?\n(※경고 : 되돌릴 수 없습니다.)"

            "네":
                
                $ persistent.clear = 0
                $ persistent.goodending1 = 0 # 클리어 여부
                $ persistent.goodending2 = 0 # 클리어 여부
                $ persistent.goodending3 = 0 # 클리어 여부
                $ persistent.normalending = 0 # 클리어 여부
                $ persistent.badending1 = 0 # 클리어 여부
                $ persistent.badending2 = 0 # 클리어 여부
                $ persistent.badending3 = 0 # 클리어 여부
                $ persistent.badending4 = 0 # 클리어 여부
                $ persistent.badending5 = 0 # 클리어 여부
                $ persistent.hiddenending = 0 # 클리어 여부
                $ persistent.hiddenendingkey = 0 #히든엔딩 트리거
                $ persistent.temcount1 = 0 #히든엔딩용 유적지 변수
                "데이터가 삭제되었습니다."
                "게임을 시작합니다."
            "아니오":
                "그대로 진행합니다."
                pass
                
    if (persistent.hiddenending == 1):
        stop music fadeout 2.0
        "과거의 기억들을 돌아볼 수 있을 것 같다."
        "혹시라도.. 알아내지 못했던 이야기가 있다면.."
        "모두 알아내고 가자."
        define i = True
        while(i):
            $name = renpy.input("내 이름은")
            menu:
                "[name]이(가) 맞습니까?"

                "예":
                    $ i = False
                    jump main
                        
                "아니오":
                    pass      

    elif (persistent.goodending1 == 1 and persistent.goodending2 == 1 and persistent.goodending3 == 1 and persistent.normalending == 1 and persistent.temcount1 == 1):
        stop music fadeout 2.0
        define i = True
        while(i):
            $name = renpy.input("내 이름은")
            menu:
                "[name]이(가) 맞습니까?"

                "예":
                    $ i = False
                        
                "아니오":
                    pass        
        play music "audio/badend.mp3" loop
        "...어라?"
        "당신은.. 누구야?"
        "갑자기 내 머릿속에.. 이 기억은 뭐지?"
        "이건.. 내 기억이 아닌 것 같으면서도, \n나의 기억이였던 것만 같아."
        "이 시작이.. 처음이 아닌것만 같은 기분이야."
        "어째서인지 모든 교주들과 한번씩은 좋은 기억을 만들었던 것만 같아."
        "..."
        "아아.. 그랬던 거였구나."
        "역시 그러면 그렇지."
        "당신이 내 뒤에서 함께했던 거구나?"
        "당신 덕분에.. 나는 클린스타클을 위기로부터 구해냈었어."
        "그것도 모든 교주들과 한번씩 말이지."
        "....그런데 어째서 다시 시작한거야?"
        "이미 모두를 행복하게 만들어줬잖아?"
        "그런데도.. 뭔가 걸리는 구석이 있었던 거지?"
        "맞아. 사실은 완벽하게 깔끔한 엔딩은 아니였어."
        "에크모트는 혜성에 불과했어."
        "그런데 스플릿시 유적지는 어째서 \n'에크모트의 시체'가 봉인되어 있다는 전설이 있던걸까?"
        "그리고 스플릿시에서 뿜어져 나오던 \n그 위험한 기운의 정체는 뭐였던 걸까?"
        "그리고..."
        "'어르신'이라고 불리는 작자들은, 그래서 뭐였던 걸까?"
        "사건 내내 흑막인 것 처럼 언급되지만, \n결국 직접적으로 나온 적은 없는걸."
        "뭔가 뒷맛이 씁쓸했단 말이지."
        "하하하.."
        "그럼 이번에는... 아예 다르게 생각해볼까?"
        "이 이야기 안에서.."
        "모든 걸 주도했었지만,"
        "반대로 단 한번도 함께 뭔가를 했던 적은 없는.."
        "{color=#e71010}누군가{color=#FFFFFF}가 있었어."
        "그 사람이..어쩌면 모든 진실을 알고 있지 않을까?"
        "그럼...다시 그 숲으로 가보자고."
        "명심해."
        "그 사람을 추적하는 거야."

        $ persistent.hiddenendingkey = 1


    elif (persistent.clear == 1):
        menu:
            "인트로를 스킵합니까?"

            "네":
                define i = True
                while(i):
                    $name = renpy.input("내 이름은")
                    menu:
                        "[name]이(가) 맞습니까?"

                        "예":
                            $ i = False
                        
                        "아니오":
                            pass
                pass
        
            "아니오":
                call intro from _call_intro

    else :
        call intro from _call_intro_1
    # 1-1 인트로

    ""
    play music "audio/forest.mp3" fadein 2.0 loop
    play sound "audio/warp.mp3"
    scene background_forest with dissolve
    if (persistent.hiddenendingkey == 1):
        show me
        c "..."
        c "돌아왔구나, 이 숲으로."
        c "어디로 가볼까?"
        hide me
        define i1 = True
        while (i1):
            menu:
                "어디로 가야하지?"
            
                "왼쪽 길":
                    show me
                    c "이 쪽은 아크룩스 님이 있던 곳인데.."
                    c "그래도 계속 갈까?"
                    hide me
                    menu:
                        "계속 갈까?"
                            
                        "계속 간다.":
                            $ i1 = False
                            call forest1 from _call_forest1
                        "역시 아니다.":
                            pass
                            

                "가운데 길":
                    show me
                    c "이 쪽은 폴라리스가 있던 곳인데.."
                    c "그래도 계속 갈까?"
                    hide me
                    menu:
                        "계속 갈까?"
                            
                        "계속 간다.":
                            $ i1 = False
                            call forest2 from _call_forest2
                        "역시 아니다.":
                            pass

                "오른쪽 길":
                    show me
                    c "이 쪽은 클라우드 씨가 있던 곳인데.."
                    c "그래도 계속 갈까?"
                    hide me
                    menu:
                        "계속 갈까?"
                            
                        "계속 간다.":
                            $ i1 = False
                            call forest3 from _call_forest3
                        "역시 아니다.":
                            pass

                "뒷 길":
                    show me
                    c "그러고보니 이 쪽으로 가보지는 않았다."
                    c "이번에는 여기로 갈까?"
                    hide me
                    menu:
                        "이쪽으로 갈까?"
                            
                        "간다.":
                            $ i = False
                            $ i1 = False
                            jump hiddenending
                                
                        "역시 아니다,":
                            pass
                    
    else:
        show me
        c "..."
        c "뭐지? 순식간에 장소가 바뀌었네.."
        c "엄청 몽환적인 느낌의 숲이구만.."
        c "근데.. 여기로 온 것까진 좋은데,"
        c "이제 어디로 가야하지?"
        c "이 망할 신같으니!!!!! 적어도 마을 한복판에서 내려줘야 할 거 아니야!!!!!!" with vpunch
        hide me
        menu :
            "어디로 가야하지?"
        
            "왼쪽 길":
                call forest1 from _call_forest1_1
            "가운데 길":
                call forest2 from _call_forest2_1
            "오른쪽 길":
                call forest3 from _call_forest3_1
    
    stop music
    scene background_black with dissolve
    ""
    scene background_main
    play music "audio/office.mp3" fadein 2.0 loop

    "그리하여 집무국에 도착했다."
    show po std
    l2 "어쩌다보니 다들 모였네~"
    show po ho
    l2 "오랜만이야! 아크룩스 언니, 클라우드 언니!"
    hide po
    show cl std
    l3 "오랜만이에요, 폴라리스. 저번 대관식 때가 마지막이였던가요?"
    hide cl
    show ak std
    l1 "확실히 셋 모두가 한 자리에 모인 건 오랜만이군.\n그간 각자의 위치에서 바빴으니.."
    hide ak
    show cl hmm
    l3 "그래서 여기 모두 모인 이유가.."
    hide cl
    show ka std
    l4 "'저 놈'의 신원을 검증하기 위해서였지."
    hide ka
    show me
    c "...저 놈이라니....."
    hide me
    show po ho
    l2 "맞아~ 말을 이쁘게 해야지, 카리오트 언니!\n안 그러면 나같은 어린애가 배운다구?"
    hide po
    show ka mad
    l4 "조용히 해, 앙증맞은 꼬맹아.\n안 그래도 바빠 죽겠는데 이게 뭔 일이야 정말.."
    hide ka
    show po ssha
    l2 "바빠? 언니가 바쁠 일이 있었나??\n발품은 우리가 팔고 있는데에~"
    hide po
    show ka mad
    l4 "이게 누굴 닮아서 이렇게 말본새가 야무져졌지?\n전대 주교님은 품격이 흘러넘치시는 분이셨는데 말야."
    hide ka
    show cl awk
    l3 "아하핫.. 둘이 자주 티격태격하고는 해요.\n[name]님이 이해해주세요."
    hide cl
    show ak eh
    l1 "잡담은 그쯤 하고..\n정식으로 소개하도록 하겠습니다."
    show ak std
    l1 "저는 아크룩스. 슈퍼노바의 현 교주입니다."
    hide ak
    show po std
    l2 "나는 폴라리스! 이클립스의 현 교주야."
    show po ang
    l2 "사실 대부분 일들은 이클립스 어르신들이 하고 계시지만.."
    hide po
    show cl std
    l3 "그리고 저는 클라우드. 아스트라의 현 교주에요."
    l3 "저희 셋이 클린스타클의 종교쪽을 대표한다고 보시면 돼요."
    l3 "물론 국왕님을 비롯한 행정직은 별도로 존재하고 있고요."
    show cl moo
    l3 "마지막으로..."
    hide cl
    show po hmm
    l2 "..."
    hide po
    show ak eh
    l1 "..."
    hide ak
    show me
    c "..."
    hide me
    show ka hmm
    l4 "...?"
    show ka hah
    l4 "뭘 봐?"
    hide ka
    "(폴라리스가 그쪽도 하라는 손짓을 한다.)"
    show ka hmm
    l4 "아. 나?"
    show ka std
    l4 "나는 카리오트."
    l4 "원래는 중앙정부 기획재정부 장관인데.."
    l4 "지금은 상황이 상황인지라, \n비상대책위원회장으로 일하고 있다."
    show ka haha
    l4 "국왕께서 나를 전적으로 신뢰하시는 탓에.."
    hide ka
    show po ang
    l2 "갑자기 자화자찬 모드?"
    hide po
    show cl awk
    l3 "능력자시긴 하죠. 최연소로 장관 자리에 오르셨으니까요~"
    hide cl
    show ak ha
    l1 "거기다 '종언서'의 일부를 처음으로 발견한 분이기도 하시죠."
    hide ak
    show me
    c "(최연소 장관? 첫인상은 끝내주게 비호감이였는데,\n보기보다 정말 능력자인가 보네..)"
    hide me
    show ak std
    l1 "소개는 이쯤에서 끝내도록 하죠."
    l1 "그래서 카리오트 씨.\n'구원자'라는 게 정말 이런 식으로 나타나는 건가요?"
    hide ak
    show cl moo
    l3 "사실 전례랄 게 없잖아요?\n클린스타클에 이 정도의 위기가 도래한 적이 있었던가요?"
    hide cl
    show po hmm
    l2 "그래서 교차 검증이란 걸 할 수가 없겠더라고~"
    l2 "옛날에도 우리나라가 위험했었는데 그때도 짱짱 용사가 왔다!\n이렇게 써있으면 얼마나 좋아?"
    hide po
    show ak eh
    l1 "그것도 그렇네.."
    hide ak
    show ka hmm
    l4 "오~ 교차 검증이라는 단어도 알아, 꼬맹이?"
    show ka std
    l4 "맞아. 확실히 저 놈의 주장만 듣고 \n저 놈을 전적으로 구원자로 신뢰하기엔 무리가 있어."
    l4 "그리고 과거 기록상으로 봐도 \n구원자로 동일시되는 존재가 있었다는 기록은 존재하지 않아."
    hide ka
    show cl std
    l3 "적어도 저희들이 기억하고 보존하는 선에서는 말이죠."
    hide cl
    show ak std
    l1 "다만.."
    l1 "확실히 이 자는 클린스타클의 정부 핵심 관료들을 제외하면\n 알 리가 만무한 모든 정보들을 알고 있었습니다."
    hide ak
    show po std
    l2 "거기다가 클린스타클 국민이라면 모를 수가 없는 \n우리 셋 얼굴도 처음 보는듯 하고~"
    hide po
    show ka std
    l4 "무엇보다도 제일 중요한 게 있어."
    hide ka
    show me
    c "제일 중요?"
    hide me
    show ka seri
    l4 "비단 우리가 발전한 기술력과 현대적인 정치 체계의 국가라고는 하지만.."
    l4 "클린스타클은 '종교'의 나라다."
    l4 "여기에서 종교적으로 합당하지 못하다는 건\n최고로 금기시되는 상황이지."
    l4 "신에게 반기를 드는 것과 동일시되는 중죄야."
    l4 "그리고 창세기는 예언서 중에서도 \n가장 시초에 기록된 것으로 전해지는 성서 중의 성서다."
    l4 "그런 창세기에서 언급하는 날에 우연히도\n자신을 구원자라고 칭하는 미지의 존재가 나타났다.."
    show ka cham
    l4 "그런데 그 존재가 우리가 처한 상황을 너무나도 잘 알고 있다?"
    l4 "일반적인 시선에서 바라보면 네가 매우 미심쩍은 존재겠지만.."
    l4 "반대로 종교적인 관점에서 바라본다면,"
    show ka hmm
    l4 "너는 더할나위 없이 완벽하게 구원자에 부합하는 인물이다.\n이 말이야."
    hide ka
    show ak wow
    l1 "!"
    hide ak
    show po wow
    l2 "!"
    hide po
    show cl hmm
    l3 "!"
    hide cl
    show ka std
    l4 "솔직히 말하자면.."
    l4 "당장에 남은 시간이 이젠 일주일도 채 없어."
    show ka cham
    l4 "정확히는 지금으로부터 예언 당일까지 6일 2시간 남았더군."
    l4 "그리고 어차피 모든 전후상황을 알고있는 사람인데, \n찬 밥 더운 밥 가릴 때가 아니기도 하고."
    hide ka
    show ak hmm
    l1 "그렇다는 건!"
    hide ak
    show cl doki
    l3 "카리오트 님께서는 [name]님이 구원자라는 걸 인정하시는 거군요!"
    hide cl
    show po ho
    l2 "와아~!"
    hide po
    show ka hmm
    l4 "어디까지나 종교적인 관점에 의거한 거야."
    show ka cham 
    l4 "내 개인적인 심증으로는 전혀 신뢰스럽지 못하거든."
    hide ka
    show me
    c "어째서?!" with vpunch
    hide me
    show ka hah
    l4 "그건 너 스스로에게 물어보도록."
    show ka std
    l4 "아무튼..[name]..이게 이름 맞았나?"
    hide ka
    show me
    c "맞습니다..."
    hide me
    show ka hmm
    l4 "오늘은 시간이 늦었으니까 여기서 쉬고 가."
    l4 "그동안 여기 교주들이랑 생각 좀 해 보고,\n앞으로 어떻게 할 지 방향성을 정하자고."
    hide ka
    show ak eh
    l1 "오늘도 밤 새겠구만.."
    hide ak
    show po sad
    l2 "성장기에 늦게 자면 안되는데에~"
    hide po
    show cl haha
    l3 "후후후... 어쩔 수 없죠~"
    hide cl
    stop music
    scene background_black with dissolve
    ""
    "예언까지 5일"
    "다음 날, 집무국 비대위실"
    scene background_main
    play music "audio/office.mp3" fadein 2.0 loop
    show po haha
    l2 "좋은 아침! 오빠~"
    hide po
    show me
    c "?!?!" with vpunch
    c "오빠...?!"
    c "(살면서 오빠라는 단어를 들어본 적이 없었는데!!!)"
    hide me
    show cl awk
    l3 "폴라리스는 모두를 똑같이 부르거든요."
    l3 "자기보다 어리면 반말, 나이 많으면 언니 오빠죠.."
    show cl std
    l3 "좋은 아침이에요, [name] 님."
    show cl hcb
    l3 "물론 저희는 한 숨도 못 잤지만요..."
    hide cl
    show me
    c "아, 클라우드 님.. 좋은 아침입니다."
    hide me
    show cl haha
    l3 "저도 이제 편하게 불러주세요~ \n님은 너무 딱딱한 호칭인걸요."
    hide cl
    show me
    c "?!" with vpunch
    c "아..ㄴ..네! 그럼.. 클라우드 씨라고 부르겠습니다."
    hide me
    show po ho
    l2 "아힉ㅋㅋ\n뭐야 오빠~ 보기보다 완전 맹추네!"
    hide po
    show me
    c "맹추!" with vpunch
    c "내 학창시절 12년이 아른거리는 단어다.."
    hide me
    show cl gal
    l3 "폴라리스!"
    hide cl
    show po std
    l2 "미안~~ 오빠 반응이 너무 맛있어서 그만~"
    hide po
    "(끼익)"
    show ak hmm
    l1 "뭐야, 다들 먼저 와있었군."
    show ak ha
    l1 "반갑습니다, [name]님."
    hide ak
    show me
    c "아, 아크룩스 님."
    hide me
    show ak std
    l1 "밤 동안에 교주들과 카리오트님들이 회의를 진행했습니다."
    l1 "그리고 그 결과..."
    show ak ha
    l1 "예언 당일까지 [name]님도 함께 활동하기로 했습니다."
    hide ak
    show cl std
    l3 "일종의 합숙 훈련같은 느낌일까요~"
    hide cl
    show po std
    l2 "응! 그렇게 됐어~"
    hide po
    show me
    c "!!!" with vpunch
    c "합숙...?"
    hide me
    show cl moo
    l3 "네. 아무래도 시간도 촉박하고.."
    l3 "사실 그보다도 결정적인 원인은.."
    hide cl
    show ka cham
    l4 "6일도 안 남은 이 시점에서 분석이랄 게\n놀라우리만치 하나도 진척되지 않았기 때문이지." with vpunch
    hide ka
    show me
    c "?!" with vpunch
    hide me
    show po ang
    l2 "총체적 난국이라고 할 수 있지!" with vpunch
    hide po
    show ak awk
    l1 "대체 그런 표현들은 누가 알려주는 거야..?"
    show ak hmm
    l1 "네, 아무튼 그렇게 되었습니다."
    hide ak
    show ka hah
    l4 "네놈은 여전히 신뢰스럽지 못하지만..."
    show ka seri
    l4 "그것과는 별개의 문제로\n우리의 분석과 연구도 심히 부족한 상태다."
    l4 "당장 종언서의 전문 자체도 발견하지 못한 상황이거든."
    hide ka
    show me
    c "(아무래도 그렇겠지. 종언서는 위조된 예언서일 거니까..)"
    c "그렇다면.. 앞으로 무얼 도우면 되는거죠?"
    hide me
    show ka cham
    l4 "안 그래도 지금 말하려던 참이다."
    show ka seri
    l4 "간략하게 설명해줄테니 잘 들으라고."
    show ka hmm
    l4 "지금 시각은 정확히 오전 9시 12분."
    $ i = True
    while(i):
        show ka hmm
        l4 "앞으로 매일 9시마다 여기에 \n나를 제외한 교주 3명이 집합할 거다."
        l4 "너는 무슨 활동을, 누구와 진행할 지 결정하면 돼."
        l4 "교주들은 전적으로 너의 의견을 따를거야."
        l4 "활동은 오전과 오후로 2번에 나눠서 진행할거고."
        l4 "모든 활동들에는 그에 따른 영향이 있을거야."
        l4 "나는 그때그때마다 방문하도록 하지."
        l4 "이해됐어?"
        menu:
            "이해됐어?"

            "넵!":
                $ i = False

            "한 번만 다시 설명해주세요...":    
                show ka hah 
                l4 "하아..."
                l4 "제대로 들으라고, 임마."
                
    show ka haha
    l4 "좋아."
    l4 "그럼 본격적으로 시작해보자고."
    l4 "작전명 '종말 막기 프로젝트'를."
    hide ka
    show me
    c "종말 막기 프로젝트..."
    hide me
    show ka seri
    l4 "즉석에서 대충 지은거다."
    hide ka
    show po ang
    l2 "와우~ 작명 너무 극혐이야!"
    show po std
    l2 "뭐 어쨌건간에~ 앞으로 함께 잘 해보자, 오빠!"
    hide po
    show cl awk
    l3 "하하핫.. 아무쪼록..5일간 잘 부탁드립니다!"
    hide cl
    show ak ha
    l1 "이하동문입니다."
    hide ak
    stop music
    scene background_black with dissolve
    "그리하여.."
    "5일간의 종말 막기가 시작되었다."
    call main from _call_main
return

label main:
    define count1 = 0 ## 종언서 전문 확인여부
    define no = 0 ## 아니오 여부
    define badending = 0 # 배드엔딩 봤는지 여부
    define bgmchange = 0 # 브금 겹치지 않게하기
    play music "audio/lobby.mp3" loop
    while(dday >= 0):
        show screen stat_overlay
        show screen stat_reason
        if (dday == 0):
            jump ending
        if (restcount == 4):
            $ dday = 0
            $ persistent.badending5 = 1
            jump restending
        if ((no == 0)and(bgmchange == 1)):
            if ((dday <= 2)):
                play music "audio/lobby2.mp3" loop
                $ bgmchange = 0
            else:
                play music "audio/lobby.mp3" loop
                $ bgmchange = 0

        scene background_main with dissolve

        if ((analysis >= 60)and(count1 == 0)and(count == 0)):
            call prophecy from _call_prophecy

        if (reason1 <= 0):
            $ persistent.badending1 = 1
            jump gameover1
        if (reason2 <= 0):
            $ persistent.badending2 = 1
            jump gameover2
        if (reason3 <= 0):
            $ persistent.badending3 = 1
            jump gameover3

        if (count == 0):
            $ time = "오전"
            menu day:
                "오전이다. 무엇을 할까?"

                "정기 회의\n(예언 해석 수치 +20)":
                    menu:
                        "정기 회의를 하시겠습니까?"

                        "예":
                            $ no = 0
                            call meeting from _call_meeting

                        "아니오":
                            $ no = 1
                            pass
                    
                "정기 예배\n(모든 교단 신앙도 +10)":
                    menu:
                        "정기 예배를 하시겠습니까?"

                        "예":
                            $ no = 0
                            call pray from _call_pray

                        "아니오":
                            $ no = 1
                            pass
                "유적지 탐사\n(선택한 교주 이성 -20 / 예언 해석 수치 +10)":
                    menu:
                        "유적지를 탐사하시겠습니까?"

                        "예":
                            menu:
                                "함께 갈 교주를 선택해주세요."

                                "아크룩스":
                                    menu:
                                        "아크룩스와 함께합니다."

                                        "예":
                                            $ bgmchange = 1
                                            $ no = 0
                                            call temple1 from _call_temple1

                                        "아니오":
                                            $ no = 1
                                            pass

                                "폴라리스":
                                    menu:
                                        "폴라리스와 함께합니다."
                                        
                                        "예":
                                            $ bgmchange = 1
                                            $ no = 0
                                            call temple2 from _call_temple2

                                        "아니오":
                                            $ no = 1
                                            pass

                                "클라우드":
                                    menu:
                                        "클라우드와 함께합니다."

                                        "예":
                                            $ bgmchange = 1
                                            $ no = 0
                                            call temple3 from _call_temple3

                                        "아니오":
                                            $ no = 1
                                            pass

                        "아니오":
                            $ no = 1
                            pass

                "여가 활동\n(모든 교주의 이성 +10)":
                    menu:
                        "여가 활동을 하시겠습니까?"

                        "예":
                            $ no = 0
                            call rest from _call_rest

                        "아니오":
                            $ no = 1
                            pass
                
        elif ((count == 1)and(dday != 0)):
            $ time = "오후"
            menu night:
                "오후다. 무엇을 할까?"
                
                "태양 관측\n(예언 해석 수치 +10 / 슈퍼노바 신앙도 +10)":
                    menu:
                        "태양 관측을 하시겠습니까?"

                        "예":
                            $ bgmchange = 1
                            $ no = 0
                            call sun from _call_sun
                        "아니오":
                            $ no = 1
                            pass

                "별자리 관측\n(예언 해석 수치 +10 / 아스트라 신앙도 +10)":
                    menu:
                        "별자리 관측을 하시겠습니까?"

                        "예":
                            $ bgmchange = 1
                            $ no = 0
                            call star from _call_star
                        "아니오":
                            $ no = 1
                            pass
                "달 관측\n(예언 해석 수치 +10 / 이클립스 신앙도 +10)":
                    menu:
                        "달 관측을 하시겠습니까?"
                        
                        "예":
                            $ bgmchange = 1
                            $ no = 0
                            call moon from _call_moon
                        "아니오":
                            $ no = 1
                            pass

                "고해성사\n(선택한 교주의 이성 +20)":
                    menu:
                        "고해성사를 하시겠습니까?"

                        "예":
                            menu:
                                "고해성사를 진행할 교주를 선택해주세요."
                                
                                "아크룩스":
                                    menu: 
                                        "아크룩스의 고해성사를 진행합니다."
                                        
                                        "예":
                                            $ no = 0
                                            call confession1 from _call_confession1

                                        "아니오":
                                            $ no = 1
                                            pass
                                
                                "폴라리스":
                                    menu: 
                                        "폴라리스의 고해성사를 진행합니다."

                                        "예":
                                            $ no = 0
                                            call confession2 from _call_confession2

                                        "아니오":
                                            $ no = 1
                                            pass
                                
                                "클라우드":
                                    menu:
                                        "클라우드의 고해성사를 진행합니다."

                                        "예":
                                            $ no = 0
                                            call confession3 from _call_confession3

                                        "아니오":
                                            $ no = 1
                                            pass

                        "아니오":
                            $ no = 1
                            pass
                            
return

label intro:
    stop music
    play music "audio/god.mp3" fadein 2.0 loop
    scene black with dissolve
    $ renpy.pause(1, hard = True)
    show text "제작 : 차현준 (컴퓨터공학부 20)" with dissolve
    $ renpy.pause(2, hard = True)
    hide text with dissolve
    show text "이 게임은 종교와 관련된 소재를 다룹니다.\n플레이하시기 전 미리 참고해주시면 감사하겠습니다." with dissolve
    $ renpy.pause(3, hard = True)
    hide text with dissolve
    a "따스한 햇살의 향기,"
    a "옷깃을 스치는 상쾌한 바람."
    a "내가 창문을 열어놓고 잤던가?"
    a "그렇게 생각하고 있던 중, 누군가가 말을 건다."
    nvl clear
    g "......세요"
    g "....일어나세요......"
    g "....일어나세요 용사여......"
    scene background_heaven with dissolve
    g "!"
    show god 
    g "일어나셨군요!"
    g "아무리 깨워도 반응이 없으셔서... 전송 과정에서 문제라도 생긴 줄 알았습니다."
    g "별 일 없으셔서 정말 다행입니다, 용사님."
    hide god
    show me
    c ".....?"
    c "여기는..."
    hide me
    show god
    g "여기는 천국... 이 세계의 순행을 관장하는 곳입니다."
    g "일단 자초지종부터 설명드려야겠군요."
    g "그 전에.. 용사님의 이름부터 알 수 있겠습니까?"
    g "용사님의 이름은 무엇입니까?"
    define i = True
    while(i):
        $name = renpy.input("내 이름은")
        menu:
            "[name]이(가) 맞습니까?"

            "예":
                $ i = False
            
            "아니오":
                pass
            
    hide god
    show me
    c "내 이름은... [name]"
    hide me
    show god
    g "그렇군요. [name]... 인 건가요."
    g "[name]님. 단도직입적으로 말씀드리겠습니다."
    g "이 세계가 처한 위기를 해결주셨으면 합니다."
    hide god
    show me
    c "......?"
    c "뭐라고요?"
    hide me
    show god
    g "말 그대로입니다."
    g "부디 이 세계의 위기를 해결해주세요."
    g "[name]님만이 가능한 일입니다."
    hide god
    show me
    c "(아니.. 이게 무슨 3류 판타지 소설 같은 상황이야?)"
    c "(이거 꿈인가..?)"
    c "(아니, 꿈이라기엔 오감도 생생하고..)"
    c "(뭣보다 주변을 둘러봐도 보이는 거라곤 이 신이라는 작자와 구름이 전부야.)"
    c "(자고 일어나니 갑자기 모르는 세계로 워프된 것부터 당황스러운데,)"
    c "(대뜸 여기를 위기로부터 지켜달라고...?)"
    c "(전생했더니 이세계 용사였던 건에 대하여, 뭐 그런건가?)"
    c "(아니, 잠깐. 이거 몰래 카메라 아니야? 이세계 전생 컨셉으로..?)"
    c "(그래, 개꿀잼 몰래카메라인가 보네. 세트장까지 전부 만들다니 꽤 공들였어..)"
    c "(하지만 이런 이세계물 유행 이미 지난 지 오랜데....)"
    hide me
    show god
    g "몰래카메라 아닙니다."
    hide god
    show me
    c "?!" with vpunch
    c "뭐야?! 어떻게 알았어??"
    hide me
    show god
    g "저는 신이니까요. \n용사님의 속마음을 읽는 것 정도는 가벼운 권능이죠."
    g "지금 이 상황.. 무척이나 당황스러우시겠죠. \n충분히 이해합니다."
    g "그렇지만.. \n이 세계의 창조주라는 타이틀을 달고서 할 말은 아니지만.."
    g "이 세계를 파멸로부터 구할 용사는\n당신이라는 결론에 도달했습니다."
    hide god
    show me
    c "...... 그래요.. 이게 전부 진짜라고 칩시다."
    c "그래서!" with vpunch
    c "그게 왜 하필 나인건데?!"
    c "그리고 앞 뒤 다 잘라먹고 \n아무튼 이 세계가 위험하다고만 하는데,"
    c "좀 명확하게 자초지종부터 설명해줘야\n 납득이라도 하지 않겠어?"
    c "당장 12시간 전까지만 해도 난 내 방 침대에서 누워있었다고!!"
    hide me
    show god
    g "음.."
    g "확실히 그렇군요. 제가 너무 성급했습니다.\n 워낙 급박한 사안인지라.."
    g "무례를 범한 점 사죄드립니다."
    g "그렇다면 천천히 설명해드리겠습니다.\n 이 세계가 처한 상황을..."
    hide god
    scene background_black with dissolve
    stop music
    ""
    # 1-2 클린스타클 배경 설명 부분
    play music "world.mp3" fadein 2.0 loop
    g "이 세계는 네 개의 국가로 나뉘어져 있습니다."
    g "그리고 네 국가들의 사이는 그다지 좋지 않죠."
    g "과거 수 차례의 전쟁을 겪었고 아직도 앙금이 남아있는 관계도 많습니다."
    g "네 국가들을 차례대로 가볍게 설명해드리자면..."
    show country1 with dissolve
    g "먼저 첫 번째 국가는 매화와 무사의 나라, 포코우넨입니다."
    hide country1
    show country2 
    g "두 번째로 병기와 군대의 나라, 샤키란틴입니다."
    hide country2
    show country4 
    g "세 번째. 과학과 로봇의 나라, 무쇼입니다."
    g "그리고 네 번째 나라가 문제가 생긴 곳이지요." 
    hide country4
    show country3 
    g "바로 우주와 교단의 나라, 클린스타클입니다."
    hide country3 with dissolve
    show maps with dissolve
    g "클린스타클은 세 종교 국가가 연합하여 건국된 연방입니다."
    g "해의 나라 라니아, 달의 나라 디아나리아,\n하늘의 나라 유피테리스가 전신이죠."
    c "흠. 내가 살던 세계의 영국이랑 비슷한 느낌이군."
    g "비슷한 사례가 있다니 이해가 훨씬 쉬우시겠군요."
    hide maps with dissolve
    show religion with dissolve
    g "세 나라는 기반이 되는 종교도 각기 다릅니다."
    hide religion with dissolve
    show religion1 with dissolve
    g "첫 번째 교단은 슈퍼노바. \n라니아의 국교이자 해를 숭배하는 교단입니다."
    hide religion1 with dissolve
    show religion2 with dissolve
    g "두 번째 교단은 이클립스. \n디아나리아의 국교이자 달을 숭배하는 교단입니다."
    hide religion2 with dissolve
    show religion3 with dissolve
    g "세 번째 교단은 아스트라. \n유피테리스의 국교이자 하늘을 숭배하는 교단입니다."
    hide religion3 with dissolve
    g "초창기에는 종교간의 화합과 발전 도모라는\n 공통된 목적 하에 눈부신 발전을 이룩하긴 했지만.."
    g "어느정도 안정기에 접어들자 가려졌던 문제점들이\n 하나 둘 드러나기 시작했습니다."
    g "먼저 세 국가 모두 스스로가 정치적으로 \n가장 강한 영향력을 행사하고자 했습니다."
    show me
    c "아무래도 그렇겠지. \n사람 사는 곳은 어디나 똑같으니까..."
    g "여기까지만 듣는다면 \n내부의 갈등이 문제라고 생각하시겠지만.."
    g "사실 진짜 문제는 그게 아닙니다."
    g "저도 속세에 파견되어 있는 천사들로부터 \n얼마 전 보고받은 내용이긴 합니다만.."
    show image "characters/종언서.png" with dissolve
    g "최근 클린스타클에서 과거 삼국시대 시절 작성된 것으로 추정되는\n '종언서'라는 이름의 예언서가 발견되었다고 합니다."
    hide image "characters/종언서.png" with dissolve
    show me
    c "예언서?"
    g "네. 예언서라 함은 제가 인간들 중 \n선택받은 몇몇에게 한 '전언'들을 기록해둔 것들입니다."
    g "여하튼 그 예언서에는 오늘로부터 정확히 1주일 뒤에\n크나큰 재앙이 들이닥칠 것이라고 적혀있다고 합니다."
    g "'에크모트'라는 이름의 괴수가... \n인간들을 심판하러 도래한다고 말이죠."
    scene background_heaven with dissolve
    show me
    c "그거 완전 판타지물 클리셰 아니야? \n어리석은 필멸자들을 창조주가 심판한다~ 어쩌구 하면서 말야."
    hide me
    show god
    g "역시 용사님이시군요. 정확히 보셨습니다. \n한 가지만 제외하고요."
    hide god
    show me
    c "한 가지?"
    hide me
    show god
    g "전 그런 전언을 내린 사실이 전혀 없다는 점입니다."
    hide god
    show me
    c "...?!" with vpunch
    c "당신 창조주라며? \n그런데 저런 예언서에 당신이 개입하지 않았다는 게 말이 돼?"
    hide me
    show god
    g "그 점이 저도 굉장히 미스테리합니다."
    g "저는 이 세계가 처음 생겨날 적부터 \n현세까지의 모든 역사들을 기억하고 또 기록하고 있습니다."
    g "그런데 아무리 제 기억과 천국의 기록들을 샅샅이 찾아봐도, \n 저런 전언을 한 흔적은 존재하지 않습니다."
    g "저는 이 사태의 원인이 \n두 가지 경우의 수 밖에 없다는 결론을 내렸습니다."
    g "첫 번째로 누군가가 철저하게 천국의 모든 보안을 뚫고\n'종언서'와 관련된 기록을 말소시켰거나,"
    g "두 번째로 클린스타클 소속의 누군가가 \n'종언서'를 마치 예언서인 것처럼 위조했거나. 입니다"
    hide god
    show me
    c "전자는 억측인거 같은데." 
    c "가능성이 높은 건 후자의 케이스 아닌가?"
    hide me
    show god
    g "맞습니다."
    g "단언컨데, 클린스타클에는 재앙이 일어날 일이 없습니다."
    g "이건 누군가에 의한 대대적인 선동으로밖에 볼 수 없어요."
    g "그래서 제가 천사들을 비밀리에 파견해서\n내부 흑막 색출 작업을 진행하려고 했는데.."
    g "클린스타클 정부기관에 전체적으로 비상사태가 선포되었다고 합니다."
    g "국가적 혼란을 막기 위해 일반 시민들은 이 사실을 모르지만요."
    hide god
    show me
    c "초비상 사태긴 하지. 확실히.."
    c "전말을 모르고 보면 멸망까지 단 일주일 남은거니까."
    hide me
    show god
    g "해서 천사들의 온전한 활동이 매우 어려워졌습니다. \n 클린스타클 전역의 행정력이 매우 예민해진 상황이기도 하고,"
    g "천사들은 신성력이라는 기운이 매우 짙기 때문이죠."
    g "클린스타클의 국민들은 바로 이질적이란 걸 알아챌거에요."
    g "그렇게 외부의 종족들을 찾아보던 중에 지구를 발견했습니다."
    g "지구는 거주하는 종족들 모두\n 아무런 기운도 없는 평범한 종족이더군요."
    g "외지인이라고 의심받을 여지가 전혀 없었기에 조건에 부합했습니다."
    g "그래서 외부인인 용사님을 부득이하게 \n신의 권능으로 이쪽 세계로 불러들인 겁니다."
    hide god
    show me
    c "몇십억분의 1의 확률을 뚫고 \n기적적으로 그 장기말로 선정된 게 나라니.."
    c "좋아해야 하나 이걸.."
    c "살면서 게임 가챠 3퍼센트 확률도 한 번도 이득본 적이 없는데."
    c "그런데, 정작 모든 사정을 듣고 보니 \n그다지 위기라는 느낌은 안 드는데?"
    c "그냥 1주일 뒤에 아무 일도 일어나지 않으면 \n적당히 해프닝으로 끝나지 않겠어?"
    hide me
    show god
    g "클린스타클이 일반적인 국가라면 괜찮겠죠."
    g "하지만 그들은 우주와 '교단'의 나라입니다."
    g "그들 스스로의 모든 행동양식은 신으로부터 비롯된 것이라고\n 무조건적으로 신뢰하고 있습니다."
    g "그들에게 있어서 종언서를 비롯한 모든 예언서는 \n용사님의 상상보다도 더욱 중요한 존재입니다."
    g "고도로 발달한 국가임에도 불구하고, \n예언서의 내용을 과학적인 근거보다도 더 신뢰하는 \n아이러니한 경우도 있을 정도니까요."
    g "그러한 예언서에 기록된 내용이 허구로 밝혀진다면, \n분명 지금보다도 더욱 큰 국가적 혼란이 야기될 겁니다."
    g "최악의 경우에는 내부 분열까지로 이어질 수도 있겠죠.\n그렇게 된다면.."
    g "클린스타클의 국력이 눈에 띄게 약해진 틈을 타서 \n다시금 국가적 전쟁이 일어날 수도 있는 일촉즉발의 상황인 겁니다."
    g "아까 말씀드렸듯이 이 세계의 국가들은\n서로 그다지 좋은 관계가 아니니까요."
    hide god
    show me
    c "흠.. 그건 듣고보니 그렇네."
    c "아직도 좀 어이없지만 이제 상황은 완벽히 이해했어."
    c "클린스타클에 직접 가서\n 무슨 일이 일어나고 있는 지 확인하면 되는거지?"
    hide me
    show god
    g "네. 맞습니다."
    g "곧바로 용사님을 클린스타클로 내려드리겠습니다. \n그곳에서 클린스타클의 국민인 것 처럼 행동하면서 의심스러운 점들을 찾아주세요."
    g "전송 과정에서 자동으로 클린스타클의 일반적인 의상으로 환복될 겁니다."
    hide god
    show me
    c "잠깐, 지금 바로?!"
    c "상황이 급한 건 알겠지만!! \n지리라던가, 정치구조라던가, 이런 걸 하나도 모르는데??"
    hide me
    show god
    g "아, 그 점은 걱정하지 않으셔도 됩니다."
    g "제가 이곳에서 계속해서 도움을 드리겠습니다."
    g "용사님 세계에서 '통신'이라고 부르는 방식처럼요."
    hide god
    show me
    c "하아..."
    c "어쩌다가 이렇게 됐는지..."
    c "알았어.. 지금 보내줘."
    hide me
    stop music
    show god
    g "용사님이라면 반드시 성공하실 겁니다."
    g "그러면.. 모쪼록 무운이 함께하시길.."
    hide god
return


label forest1:
    show me
    c "그래. 왼쪽으로 가보자."
    hide me
    "왼쪽 길로 들어선 지 몇분이 흘렀다."
    show me
    c "........."
    c "... 아무래도 길을 잃은 것 같다."
    c "여긴.. 어디지..?"
    hide me
    "거기, 누구?"
    show me
    c "!" with vpunch
    hide me
    show ak std
    l1 "이 쪽은 허가받지 않은 분은 출입할 수 없는데."
    l1 "...그쪽은 누구시죠?"
    hide ak
    show me
    c "아.. 그게... 저는.. "
    menu:
        "저는...."

        "이 나라를 구하기 위해 온 용사 [name]입니다!":
            hide me
            show ak wow
            l1 ".."
            hide ak
            show me
            c "..."
            hide me
            show ak awk
            l1 "...??"
            hide ak
            show me
            c "네.. 그러니까 말 그대로입니다...."
            hide me
            show ak eh
            l1 "하아.. 안 그래도 바빠 죽겠는데.."
            show ak mad
            l1 "이상한 사람까지 난입하고 난리야...."
            hide ak
            show me
            c "잠깐잠깐잠깐만요!!! 이상한 사람이라니!!"
            c "초면에 대놓고 앞에서 험담이라니, 너무하시네!"
            hide me
            show ak awk
            l1 "그야.. 어떤 정상인이 밤 11시에 정부 사유지 한복판에서\n대뜸 이 나라를 구하러 왔다고 하겠어요."
            hide ak
            show me
            c "(아..지금 밤 11시였구나..)"
            c "....시간이 벌써 이렇게 늦은 줄 몰랐습니다.."
            c "(근데 생각해보니까, 이 여자애는 정체가 뭐지?)"
            c "(그닥 나이가 많아보이지는 않은데,\n얘도 정부 소속인건가?)"
            c "그보다, 이제 그쪽도 본인이 누군지 알려주세요."
            hide me
            show ak hmm
            l1 "흠.. 제 얼굴을 모르는 분도 계셨군요."
            hide ak
            show me
            c "(보기보다 좀 자존감이 높은 애구나..)"
            hide me
            show ak std
            l1 "뭐 다른 교단 소속이시면 모를 만도 하겠군요."
            l1 "저는 슈퍼노바 현 교주, 아크룩스입니다."
            hide ak
            show me
            c "?!" with vpunch
            c "슈퍼노바라면... 제 1교단?!"
            hide me
            show ak std
            l1 "맞습니다."
            l1 "일단 밖으로 안내해드리겠습니다."
            l1 "그쪽에서 신원 조회를 잠시 진행할거에요."
            l1 "상황을 보니 고의성은 없으신 것 같지만.. \n어쨌거나 이 시간에 무단 침입은 높으신 분들이 \n별로 좋게 보지는 않을 거거든요."
            hide ak
            show me
            c "(뭐?! 신원 조회?!?!?!?!)" with vpunch
            c "(이런 건 얘기에 없었잖아, 신 이양반아!!!!!!!!)"
            c "네? 신원 조회요..?"
            hide me
            show ak hmm
            l1 "아, 걱정 마세요. \n그쪽 신원만 확인되면 큰 문제는 없을겁니다."
            show ak std
            l1 "요즘 행정처리가 완전 대충대충이라서요."
            hide ak
            show me
            c "(신원이 확인될 리가 만무하잖아!!)"
            c "(어떻게 해야하지???)"
            c "(일단 급한대로 뭐라도 말해보자.)"

        "물어보시는 그쪽은 누구시죠?":
            hide me
            show ak eh
            l1 "질문에 질문으로 답하시다니.."
            show ak std
            l1 "그래요, 저부터 말씀드리죠."
            l1 "저는 아크룩스."
            l1 "슈퍼노바의 현 교주입니다."
            hide ak
            show me
            c "(슈퍼노바....라면, 클린스타클의 3개 종교 중 하나였지.)"
            c "(이 애가 슈퍼노바의 현 교주?)"
            c "(교주라는 직책을 맡기엔 되게 어려보이는데..)"
            hide me
            show ak std
            l1 "그래서, 당신은 누구시죠?"
            hide ak
            show me
            c "저는.."
            c "저는 [name]입니다."
            hide me
            show ak std
            l1 "[name]님이시군요."
            l1 "혹시, 어디 소속인지 여쭤봐도 괜찮을까요?"
            hide ak
            show me
            c "(마땅히 지어낼만한 신분이 안 떠올라..)"
            c "(이 나라 체계를 하나도 모르는데 어떻게 해!!)"
            c "(그냥 사실대로 말하는 편이 나으려나...)"
            c "그..... 저는....."
            c "사실 이쪽 세계 출신이 아니에요."
            hide me
            show ak awk
            l1 "네..?"
            l1 "그게 무슨 말씀이신가요."
            show ak mad
            l1 "명확한 신분을 밝히지 않으시면 \n법적으로 문제가 될 수 있습니다, [name]님."
            hide ak
            show me
            c "(먹힐 리가 없지!!!)" with vpunch
            c "(망했다!!!!!!)" with vpunch
            c "(일단 화제를 급하게 돌려보자.)"


    c "그, 그보다! 곧 이 나라에 큰 위험이 도래할거라면서요!"
    hide me
    show ak wow
    l1 "!" with vpunch
    l1 "그걸 어떻게..?"
    show ak awk
    l1 "그 사안은 극비리에 부쳐졌을텐데...\n어떻게 민간인이 알고 있는거죠?"
    show ak mad
    l1 "하여간에 공무원들 일처리 꼬라지 하고는.."
    hide ak
    show me
    c "갑자기 공무원들을 깐다고..?" 
    c "아무튼, 그쪽 말대로 일반인이라면 모를 정보를 알고 있는데."
    c "제가 이쪽 세계 사람이 아니란 증거 아니겠어요?"
    hide me
    show ak eh
    l1 "아니.. 그 정도 가지고는..."
    l1 "정부 쪽 인맥이 있는 분이라면 전해 들었을 수도 있겠죠."
    show ak awk
    l1 "뭣보다, 바깥 세계 출신이라는 얘기를 어떻게 믿겠습니까."
    l1 "암만 여기가 종교 국가라지만.."
    hide ak
    show me
    c "종언서."
    hide me
    show ak wow
    l1 "?!" with vpunch
    hide ak
    show me
    c "전 종언서의 존재를 알고 있어요."
    c "지금 클린스타클에 비상사태가 선포된 이유가 그것 때문, 아닌가요?"
    hide me
    show ak wow
    l1 "정말... 모든 걸 알고 있어..?"
    hide ak
    show me
    c "저는 이 세계를 구하러 모든 정보를 듣고 파견되었어요."
    c "전적으로 클린스타클을 도우러요."
    hide me
    show ak awk
    l1 "설마.."
    l1 "창세기에 나와있는 구원자가..?"
    hide ak
    show me
    c "(구원자..?)"
    hide me
    show god
    g "(아아, 용사님! 들리세요??)"
    hide god
    show me
    c "!!!!" with vpunch
    hide me
    show god
    g "(머릿속으로 대답하시면 됩니다.)"
    hide god
    show me
    c "(아, 통신한다고 했었지.)"
    c "(깜짝 놀랐네..)"
    hide me
    show god
    g "(전송 채널 설정을 잘못 해서 한박자 늦게 연락이 닿았네요.)"
    g "(생각해보니 아까 설명을 안 해드린 부분이 있더라고요.)"
    g "('창세기'라는 예언서가 있습니다.)"
    g "(이는 제가 클린스타클에 실제로 내린 예언서 중 하나죠.)"
    g "(그리고 창세기에는 구원자라는 존재가 등장합니다.)"
    g "(클린스타클이 위기에 빠졌을 때.. \n클린스타클을 구원해줄 용사의 명칭이죠.)"
    g "(사실 제가 보험의 느낌으로 넣어둔 \n데우스 엑스 마키나같은 존재지만요...)"
    hide god
    show me
    c "(...어째 얘기하는 게..)"
    hide me
    show god
    g "(네. 바로 용사님이 그 구원자가 맞습니다.)"
    g "(제가 용사님을 불러들인 또다른 이유기도 하지요.)"
    g "(클린스타클 국민들 모두가\n구원자의 존재를 안다고 할 수는 없지만..)"
    g "(혹시 이를 아는 사람을 만난다면, \n용사님의 신분을 납득시킬 때 큰 도움이 될 겁니다.)"
    g "(그럼 조만간 다시 연락드리겠습니다..)"
    hide god
    show me
    c "(잠깐, 이거 단방향으로만 가능한거야?)"
    hide me
    show god
    g "(아쉽게도 그렇습니다.)"
    g "(필멸자가 신에게 연락을 취한다는 건 상정 자체를 안해봐서요.)"
    hide god
    show me
    c "(......그래라.)"
    hide me
    show ak eh
    l1 "..저기, [name]님?"
    hide ak
    show me
    c "!"
    c "예, 아크룩스님."
    hide me
    show ak eh
    l1 "일단 집무국으로 가시죠."
    l1 "지금 머릿속이 굉장히 혼란스럽습니다만..."
    hide ak
    show me
    c "믿어주시는 건가요?"
    hide me
    show ak std
    l1 "아직은요."
    l1 "확인해봐야 할 게 있습니다."
    hide ak
    show me
    c "네.."
    hide me
return

label forest2:
    show me
    c "좋아. 가운데 길로 쭉 가보자."
    hide me
    "그렇게 몇 분이 더 흘렀다."
    show me
    c "........."
    c "숲 말고는 아무것도 안 보여."
    c "여긴 대체 어디지..."
    c "길을 잃었나보다......"
    hide me
    "거기, 누구?"
    show me
    c "!" with vpunch
    hide me
    show po std
    l2 "잉? 당신은 누구야??"
    l2 "여기는 아무나 들어올 수 있는 곳이 아닌데~"
    hide po
    show me
    c "아.. 그게... 나는.. "
    hide me
    menu:
        "나는...."

        "이 나라를 구하기 위해 온 [name] 용사야!":
            show po ang
            l2 "잉?"
            show po sad
            l2 "응.. 글쿠나.."
            hide po
            show me
            c "뭐야 그 반응.."
            hide me
            show po hmm
            l2 "그야.."
            l2 "유치원생이나 할법한 말을 해놓고..\n어떤 반응을 원하는거야..."
            hide po
            show me
            c "..."
            c "무덤덤하게 팩트로 때리다니.."
            c "그보다, 너는 누구야?"
            hide me
            show po std
            l2 "음, 나?"
            l2 "응.. 그러네!\n아직 모를만도 하겠구나~"
            l2 "나는 폴라리스!"
            l2 "이클립스의 대장, 다시말해 교주야!"
            hide po
            show me
            c "?!" with vpunch
            c "(이클립스...면 이 나라의 교단 중 하나잖아?)"
            c "(이 애가.. 이클립스의 교주라고?)"
            c "(나이도 그다지 많지 않아 보이는데..)"
            c "네가.. 교주?"
            hide me
            show po haha
            l2 "응!"
            show po std
            l2 "원래 세 달 전까지만 해도\n아빠가 교주셨는데.."
            l2 "최근들어 많이 편찮으셔서,\n 유일한 직계 가족인 내가 교주가 됐어."
            l2 "어차피 일 대부분은 교회 어르신들이 \n도와주고 계시지만~ 헤헤.."
            hide po
            show me
            c "(일종의 대리청정인건가..\n역시 완전한 교주까지는 아니였구나.)"
            c "그렇구나."
            hide me
            show po hmm
            l2 "그보다~"
            l2 "여기서 뭘 하고 있던거야?"
            l2 "모르는 사람이 이유없이 들어오면...\n조사국? 심문국?로 보내라고 어르신들이 그랬는데.."
            hide po
            show me
            c "응?! 조사국??" with vpunch
            c "그게 무슨 소리야?"
            hide me

            
            

        "너부터 누군지 먼저 밝혀라!":
            show po ang
            l2 "앗! 그렇네!"
            show po std
            l2 "나는 폴라리스!"
            l2 "이클립스의 대장, 다시말해 교주야!"
            hide po
            show me
            c "?!" with vpunch
            c "(이클립스라면.. 이 나라의 2교단.)"
            c "(이렇게 어린 애가.. 이클립스의 교주라고?)"
            c "(잘해봐야 중학생 쯤 돼보이는데..)"
            c "교주... 라고?"
            hide me
            show po std
            l2 "아하! 아직 모를만도 하겠구나~"
            l2 "원래 세 달 전까지만 해도\n아빠가 교주를 맡고 있었는데.."
            show po sad
            l2 "최근들어 많이 편찮으셔서..\n유일한 직계 가족인 내가 교주가 됐어."
            l2 "물론 대부분의 일들은 어르신들이 도와주셔서\n내가 하는 일은 많지 않지만..."
            hide po
            show me
            c "그렇군.. 너는 일종의 바지사장 역할인건가.."
            hide me
            show po std
            l2 "바지사장? 이클립스는 바지같은건 안 팔아~"
            hide po
            show me
            c "아니.. 그런 뜻이 아니라.."
            hide me
            show po std
            l2 "근데 그래서~ 이름은 뭐야??"
            hide po
            show me
            c "아, 정작 내 이름을 얘기 안했구나."
            c "나는 [name]."
            c "이 세계를 구하러...\n다른 세계에서 넘어왔어."
            hide me
            show po std
            l2 "아하~ [name] 씨구나. 만나서 반가워!"
            show po hmm
            l2 "그나저나.. 다른 세계??? 으음..."
            l2 "그런건 내 친구들도 안 믿는데..."
            show po ang
            l2 "혹시 보기보다 어린거야??"
            hide po
            show me
            c "컥!"
            c "당연히 믿을거라고 생각은 안했다만...\n생각보다 더 아픈 취급이네.."
            hide me
            show po wow 
            l2 "앗! 맞아!"
            show po hmm
            l2 "모르는 사람이 아무 이유없이 들어오면..."
            l2 "조사국? 심문국? 로 보내라고 어르신들이 그랬는데.."
            hide po
            show me
            c "뭐?!" with vpunch
            c "(이런 건 얘기에 없었잖아, 신 이양반아!!!!!!!!)"
            c "그게 무슨 소리야?"
            hide me

    show po hmm
    l2 "나도 가본 적이 없어서 잘은 모르겠지만.."
    l2 "일종의 경찰서 같은 거랄까?"
    l2 "가서 조사같은 걸 받고.. \n문제가 된다면 잡혀갈 수도 있겠지??"
    hide po
    show me
    c "!!!!" with vpunch
    c "(시작부터 위기다!)"
    c "(여기서 끌려간다면 무조건 구속될거야..!)"
    hide me
    show po std
    l2 "그럼 일단 그쪽으로 가볼ㄲ.."
    hide po
    show me
    c "잠깐!!!" with vpunch
    hide me
    show po ang
    l2 "에??"
    hide po
    show me
    c "합당한 이유가 있으면 된다고 했지?!"
    c "이 나라에 큰 재앙이 닥칠거라면서?"
    hide me
    show po wow
    l2 "엇?!"
    l2 "[name] 씨가 그걸 어떻게 알아??"
    l2 "이건 엄청 중요한 비밀이라고 어르신들이 신신당부했는데.."
    hide po
    show me
    c "그게 바로 내가 바깥에서 왔다는 증거야."
    c "나는.. 종언서의 존재를 알고 있어."
    hide me
    show po wow
    l2 "!!!!" with vpunch
    hide po
    show me
    c "종언서에서 1주일쯤 뒤에 이 나라에 \n큰 위기가 올거라고 했다면서."
    c "나는 그걸 막으려고 여기 온거야. 정말로."
    c "(..이렇게 다 질러봐도 되는걸까?!)"
    c "(모르겠다.. 안 먹히면 신 그 양반이\n어떻게든 처리해주겠지..)"
    hide me
    show po hmm
    l2 "...."
    l2 "........."
    hide po
    show me
    c "(제기랄.. 안 통하는건가..)"
    c "저.."
    hide me
    show po ang
    l2 "뭐라는지 잘 모르겠어!!" with vpunch
    hide po
    show me
    c "엥?!" with vpunch
    hide me
    show po std
    l2 "종언서라는 성서가 있는 건 맞는데~"
    l2 "아직 제대로 내용을 본 건 아니거든.."
    hide po
    show me
    c "아직 내용을 안 봤다고?!" with vpunch
    c "너 교주라며?!"
    c "교주가 나라의 재앙에 관한 사안을 모른다니?!"
    hide me
    show po wow
    l2 "잠깐!!!!" with vpunch
    show po sad
    l2 "나도 내 잘못인 건 알아!! 하지만.."
    show po hmm
    l2 "처리할 일이 너무 많더라고!!\n업무를 넘겨받은 지 얼마 안 돼서.. 헤헤"
    l2 "그래서 그런 세세한 것들은\n어르신들이 대부분 도맡아 하셨거든.."
    l2 "난 우리 나라가 1주일 뒤면 큰일이 난다고만 들었어."
    hide po
    show me
    c "..."
    c "(나이가 너무 어리다 싶었는데..)"
    c "(어지간한 중요 사안들은 전부 배제당하고 있었구만..)"
    c "그럼.. 어떡할거지?"
    hide me
    show po hmm
    l2 "음.."
    show po std
    l2 "그러면.. 일단 집무국으로 가볼까?"
    hide po
    show me
    c "집무국?"
    hide me
    show po std
    l2 "응. 거기에 왕 똑똑한 언니가 있거든."
    show po hmm
    l2 "재수는 좀 없지만...."
    hide po
    show me
    c "재수..?"
    hide me
    show po ang
    l2 "앗! 아니야!" with vpunch
    show po std
    l2 "암튼 일단 그 언니한테 가서 물어보자구."
    hide po
    show me
    c "어째 영 못 미더운데.."
    c "일단 알았어."
    hide me
return

label forest3:
    show me
    c "흠, 오른쪽으로 가볼까?"
    hide me
    "그렇게 몇 분이 더 흘렀다..."
    show me
    c ".........."
    c "..............."
    c "아무래도.... 길을 잃은 것 같다."
    c "여긴 어디지...?"
    hide me
    "거기, 누구?"
    show me
    c "!" with vpunch
    hide me
    show cl std
    l3 "어라, 처음 뵙는 얼굴이네요."
    l3 "이 쪽은 일반인이 출입할 수 없는 구역이에요."
    show cl hmm
    l3 "길을 잃으신건가요?"
    hide cl
    show me
    c "아.. 그게... 저는.."
    hide me
    menu:
        "저는...."
        
        "이 나라를 구하기 위해 온 용사 [name]입니다.":
            show cl awkmoo
            l3 "..."
            show cl awk
            l3 "아하!"
            l3 "용사님이시군요~"
            hide cl
            show me
            c "믿어주시는건가요?"
            hide me
            show cl hmm
            l3 "음.."
            show cl awk
            l3 "진심이셨나요?"
            hide cl
            show me
            c "..."
            c "그....어느정도는요.."
            hide me
            show cl awkmoo
            l3 "일단은.. 알겠습니다."
            show cl moo
            l3 "그보다, 이 곳에 계시면 안돼요."
            l3 "방금 말씀드렸듯이 이곳은 정부 관할구역이거든요."
            hide cl
            show me
            c "(하필이면 이런 곳으로 워프를 시키냐!!!)"
            c "아하.. 몰랐어요, 죄송합니다."
            hide me
            show cl std
            l3 "죄송할 것 까지야~"
            l3 "제가 나가는 길을 알려드릴게요."
            hide cl
            show me
            c "감사합니다.. 그보다,"
            c "그 쪽은 누구시죠?"
            hide me
            show cl awk
            l3 "어머."
            l3 "저를 모르시는 건가요?"
            l3 "혹시 TV나 뉴스에서 몇번 보이지 않았던가요?"
            hide cl
            show me
            c "(뭐야? 이 사람, 유명인사였나?)"
            c "아... 그게..."
            c "저희 집에 TV가 없어서요.."
            hide me
            show cl awk
            l3 "앗."
            l3 "죄송합니다..\n 그런 가능성을 염두해두지 않았군요."
            show cl std
            l3 "저는 클라우드라고 합니다."
            l3 "아스트라의 현 주교죠."
            hide cl
            show me
            c "?!" with vpunch
            c "(아스트라라면.. 이 나라의 3교단이였지.)"
            c "(이 사람이 아스트라의 수장?!)"
            c "(한 종교의 수장치고는 좀 젊어보이는데..)"
            c "아스트라의.. 교주시라고요?"
            c "클린스타클의 3교단인?"
            hide me
            show cl std
            l3 "네."
            show cl awk
            l3 "아무래도 3교단인만큼 \n인지도는 조금 부족한가 보군요."
            hide cl
            show me
            c "(왠지 상처를 줘버린 것 같다..)"
            hide me
            show cl moo
            l3 "그런데 [name]님."
            hide cl
            show me
            c "네?"
            hide me
            show cl moo
            l3 "어떻게 이곳 안까지 오신거죠?"
            l3 "이 곳은 정부 관할 지역 중에서도\n제일 깊숙한 곳인데.."
            l3 "개인이 오고싶다고 올 수 있는 곳이 아닌데.."
            hide cl
            

        "네.. 길을 잃었습니다. 여긴 어디죠?":
            show cl hmm
            l3 "어머, 역시 그러셨군요."
            l3 "여긴 정부 관할구역이에요."
            show cl std
            l3 "나가시는 길을 알려드리겠습니다."
            hide cl
            show me
            c "감사합니다!"
            c "아니.. 이게 아니지."
            c "저는 [name]이라고 합니다."
            c "혹시 그쪽은 누구시죠?"
            hide me
            show cl awk
            l3 "갑자기 통성명을?"
            l3 "그보다, 저를 모르시는건가요?"
            hide cl
            show me
            c "...?"
            c "(이곳에서 유명한 사람인가?)"
            c "혹시, 누구신지 여쭤보면 실례일까요?"
            hide me
            show cl awkmoo
            l3 "음...."
            show cl awk
            l3 "네, 뭐.. 모를 수도 있겠군요."
            show cl std
            l3 "저는 클라우드라고 합니다."
            l3 "아스트라의 현 주교죠."
            hide cl
            show me
            c "!!!!"
            c "(아스트라의 주교?!)"
            c "(아스트라라면 이 세계의 3교단 중 하나잖아?!)"
            c "(너무 젊어서 주교일거라고는 상상도 못했어..)"
            hide me
            show cl awk
            l3 "뭔가 이제야 알아보시는 눈치네요.."
            l3 "아스트라의 인지도의 현주소를 알게 해주셨어요.\n감사합니다.."
            hide cl
            show me
            c "아.. 아니요.. 이건 제가 특수한거라.."
            c "그런데 여기가 정부 관할 구역이라고요?"
            hide me
            show cl std
            l3 "네. 맞아요."
            l3 "아시다시피 '스플릿시' 유적지는 인체에 유해한 성분이 나오거든요."
            l3 "그래서 출입 자체가 금지되어 있습니다."
            show cl moo
            l3 "그래서 말인데.."
            l3 "어떻게 이 곳까지 오신거죠?"
            l3 "유적지 입구는 철저하게 지켜지고 있을텐데.."
            hide cl

    show me
    c "!" with vpunch
    c "(여기가 그런 장소였던 건가..)"
    hide me
    show cl dead
    l3 "혹시 [name]님.. \n떳떳하지 못한 일을 벌이시고 계셨나요?"
    l3 "잠깐 신원확인이 필요할 것 같군요.."
    hide cl
    show me
    c "(제기랄. 의심받기 시작했다..)"
    c "(뭐라고 둘러대야 하지?)"
    c "(신원확인이 되지 않는다면..\n활동에 제약이 생길거야.)"
    hide me
    show god
    g "(똑똑.)"
    hide god
    show me
    c "!!!!" with vpunch
    c "(뭐, 뭐야?!)"
    hide me
    show god
    g "(신입니다, 용사님.)"
    g "(통신으로 도움을 드린다고 했었죠?\n그래서 연락드렸습니다.)"
    show me
    hide god
    c "(통신이란 게.. 내 머릿속에서 \n환청이 들리는 방식이였던거냐..)"
    hide me
    show god
    g "(거두절미하고, 본론부터 말씀드리자면..)"
    g "(제가 아까 미처 설명해드리지 못한 부분이 있었습니다.)"
    show me
    hide god
    c "(그게 뭐지?)"
    hide me
    show god
    g "('창세기'라는 예언서가 있습니다.)"
    g "(이는 제가 클린스타클에 실제로 내린 예언서 중 하나죠.)"
    g "(그리고 창세기에는 '구원자'라는 존재가 등장합니다.)"
    g "(구원자는, 클린스타클이 위기에 빠졌을 때.. \n클린스타클을 구원해줄 용사의 명칭이죠.)"
    g "(사실 제가 보험의 느낌으로 넣어둔 \n데우스 엑스 마키나같은 존재지만요...)"
    show me
    hide god
    c "(...어째 얘기하는 게..)"
    hide me
    show god
    g "(네. 바로 용사님이 그 구원자가 맞습니다.)"
    g "(제가 용사님을 불러들인 또다른 이유기도 하지요.)"
    g "(클린스타클 국민들 모두가\n구원자의 존재를 안다고 할 수는 없지만..)"
    g "(혹시 이를 아는 사람을 만난다면, \n용사님의 신분을 납득시킬 때 큰 도움이 될 겁니다.)"
    g "(일단 급한 내용은 전달드렸으니..)"
    g "(조만간 다시 연락드리겠습니다. 그럼.)"
    show me
    hide god
    c "(...)"
    c "(원래는 조용히 활동하려고 했는데..)"
    c "(상황이 상황이니만큼, 사실대로 말해봐야겠군.)"
    hide me
    show cl moo
    l3 "[name]님? 잠깐 이쪽으로 오시겠어요?"
    show me
    hide cl
    c "..그.."
    c "저는 '구원자'에요."
    c "창세기에 나오는.. 그 구원자요."
    hide me
    show cl awk
    l3 "네?"
    l3 "갑자기 그게 무슨 말씀이시죠?"
    show cl awkmoo
    l3 "그보다도 그걸 어떻게.."
    show me
    hide cl
    c "1주일."
    c "1주일 뒤면.. 여기에 큰 재앙이 닥치죠?"
    c "에크모트라는 괴물이.. 부활하잖아요."
    hide me
    show cl hmm
    l3 "!!!" with vpunch
    l3 "그 것도 알고 계셨던 건가요??"
    show cl awk
    l3 "아.. 아하, 이제 알았다."
    l3 "[name]님 사실은 정부의 고위 관계자셨던 거죠?"
    l3 "저 조차 신원을 알 지 못할 정도로 높은 위치의.."
    show me
    hide cl
    c "아니요."
    c "저는 분명 오늘 이 나라에 처음 왔습니다."
    hide me
    show cl awkmoo
    l3 "하지만.. 그게 아니라면.."
    l3 "대체 그런 1급 기밀들을 어떻게.."
    l3 "잠깐만요, 너무 혼란스럽네요."
    l3 "분명 구원자라는 개념을 성서에서 보기는 했지만.."
    l3 "이렇게 갑작스럽게 나타나실 줄은.."
    show me
    hide cl
    c "제가 어떻게 하면 신뢰를 드릴 수 있을까요?"
    hide me
    show cl awkmoo
    l3 "...."
    show cl hmm
    l3 "아!"
    show cl std
    l3 "일단 집무국으로 가시죠."
    l3 "그 곳이라면.. 검증할 수 있을 것 같아요."
    hide cl
return

label meeting:
    show me
    c "오늘은 정기 회의를 소집하겠습니다."
    c "모두의 정보를 종합해서 앞으로의 방향성을 정하겠습니다."
    hide me
    show cl std
    l3 "좋아요~"
    hide cl
    show ak std
    l1 "그동안 수집했던 정보들을 공유해드리겠습니다."
    hide ak
    show po std
    l2 "내가 알아낸 것들도 알려줄게~"
    hide po
    "그렇게 회의를 진행했다."
    $ analysis += 20
    $ count += 1
    "정기 회의를 했습니다."
return

label pray:
    show me
    c "오늘은 정기 예배를 진행하겠습니다."
    if (yebecount == 0):
        c "그런데 생각해보니..."
        c "세 종교가 진행방식을 공유하는 건가요?"
        c "제가 살던 세계에서는 다른 종교끼리는\n진행하는 방식이 달랐거든요."
        hide me
        show cl std
        l3 "아. 그 점이라면 걱정하지 않으셔도 돼요~"
        hide cl
        show ak std
        l1 "저희 세 종교는 사실 같은 뿌리로부터 나옵니다."
        hide ak
        show po std
        l2 "그래서 큰 흐름은 비슷하고~\nr각자 속으로 기도하는 세부적인 부분만 좀 달라!"
        hide po
        show ak hmm
        l1 "어차피 주기도문은 교주인 저희가 외울테니 \n크게 걱정하지 않으셔도 됩니다."
        hide ak
        show me
        c "아하. 그럼 진행이 편하겠군요."
        c "그럼 옆에서 지켜보고 있겠습니다.."
        hide me
        show ak std
        l1 "기도문은 제가 외우겠습니다."
        hide ak
        show po sad
        l2 "(따분해...)"
        hide po
        show cl awk
        l3 "속마음이 다 보여, 폴라리스."
        hide cl
        show ak std
        l1 "우주에 계신 아버지의 이름이 빛나실지어다."
        l1 "전지전능하신 아버지, 모든 우주의 영광을 받으실지어다."
        hide ak
        show po hmm
        l2 "레나폰트."
        hide po
        show cl std
        l3 "레나폰트."
        hide cl
        show me
        c "(레나폰트가 아멘과 같은 느낌인가 보네..)"
        c "레나폰트."
        hide me
        "(그렇게 예배가 진행되었다.)"
        $ yebecount = 1
    elif (yebecount == 1):
        c "그럼 바로 진행하죠."
        c "우주에 계신 아버지의 이름이 빛나실지어다."
        c "전지전능하신 아버지, 모든 우주의 영광을 받으실지어다."
        hide me
        show po wow
        l2 "헉! 그걸 다 외운거야?! \n나도 아직 다 못 외웠는데~" with vpunch
        hide po
        show ak eh
        l1 "교주씩이나 돼서 자랑이다.."
        show ak ha
        l1 "[name]님, 정말 기억력이 대단하시군요."
        hide ak
        show cl haha
        l3 "그러게요~ 앞으로의 진행을 맡겨도 되겠어요~"
        hide cl
        show me
        c "하하... 감사합니다.."
        c "(사실은...)"
        hide me
        show god
        g "(제가 머릿속에서 도와드리고 있지만요~)"
        hide god
        show me
        c "(그러하다.)"
        c "(뭐 보여지는 그림만 좋으면 됐지..)"
        c "그럼, 레나폰트."
        hide me
        show ak ha
        l1 "레나폰트."
        hide ak
        show po std
        l2 "레나폰트!"
        hide po
        show cl std
        l3 "레나폰트~"
        hide cl
        "(그렇게 예배가 진행되었다.)"
        $ yebecount = 2
    else:
        show me
        c "그럼 바로 진행하겠습니다."
        c "우주에 계신 아버지의 이름이 빛나실지어다..."
        hide me
        hide me
        show ak ha
        l1 "레나폰트."
        hide ak
        show po std
        l2 "레나폰트!"
        hide po
        show cl std
        l3 "레나폰트~"
        hide cl
        "(그렇게 예배가 진행되었다.)"

    $ supernovapower += 10
    $ eclipsepower += 10
    $ astrapower += 10
    $ count += 1
    "정기 예배를 했습니다."
return

label temple1:
    scene background_ruin with dissolve
    play music "audio/ruin.mp3" fadein 2.0 loop
    if (temcount == 0):
        show ak hmm
        l1 "흠."
        l1 "유적지에 직접적으로 오는 것은 처음이군요."
        hide ak
        show me
        c "어라, 그러신가요?"
        c "당연히 와 보신 곳일줄 알았어요."
        hide me
        show ak std
        l1 "네. 이곳의 정식 명칭은 스플릿시."
        l1 "클린스타클이 건국되기 훨씬 이전부터 있던 유적지입니다."
        l1 "이 곳에 에크모트의 봉인이\n위치해있다고 전해지기도 하고요."
        show ak mad
        l1 "최근들어 매우 유독한 기운이\n중심지로부터 계속해서 나오고 있습니다."
        l1 "부활이 임박한 탓인지.. 봉인이 약해진 것 때문인 듯 하고요."
        hide ak
        show me
        c "!!" with vpunch
        c "에크모트의 봉인이요?!"
        hide me
        show ak hmm
        l1 "네. 모르셨군요."
        show ak std
        l1 "종언서에 그렇게 서술된 구절이 있습니다."
        l1 "사실 종언서 자체가 발견된 지 얼마 되지도 않았고.."
        l1 "저희도 종언서를 지속적으로 해독중인지라\n확실한 내용은 아닙니다만,"
        l1 "개인적으로 이 강력한 기운은 \n그게 아니라면 설명이 안 된다고 생각합니다."
        hide ak
        show me
        c "(종언서에 그렇게 적혀있었다?)"
        c "(뭔가 석연치 않은데..)"
        c "(왜 하필 이곳이여야 했던 거지?)"
        c "유독한 기운이라.."
        c "노출되면 분명히 좋지 않은 영향을 미치겠죠?"
        c "외곽만 빠르게 조사하고 돌아가야겠군요.."
        hide me
        show ak std
        l1 "그러도록 하죠."
        l1 "뭐, 장기간 노출되지만 않는다면 별 문제 없을겁니다."
        hide ak
        $ temcount = 1
        $ persistent.temcount1 = 1
    else:
        show ak std
        l1 "이번에도 유적지 조사입니까."
        hide ak
        show me
        c "그렇게 됐습니다.."
        c "위험한 곳에 가게 해서 죄송합니다.."
        hide me
        show ak hmm
        l1 "앗, 아뇨."
        l1 "딱히 싫다는 뜻은 아니였습니다."
        show ak std
        l1 "뭐든 하려면 제대로 해야죠."
        hide ak
        show me
        c "그렇다면 다행이네요..."
        c "이번에는 뭔가 알아낼 수 있었으면 좋겠어요."
        hide me
        show ak ha
        l1 "저 역시 그렇습니다."
        hide ak
    $ reason1 -= 20
    $ analysis += 30
    $ count += 1
    stop music
    "유적지를 탐사했습니다."
return

label temple2:
    scene background_ruin with dissolve
    play music "audio/ruin.mp3" fadein 2.0 loop
    if (temcount == 0):
        show po std
        l2 "오, 여긴 처음 와보는걸?"
        l2 "스플릿시 유적지~"
        hide po
        show me
        c "여기 이름이 스플릿시구나.."
        c "그보다도, 여긴 처음 와본거야?"
        hide me
        show po std
        l2 "응!"
        show po hmm
        l2 "일단 우리 마을에서 굉장히 먼 곳이기도 하고.."
        l2 "뭣보다도 엄청 위험한 곳이다 보니~\n어르신들이 절대 안 데리고 다녔거든."
        hide po
        show me
        c "엄청 위험하다니..?"
        c "여기 평범한 유적지 같은게 아니였던 거야?"
        hide me
        show po std
        l2 "아, 모든 걸 다 아는건 아니였구나. 오빠?"
        l2 "여긴 종언서에서 에크모트의 봉인이\n위치해있다고 전해진 곳이야."
        l2 "오빠가 막으려고 온 그거~"
        hide po
        show me
        c "!!" with vpunch
        c "뭐, 뭐야!! 그런 곳이였어?!"
        hide me
        show po haha
        l2 "아하핫! 사실 우리도\n종언서에 그렇게 나와있어서 최근에 안 사실이야."
        l2 "원래는 그냥 옛~날부터 있었던 유적지, \n그 이상 그 이하도 아니였다구."
        hide po
        show me
        c "(종언서에 그렇게 적혀있었다?)"
        c "(뭔가 석연치 않은데..)"
        c "(왜 하필 이곳이여야 했던 거지?)"
        c "그렇군.."
        hide me
        show po hmm
        l2 "어쨌거나~ 그런 괴물이 묻혀있는 곳이라 그런지,"
        l2 "여기 공기, 얼마 전부터 엄청나게 독해졌다구."
        l2 "진짜 조만간 부활하려나 봐~"
        l2 "오래 있는 건 그다지 추천되지 않는다네~"
        l2 "물론 여긴 바깥쪽이라 그나마 괜찮겠지만 말이야."
        hide po
        show me
        c "....."
        c "빨리 둘러보고 나가자."
        hide me
        show po haha
        l2 "아학ㅋㅋㅋ 쫄은 거야, 오빠?"
        c "시끄러!" with vpunch
        $ temcount = 1
        $ persistent.temcount1 = 1
    else:
        show po std
        l2 "이번 외출은 유적지 탐사인가~"
        hide po
        show me
        c "으응.."
        hide me
        show po std
        l2 "밖으로 돌아다니는 건 항상 좋더라~"
        hide po
        show me
        c "이런 곳인데도 괜찮은 거냐.."
        hide me
        show po haha
        l2 "당연히 여긴 썩 좋은 곳은 아니지만~ 헤헤."
        hide po
        show me
        c "...."
        c "(어린 애인데 위험한 곳에 데리고 다니는 게 미안하네..)"
        c "(빠르게 둘러보고 가자.)"
        hide me
    $ reason2 -= 20
    $ analysis += 30
    $ count += 1
    stop music
    "유적지를 탐사했습니다."
return

label temple3:
    scene background_ruin with dissolve
    play music "audio/ruin.mp3" fadein 2.0 loop
    if (temcount == 0):
        show cl hmm
        l3 "여길 직접 오는 건 처음이네요~"
        hide cl
        show me
        c "어? 처음 와보셨군요?"
        hide me
        show cl std
        l3 "네. 아무래도 교주들이 직접 올 곳은 아니다 보니까요~"
        hide cl
        show me
        c "직접 올 곳이 아니라니.."
        c "뭔가 대단한 곳인가요?"
        hide me
        show cl hmm
        l3 "아, [name]님도 모르셨나 보네요?"
        l3 "여긴 에크모트의 봉인이 위치해있다고 전해지는.."
        l3 "스플릿시 유적지거든요."
        show cl std
        l3 "종언서에도 나와있어요~"
        hide cl
        show me
        c "!" with vpunch
        c "에크모트의 봉인이요?!"
        hide me
        show cl moo
        l3 "네에. 그래서 엄청 위험한 곳이죠."
        l3 "사실 저희도 그 사실 자체는 종언서 덕분에 알았어요."
        l3 "그게 아니였다면 그저 어느 나라에나 있는\n평범한 유적지 정도로 생각했겠죠?"
        hide cl
        show me
        c "(종언서에 그렇게 적혀있었다?)"
        c "(뭔가 석연치 않은데..)"
        c "(왜 하필 이곳이여야 했던 거지?)"
        c "그렇네요."
        hide me
        show cl moo
        l3 "이렇게 외곽을 보는 것 정도는 괜찮겠지만.."
        l3 "심층부에는 뭐가 있을지 그 누구도 모른다네요~"
        l3 "최근들어 실제로 위험한 기운이\n뿜어져 나오고 있다고도 하구요."
        l3 "아마 에크모트의 봉인이 약해진 탓이겠죠?"
        hide cl
        show me
        c "....."
        c "갑자기.. 오한이.."
        c "빠르게 둘러보고 갈까요..?"
        hide me
        show cl haha
        l3 "아하하. 네, 그러죠."
        show cl std
        l3 "너무 걱정하지는 마세요."
        l3 "여기 잠깐 있는다고 크게 영향을 미치진 않을거에요."
        hide cl
        $ temcount = 1
        $ persistent.temcount1 = 1
    else:
        show cl std
        l3 "이번에는 유적지로 오는군요~"
        hide cl
        show me
        c "넵."
        c "그렇게 됐습니다.."
        c "신속하게 탐사하고 오죠."
        hide me
        show cl doki
        l3 "어머, 듬직해지셨네요."
        show cl haha
        l3 "좋아요~"
        hide cl
    $ reason3 -= 20
    $ analysis += 30
    $ count += 1
    stop music
    "유적지를 탐사했습니다."
return

label sun:
    show me
    c "오늘의 오후 활동은 태양 관측입니다."
    hide me
    show ak std
    l1 "제가 동행해야겠군요."
    hide ak
    stop music
    scene background_sun with dissolve
    play music "audio/sun.mp3" loop fadein 2.0
    if (suncount == 0):
        show ak std
        l1 "바로 이곳입니다."
        l1 "이 언덕이 이 근방에서 가장 해가 잘 드는 언덕입니다."
        l1 "슈퍼노바에서는 이곳을 해가 우는 언덕이라고 불러요."
        show ak ha
        l1 "종교 행사 때 슈퍼노바의 신도들과 자주 오고는 했죠."
        show ak hmm
        l1 "그런데 이 곳으로 온 특별한 이유가 있는 건가요?"
        hide ak
        show me
        c "음."
        c "(당연히 없지!!!!)" with vpunch
        c "(애당초 재앙은 조작된 사실이니까 안 막아도 되니까!!!!!)"
        c "(이렇게 한 명씩 직접 함께 다녀보면서 \n의심스러운 부분이 있는지 판단하는 게 진짜 이유다..)"
        c "사실 별다른 이유는 없습니다..."
        c "혹시 태양을 관측하면 뭔가 단서가 있지 않을까? 해서.."
        hide me
        show ak wow
        l1 "....."
        show ak eh
        l1 "첫 만남때도 그랬지만, 굉장히 특이한 성격이시군요.."
        show ak std
        l1 "그래도 뭐, 아예 허무맹랑한 말은 아니네요."
        l1 "클린스타클의 종교들은 천문에서 비롯된 종교인 만큼.."
        l1 "천문 활동이 종교 활동과도 관련하는 부분이 있거든요."
        l1 "이런 종교 활동을 조금이라도 더 열심히 하다 보면,"
        show ak ha
        l1 "신께서 응답하실 가능성이 있지 않을까요?"
        hide ak
        show me
        c "(뭐.. 틀린 말은 아니네.)"
        c "(신이 존재하기는 하니까...)"
        c "바로 그 태도입니다!!"
        c "그럼, 시작해볼까요."
        hide me
        show ak ha
        l1 "네."
        hide ak
        $ suncount = 1
        stop music
    elif (suncount == 1):
        show ak std
        l1 "또 오는군요."
        l1 "사실 재앙까지의 시간이 촉박합니다만은.."
        l1 "이제와서 뾰족한 수가 있는 것도 아니고."
        l1 "결국 종교적인 부분에 의지할 수 밖에 없는 것 같네요."
        show ak ha
        l1 "훗."
        hide ak
        show me
        c "갑자기 웃음을?"
        hide me
        show ak std
        l1 "갑자기 든 생각입니다만.."
        l1 "조금 웃기지 않나요."
        hide ak
        show me
        c "어떤 부분이?"
        hide me
        show ak std
        l1 "우리 클린스타클은.. \n분명 과학적으로 뛰어난 국가에요."
        l1 "그런 나라가 동시에 종교에도 매몰되어 있다는 점이.."
        show ak sad
        l1 "조금은 이상한 것 같아서요."
        l1 "어떨때는 이게 족쇄의 역할을 하는 것 같기도 하고요."
        l1 "만약 우리가 종교와 관련이 없었더라면.."
        l1 "이 상황에 좀 더 유연하게 대처할 수 있지 않았을까요?"
        l1 "어르신들의 종교에 대한 집착 때문에.."
        l1 "과거에 사로잡혀서, \n앞으로 나아가지 못하는 것만 같다는 생각이 들고는 해요."
        hide ak
        show me
        c "그게 왜 이상한가요?"
        hide me
        show ak eh
        l1 "...?"
        hide ak
        show me
        c "제가 살던 곳 얘기인데요,"
        c "그곳에서도.. 종교는 이성적인 관점에서는 \n말이 안 된다고들 생각해요."
        c "그럼에도 많은 사람들이 종교를 가지고 있죠."
        c "제 생각에는..."
        c "많은 사람들이 마음 한켠에는 불안한 구석이 있는 거에요."
        c "그래서... 그 불안한 감정을 이겨내려고, 극복하려고."
        c "종교라는 존재에 의지하게 되는 것 같아요."
        c "그래서, 그게 뭐 잘못됐나요?"
        hide me
        show ak hmm
        l1 "!" with vpunch
        hide ak
        show me
        c "결국 종교를 통해서 위로받았잖아요?"
        c "저는 이렇게 생각해요."
        c "종교를 이성적인 관점에서 바라보고\n논쟁하려 드는 건 정말 의미없는 행동이라고요."
        c "그런 주제가 과연 어느 쪽이 맞다는 결론에 도달할 수 있을까요?"
        c "본질은 그게 아니에요."
        c "종교는 지친 사람들에게 평온을 줄 수 있는 \n쉼터 역할을 해주는 것에 의의가 있다고 생각해요."
        c "특히나 요즘같은 각박한 세상에서는요."
        c "무한 경쟁 사회에서 종교나 팬덤 문화같은 \n도피처도 있어야 좀 숨통이 트이지 않겠어요?"
        c "아! 물론 제 세계의 관점이 많이 반영된 얘기긴 합니다."
        c "여기도 각박한 지는 잘 모르겠지만요...."
        c "여하튼.."
        c "아크룩스 님도 조금은 편해져보시는게 어떨까요?"
        c "어쩌다보니 좀 주접을 떨었네요. 죄송합니다.."
        hide me
        show ak ha
        l1 "...아뇨,"
        l1 "정말로, 정말로 다가오는 말이였습니다."
        l1 "[name]님께서 이렇게 생각이 깊으신 분인줄 몰랐어요."
        l1 "제가 생각이 잠시 짧았던 것 같습니다."
        l1 "한 교단의 수장이 되어서... \n교단의 존재 의의에 의구심을 갖다니."
        l1 "감사합니다, [name]님."
        l1 "다시금 마음을 다잡겠습니다."
        hide ak
        show me
        c "아뇨, 도움이 되셨다니 저야말로 다행입니다.."
        c "이방인인 제가 하기에는 \n주제넘은 소리로 들렸을 수도 있었을 텐데."
        $ suncount = 2
        stop music
    elif (suncount == 2):
        show ak ha
        l1 "날씨가 좋네요."
        l1 "언제 와도 싱그러운 곳입니다."
        hide ak
        show me
        c "그러게요."
        hide me
        show ak eh
        l1 "...."
        l1 "저, [name]님?"
        hide ak
        show me
        c "네??"
        hide me
        show ak eh
        l1 "이번 사태가 잘 해결되고 나면.."
        l1 "혹시 떠나시는 걸까요?"
        l1 "[name]님은 구원자.. 이시니까요."
        hide ak
        show me
        c "음.."
        c "솔직히, 그건 저도 확답을 못 드리겠네요."
        c "(신이 그런 부분까지 알려주지는 않았으니까...)"
        hide me
        scene cg_ak1 with dissolve
        l1 "...."
        l1 "만약.."
        l1 "만약 떠나시지 않게 된다면."
        l1 "저와 제 고향에도 가보시지 않겠습니까."
        l1 "그 쪽의 언덕에도, \n이곳 못지 않은 예쁜 경치를 가진 곳이 있거든요."
        l1 "제가 어릴 적에 마음이 초조하면 가곤 했던 곳인데.."
        l1 "[name]님께 소개해드리고 싶습니다."
        c "!" with vpunch
        c "저야.. 당연히 좋죠."
        c "아마 시간적 여유가 있을 거에요."
        c "(뭐.. 신한테 어떻게든 얘기해보면 되지 않을까?)"
        l1 "긍정적으로 받아주셔서 다행입니다."
        l1 "..."
        l1 "교주들을 제외한 다른 누군가한테... \n이렇게 제안을 해본 건 처음입니다."
        l1 "그동안에는 제 속을 얘기한다는 것에 \n막연한 두려움이 있었거든요."
        l1 "그런데 저번의 얘기를 듣고서..."
        l1 "조금은, 달라져보려고 합니다."
        l1 "조금은.. 더 솔직해져보려고 합니다."
        c "..."
        c "좋은 변화네요!"
        c "혼자만 짊어지고 가려 하면, 병 난다고요."
        l1 "훗."
        l1 "노을이 예쁘네요."
        l1 "태양은... 질 무렵에 가장 화려하게 빛나는 것 같습니다."
        c "그러게요."
        $ suncount = 3
        scene background_sun with dissolve
        stop music

    else:
        show ak ha
        l1 "언제 와도 늘 싱그러운 곳입니다."
        hide ak
        show me
        c "그러게요, 정말로.."

    $ supernovapower += 10
    $ analysis += 10
    $ count = 0
    $ dday -= 1
    "태양을 관측했습니다."
return

label star:
    show me
    c "오늘의 오후 활동은 별자리 관측입니다."
    hide me
    show cl std
    l3 "그럼 제가 동행할게요~"
    hide cl
    scene background_star with dissolve
    play music "audio/star.mp3" fadein 2.0 loop
    if (starcount == 0):
        show me
        c "여기가 바로.."
        hide me
        show cl std
        l3 "네에~"
        l3 "클린스타클에서 은하수가 가~장 잘 보이는 숲이랍니다!"
        show cl hmm
        l3 "어찌나 잘 보이는지, \n별이 하늘에 잡아먹힌 것만 같다는 뜻에서.."
        show cl std
        l3 "별이 먹힌 꿈길이라고 부르고 있어요."
        l3 "가끔씩 아스트라 자매들과 놀러오고는 한답니다."
        hide cl
        show me
        c "그렇군요."
        c "그럼, 혹시 별자리들의 설명도 가능하신가요?"
        hide me
        show cl haha
        l3 "설명이라~ 좋죠!"
        show cl std
        l3 "저 쪽에 보이는 새 모양의 별자리가 보이시나요?"
        l3 "저게 바로 참새자리랍니다."
        l3 "바로 지금같은 가을에 아주 잘 보이는 별자리죠."
        hide cl
        show me
        c "참새자리라....."
        c "뭔가 굉장히 하찮으면서도 귀여운 별자리네요.."
        hide me
        show cl haha
        l3 "아하핫. 재미있는 한줄평이네요~"
        show cl moo
        l3 "그런데 [name]님, 실례지만."
        l3 "이런 별자리 관측이 재앙의 대비와 \n어떤 관련이 있는건가요?"
        l3 "물론 천체 관측이 아스트라에서는 \n굉장히 경건한 행위이긴 하지만.."
        l3 "이건 그저 종교적 행위에 지나지 않는걸요."
        hide cl
        show me
        c "음."
        c "(당연히 없지!!!!)" with vpunch
        c "(애당초 재앙은 조작된 사실이니까 안 막아도 되니까!!!!!)"
        c "(이렇게 한 명씩 직접 함께 다녀보면서 \n의심스러운 부분이 있는지 판단하는 게 진짜 이유다..)"
        c "사실.. 구체적인 이유는 없습니다."
        c "그래도 아무것도 안 하는 것 보다야 의미있지 않을까요?"
        hide me
        show cl std
        l3 "음. 그것도 그렇네요~"
        l3 "아시다시피 저희도 이렇다 할 소득은 없잖아요?"
        show cl moo
        l3 "종언서가 발견된 지도 벌써 보름도 더 지났는데.."
        l3 "에크모트가 정확히 어디에서 나타나는지조차 미궁이에요."
        l3 "그저 머지않아 이 나라에 부활한다는 것만 알고 있죠."
        l3 "과연 신님의 뜻이 무엇인 걸까요...?"
        l3 "정말 저희의 오만함을 심판하시려는 걸까요..."
        hide cl
        show me
        c "(그럴리가...)"
        c "(그보다, 클라우드의 말들을 들어보니\n더더욱 조작됐다는 사실이 와닿는군.)"
        c "(구체적인 내용은 없이.. \n그저 재앙이 도래할 것이라고만 얘기하고 있어.)"
        c "(아무튼 재앙이 도래하니 너희는 막아야 한다..\n뭔가 이런 느낌이랄까.)"
        c "설마요."
        c "적어도 제가 아는 신은 그렇게 무자비하지 않아요."
        hide me
        show cl awk
        l3 "정말 신이라도 만나보신듯한 문장이군요."
        hide cl
        show me
        c "(맞다.)"
        hide me
        show cl std
        l3 "좋아요~ 어찌되었건 간에 조금이라도 더 노력해보죠."
        hide cl
        $ starcount = 1
    elif (starcount == 1):
        show me
        c "또 오게 되는군요."
        hide me
        show cl std
        l3 "올 때마다 무아지경에 빠지게 되는 숲이에요~"
        l3 "어릴 적마다 이곳에 와서 명상을 하곤 했죠."
        hide cl
        show me
        c "명상이라... 굉장히 고상한 취미군요."
        hide me
        show cl haha
        l3 "아하핫~ 그런 말 많이 들었어요."
        show cl std
        l3 "[name]님은 취미가 있으신가요?"
        hide cl
        show me
        c "저는..."
        c "저는 원래 있던 세계에서 \n'컴퓨터'라고 불리는 걸 했었어요."
        c "그중에서도 게임을 주로 했죠."
        c "(말하고 보니 좀 한심하다..)"
        hide me
        show cl hcb
        l3 "컴퓨터는 여기에도 있는걸요~"
        l3 "이래봬도 우리 나라, \n이 세계에서는 과학력이 뛰어난 편에 속한답니다?"
        hide cl
        show me
        c "헉. 당연히 없거나 다른 이름일 줄 알았어요.. 죄송합니다..."
        hide me
        show cl haha
        l3 "아하하핫, 장난이에요."
        l3 "[name]님은 반응이 참 재밌으신 것 같아요."
        show cl std
        l3 "그런데 좀 신기하네요~\n여기서도 거기서도 컴퓨터라고 불린다니."
        l3 "[name]님의 세계와 이쪽 세계는 \n어쩌면 비슷한 부분이 많았을지도 모르겠네요~"
        hide cl
        show me
        c "(이제와서 생각해보니 그렇다.)"
        c "(세계의 풍경이나.. 거주민들의 모습이나..\n얼핏 보면 지구라고 착각이 들 정도야.)"
        c "(아마 이것도 신, 그 양반이 말한 '내가 가장 적합한 인물로 선정된 이유'의 일부겠지?)"
        hide me
        show cl std
        l3 "그래도 뭔가 몰두할 게 있다는 건 좋은 거에요, 그렇죠?"
        hide cl
        show me
        c "아, 네."
        c "아무래도 그렇죠."
        c "취미랄 게 없었다면.. \n정말 지루했을 거에요, 이 세상."
        hide me
        show cl moo
        l3 "저 역시도요."
        l3 "사소한 것 하나일지라도, \n자세히 보면 몰두할 구석이 있답니다."
        l3 "...."
        l3 "[name]님."
        hide cl
        show me
        c "예. 클라우드 씨."
        hide me
        show cl moo
        l3 "조금 뜬금없는 소리지만.."
        show cl std
        l3 "저는... 이 세계를 정말 소중하게 생각해요."
        l3 "폴라리스와 아크룩스, 카리오트 씨까지.\n모두가 저에게는 친구이자, 은인이자, 동료에요."
        hide cl
        show me
        c "아무럼요. 셋이 사이가 정말 좋아보였습니다."
        c "마치 친구들과 노는 걸 보는 기분이였어요."
        c "(신의 말대로라면 분명 세 교단끼리는 \n서로 견제하는 태도여야 할텐데..)"
        c "(지금까지의 행보만 보면 서로간의 사이는 좋아보였지, 분명히..)"
        hide me
        show cl haha
        l3 "아하하. 보이는대로 실제로도 그렇답니다."
        show cl moo
        l3 "비록 정계의 다른 어르신들은 \n다른 교단을 탐탁치 않게 여기시지만.."
        show cl std
        l3 "교주끼리의 관계는 그렇지 않아요."
        l3 "저희 셋은 같은 스승님으로부터 교육받았거든요."
        hide cl
        show me
        c "(스승?)"
        c "(교주들을 양성한 별도의 인물이 또 있는건가..)"
        c "스승님..?"
        hide me
        show cl hmm
        l3 "아.. 설명하자면 좀 복잡하신 분이에요."
        show cl moo
        l3 "그냥..지금은 의식불명이신 상태라고만 해 두죠."
        l3 "아무튼, 스승님은 어르신들과는 다르게 \n저희를 전적으로 도와주신 분이에요."
        hide cl
        show me
        c "앗, 이해했습니다."
        c "(거듭 교주들의 나이가 전체적으로 어리다고 느꼈는데..)"
        c "(이들을 교주의 자격을 갖추게끔 이끌어준 인물이였나보군.)"
        c "(그보다, 교주들은 어디까지나 종교쪽의 얼굴마담 역할만 맡고 있고,\n'어르신'이라는 정계 세력이 실권을 쥐고 있는건가.)"
        c "(순수함을 정치놀이에 이용하고 있다니..)"
        c "(파고들수록 속이 썩은 국가로군.)"
        hide me
        show cl std
        l3 "스승님과 함께... 다른 두 교주들과 함께...."
        l3 "오랜 기간 같이 생활하고, 많은 것을 보고 느꼈죠."
        l3 "그 때 깨달았어요."
        l3 "이 세계와 모두의 삶은 정말 소중하다고.."
        l3 "영원에 가까운 세계에 비하면 인간의 삶은 티끌이지만,"
        l3 "인간이 있었기에 이런 세계가 만들어질 수 있었잖아요."
        l3 "한편으로.. 세계에는 \n저희의 힘으로도 어떻게 할 수 없는 장엄한 자연이 많아요."
        l3 "마치 이 별자리들처럼요."
        l3 "당시에는 사소하다고 느꼈을 것들이라도.."
        show cl haha
        l3 "지나고 돌이켜보면 \n그 때는 몰랐던 의미가 숨어있던 것들이 참 많아요."
        show cl std
        l3 "저는 이 세계를 지키고 싶어요. 정말로요."
        show cl moo
        l3 "그래서 더더욱 그 괴물이 다시금 부활하지 못하게 막아야만 해요."
        hide cl
        show me
        c "클라우드 씨.."
        c "걱정하지 마세요."
        c "그걸 막기 위해서 제가 이곳에 온 거니까요."
        c "저도 전적으로 돕겠습니다."
        hide me
        show cl doki
        l3 "감사해요."
        l3 "여기에 와주신 것도,"
        l3 "제 응석을 받아주신 것도..."
        hide cl
        $ starcount = 2

    elif (starcount == 2):
        show me
        c "자주 오게 되네요."
        hide me
        show cl haha
        l3 "아하핫, 어쩌다 보니 그러네요~"
        show cl std
        l3 "그래도 좋지 않으신가요?"
        l3 "이 곳의 풍경은 봐도봐도 질리지 않는걸요."
        hide cl
        show me
        c "확실히.. 그렇습니다."
        c "올 때마다 새로운 별자리를 배워가는 것도 좋구요."
        hide me
        show cl moo
        l3 "오늘은 어떤 별자리가 보일까요.."
        show cl hmm
        l3 "아! 저 쪽에 저거, 보이시나요?"
        hide cl
        show me
        c "음... 아. 네."
        c "뭔가.. 눈사람처럼 생겼는데요?"
        c "숫자 8 같기도 하고.."
        hide me
        show cl haha
        l3 "맞아요!"
        l3 "저건 안경자리라고 불리는 별자리랍니다."
        hide cl
        show me
        c "하필.... 안경이라."
        hide me
        show cl std
        l3 "굉장히 좋은 의미를 갖는 자리에요."
        l3 "앞으로의 길이 순탄하고 편안할 것이라는......"
        show cl moo
        l3 "어라?"
        hide cl
        c "응? 왜 그러시죠?"
        show me
        "(무언가 소리가 들려온다.)"
        c "잠깐, 이게 무슨 소리죠?"
        hide me
        "쉿."
        scene cg_cl1 with dissolve
        l3 "들리시나요?"
        c "음?"
        play sound "audio/bell.mp3"
        c "!" with dissolve
        l3 "대성당에서 울리는 소리에요."
        l3 "하루의 모든 일정이 종료되면 \n저렇게 종소리가 울려퍼진답니다."
        l3 "저 소리를 들을때마다... \n마음이 조금은 진정되는 것 같아요." 
        c "그렇네요."
        c "정말 편안한 종소리에요."
        l3 "한편으로는, 이런 생각이 들어요."
        l3 "오늘은.. 어제 죽은 이가 그토록 바라던 내일이였는데."
        l3 "오늘 하루가.. 무의미하게 흘러가지는 않았을까?"
        c "..."
        c "어떠셨나요, 오늘은?"
        l3 "오늘은."
        l3 "의미가 깊었죠."
        l3 "아침의 활동도 있었고..."
        l3 "무엇보다, 지금..."
        l3 "!" with vpunch
        scene background_star with dissolve
        show cl hcb
        l3 "어..어찌되었던, 오늘은 의미깊은 하루였어요."
        show cl awk
        l3 "그럼! 다시 별자리를 보러 갈까요?"
        hide cl
        show me
        c "(방금.. 지금이라고 말하려다가 그만두지 않았나..?)"
        c "(......)"
        hide me
        "(뭘 말하려고 했던걸까?)"
        $ starcount = 3

    else:
        show me
        c "자주 오게 되네요."
        hide me
        show cl haha
        l3 "아하핫. 그러게요~"
        hide cl

    $ astrapower += 10
    $ analysis += 10
    $ dday -= 1
    $ count = 0
    "별자리를 관측했습니다."
return

label moon:
    show me
    c "오늘의 오후 활동은 달 관측입니다."
    hide me
    show po std
    l2 "응! 그럼 내가 따라갈게!"
    hide po
    scene background_moon with dissolve
    play music "audio/moon.mp3" fadein 2.0 loop
    if (mooncount == 0):
        show po std
        l2 "도착했어!!"
        l2 "할아버지들이랑 늘 달 보러 오던 산, 맞아!"
        l2 "적어도 내가 아는 선에선 가장 달이 크게 보이는 곳이야!"
        l2 "이름하야 달이 잠든 성소!!"
        hide po
        show me
        c "이름 잘 지었네."
        c "정말 달이 고이 잠든 것 같이 평온해."
        c "그럼.. 달 관측을 시작해볼까?"
        hide me
        show po std
        l2 "좋아!"
        show po hmm
        l2 "그런데, 달을 보는게 도움이 될까?"
        l2 "이건 우리 이클립스에선 성스러운 일이긴 한데.."
        l2 "예언을 해석하거나.. 재앙을 막거나!\n그런 쪽이라는 거리가 좀 있는 것 같아서!"
        show po ang
        l2 "앗! 절대 오빠를 못 믿거나 그러는 건 아니야!"
        show po hmm
        l2 "그냥 궁금해서~ 특별한 이유가 있나!"
        hide po
        show me
        c "음."
        c "(당연히 없지!!!!)" with vpunch
        c "(애당초 재앙은 조작된 사실이니까 안 막아도 되니까!!!!!)"
        c "(이렇게 한 명씩 직접 함께 다녀보면서 \n의심스러운 부분이 있는지 판단하는 게 진짜 이유다..)"
        c "(그래도 뭐라고 얘기는 해보자.)"
        c "우리 나라에서는 말야,"
        c "달을 바라보면서 소원을 빌고는 해."
        c "그래서 와버렸다!.. 뭐 이런 느낌이야."
        hide me
        show po std
        l2 "그런 느낌이구나!!"
        show po haha
        l2 "완벽하게 이해했어!!"
        show po std
        l2 "클린스타클에서도 그런 전통이 있다구."
        l2 "달을 바라보면서 소원을 비는 거 말야."
        l2 "오빠네 세계에서도 그런다니, 재밌네~"
        l2 "뭔가.. 어느 세계든 비슷하구나 싶고!"
        hide po
        show me
        c "그러게."
        c "(확실히, 이쪽 세계는 지구와 비슷한 구석이 많아.)"
        c "(아무래도.. 비슷한 환경에 있던 나를 데려왔다는\n신의 말이 이런 뜻이였나 보군.)"
        c "그럼.. 소원을 빌어볼까."
        c "(...)"
        c "(부디 흑막을 찾아낼 수 있길.)"
        hide me
        show po std
        l2 "무슨 소원 빌어?"
        hide po
        show me
        c "!" with vpunch
        c "깜짝아! 넌 소원 안 빌어?"
        hide me
        show po std
        l2 "벌써 빌었다구~"
        hide po
        show me
        c "뭐? 엄청 빠르네.."
        c "넌 뭐라고 빌었어?"
        hide me
        show po ho
        l2 "비~밀!"
        hide po
        show me
        c "...."
        c "그래라..."
        $ mooncount = 1
    elif (mooncount == 1):
        show po std
        l2 "또 오는구나~"
        l2 "바깥 나가는 건 언제나 좋아!"
        l2 "특히 이쪽은 더더욱~~~"
        hide po
        show me
        c "확실히. 안에만 있으면 답답하지."
        c "그럼.. 오늘도 달을 바라보면서!"
        hide me
        show po std
        l2 "소원도 빌구~"
        l2 "달 관측도 하고!"
        hide po
        show me
        c "달에 대해 뭔가 아는 게 있어, 폴라리스는?"
        hide me
        show po hmm
        l2 "응? 그건 무슨 질문?"
        l2 "나.. 이래봬도 달을 숭배하는 교단의 교주라구?"
        l2 "어렸을 적에 선생님한테 달에 대한 모든 걸 교육받았어!"
        l2 "다른 교주 언니들이랑 같이 말야."
        hide po
        show me
        c "(음? 선생님?)"
        c "(세 교주들을 모두 아우르는 별도의 인물인가.)"
        c "선생님?"
        hide me
        show po hmm
        l2 "아! 지금은 안 계신 분이야.."
        show po sad
        l2 "작년에 갑자기 의식불명이 되셨거든."
        hide po
        show me
        c "아, 미안.."
        c "민감한 주제를 물어본건가."
        hide me
        show po std
        l2 "아냐아냐!! 괜찮아~"
        l2 "오빠는 외지인인데, 어떻게 그런 걸 바로 캐치해!"
        l2 "어쨌건간에 그렇게 달을 집중적으로 공부해서.."
        l2 "이젠 달을 바라보는 것만으로도 \n오늘의 날짜, 지금 우리의 위치.. 다 계산된다구!"
        l2 "물론 천문기술의 발달로 그다지 의미없긴 하지만.. 히히"
        hide po
        show me
        c "컥. 그건 좀 슬픈데."
        c "그나저나.. 다른 분들도 잘 하고 있으려나?"
        hide me
        show po hmm
        l2 "음.."
        show po std
        l2 "그건 크게 걱정하지 않아도 돼!"
        hide po
        show me
        c "어라, 뭔가 진전이 있는거야?"
        hide me
        show po ho
        l2 "아니! 사실 이렇다 할 건 하나도 없어!"
        hide po
        show me
        c "?!" with vpunch
        c "그럼 대체 무슨 근자감인 건데?!"
        hide me
        show po hmm
        l2 "왜냐면.."
        l2 "그 언니들도 정말 노력하는 언니들이거든."
        l2 "분명 각자의 위치에서 뭔가 알아내고 말거야."
        l2 "나는 그 둘에 비하면 완전 어린애라구."
        show po haha
        l2 "실제로도 어리긴 하지만~ 큭큭."
        hide po
        show me
        c "(그냥 천진난만하기만 한줄 알았는데, 꽤나 이타적이네..)"
        c "그럴수록 너도 힘내야지."
        c "너도 그 둘에 뒤쳐지지 않는 멋진 교주가 되어야지."
        hide me
        show po sad
        l2 "오빠....!"
        show po ho
        l2 "완전 아빠 같았어!"
        hide po
        show me
        c "켁." with vpunch
        c "너랑 안 다녀."
        hide me
        show po ang
        l2 "농담!!!!! 농담!!!!!"
        $ mooncount = 2
    elif (mooncount == 2):
        show po std
        l2 "또 또 오는구나~~"
        hide po
        show me
        c "이젠 길도 외우겠군."
        hide me
        show po ho
        l2 "케케. 정말?"
        show po std
        l2 "그보다.. 오늘은 뭔가 달이 더 밝은 것 같네."
        l2 "보자.. 오늘 날짜가.."
        show po ang
        l2 "헉!" with vpunch
        hide po
        show me
        c "왜 그래?"
        hide me
        show po wow
        l2 "오늘이 바로 그 날이였어!!!!!"
        hide po
        show me
        c "무슨 날..?"
        hide me
        show po std
        l2 "3년만에 돌아온, 달이 크게 보이는 슈퍼문 데이!!"
        l2 "이거 완전 드문 날인데, 운이 좋은걸 우리?!"
        hide po
        show me
        c "아하, 그런 거였나."
        c "..확실히, 달이 엄청 크고 밝군."
        c "밤인데도 낮인 것 처럼 환할 지경이야."
        hide me
        show po std
        l2 "오빠, 오빠!"
        l2 "슈퍼문 데이니까 해야하는 일이 있어!"
        hide po
        show me
        c "응?"
        c "그게 뭐지?"
        hide me
        show po ho
        l2 "받아."
        "(무언가 손에 쥐어준다.)"
        hide po
        show me
        c "이게 뭐...."
        "(메뚜기 한마리가 뛰쳐나온다.)"
        c "!!!!!!!!!!!" with vpunch
        c "크헉!!!"
        hide me
        show po haha
        l2 "캬카카카카칵!!!" with vpunch
        l2 "사실 그런건 없고 메뚜기였습니다!!!!"
        hide po
        show me
        c "이런 장난을......"
        c "완전 어린애답구나, 폴라리스...."
        hide me
        show po std
        l2 "오빠는 내 장난을 참 잘 받아주는 것 같아."
        show po hmm
        l2 "..."
        show po sad
        l2 "갑자기 장난쳐놓고 진지한 얘기 해서 미안한데,"
        l2 "잠깐 혼잣말 좀 해도 될까?"
        hide po
        show me
        c "(다이나믹한 분위기변환이군....)"
        c "응."
        hide me
        show po hmm
        l2 "어릴 적에 엄마는 나를 낳으신 뒤 \n머지않아 돌아가셨다고 해."
        l2 "그래서 형제나 자매는 없고 나 혼자뿐이였어."
        l2 "그리고 아빠는...."
        show po sad
        l2 "분명 좋으신 분이지만, \n상냥하기까지는 못하신 분이였어."
        l2 "늘 나를 엄격하게 기르셨지."
        l2 "지금 와서 보면 이해는 돼.\n한 교단의 교주가 가져야 할 무게감이란 게 있잖아."
        l2 "하지만 그 때의 나는 그걸 이해하지 못했던 것 같아."
        l2 "나도 부모님들과 같이 소풍도 가고,\n외식도 해봤으면 했어."
        l2 "나도 부모님이 어리광이나 장난을 받아줬으면 했어."
        l2 "평범하다는 게 어떤 기분이였는지 몰라서, \n 느껴보고 싶었어."
        l2 "더 우스운건 말이지,"
        l2 "아빠마저 편찮아지시고.. 처음으로 든 감정이."
        l2 "슬픔보다는 아쉬움에 가까웠다는 거야."
        l2 "정말로 저런 추억의 조각들을\n가지지 못한 채로 살아가게 될까봐.."
        hide po
        scene cg_po1 with dissolve
        l2 "하지만.. 이제는 알 것 같아."
        l2 "이 평범하다는 게... 이렇게나 즐거운 일이란 걸.."
        l2 "다 오빠 덕분이야."
        c "!" with vpunch
        c "내가 한 게 뭐가 있다고."
        c "하지만.. 위로가 되었다면 다행이야."
        l2 "응!"
        l2 "앗! 너무 내 말만 했네!"
        l2 "날이 슬슬 추워지는 것 같아.\n빨리 달 마저 보고 돌아갈까?"
        scene background_moon with dissolve
        $ mooncount = 3

    else:
        show po std
        l2 "또 또 또 오는구나~~~"
        hide po
        show me
        c "또가 계속 늘어나는 기믹이였군.."
        hide me

    $ eclipsepower += 10
    $ analysis += 10
    $ dday -= 1
    $ count = 0
    "달을 관측했습니다."
return

label rest:
    show me
    c "이번의 오전 활동은..."
    c "없습니다!"
    hide me
    if (restcount == 0):
        show po haha
        l2 "와!!!!!!" with vpunch
        hide po
        show ak awk
        l1 "너무 좋아하는거 아니야..?"
        show ak eh
        l1 "그런데, 지금같은 때에 \n쉬는 게 맞는 걸까요?"
        l1 "1분 1초가 아까운 상황인데..."
        hide ak
        show cl haha
        l3 "아하하~"
        show cl std
        l3 "그렇지만 우리, 종언서가 발견된 뒤로 \n단 한 번도 쉬지 못했다구?"
        show cl haha
        l3 "조금씩은 쉬는 것도 괜찮다고 생각해요~"
        show ak std
        hide cl
        l1 "흠.."
        l1 "시기가 시기긴 하지만.."
        show ak ha
        l1 "조금 컨디션 조절을 해둘 필요는 있겠군."
        hide ak
        show po std
        l2 "좋아~ 난 지금부터 잘거야!"
        hide po
        show cl std
        l3 "그럼 오후에 뵙겠습니다."
        hide cl
    else :
        show ak awk
        l1 "또?!"
        hide ak
        show po ho
        l2 "좋은 게 좋은거지~~!"
        hide po
        show cl std
        l3 "[name]님의 계획이 있으시겠죠."
        l3 "저희는 전적으로 따르겠습니다."
        hide cl
        show ak eh
        l1 "뭐.... 그렇게 하자고 하긴 했지만.."
        show ak std
        l1 "하아...."
        l1 "이젠 모르겠다.."
        hide ak
    $ restcount += 1
    $ reason1 += 10
    $ reason2 += 10
    $ reason3 += 10
    $ count = 1
    "여가 활동을 했습니다."
return

label confession1:
    if (confessioncount1 == 0):
        show ak std
        l1 "고해성사는 신과 소통할 수 있는 \n가장 정직한 창구라고 여겨집니다."
        l1 "모든 클린스타클의 국민들은 \n고해성사의 시간을 적어도 달에 한번은 갖죠."
        hide ak
        show me
        c "그건 우리 세계의 종교들과도 비슷하군요.."
        c "그럼, 그간의 죄를 참회하는 시간을 갖겠습니다."
        hide me
        show ak ha
        l1 "네."
        hide ak
        "(몇 분이 흘렀다.)"
        show me
        c "끝나셨을까요?"
        hide me
        show ak ha
        l1 "네, 모두 마무리됐습니다."
        l1 "마음이 한결 가벼워졌군요."
        l1 "부디 신께서 굽어보시길...."
        hide ak
        show god
        g "(^^)"
        hide god
        show me
        c "(...)"
        c "(내 머리속에 갑자기 나타나지 말라고.)"
        hide me
        $ confessioncount1 += 1
    else:
        show ak hmm
        l1 "이번에도 고해성사인가요."
        hide ak
        show me
        c "네. 마음을 비우는 게 무엇보다 중요하거든요."
        hide me
        show ak std
        l1 "..."
        show ak ha
        l1 "동의합니다."
        hide ak
    $ reason1 += 20
    $ dday -= 1
    $ count = 0
    "아크룩스와 고해성사를 했습니다."
return

label confession2:
    if (confessioncount2 == 0):
        show po hmm
        l2 "고해성사는 뭔가 따분하단 말이지."
        show po std
        l2 "사실.. 교주라는 직책을 달고 \n할 말은 아니지만. 큭큭."
        hide po
        show me
        c "잘 아는구나.."
        hide me
        show po std
        l2 "그럼, 시작하자구."
        l2 "오빠랑 내 속의 죄를 모두 털어내는거야!"
        hide po
        "(몇 분이 흘렀다.)"
        show me
        c "다 됐어?"
        hide me
        show po std
        l2 "응!"
        l2 "마음이 완전 깨끗해진 기분이야!"
        show po haha
        l2 "이제 새 사람이 되었으니, 더 열심히 해보자구~"
        hide po
        show me
        c "좋아!"
        hide me
        show god
        g "(좋아요!)"
        hide god
        show me
        c "(!)" with vpunch
        c "(갑자기 나타나지 말라고!)"
        hide me
        $ confessioncount2 += 1
    else:
        show po sad
        l2 "우우.. 또 고해성사야?"
        l2 "성스러운 행위인건 맞지만.."
        hide po
        show me
        c "귀찮다고?"
        hide me
        show po ang
        l2 "아..아니! 그럴리가~"
        hide po
        show me
        c "표정은 못 숨기는거 같은데.."
        hide me
    $ reason2 += 20
    $ dday -= 1
    $ count = 0
    "폴라리스와 고해성사를 했습니다."
return

label confession3:
    if (confessioncount3 == 0):
        show cl std
        l3 "[name]님과 고해성사는 처음이군요~"
        show cl doki
        l3 "어쩐지 묘한 기분이네요."
        show cl std
        l3 "고해성사는 해보신 적이 있나요?"
        hide cl
        show me
        c "아, 원래 세계에서도 있는 행위인지라.."
        c "대충 뭔 지는 알아요."
        c "그간 저지른 죄를 신에게 속죄하는..\n종교적으로 굉장히 의미있는 행위잖아요."
        hide me
        show cl haha
        l3 "어머, 클린스타클 국민들보다도 더 박식하신걸요~"
        hide cl
        show me
        c "방금 그 발언.... 교주가 하기엔 위험한 것 같은데."
        hide me
        show cl haha
        l3 "아하핫~ 나쁜 뜻은 전혀 없었어요."
        show cl std
        l3 "맞아요. 고해성사는 정말로 중요한 의미를 갖는답니다."
        l3 "그럼, 잠시 각자의 시간을 가져볼까요?"
        hide cl
        "(몇 분이 흘렀다.)"
        show me
        c "끝나셨나요?"
        hide me
        show cl std
        l3 "네."
        l3 "[name]님도, 저도, 뜻깊은 시간이 되었기를.."
        hide cl
        show me
        c "비나이다."
        hide me
        show god
        g "(뜻깊었어요~)"
        show me
        hide god
        c "(......)"
        c "(이젠 안방 드나들듯이 머리속에 나타나는군..)"
        hide me
        $ confessioncount3 += 1
    else:
        show cl hmm
        l3 "오늘도 고해성사군요."
        show cl std
        l3 "언제 얼마나 해도 전혀 부족하지 않아요~"
        l3 "그럼 바로 진행해볼까요?"
        hide cl
        show me
        c "아, 넵."
        hide me
        show cl moo
        l3 "부디 신께서 저희의 속죄를 들어주시기를.."
        hide cl
        show me
        c "비나이다."
        hide me
    $ reason3 += 20
    $ dday -= 1
    $ count = 0
    "클라우드와 고해성사를 했습니다."
return

label gameover1:
    stop music fadeout 2.0
    play music "audio/badend.mp3" fadein 1.0 loop
    "(아크룩스가 들어온다.)"
    show ak std
    l1 "[name]님."
    hide ak
    show me
    c "네?"
    c "무슨 일이시죠?"
    hide me
    show ak std
    l1 "불현듯 든 생각입니다만.."
    show ak haha
    l1 "굳이 재앙을 막아야 할 이유가 있을까요?"
    hide ak
    show me
    c "??"
    c "갑자기 그게 무슨 말씀.."
    hide me
    show ak ha
    l1 "[name]님은 구원자니까 아시겠지만.."
    l1 "클린스타클은 속부터 썩어있잖아요?"
    l1 "겉으로는 가장 성스럽고 발전된 나라인 척 하지만,"
    show ak haha
    l1 "사실은 그걸 정치싸움에 이용하려는\n윗 분들만 가득한 나라인걸요."
    hide ak
    show me
    c "그런.."
    c "하지만, 이번에 재앙을 막고 나서.."
    c "조금씩이나마 고쳐나가면 되는 부분 아닐까요..?"
    hide me
    show ak std
    l1 "아니요."
    l1 "사실 그동안에는 혼란스러운 마음이였습니다만.."
    l1 "유적지에 다녀온 이후로.. 갈피를 잡은 것 같습니다."
    show ak gal
    l1 "여기는.. 더이상 지킬 가치가 없다고요."
    hide ak
    show me
    c "?!" with vpunch
    c "대체 그게 무슨 소리에요?!"
    c "분명 며칠 전까지만 해도 \n종말 막기에 진심이셨던 분이.."
    c "!" with vpunch
    hide me
    show image "backgrounds/아크룩스흑화.jpg" with dissolve
    l1 "..."
    l1 "보이시나요?"
    c "대체 그 모습은...?"
    l1 "유적지가 위험하다고 했던 이유.."
    l1 "그게 바로 이 이유에서였어요."
    l1 "유적지에 깔린 의문의 기운은..."
    l1 "사람의 내면에 내재된 욕망을 발현시키죠."
    l1 "클린스타클에서는.. 이걸 발현병이라고 부르고요."
    c "그렇다면 아크룩스님 마음 속의 욕망이.."
    c "그런 괴물과도 같은 모습이라는 거에요?"
    c "말도 안 돼.."
    l1 "..."
    l1 "잠깐이나마... \n이 세계를 바꿀 수 있을지도 모른다고 믿었어요."
    l1 "그런데.... 그조차도 허황된 꿈이였던 것 같군요."
    l1 "제 진정한 속마음은 이랬는데 말이죠."
    l1 "유적지의 기운이... \n머리속에서 저에게 속삭였습니다."
    l1 "이 넘치는 힘이라면..."
    l1 "클린스타클을 단신으로라도 멸망시킬 수 있어."
    scene black with dissolve
    show ak sad
    l1 "미안합니다. [name]님."
    l1 "재앙에 의해 무너질 바에야..\n나 스스로가 재앙이 된다.."
    show ak ha
    l1 "이게 이 난관을 해쳐나갈 저의 판단입니다.."
    l1 "부디 다른 자매들을 원망하지 말고.. \n저만을 원망하시길."
    hide ak
    "(그렇게 말하고 아크룩스는 사라진다.)"
    show me
    c "잠깐만요! 아크룩스님!!!"
    c "원망... 안할테니까..."
    c "한 번만 다시 생각해주시면 안되나요...?"
    c "..........."
    hide me
    show god
    g "(...)"
    g "([name]님.)"
    hide god
    show me
    c "!" with vpunch
    hide me
    show god
    g "(아무래도 이번엔 여기까지인가 봅니다.)"
    g "(저는 세계를 다시 되돌리고..)"
    g "(세계선을 새롭게 분리시킨 다음,)"
    g "(다른 용사님을 물색해야겠습니다.)"
    g "(자칫하면 세계 자체가 소멸될 수도 있는 \n굉장히 리스크있는 일이지만..)"
    g "(어쩌겠어요, 방법이 없는 걸.)"
    g "(어찌됐건, 고생하셨습니다. [name]님...)"
    hide god
    show me
    c "(...............)"
    c "(혹시라도, 혹시라도 다음 기회가 주어진다면.)"
    c "(이성을 관리하고... \n유적지 탐사에 너무 매몰되지 말자..)"
    hide me
    "Bad Ending#1 : 극야"
    jump credits_bad
    
return 

label gameover2:
    stop music fadeout 2.0
    play music "audio/badend.mp3" fadein 1.0 loop
    "(폴라리스가 들어온다.)"
    show po dead
    l2 "...아..."
    hide po
    show me
    c "왜 그래, 폴라리스?"
    hide me
    show po dead
    l2 "기분이.. 이상해."
    l2 "갑자기.. 아무것도 하기가 싫어졌어."
    hide po
    show me
    c "..??"
    c "갑자기 그게 무슨 소리야?"
    hide me
    show po dead
    l2 "모르겠어, 나도.."
    l2 "그냥... 조금만.. 쉬면 안될까?"
    hide po
    show me
    c "...."
    c "폴라리스, 힘든 건 이해해."
    c "하지만.. 카리오트 님이 말했잖아."
    c "시간은 촉박하고, 알아낸 건 너무나도 없어.."
    c "이런 상황에서 너까지..{nw}"
    hide me
    show po gal
    l2 "그만!" with vpunch
    hide po
    show me
    c "!" with vpunch
    c "폴라리스!!"
    hide me
    show po gal
    l2 "나 이제.. 지쳤어!"
    l2 "더는... 못하겠어.."
    l2 "종말 막기고 뭐고...."
    l2 "다 그만둘래."
    hide po
    scene cg_po2 with dissolve
    c "..!" with vpunch
    c "너.. 얼굴이 왜 그래?!"
    l2 "...이제야 눈치챈거야?"
    l2 "아마도 유적지에 너무 오래 머문 탓이겠지."
    l2 "유적지가 위험하다고 했던 거.. 기억 나?"
    l2 "이게 바로 그 이유야."
    l2 "유적지는... 사람의 마음을 갉아먹어."
    l2 "그러다가.. 그 사람의 한계가 올 때쯤.."
    l2 "이렇게 변이를 일으키지."
    l2 "이걸 우리는 '발현병'이라고 불러.."
    c "제기랄."
    c "막을 방법은.. 없는거야?!"
    l2 "....."
    l2 "이미 늦었어."
    l2 "한 번 시작된 발현은.. 돌이킬 수 없어.."
    l2 "그리고... 근시일 내로 정신을 잃고 \n본능에 따라 움직이게 한다지.."
    l2 "...."
    l2 "미안."
    l2 "처음부터 나같은 어린애한테는 무리였나 봐."
    l2 "처음부터... 나서지 않았더라면..."
    l2 "이런 일도 없었을텐데...."
    scene background_black with dissolve
    show po dead
    l2 "내가 재앙이 되어버린 것만 같네.."
    show po ssha
    l2 "하핫.."
    hide po
    "(폴라리스가 쓰러진다.)"
    c "..안 돼!!"
    c "(이럴 줄 알았더라면.... \n유적지에 그렇게 많이 가지는 않았을텐데...)"
    c "(한 번만... 한 번만 돌이킬 수는 없을까?)"
    c "(제발.. 한 번만이라도...)"
    show god
    g "(...)"
    g "([name]님.)"
    hide god
    c "!" with vpunch
    show god
    g "(아무래도 이번엔 여기까지인가 봅니다.)"
    g "(저는 세계를 다시 되돌리고..)"
    g "(세계선을 새롭게 분리시킨 다음,)"
    g "(다른 용사님을 물색해야겠습니다.)"
    g "(자칫하면 세계 자체가 소멸될 수도 있는 \n굉장히 리스크있는 일이지만..)"
    g "(어쩌겠어요, 방법이 없는 걸.)"
    g "(어찌됐건, 고생하셨습니다. [name]님...)"
    hide god
    c "(...............)"
    c "(혹시라도, 혹시라도 다음 기회가 주어진다면.)"
    c "(이성을 관리하고... \n유적지 탐사에 너무 매몰되지 말자..)"
    "Bad Ending#2 : 삭(朔)"


    jump credits_bad

label gameover3:
    stop music fadeout 2.0
    play music "audio/badend.mp3" fadein 1.0 loop
    "(클라우드가 들어온다.)"
    show cl moo
    l3 "...[name]님?"
    l3 "계신가요."
    hide cl
    show me
    c "아, 클라우드 씨."
    c "무슨 일이신가요?"
    hide me
    show cl dead
    l3 "...."
    l3 "[name]님은..제가 어떠한 결정을 내려도.."
    l3 "존중해주실 수 있나요?"
    hide cl
    show me
    c "네...?"
    c "네. 존중합니다."
    c "그런데 갑자기 그게 무슨...?"
    hide me
    show cl dead
    l3 "[name]님.."
    l3 "유적지에서 했던 말, 기억하시나요?"
    l3 "유적지의 기운은..엄청 위험하다고요."
    l3 "..."
    hide cl
    show image "backgrounds/클라우드흑화.jpg" with dissolve
    l3 "그 의미가.. 이거였던 걸까요?"
    c "?!" with vpunch
    c "대체 그 모습은..?!"
    l3 "...."
    l3 "이건.. '발현병'이라는 병이에요.."
    l3 "감염자를 본인의 욕망이 반영된 괴물로 서서히 변이시키죠..."
    l3 "그 끝에는... 이성을 잃은 '재앙'이 있을 뿐이고요."
    l3 "외곽에서 조심하면 괜찮을 줄 알았는데..."
    l3 "아니였나 봐요."
    c "발현병...?!"
    c "그런.."
    c "치료법은 없는건가요?"
    l3 "..."
    l3 "네, 아마도요."
    l3 "이런 상태로는.. 일을 이어갈 수 없겠어요."
    l3 "죄송해요, [name]님."
    l3 "도움이 되어드리고 싶었는데.."
    l3 "이런 결과가 되어버려서...."
    c "잠깐만요! 정신 차려보세요!!"
    c "제가 어떻게든 해볼테니까...! 제발..!"
    l3 "이미 늦었어요.."
    scene black
    "(클라우드의 품에서 무언가 예리한 것이 나온다.)"
    l3 "정신을 빼앗기고 모두에게 폐를 끼칠 바에는.."
    l3 "제가 먼저 사라지는 편이..."
    c "!!!!" with vpunch
    c "안 돼!!!"
    c "(이런 결과를 낳을 줄은.. 몰랐다고!!!!)"
    c "(한 번만.. 한 번만 되돌려주면 안될까..?)"
    show god
    g "(...)"
    g "([name]님.)"
    hide god
    show me
    c "!" with vpunch
    hide me
    show god
    g "(아무래도 이번엔 여기까지인가 봅니다.)"
    g "(저는 세계를 다시 되돌리고..)"
    g "(세계선을 새롭게 분리시킨 다음,)"
    g "(다른 용사님을 물색해야겠습니다.)"
    g "(자칫하면 세계 자체가 소멸될 수도 있는 \n굉장히 리스크있는 일이지만..)"
    g "(어쩌겠어요, 방법이 없는 걸.)"
    g "(어찌됐건, 고생하셨습니다. [name]님...)"
    hide god
    show me
    c "(...............)"
    c "(혹시라도, 혹시라도 다음 기회가 주어진다면.)"
    c "(이성을 관리하고... \n유적지 탐사에 너무 매몰되지 말자..)"
    hide me

    "Bad Ending#3 : 그리고 아무도 없었다"
    jump credits_bad
return 

label prophecy:
    "(카리오트가 들어온다.)"
    show ka std
    l4 "잠깐 주목."
    l4 "어제 너희들의 활동을 토대로,\n매우 중요한 정보를 발견했어."
    hide ka
    show po hmm
    l2 "응? 정보?"
    hide po
    show ak hmm
    l1 "그게 뭐죠?"
    hide ak
    show ka hmm
    l4 "'종언서'에서 제일 중요한 구절의 전문이다."
    hide ka
    show cl dead
    l3 "전문이요?!" with vpunch
    hide cl
    show ka std
    l4 "그래. 지금부터 읽어주지."
    hide ka
    prophecy1 "종언서 3장"
    prophecy1 "1. 아버지께서 보시기에 인간 세상이 심히 혼란하여 보기에 좋지 않더라."
    prophecy1 "2. 이에 당신께서 어리석은 자들 중 하나에게 이르셨으니"
    prophecy1 "3. 해가 서럽게 울고 달이 지쳐 스러져가는 날,"
    prophecy1 "4. 세계를 머금은 찬연히 빛나는 별들 사이로"
    prophecy1 "5. 짐승의 모습을 한 재앙이 찾아오리라"
    prophecy1 "6. 그 말씀에 모두가 놀라 눈물을 흘리며 잘못을 참회하였으니"
    prophecy1 "7. 마을 하나를 거친 뒤에야 아버지께서 노여움을 거치시더라."
    show ak wow
    l1 "확실히.. 종말을 예견하는 내용이군요."
    nvl clear    
    hide ak
    show po wow
    l2 "음~......"
    show po ang
    l2 "(뭔 소린지 잘 모르겠지만 무서운 내용인거 같네..)"
    hide po
    show cl no
    l3 "아아..."
    hide cl
    show ka seri
    l4 "....."
    l4 "포인트는 그게 아니야."
    l4 "그건 어차피 다들 아는 거잖아."
    show ka std
    l4 "이 구절은...."
    l4 "구체적인 장소와 시간을 암시하는 것 같아."
    hide ka
    show me
    c "?!" with vpunch
    hide me
    show ak eh
    l1 "너무 추상적인 표현뿐이라 확실하지는 않지만.."
    show ak std
    l1 "해가 서럽게 운다는 건 해가 질 무렵을,"
    hide ak
    show po hmm
    l2 "달이 지쳐 스러져간다는 건 \n달이 보름을 지나 하현을 향해 가는 시점을,"
    hide po
    show cl hmm
    l3 "세계를 머금은 찬연히 빛나는 별들은..."
    l3 "잘은 모르겠지만.."
    l3 "별들이 보이는 어떤 지점.. 일까요."
    hide cl
    show ka hmm
    l4 "맞아."
    show ka seri
    l4 "그게 도대체 어딘지는 모르겠지만 말이야."
    l4 "그래도 스플릿시 유적지 인근이 아닐까, 추정중이야."
    if (temcount == 0):
        hide ka
        show me
        c "스플릿시..?"
        hide me
        show ka cham
        l4 "뭐야, 한 번도 안 가봤던건가."
        show ka seri
        l4 "에크모트의 봉인이 위치해있다고 추정되는 곳이다."
        l4 "그래서인지 유독한 기운이 엄청 뿜어나오고 있고."
        hide ka
        show me
        c "!!!!" with vpunch
        c "그런 곳이였던 건가..."
    else:
        l4 "아무래도 그 쪽이 에크모트의 봉인이 위치해 있으니까."    
        hide ka
        show me
        c "합당한 추론같군요."
    c "그나저나, 시간이 너무 촉박한데.."
    c "스플릿시 전역을 조사해야 하는 겁니까?"
    hide me
    show ak eh
    l1 "그럼 앞으로의 방향성은.."
    hide ak
    show cl awkmoo
    l3 "저 위치를 찾는 데에 집중해야 하는걸까요?"
    hide cl
    show po hmm
    l2 "라고 말하고 싶었어!"
    hide po
    show ka hmm
    l4 "뭐, 그건 너희들이 굳이 발품팔지 않아도 돼."
    show ka haha
    l4 "이미 중앙정부에서 수많은 인원들이 대조 분석중이니까."
    show ka std
    l4 "단지, 저 구절을 전해주고 싶었을 뿐."
    l4 "너희는 하던대로 재앙을 막을 방법을 강구해보라고."
    show ka haha
    l4 "그럼 남은 기간동안도 힘내고."
    hide ka
    show me
    c "넵."
    hide me
    "(카리오트는 돌아갔다.)"
    
    $ count1 = 1
return

label ending:
    stop music
    scene black
    "예언 당일, 오전"

    if (analysis >= 60):
        play music "audio/think.mp3" fadein 2.0 loop
        scene background_bedroom with dissolve
        "[name]의 침실"
        show me
        c "드디어... 당일인가."
        hide me
        show god
        g "(뭔가 좀 알아낸 게 있으신가요?)"
        hide god
        show me
        c "깜짝아!"
        c "음.... 알아낸 거라."
        c "5일간의 활동을 하면서 느낀 점은.."
        c "분명 무언가 미심쩍은 부분이 있었어."
        c "원본조차 발견되지 않았던 종언서.."
        c "그나마 발견된 구절은 대부분 재앙에 관련된 부분들뿐.."
        c "맹목적으로 재앙이 존재할 거라는 사실에만 \n매몰되게 만드는 것 같았지."
        c "정작 이 일을 진행중인 모두가 \n구체적으로 어떤 재앙이 도래하는 지는 모르고 있고."
        c "하지만.. 심증만 있을 뿐, \n누가 흑막이라고 특정할 수는 없는 상황이야."
        if (suncount == 3):
            c "대부분의 활동을.. 아크룩스 님과 함께 했던지라,"
            c "다른 쪽의 상황을 잘 체크해보지는 못했어."
        if (mooncount == 3):
            c "대부분의 활동을.. 폴라리스와 함께 했던지라,"
            c "다른 쪽의 상황을 잘 체크해보지는 못했어."
        if (starcount == 3):
            c "대부분의 활동을.. 클라우드 씨와 함께 했던지라,"
            c "다른 쪽의 상황을 잘 체크해보지는 못했어."        
        hide me
        show god
        g "(개인적으로 추측하는 부분은 있으신가요?)"
        hide god
        show me
        c "흠."
        c "이 나라의 '어르신'이라는 작자들,\n뭔가 많이 수상하더군."
        c "아무것도 모르는 세 교주들을 얼굴마담으로 세워두고...\n 본인들은 뒤에서 실권을 장악하고 있는 느낌이였어."
        c "정작 세 교주들 간의 사이는 원만했고."
        c "듣자하니 같은 스승 아래에서 교육을 받았다고 해."
        hide me
        show god
        g "(그렇습니까..)"
        g "(하지만 이제는 예언 당일.)"
        g "(뭐라도 행동하지 않으면...)"
        hide god
        show me
        c "하.. 그러게 말이야."
        c "어떻게 해야 하지..."
        hide me
        "(문이 열린다.)"
        show ka seri
        l4 "어이! [name]!!"
        l4 "기적적으로... \n종언서에서 말하는 위치와 시각을 찾은 것 같아."
        hide ka
        show me
        c "!!!" with vpunch
        c "그게 정말이에요?"
        hide me
        show ka haha
        l4 "그래."
        hide ka
        show me
        c "(이러면...어떻게 되는거지?)"
        c "(저게 실존하는 위치라는 거잖아?)"
        c "(종언서가 조작된 게 아닌건가?)"
        hide me
        show god
        g "(일단은 따라보시죠.)"
        g "(예의주시하고 있겠습니다.)"
        hide god
        if (suncount == 3):
            #해피 엔딩1 - 아크룩스 루트
            $ persistent.goodending1 = 1
            call happyending1 from _call_happyending1
            call credits_good from _call_credits_good
        elif (mooncount == 3):
            #해피 엔딩2 - 폴라리스 루트
            $ persistent.goodending2 = 1
            call happyending2 from _call_happyending2
            call credits_good from _call_credits_good_1
        elif (starcount == 3):
            #해피 엔딩3 - 클라우드 루트
            $ persistent.goodending3 = 1
            call happyending3 from _call_happyending3
            call credits_good from _call_credits_good_2
        else :
            $ persistent.normalending = 1
            call normalending from _call_normalending
            call credits_good from _call_credits_good_3
            #노말 엔딩
    else:
        $ persistent.badending4 = 1
        call badending4 from _call_badending4
        call credits_bad from _call_credits_bad
        #배드 엔딩
return

label restending:
    # 여가활동 4회 이상 배드엔딩
    play music "audio/badend.mp3"
    "(카리오트가 들어온다.)"
    show ka cham
    l4 "[name], 잠깐 나좀 보자."
    hide ka
    show me
    c "아, 네?"
    hide me
    show ka hah
    l4 "..."
    l4 "어이. [name]."
    l4 "이게 진짜 네 계획이였던 거야?"
    l4 "계속해서 쉬기만 하는게?"
    hide ka
    show me
    c "그... 그게,"
    hide me
    show ka hah
    l4 "너, 처음부터 의심스럽긴 했지만.."
    l4 "진짜 구원자고 뭐고 아무것도 아니였던 거냐?"
    show ka cham
    l4 "교주들은 착하니까 너한테 뭐라고 하지 않았겠지만.."
    show ka hah
    l4 "나는 아니거든."
    l4 "오전 활동은 아무것도 안 하고, 계속 쉬기만 하고..."
    show ka seri
    l4 "..."
    l4 "이제 진짜 시간도 얼마 안 남았는데,"
    show ka ssha
    l4 "이제와서 대체 뭘 할 수 있지?"
    l4 "아니, 애당초 너에게 계획이란게 존재하긴 하는건가?"
    show ka seri
    l4 "너 때문에 모든게 어그러졌어."
    l4 "이제... 어떤 재앙이 일어나더라도 막을 수 없을거라고."
    l4 "나와 교주들은 너를 신뢰했는데.."
    l4 "...하아"
    show ka hah
    l4 "처음부터 맡기는 게 아니였는데."
    hide ka
    show me
    c "(진짜 망했다..)"
    c "(신뢰를 완전히 잃어버렸어..)"
    c "(이제 와서 재앙이 절대 일어나지 않을거라고 말해도 \n전혀 먹히지 않을꺼야....)"
    c "(흑막을 찾는 것도 불가능할 거고...)"
    hide me
    show god
    g "(...[name]님.)"
    g "(시원하게 말아드셨군요.)"
    hide god
    show me
    c "(.........)"
    hide me
    show god
    g "(아무래도 이번엔 여기까지인가 봅니다.)"
    g "(저는 세계를 다시 되돌리고..)"
    g "(세계선을 새롭게 분리시킨 다음,)"
    g "(다른 용사님을 물색해야겠습니다.)"
    g "(자칫하면 세계 자체가 소멸될 수도 있는 \n굉장히 리스크있는 일이지만..)"
    g "(어쩌겠어요, 방법이 없는 걸.)"
    g "(어찌됐건, 고생하셨습니다. [name]님...)"
    hide god
    show me
    c "(...............)"
    c "(혹시라도, 혹시라도 다음 기회가 주어진다면.)"
    c "(여가 활동에 너무 매몰되지 말자..)"
    hide me
    stop music fadeout 2.0
    "Bad Ending #5\n휴식은 적당히"
    jump credits_bad

return

label happyending1:
    "(아크룩스가 들어온다.)"
    stop music fadeout 2.0
    play music "audio/battle.mp3" fadein 2.0 loop
    show ak hmm
    l1 "[name]님!"
    hide ak
    show me
    c "예, 아크룩스님?"
    hide me
    show ak std
    l1 "슈퍼노바 자매들의 정보에 따르면.."
    show ak mad
    l1 "중앙 정부가 위치한 아폴로 성의 뒷산에서, \n오후 9시 경 재앙이 재현될 거라고 해요."
    show ak std
    l1 "그곳으로.. 함께 가시죠."
    l1 "이곳으로부터 북쪽으로 좀 많이 떨어져 있는지라.."
    l1 "가는 데 시간이 좀 걸릴 겁니다. \n지금 이동하는 편이 좋을 것 같아요."
    hide ak
    show me
    c "...!"
    c "네!!"
    hide me
    scene background_backmo with dissolve
    "예언 당일, 20시 50분"
    "아폴로 성, 뒷산 인근"
    show me
    c "여기인가..."
    hide me
    show ak std
    l1 "이 산은.."
    l1 "먼 옛날, 문명을 이룩했었다고 해요."
    l1 "하지만 에크모트의 강림이라는 재앙으로..."
    l1 "모든 주민들이 희생당하고 말았죠."
    l1 "..."
    l1 "예언까지 앞으로 10분..."
    show ak mad
    l1 "이번에는.. 무슨 일이 있어도."
    l1 "클린스타클을 지킬 거에요."
    hide ak
    show me
    c "아크룩스 님.."
    hide me
    show ak std
    l1 "[name]님..."
    l1 "저는 사실.. 이 나라를 원망했어요."
    hide ak
    show me    
    c "!"
    hide me
    show ak std
    stop music fadeout 2.0
    play music "audio/sad.mp3"
    l1 "슈퍼노바의 교주씩이나 돼서 할 말은 아닙니다만.."
    l1 "어릴 적, 우연히 스승님을 따라갔다가 \n정치인들간의 다툼을 본 적이 있어요."
    l1 "종교를 위하는 척을 하면서\n사실은 자기 밥그릇 싸움을 하는 정계 위원들을 보면서,"
    l1 "겉과 속이 너무나도 다른 이 나라에..\n환멸감이 느껴질 정도였어요."
    l1 "그래서 저번에 태양을 관측하면서도..\n계속해서 회의감이 들었던 거고요."
    l1 "하지만..."
    l1 "[name]님과 계속해서 행동하다 보니.."
    show ak ha
    l1 "이 세계, 모르고 살았던 아름다운 경치들이 참 많았더라고요."
    l1 "지저귀는 새들이라던가...\n붉게 피어오르는 석양의 장관이라던가..."
    show ak mad
    l1 "비록 뒷사정은 마음에 들지 않지만."
    show ak ha
    l1 "그렇다고 그 아름다운 자연들까지 \n모조리 싫어하지는 않던 거였어요."
    l1 "아니, 어쩌면.. 이 나라를 사랑했던 걸지도 모르겠네요."
    l1 "그리고 이 아름다운 나라를 \n'어르신'들이 훼방놓는 게 미웠던 거고요."
    l1 "저도 몰랐던 제 속마음이에요."
    l1 "그걸 [name]님께서 자각하게 해주셨어요."
    hide ak
    show me
    c "맞아요."
    c "긍정적인 부분만을 바라보는 건 분명 쉽지 않아요."
    c "하지만..."
    c "부정적인 부분만을 바라보려고 한다면,"
    c "계속에서 그것에만 사로잡히게 될 뿐이에요."
    c "고인물은.. \n다시 새로운 물로 바꿔내면 되는 거에요."
    c "긍정적인 부분만 바라보고 살기에도.."
    c "이 세상은 많이 바쁘거든요. 하하."
    hide me
    show ak ha
    l1 "..."
    l1 "다시금 감사드립니다."
    l1 "이 세계를 제대로 바라볼 수 있게 해주셔서."
    l1 "그리고..."
    hide ak
    show image "backgrounds/ecmot.png" with dissolve
    l1 "함께 이 장관을 바라볼 수 있게 해주셔서요."
    c "아...."
    c "이건... 별똥별."
    c "아름답네요."
    l1 "[name]님."
    l1 "그거 아세요?"
    c "네?"
    l1 "사실... 재앙은 존재하지 않았었어요."
    c "?!"
    c "그걸.. 어떻게?!"
    c "알고 계셨던 거에요?"
    l1 "어제의 활동을 마치고 나서, \n슈퍼노바의 과학자들에게 연락이 왔어요."
    l1 "종언서의 구절에서 말하는 위치 좌표와,\n과거의 데이터를 대조해서 분석해본 결과..."
    l1 "종언서에서 말하는 에크모트(Ecmot)는,"
    l1 "수백 년 주기로 클린스타클에 다시 돌아오는.."
    l1 "혜성(Comet)이였던 거에요."
    c "!!!!!" with vpunch
    c "혜성......!"
    c "혹시, 이 산 인근..."
    c "그 당시에 큰 피해를 입었다는 게..?"
    l1 "눈치채셨군요, 맞아요."
    l1 "약 600여년 전.. \n이곳에 에크모트의 파편이 일부 추락했고,"
    l1 "이곳의 주민들에게 큰 피해를 입혔다고 해요."
    c "역시!"
    c "(그렇다면.. 모든 의문점들이 설명이 돼!)"
    c "(종언서는 예언서 같은게 아니였던 거야.)"
    c "(그저 실제로 일어났었던 \n과거의 천문 현상을 기록했던 고서일 뿐.)"
    c "(과거의 사람들은..\n현대의 사람들에게 경고를 해준 거였어.)"
    c "(600년 뒤에 다시금 운석이 떨어질 수 있으니.. \n미리 대비를 하라고!)"
    c "(당연히 흑막같은 건.. 존재하지 않았고.)"
    l1 "[name]님."
    l1 "그동안 정말로 고생 많으셨습니다."
    l1 "종언서가..진짜 예언서가 아니란 걸 알고 계셨으면서도.."
    l1 "저희를 이끌어주셔서요."
    l1 "[name]님 덕분에 저희는 다시 단결할 수 있었어요."
    l1 "[name]님의 노고가 없으셨다면..\n이러한 진실을 알지 못했을 거에요."
    l1 "아니, 알았더라도.."
    l1 "지금처럼 받아들일 수는 없었겠죠."
    l1 "다시한번, 정말로 감사드립니다."
    c "....아크룩스 님."
    c "저야말로, 감사드립니다."
    c "제 말을 전적으로 신뢰해주셔서."
    c "그렇지 않았더라면.. 여기까지 오지도 못했을 거에요."
    c "...."
    c "에크모트..."
    c "정말로, 한 마리의 용과도 같군요."
    l1 "네."
    l1 "정말이지..."
    l1 "아름답습니다."
    scene black
    "그 이후..."
    "혹시라도 모를 운석 충돌 사태에 대비하기 위해 파견되었던 \n군사들은 아무 일이 없는 것을 확인하고 부대로 복귀했다."
    "재앙의 실현을 그 누구보다도 신뢰했었고 \n그것을 막기 위한 단합으로 민심을 챙기던 일부 정치 세력은.."
    "그것이 일개 천문 현상에 불과함에도 제대로 된 해석은 커녕 \n과대해석으로 국가적 혼란을 야기했다며 이후 완전히 입지를 잃었다."
    "비록 시민들은 그 1달 사이에 \n무슨 일이 일어난 지 전혀 모르지만."
    "나는...."
    "신에게 더없는 찬사를 받으며, \n이 세계에서 원하는 만큼 놀고먹고 있다가 가도 된다는 특혜아닌 특혜를 받았다."
    "그런지라..."
    ""
    "예언 당일로부터 2주일 후,"
    "슈퍼노바 관할구역, 헬리오스 성 어딘가"
    show ak hmm
    l1 "[name]님!"
    l1 "여기까지만 오면 됩니다!!"
    l1 "힘내세요!!"
    "아크룩스가 꼭 보여주고 싶은 곳이 있다고 해서..\n새벽부터 강행군 중이다."
    hide ak
    show me
    c "헤엑...... 헥..."
    c "너무..... 높은데요......"
    c "허억... 헉.."
    hide me
    show ak hmm
    l1 "조금만 더!!!!"
    hide ak
    show me
    c "하아....... 후우......."
    c "도착했다."
    hide me
    show ak ha
    l1 "수고 많으셨습니다!"
    l1 "앞을 내려다보시겠어요?"
    hide ak
    show me
    c "...하아....."
    "(언덕을 내려다본다.)"
    c ".....!!!"
    hide me
    scene background_hill with dissolve
    ""
    show me
    c "이 풍경은...!"
    hide me
    show ak haha
    l1 "어때요?"
    l1 "제가 꼭 모시고 오고 싶었습니다."
    hide ak
    show me
    c "...."
    c "정말 아름답군요."
    hide me
    show ak haha
    l1 "좋아하실 줄 알았어요."
    l1 "그럼... 지금부터 천천히 즐겨볼까요."
    l1 "백야... 언덕을요."
    hide ak
    ""
    "Happy Ending#1 : 백야"
return

label happyending2:
    "(폴라리스가 들어온다.)"
    stop music fadeout 2.0
    play music "audio/battle.mp3" fadein 2.0 loop
    show po wow
    l2 "[name] 오빠!"
    hide po
    show me
    c "폴라리스!"
    hide me
    show po hmm
    l2 "이클립스 언니 오빠들이 말해줬어!"
    l2 "중앙 정부가 위치한 아폴로 성의 뒷산에서, \n오후 9시쯤에 재앙이 재현될 거라고!"
    hide po
    show me
    c "!!!"
    c "그럼, 빨리 그 쪽으로 가야하는 거 아니야?!"
    hide me
    show po std
    l2 "응! 두 말 하면 잔소리지!"
    l2 "빨리 가자구!"
    hide po
    scene background_backmo with dissolve
    "예언 당일, 20시 50분"
    "아폴로 성, 뒷산 인근"
    show me
    c "여기인가..."
    hide me
    show po hmm
    l2 "북쪽이라 그런지, 완전 추운걸?"
    l2 "아폴로 성은.. 평생 처음 와보는 곳이야."
    l2 "교주가 되고서도 말이지."
    hide po
    show me
    c "응?"
    c "한 번도 중앙 정부쪽을 못 와봤다고?"
    stop music fadeout 2.0
    hide me
    show po sad
    l2 "..."
    l2 "전에도 얘기했겠지만.."
    l2 "아빠는 엄청나게 엄격한 분이였어."
    l2 "그런 일들에.. 나를 사실상 배제했었지."
    l2 "다 나를 위해서라고 늘 말씀하셨지만..."
    hide po
    show me
    c "어째서?"
    c "네가 후대 교주가 되려면..\n오히려 그런 일들을 미리 체험시켜줘야 하는거 아니야?"
    c "이해할 수 없는데."
    hide me
    show po sad
    l2 "그러게 말이지."
    play music "audio/sad.mp3"
    show po hmm
    l2 "..."
    show po sad
    l2 "사실, 전에는 솔직하게 말하지 못했는데."
    l2 "아빠는 나를 많이 못마땅해 하셨던 것 같아."
    l2 "아빠의 뒤를 이어서 내가 후대 교주가 되었는데도,"
    l2 "'어르신'들에게 거의 대부분의 일을 맡기셨었거든."
    l2 "진중함이라고는 찾아볼 수 없는 성격에.."
    show po ssha
    l2 "어딘가 엉성한 느낌이 많잖아? \n아무래도...헤헤."
    l2 "완벽주의자인 아빠에게.. 나는 결점같은 존재였나봐."
    hide po
    show me
    c "폴라리스..그런 취급을 받아왔던거야..?"
    c "그건.. 너무하잖아!"
    hide me
    show po hmm
    l2 "오빠 생각에도.. 그렇지?"
    l2 "겉으로는 멀쩡한 척, 천진난만한 척 했지만 말야,"
    show po sad
    l2 "많이 울었었어. 혼자서.."
    l2 "나도 다른 두 언니들과 같은 교육을 받았고.."
    l2 "혼자서도 잘 해낼 수 있을 거라고 생각했어."
    l2 "그런데 다른 사람들의 생각은 \n그렇지 않았다는 거잖아?"
    l2 "속으로 정말 슬펐어."
    l2 "..."
    show po haha
    l2 "그래도..이젠 괜찮아."
    l2 "오빠만큼은.. 나의 있는 그대로의 모습을 받아줬어."
    l2 "그러면서도.. 모든 일에는 함께 데려가줬지."
    l2 "단 한 명이라도 나를 믿어준다면..."
    show po ang
    l2 "아니지!"
    l2 "[name] 오빠, 아크룩스 언니, 클라우드 언니, 카리오트 씨..."
    l2 "이렇게나 나를 믿어주는 사람들이 많았잖아?!"
    show po std
    l2 "어쨌든..그거면, 된거야."
    l2 "나를 믿어주는 사람들이 있으니까.."
    show po haha
    l2 "나를 믿어주지 못하는 사람들의 마음도,\n하나 하나 바꿔가면 되는 거잖아?"
    hide po
    show me
    c "맞아."
    c "다른 모두에게 네가 교주가 되기에 \n부족함이 없음을 보여주면.."
    c "여론은 서서히 바뀌어 나갈 거야."
    hide me
    show po std
    l2 "응! 바로 그 말이야!"
    l2 "고마워 오빠."
    l2 "나를 믿어줘서."
    l2 "그믐달이였던 내 마음을..."
    hide po
    show image "backgrounds/ecmot.png" with dissolve
    l2 "보름달로 채워줘서."
    c "!"
    c "이건.. 별똥별?"
    l2 "맞아!"
    l2 "진짜 예쁘지?"
    l2 "이거 진짜 보기 쉽지 않은건데~ \n오빠 운이 좋은 거야."
    c "응..정말 예뻐."
    c "우리 세계에서도.."
    c "별똥별을 보기는 쉽지 않거든."
    c "그런데.."
    c "지금 시간이..."
    c "9시 2분?!" with vpunch
    c "뭐야?!"
    c "재앙은?!"
    l2 "흐히히히.."
    l2 "재앙은...."
    l2 "없었습니다!!!!"
    c "응?!" with vpunch
    c "너.. 알고 있던 거였어?"
    l2 "응?"
    l2 "그럼~ 내가 누군데!"
    l2 "...장난이고, 이클립스 똑똑이 언니 오빠들이 말해줬어."
    l2 "에크모트(Ecmot)는.. 괴물이 아니였다고!"
    l2 "...사실은, '운석'(Comet)이였던 거지!"
    l2 "그것도.. 아~주 긴 시간을 거쳐서 돌아오는!"
    c "!!"
    c "(그런 거였나!)"
    l2 "수백년 전에..이 마을에 저 에크모트 혜성의 파편이 떨어졌다고 해."
    l2 "그로 인해 수많은 사람들이 다치거나 죽었고 말이야."
    c "(그렇다면.. 모든 의문점들이 설명이 돼!)"
    c "(종언서는 예언서 같은게 아니였던 거야.)"
    c "(그저 실제로 일어났었던 \n과거의 천문 현상을 기록했던 고서일 뿐.)"
    c "(과거의 사람들은..\n현대의 사람들에게 경고를 해준 거였어.)"
    c "(600년 뒤에 다시금 운석이 떨어질 수 있으니.. \n미리 대비를 하라고!)"
    c "(당연히 흑막같은 건.. 존재하지 않았고.)"
    l2 "[name] 오빠."
    l2 "다시 한번, 정말 고마워."
    l2 "나를 이끌어줘서!"
    l2 "오빠 덕분에.."
    l2 "다시 이클립스를 이끌어나가 볼 용기가 생겼어!"
    l2 "더 이상.. 나는 혼자가 아니야."
    l2 "나를 믿어주는 사람들이 있으니까!"
    c "...!"
    c "그래!"
    c "너를 진심으로 믿어, 폴라리스!"
    c "너는.. 어엿한 한 교단의 교주니까!"
    l2 "응!"
    scene black
    "그 이후..."
    "혹시라도 모를 운석 충돌 사태에 대비하기 위해 파견되었던 \n군사들은 아무 일이 없는 것을 확인하고 부대로 복귀했다."
    "재앙의 실현을 그 누구보다도 신뢰했었고 \n그것을 막기 위한 단합으로 민심을 챙기던 일부 정치 세력은.."
    "그것이 일개 천문 현상에 불과함에도 제대로 된 해석은 커녕 \n과대해석으로 국가적 혼란을 야기했다며 이후 완전히 입지를 잃었다."
    "비록 시민들은 그 1달 사이에 \n무슨 일이 일어난 지 전혀 모르지만."
    "나는...."
    "신에게 더없는 찬사를 받으며, \n이 세계에서 원하는 만큼 놀고먹고 있다가 가도 된다는 특혜아닌 특혜를 받았다."
    "그런지라..."
    "예언 당일로부터 2주일 후,"
    "이클립스 관할 구역 어딘가"
    show po std
    l2 "[name] 오빠!"
    l2 "이쪽이야!"
    hide po
    show me
    c "그래! 따라가고 있다고!"
    c "걸음이 정말 빠르네.."
    "오늘은 정말 대단한 걸 보여준다는 폴라리스의 말에,\n늦은 밤이지만 발걸음을 서두르고 있는 것이다."
    c "..."
    c "여긴가?"
    c "!!"
    hide me
    scene background_supermoon with dissolve
    ""
    show po std
    l2 "도착했어!"
    l2 "그 때 봤었던 달보다 훨~씬 크지?!"
    show po haha
    l2 "'초 슈퍼 슈퍼 문'일지도 몰라, 이건!!"
    hide po
    show me
    c "정말.."
    c "내가 지금까지 봐왔던 그 어떤 달보다.. 크고 밝아!"
    hide me
    show po haha
    l2 "히히."
    l2 "매번 참 만족스러운 반응이란 말이지."
    show po std
    l2 "그럼.. 보름달을 봤으니까 소원을 빌어야겠지?!"
    hide po
    show me
    c "그래."
    c "..."
    c "(이 세계에.. 평화가 함께하길.)"
    c "(그리고...)"
    c "(폴라리스가 행복할 수 있기를.)"
    hide me
    show po hmm
    l2 "... 다 빌었어?"
    hide po
    show me
    c "응."
    hide me
    show po std
    l2 "뭐라고 빌었어?"
    hide po
    show me
    c "별 건 아니고.."
    c "이 세계가 평화로울 수 있게 해달라고."
    c "너는?"
    hide me
    show po hmm
    l2 "나?"
    l2 "나는...."
    show po haha
    l2 "비~밀!!!!!" with vpunch
    hide po
    ""
    "Happy Ending#2 망(望)"
return
    

label happyending3:
    "(클라우드가 들어온다.)"
    stop music fadeout 2.0
    play music "audio/battle.mp3" fadein 2.0 loop
    show cl dead
    l3 "[name]님!"
    hide cl
    show me
    c "네, 클라우드 씨!"
    show cl gal
    l3 "아스트라 자매들이 알려준 정보에 따르면..."
    l3 "중앙 정부가 위치한 아폴로 성의 뒷산에서, \n오후 9시 쯤 재앙의 재현이 일어날 거라고 해요!"
    hide cl
    show me
    c "!!!" with vpunch
    c "그렇다면 한시라도 빨리 그쪽으로 가죠!"
    hide me
    show cl moo
    l3 "네!"
    l3 "이동 차량과 자원을 준비하겠습니다!"
    hide cl
    scene background_backmo with dissolve
    "예언 당일, 20시 50분"
    "아폴로 성, 뒷산 인근"
    show cl moo
    l3 "도착했네요."
    l3 "예언 시간까지는.. 10분정도 남았네요."
    hide cl
    show me
    c "생각보다 너무 오래 걸렸어요."
    c "클린스타클.. 사실은 엄청 넓은 나라였구나."
    hide me
    show cl moo
    l3 "여긴.. 클린스타클의 중심이 되는 성.. 아폴로에요."
    l3 "슈퍼노바의 전신인 라니아의 영토였던 곳이죠."
    l3 "위도가 높은 편이라.. \n일년 내내 겨울인 곳이기도 하구요."
    show cl hmm
    l3 "그보다도..뒷산에 이런 자그마한 마을이 있었다니."
    l3 "몰랐어요.."
    hide cl
    show me
    c "아무래도, 나라 전역을 안다는 게 쉽지는 않겠죠."
    hide me
    show cl moo
    l3 "그러게요."
    l3 "정말 여기저기 돌아다녔다고 생각했는데."
    l3 "아직도 모르는 지역이 있다니.."
    hide cl
    show me
    c "클라우드 님 정도면 정말 활동적인 편인걸요?"
    c "(당장 나는 지구의 내 집 근처도 잘 모르니까..)"
    stop music fadeout 2.0
    hide me
    show cl moo
    l3 "..."
    l3 "[name]님.."
    show cl std
    l3 "오늘따라, 밤하늘에 별이 참 많이 보이네요."
    l3 "근처에 건물들의 불빛이 적어서일까요?"
    hide cl
    show me
    c "정말이네요."
    c "그 때, 별자리를 관측했을 때보다..\n훨씬 더 많은 것 같아요."
    play music "audio/sad.mp3"
    hide me
    show cl std
    l3 "갑자기 떠오른 이야기 하나 해드릴까요?"
    l3 "아스트라가 하늘을 숭배하는 이유는.."
    l3 "하늘이 세계를 비추는 도화지와도 같다고 생각하기 때문이에요."
    show cl hmm
    l3 "하늘을 바라보고 있으면.. 생각보다 많은 일들이 일어난다는 거.\n알고 계셨나요?"
    l3 "하늘을 가로지르는 수많은 사람들의 노고가 담긴 비행기,"
    l3 "하늘로 날아오르는 어린아이의 동심과 같은 풍선들,"
    show cl std
    l3 "하늘에서 보이는 모든 것들은,\n사실 우리 세계를 비추는 거울이랍니다."
    l3 "그리고 하늘에서 우리를 조용히 바라보면서 \n무어라 속삭이는 신의 작은 눈동자를.."
    l3 "아스트라는 '별'이라고 생각해요."
    l3 "저 작은 별 하나하나가.. 저희를 굽어살피고 있다라고 믿는 거에요."
    hide cl
    show me
    c "오..."
    c "굉장히 상상력이 풍부한 종교군요, 아스트라는."
    hide me
    show cl haha
    l3 "아하하~!"
    l3 "칭찬으로 들을게요!"
    show cl std
    l3 "아스트라는 기상현상들도 재미있게 해석했답니다."
    l3 "신이 인간들을 노여워하실 때면.."
    l3 "하늘에 먹구름이 껴서 비가 내리고, \n천둥번개가 친다고 믿죠."
    l3 "비는 신님의 눈물이고.. 천둥번개는 신의 고함소리 이구요."
    show cl moo
    l3 "그리고.."
    l3 "신이 인간들을 굽어살피고자 하실때면.."
    show cl std
    l3 "하늘에 헤아릴 수 없을만큼 따스한 빛을 내리신다고 믿어요."
    l3 "[name]님의 세계에서는..."
    hide cl
    show image "backgrounds/ecmot.png" with dissolve
    l3 "별똥별이라고 불리는 존재죠."
    c "!"
    c "정말....아름답네요."
    c "마음 한켠이 찡해질 정도에요."
    l3 "별똥별은.. 정말 오랜만에 보는 것 같네요."
    l3 "오늘만큼은 신께서 저희 인간들을 보듬어주시는 걸까요?"
    c "..."
    c "하필 오늘같은 때에..?"
    c "어?! 그보다...."
    c "지금 시간이 몇시죠?!"
    c "10분을 훌쩍 넘겨버린 것 같은데..?!"
    c "!!" with vpunch
    c "9시 2분?!"
    l3 "어머, 벌써 시간이 그렇게 되었나요?"
    l3 "딱 알맞은 타이밍에 말씀드리려고 했는데.. 아쉬워요."
    l3 "이왕 늦어버린거, 바로 말씀드릴게요."
    l3 "[name]님!"
    l3 "재앙은.. 사실 없던 거였어요!"
    c "네?"
    c "대체 그게 무슨.."
    c "아니....그게 아니라, 알고 계셨던 거였어요?!"
    c "언제부터?"
    l3 "어제 밤에, \n종언서와 수많은 서적들을 대조하던 연구진에게서 연락이 왔어요."
    l3 "에크모트(Ecmot)는.. 재앙이 아니라,"
    l3 "혜성(Comet)이라고요."
    l3 "그것도... 주기가 수백년에 달하는 혜성이죠."
    c "!!!"
    c "에크모트가... 혜성?!"
    l3 "이 마을에는.."
    l3 "수백년 전, \n에크모트가 인근을 지날 때 떨어져 나온 파편이 충돌했어요."
    l3 "그로 인해 수많은 사람들이 피해를 입었었죠."
    l3 "종언서는..."
    l3 "'예언서' 같은 게 아니였어요."
    l3 "바로..그 때의 기록을 해둔 '역사서' 였던 거에요."
    l3 "에크모트를 마치 살아있는 재앙과도 같이 묘사해서.."
    l3 "후대에게 경고를 해주고 싶었던 거죠."
    c "(그런 거였나..)"
    c "(그렇다면.. 별다른 흑막이 없는 것도 설명이 돼.)"
    c "그게.. 진실이였군요..."
    c "다행이야..."
    c "별 일이 없어서.."
    l3 "안심하긴 이르다구요?"
    l3 "이번에도 파편이 충돌할 수도 있는걸요~"
    c "?!" with vpunch
    l3 "아하하~ 장난이에요."
    l3 "분석 결과 이번에는 그럴 가능성이 0퍼센트에 수렴한다고 하네요."
    l3 "..."
    l3 "[name]님."
    l3 "정말 고생 많으셨어요."
    l3 "종언서가.. 진짜 예언서가 아니라는 걸 알고 계셨던 거죠?"
    c "...네."
    l3 "하지만.. 저희들의 신념을 위해서 묵언하셨던 거고요."
    l3 "...감사드려요, 그 상냥함에."
    l3 "덕분에... 클린스타클은 다시 화합할 수 있었어요."
    l3 "불신과 견제의 과거를 딛고.."
    l3 "그리고 재앙이 일어나지 않았다는 사실에, \n종언서의 내용도 거짓이 아니라는 사실에도요."
    l3 "모두 [name]님 덕분이에요."
    c "아, 아뇨. 제가 한 게 뭐가 있다고요.."
    c "모두 절 믿고 따라준 클라우드 씨 덕분입니다."
    l3 "...후훗."
    l3 "마지막까지 겸손하시네요~"
    l3 "뭐.. 그런 모습이 매력있는 거지만요."
    l3 "이번 별똥별은.."
    l3 "정말로 신께서 저희에게 내려주시는 찬사같네요."
    l3 "하늘은 정말이지.."
    l3 "이 세계를 비추는 거대한 거울같아요."
    c "그러게요."
    scene black with dissolve
    "그 이후..."
    "혹시라도 모를 운석 충돌 사태에 대비하기 위해 파견되었던 \n군사들은 아무 일이 없는 것을 확인하고 부대로 복귀했다."
    "재앙의 실현을 그 누구보다도 신뢰했었고 \n그것을 막기 위한 단합으로 민심을 챙기던 일부 정치 세력은.."
    "그것이 일개 천문 현상에 불과함에도 제대로 된 해석은 커녕 \n과대해석으로 국가적 혼란을 야기했다며 이후 완전히 입지를 잃었다."
    "비록 시민들은 그 1달 사이에 \n무슨 일이 일어난 지 전혀 모르지만."
    "나는...."
    "신에게 더없는 찬사를 받으며, \n이 세계에서 원하는 만큼 놀고먹고 있다가 가도 된다는 특혜아닌 특혜를 받았다."
    "그런지라..."
    "예언 당일로부터 2주일 후"
    scene background_park with dissolve
    show cl hmm
    l3 "그래서.."
    l3 "[name]님의 원래 세계에서,"
    show cl std
    l3 "[name]님은 대학생이였다는 거네요?"
    l3 "대학이라 함은.. 고등 교육 기관이고요."
    hide cl
    show me
    c "그렇습니다."
    hide me
    show cl haha
    l3 "멋지네요!"
    l3 "클린스타클에서 잠시 재능기부도 해보시지 않겠어요?"
    hide cl
    show me
    c "컥!"
    c "그.. 그정도 급은 아닙니다.."
    hide me
    "세계가 어느정도 다시 안정된 뒤, \n클라우드 씨와 여유를 즐기고 있는 중이다."
    show cl hmm
    l3 "날씨가 점점 추워지네요."
    l3 "곧 겨울이 되겠는걸요~"
    hide cl
    show me
    c "그러게요."
    c "내년부턴 뭔가 달라지겠죠, 이곳도?"
    hide me
    show cl haha
    l3 "아하하~..과연 어떨까요?"
    show cl moo
    l3 "그간은 정말 반쪽짜리의 교주 직책이였는데.."
    show cl std
    l3 "이번 사건 이후로 많이 개편된다고 하네요."
    hide cl
    show me
    c "다시 바빠지시겠는데요?"
    hide me
    show cl std
    l3 "어쩔 수 없는걸요, 교주의 일이니까요."
    show cl moo
    l3 "그래도.."
    show cl std
    l3 "[name]님 덕분에 많은 게 바로잡혔어요."
    show cl doki
    l3 "그리고.. 소중한 사람들도 지킬 수 있었고요."
    hide cl
    show me
    c "네."
    c "다른 교주들도.. 카리오트 씨도... 클라우드 씨도.."
    hide me
    show cl doki
    l3 "한 명이 빠졌는걸요?"
    hide cl
    show me 
    c "네?"
    c "그게 누구..."
    hide me
    show cl moo
    l3 "아~ 뭔가 출출해졌어요."
    l3 "점심이라도 먹으러 갈까요?"
    hide cl
    show me
    c "...그러게요. 저도 배고픈 것 같아요."
    c "슬슬 일어날까요?"
    hide me
    show cl doki
    l3 "........"
    show cl hcb
    l3 "바보~"
    hide cl
    ""
    "Happy Ending#3 : 하늘은 세계의 거울"

return

label normalending:
    stop music fadeout 2.0
    play music "audio/battle.mp3" fadein 2.0 loop
    "(모든 교주들이 들어온다.)"
    show ak mad
    l1 "[name]님! 어서 준비를!"
    hide ak
    show po hmm
    l2 "맞아! 시간이 얼마 없다구!"
    l2 "거긴 여기서 엄~청 멀단 말야!"
    hide po
    show cl hmm
    l3 "어서 아폴로 성으로 이동하죠!"
    hide cl
    show me
    c "모두들..!"
    c "네!!"
    hide me
    scene background_backmo with dissolve
    "예언 당일, 20시 50분"
    "아폴로 성, 뒷산 인근"
    show me
    c "예언까지 10분 남기고.. 간신히 도착했다."
    c "이곳이.. 예언서에서 말한 장소."
    hide me
    show po ho
    l2 "엄청 아기자기한 마을들도 있어!"
    hide po
    show cl haha
    l3 "그러게요~ 이런 곳이 있는 줄은.."
    l3 "이쪽은 대부분 설원 지대인줄 알았는데 말이죠."
    hide cl
    show ak std
    l1 "종언서에 따르면.."
    l1 "먼 옛날, 에크모트가 이곳에 강림했을 때.."
    l1 "이곳의 주민들이 큰 해를 입었다고 하네요."
    hide ak
    show cl moo
    l3 "에크모트..."
    l3 "대체 얼마나 강력한 괴물인거죠?"
    hide cl
    show po std
    l2 "하지만 클린스타클의 병사들도 함께 있다고!"
    l2 "무서울 건 하나도 없어!!"
    hide po
    show me
    c "맞아."
    c "모두가 함께라면..."
    hide me
    "(하늘에서 뭔가 보이기 시작한다.)"
    show me
    c "!!" with vpunch
    c "저건...!"
    hide me
    show image "backgrounds/ecmot.png" with dissolve
    ""
    show ak std
    l1 "별똥별?"
    hide ak
    show po ho
    l2 "예쁘다~ 별똥별은 살면서 거의 못봤는데."
    hide po
    show cl std
    l3 "그러게요. 마치 한 마리의 용과도 같네요."
    hide cl
    show me
    c "... 이런 타이밍에 별똥별이라니."
    c "...어?"
    c "잠깐만..지금 시간이.."
    c "?!" with vpunch
    c "9시.. 정각?!"
    c "재앙은..?!"
    hide me
    show ak awk
    l1 "...!!"
    hide ak
    show po wow
    l2 "뭐지?!"
    hide po
    show cl dead
    l3 "예언 시간이... 도래했는데.."
    l3 "아무런 변화가?"
    hide cl
    show me
    scene black with dissolve
    c "(잠깐!)"
    c "(뭔가 떠오를 것만 같다.)"
    c "(종언서에서 재앙을 묘사한 구절.. 뭐라고 나와있었지?)"
    hide me
    $ i = True
    while (i):
        menu : 
            "종언서의 구절은"

            "짐승의 모습을 한 재앙":
                $ i = False

            "천사의 모습을 한 재앙":
                "이건 아니였던 것 같아."

            "악마의 모습을 한 재앙":
                "이건 아니였던 것 같아."
    show me
    c "(그래.. 짐승의 모습을 한 재앙..!)"
    c "(클라우드 씨의 말대로... \n저 별똥별... 마치 한마리의 용과도 같다.)"
    c "(그렇다는 건!)"
    hide me
    $ i = True
    while (i):
        menu :
            "에크모트의 정체는"
            
            "용":
                "용 그 자체는 아니지 않을까?"

            "혜성":
                $ i = False
            
            "클라우드 씨":
                "이건 진짜 아닐거 같은데?"
    stop music fadeout 2.0
    play music "audio/sad.mp3" fadein 2.0 loop
    scene background_backmo with dissolve
    show me
    c "... 알아낸 것 같아요."
    hide me
    show ak eh
    l1 "네?"
    hide ak
    show po hmm
    l2 "뭘 말이야?"
    hide po
    show me
    c "재앙의 정체에 대해서요."
    hide me
    show cl hmm
    l3 "뭔가 알아내셨군요!!"
    hide cl
    show ak hmm
    l1 "그 정체가 뭐죠?"
    hide ak
    show me
    c "재앙.. 그러니까 에크모트(Ecmot)는..."
    c "'혜성(Comet)'이였던 거에요."
    hide me
    show ak wow
    l1 "...!!" with vpunch
    hide ak
    show po wow
    l2 "혜성!!" with vpunch
    hide po
    show cl dead
    l3 "에크모트가.. 혜성?" with vpunch
    hide cl
    show me
    c "네. 그것도.. 주기가 엄청나게 긴 혜성인거죠."
    c "이 마을이 먼 옛날에 입었었다는 재앙.."
    c "그건 저 에크모트 혜성의 파편이 떨어져 충돌했던 거에요."
    hide me
    show cl moo
    l3 "그 말이 사실이라면.."
    l3 "클린스타클의 역사서들을 살펴보면 검증이 될 거에요."
    hide cl
    show ak std
    l1 "안 그래도 지금 아카이브를 뒤지는 중이야."
    show ak wow
    l1 "...!"
    l1 "XXXX년 XX월 XX일...\n아폴로 성 인근 마을에 운석이 충돌.."
    l1 "운석은.. 주기가 수백년에 달하는 것으로 추정..."
    hide ak
    show po wow
    l2 "정말이야..!"
    l2 "[name] 오빠 말대로야!"
    hide po
    show me
    c "..."
    c "(이제야 종언서에 대한 모든 의문이 풀렸어.)"
    c "(어째서 흑막이 존재하지 않는지도.)"
    c "종언서는... 그저 역사서였을 뿐이에요."
    c "그것도.. 아주 엄밀하게 서술된.."
    c "먼 훗날.. 후손들이 같은 피해를 입지 않았으면 하는\n선조들의 경고가 적혀있던 거에요."
    c "다만 그게 시간이 지나고 와전되면서.."
    c "일종의 예언서와도 같이 변질된거죠."
    hide me
    show ak awk
    l1 "그런 거였나...!"
    l1 "우연으로 치부하기에는.."
    l1 "너무나도 딱 맞아 떨어지는 과거의 사례.."
    hide ak
    show po hmm
    l2 "그게.. 종언서의 진실이였구나."
    show po std
    l2 "하긴~ 우리 클린스타클에선 그간\n정말 별별 예언서들을 다 파해쳤는데!"
    l2 "저게 이제와서 뜬금포로 나온데다가,\n해석조차 더딘 게 말이 안됐지!"
    hide po
    show cl moo
    l3 "과연..."
    l3 "드디어 모든 퍼즐이 맞춰지는 것 같네요.."
    hide cl
    show me
    c "...."
    c "다행이네요."
    c "에크모트가.. 진짜 재앙이 아니였어서."
    hide me
    show ak ha
    l1 "아닙니다."
    l1 "[name]님의 노고가 있었기에, 여기까지 진척할 수 있었던 거에요."
    hide ak
    show po ho
    l2 "맞아!"
    show po ang
    l2 "우리 정말 1주일 전까지만 해도 아무것도 몰랐는걸?"
    hide po
    show cl awk
    l3 "정작 여기에 와서까지도 그 사실을 일말조차 몰랐으니까요."
    l3 "어째서 그 누구도 저게 혜성이라는 생각조차 못했던 걸까요?"
    hide cl
    show ak std
    l1 "아닌게 아니라.."
    show ak ha
    l1 "[name]님 뿐 아니라...모두들, 정말 고생했어."
    l1 "각 교단 혼자서는 분명 벅찼을 일이야."
    hide ak
    show po std
    l2 "맞아! 특히 나 혼자서는 진짜 아무것도 알아내지 못했을 거라구~"
    show po haha
    l2 "언니들이 같이 도와준 덕분에 더 수월했어!!"
    hide po
    show cl haha
    l3 "아하하~ 옛날 기억이 떠오르네요."
    l3 "그땐 정말 모두 한 몸이 된 것처럼 생활했었는데 말이죠."
    hide cl
    show ak sad
    l1 "...어째서 이렇게까지 서로 견제하게 된 걸까?"
    hide ak
    show po sad
    l2 "옛날엔 다들 사이 좋았는데 말이야."
    hide po
    show me
    c "(...이건 역시 '어르신'들의 영향이겠지.)"
    hide me
    show cl std
    l3 "뭐! 아무렴 어때요~"
    l3 "지금부터라도.. 이번 종말 막기를 교훈삼아서!"
    show cl haha
    l3 "다시 함께 사이좋게 발전을 도모하면 되는 거 아니겠어요?"
    hide cl
    show ak haha
    l1 "맞아."
    show ak mad
    l1 "이번 사태도.. 전적으로 그 양반들의 주도로 이루어졌지."
    l1 "처음부터 뭔가 과할 정도로 호들갑떤다 싶었었는데.."
    l1 "역시 내부의 혼란을 잠재우는 건 공동의 적이다.. 이건가."
    l1 "우리들은.. 정계의 노인네들과는 달라져야만 해."
    hide ak
    show po mad
    l2 "그 할아버지들~ 난 완전 투명인간 취급한다니깐?"
    l2 "어리다고 무시하는 거야 뭐야!"
    hide po
    show cl moo
    l3 "다들 아픈 과거를 하나씩은 가지고 있는 법이죠."
    show cl std
    l3 "모쪼록.. 함께 클린스타클에 변화의 바람을 일으켜봐요."
    l3 "그건.. 우리만이 할 수 있는 일이에요."
    hide cl
    show ak ha
    l1 "좋아."
    l1 "그동안에는 여러 사정으로 불가능했었지만.."
    l1 "앞으로는 보다 많이 왕래하자고."
    show ak haha
    l1 "정계의 간섭으로부터 벗어나려면,\n먼저 종교계의 단합이 선행되어야 할테니까."
    hide ak
    show po ho
    l2 "응응!"
    l2 "난 아빠랑 다르니까! 언니들이랑 함께할거라고!"
    hide po
    show me
    c "...바람직한 방향성입니다."
    c "비록 이방인이지만.. 응원할게요."
    hide me
    show po ang
    l2 "이방인이라니?!"
    show po haha
    l2 "오빠도 어엿한 클린스타클 식구인걸?"
    hide po
    show cl haha
    l3 "아하핫~ 정말로. 혼자만 빠져나가려고!"
    hide cl
    show ak ha
    l1 "훗."
    l1 "바람이.... 부네요."
    hide ak
    "변화의 바람이."
    scene black with dissolve
    ""
    "그 이후로..클린스타클은 어떻게 되었을까?"
    "과거의 혼란을 청산하고.. 새로운 미래로 나아갔을까?"
    "나는 그동안의 피로가 누적된 탓인지 쓰러지다시피 잠들었고.."
    show image "backgrounds/내방.jpg" with dissolve
    "정신을 차려보니 다시금 내 방에 돌아와 있었다."
    "꿈이라고 생각하기에는 너무나도 생생했던 1주일간의 소동이였다."
    "무엇보다도.. 머리맡에 놓여진 메모.."
    "'이번에는 정말 실례드렸습니다. 조만간 용사님 세계의 신으로부터 보답이 올 거에요. \n-이세계 신-'"
    show me
    c "이건 역시.. 그 모든 게 진짜였다는 거겠지?"
    c "그나저나, 막무가내로 불러놓고는.."
    c "일이 해결됐으니 곧바로 원래 세계로 보내버리다니."
    c "뭔가 시원섭섭한 기분인걸."
    c "그래도 이세계 용사 라이프인데~\n조금은 즐겨보고 싶었단 말야."
    c "..."
    c "보답이라..."
    c "뭐.."
    c "다음 번 게임 가챠에서 대박나기 정도면 좋겠는데."
    c "...잠깐, 지금 며칠이나 지났지??"
    c "!!!" with vpunch
    c "보름이나 지나갔잖아.. 벌써?!"
    c "자취생에다가 아싸였으니 망정이지..\n하마터면 실종신고 당할 뻔 했군."
    c "..."
    c "모르겠다~ 그동안 밀렸던 일퀘나 해야겠다."
    hide me
    ""
    "Normal Ending : 새로운 바람"
return

label badending4:
    play music "audio/think.mp3" fadein 2.0 loop
    scene background_bedroom with dissolve
    "예언 당일, 새벽"
    "[name]의 침실"
    show me
    c "..."
    c "망했다."
    c "알아낸 정보가 너무나도 없어.."
    c "이래서는 이도저도 아니잖아.."
    hide me
    show god
    g "(그러니까 말이에요~)"
    g "(제 안목이 틀렸던 걸까요?)"
    hide god
    show me
    c "(조용히 해!)" with vpunch
    c "(애당초 5일밖에 안되는 시간에 \n대체 뭘 어떻게 하라는거야!!)"
    c "(그리고 말이야,)"
    c "(이렇게 교주들과 협업하는 과정까지 이끌고 온 것도 \n온전히 내 힘으로 해온거잖아!!)"
    hide me
    show god
    g "(그건~ 용사님께서 충분히 이끌 능력이 된다는 판단 하에\n저는 지켜보기만 한..{nw})"
    hide god
    "(카리오트가 들어온다.)"
    show ka hmm
    l4 "[name]!"
    l4 "오늘.. 모든 게 결정나는군."
    l4 "뭔가 알아낸 건 있어?"
    hide ka
    show me
    c "..."
    c "안타깝게도.. 별로 없어요."
    c "최대한 노력했지만.."
    c "주어진 시간 자체가 너무나도 짧았어요."
    c "죄송합니다.."
    hide me
    show ka seri
    l4 ".......뭐,"
    show ka std
    l4 "어느정도 예상했던 부분이야."
    l4 "아무리 신께서 보낸 구원자라고 해도.."
    l4 "5일동안 아무런 정보도 없는 상태를 어떻게 해결하겠어."
    show ka haha
    l4 "그래도 고생했다."
    show ka std
    l4 "네가 열심히 일한 건.. 모두들 알고 있으니까."
    hide ka
    show me
    c "....감사합니다."
    hide me
    show ka std
    l4 "집무국에 다들 모여있어."
    l4 "그쪽으로 가서..\n앞으로 어떻게 되는지나 겸허하게 받아들이자고."
    hide ka
    stop music fadeout 2.0
    "(그렇게 카리오트와 함께 집무국으로 향했다.)"
    scene background_main with dissolve
    play music "badend.mp3" fadein 2.0 loop
    show po std
    l2 "오! 왔구나!"
    l2 "기다리고 있었어~"
    hide po
    show ak std
    l1 "오셨군요."
    l1 "클린스타클 정예군을 전역에 배치했습니다."
    l1 "혹시모를 사태에 대비하기 위해서요."
    l1 "저희는 여기에서 상황을 지켜보도록 하죠."
    hide ak
    show cl moo
    l3 "함께 기도드려요.."
    l3 "부디 신께서 굽어살피시길.."
    hide cl
    show me
    c "..네."
    hide me
    "예언 당일, 오후 9시"
    show me
    c "...."
    hide me
    show ak eh
    l1 "...."
    hide ak
    show po sad
    l2 "우웅...."
    hide po
    show cl awk
    l3 "아하하..."
    hide cl
    show ka seri
    l4 "어째서.. 아무 일도 일어나지 않는거지?"
    hide ka
    show ak eh
    l1 "그러게요."
    l1 "종언서에 나와있는 예언일은.. 분명 오늘일텐데.."
    hide ak
    show po hmm
    l2 "그...혹시.."
    l2 "종언서가 틀렸던 게 아닐까?"
    hide po
    show cl gal
    l3 "폴라리스!" with vpunch
    l3 "처음 종말 막기 때도 얘기했잖아."
    l3 "종언서에 의문을 갖는 건..\n신에게 의문을 품는 행위와 다를 바 없다고."
    l3 "장난으로라도 그런 말은 말아."
    hide cl
    show po sad
    l2 "하지마안~"
    l2 "우리가 5일동안 놀기만 한것도 아니고!"
    l2 "열심히 뛰어다녔는데 아무런 소득도 없었잖아!"
    l2 "그리고 심지어 우리만 일한것도 아니야!"
    l2 "완전 똑똑한 박사 오빠 언니들도 달라붙어서 \n종말 막기에만 몰두했는데.."
    l2 "아무런 증거를 못 찾는게 말이나 되냐고!"
    hide po
    show ak sad
    l1 "..."
    l1 "폴라리스의 응석을 감안하더라도.."
    l1 "솔직히 어느정도 동의하는 바야."
    l1 "여태까지의 예언서 분석 사례를 통틀어봐도.."
    l1 "이 정도로 아무 소득도 없었던 적은 없었어.."
    l1 "정말 이런 결론에 도달하고 싶지는 않았지만.."
    show ak eh
    l1 "종언서 자체가.. 조작됐던 건 아닐까..?"
    l1 "실제로 일부 연구진들이 제시한 가설이기도 하고."
    hide ak
    show cl no
    l3 "....!"
    l3 "아크룩스.. 너까지!"
    hide cl
    show ka seri
    l4 "어이, 분위기가 과열되는 것 같은데 진정해."
    l4 "아직 예언 당일이 끝나기까지 3시간이나 남아있다고."
    l4 "마지막까지 상황을 지켜본 다음에 판단해도 늦지 않아."
    hide ka
    show ak awk
    l1 "하지만 군부도 이제까지 별다른 이상징후는 없다고 하는데.."
    l1 "이러는 동안에 생기는 안보 공백도 감안해주셔야.."
    hide ak
    show cl gal
    l3 "그럼 다 그만둬!" with vpunch
    hide cl
    show me
    c "!!"
    hide me
    show cl no
    l3 "다들 이렇게 회의적이면서.. \n그동안 대체 어떻게 함께 일했었던 거야?"
    hide cl
    show ak no
    l1 "클라우드!"
    l1 "모든 예언서의 내용이 진실된다는 보장은 없어."
    l1 "우리가 종교 국가인 건 맞지만..\n한편으로는 과학의 국가기도 하잖아."
    l1 "이성적으로 바라볼 사안은 이성적으로 바라보자고!"
    l1 "분석 데이터 상으로도 그렇고..\n우리가 실제로 체감하고 있기에도.."
    l1 "지금 계속 쳇바퀴만 돌고 있다는 생각 안 들어?"
    l1 "계속 이 자체에만 매몰되었다가는 \n장기적으로 봤을때 손실밖에 없어!"
    hide ak
    show po gal
    l2 "그래! 어떻게 항상 맞기만 하겠어~"
    l2 "한번쯤은 틀렸을 수도 있지~ 하고 넘어가면 되는 거지!!"
    hide po
    show cl dead
    l3 "하."
    l3 "뭐만 하면 과학적으로.. 이성적으로.."
    l3 "이랬다가.. 저랬다가.."
    show cl ssha
    l3 "너희들의 신념이 그정도였다는 거지?"
    l3 "나만 또 매번 진심이였던 거고."
    hide cl
    show po gal
    l2 "잠깐! 그게 왜 그렇게 이어지는 건데?!" with vpunch
    l2 "사과해!"
    hide po
    show cl dead
    l3 "..."
    show cl ssha
    l3 "어르신들 말이 옳았는지도 모르겠네."
    l3 "아스트라가 제 3교단이라는 이유만으로..\n은연중에 무시당하고 있다는 거."
    hide cl
    show ak gal
    l1 "!" with vpunch
    l1 "너.. 다시 말해봐."
    l1 "우릴 계속 그딴 식으로 생각해왔다는 거야?"
    hide ak
    show cl ssha
    l3 "안 그래도 계속해서 논의되고 있던 주제였어."
    l3 "아스트라의 연방 탈퇴 말이야."
    l3 "이번에야말로 결착을 지을 수 있겠네."
    show cl dead
    l3 "더이상 너네랑 못해먹겠어."
    show cl gal
    l3 "때려 쳐!!" with vpunch
    hide cl
    "(클라우드가 자리를 박차고 나간다.)"
    show po gal
    l2 "하!"
    l2 "뭐야 저 태도는?"
    l2 "자기는 아무 잘못도 없다는 거야?"
    l2 "뭐만 하면 종교적으로~ 신께서~ 어쩌구 저쩌구."
    l2 "아주 잔다르크 납셨어!"
    hide po
    show ka hah
    l4 "이런 제기랄.."
    show ka seri
    l4 "이런 상황이 도래하지 않기만을 바랬는데.."
    l4 "클라우드가 독실한 신자인 건 알았지만.."
    l4 "저 정도였을 줄이야.."
    hide ka
    show me
    c "...."
    c "이제... 어떻게 해야...."
    hide me
    show god
    g "(...[name]님.)"
    g "(시원하게 말아드셨군요.)"
    hide god
    show me
    c "(!)"
    hide me
    show god
    g "(예상했던 대로.. 종언서가 거짓으로 판명난 건,)"
    g "(종교 국가인 클린스타클에게 큰 내분의 씨앗이 될 수 밖에 없었어요.)"
    g "(아무래도 이번엔 여기까지인가 봅니다.)"
    g "(저는 세계를 다시 되돌리고..)"
    g "(세계선을 새롭게 분리시킨 다음,)"
    g "(다른 용사님을 물색해야겠습니다.)"
    g "(자칫하면 세계 자체가 소멸될 수도 있는 \n굉장히 리스크있는 일이지만..)"
    g "(어쩌겠어요, 방법이 없는 걸.)"
    g "(어찌됐건, 고생하셨습니다. [name]님...)"
    hide god
    show me
    c "(...............)"
    c "(혹시라도, 혹시라도 다음 기회가 주어진다면.)"
    c "(조금 더 예언 분석에 집중해보자.)"
    hide me
    ""
    "Bad Ending#4 : 우려가 현실로"
return

label hiddenending:
    define supernovaguild = 0
    define eclipseguild = 0
    define astraguild = 0
    scene black
    stop music fadeout 2.0
    play music "audio/think.mp3" fadein 2.0
    "(뒷 길)"
    show image "backgrounds/forest2.jpg" with dissolve
    show me
    c "..."
    c "이 쪽은 집무국으로 향하는 길이야."
    c "누군가를 만날 지도 모르겠군."
    hide me
    "(저 멀리 누군가가 보인다.)"
    show ka seri
    l4 "하아.."
    l4 "이번 일만.. 성공한다면."
    show ka ssha
    l4 "클린스타클을 다시 위대하게 만들 수 있어."
    show ka cham
    l4 "...?" with vpunch
    show ka seri
    l4 "거기 누구?"
    hide ka
    show me
    c "(잠깐의 연기가 필요하겠는걸?)"
    c "안녕하십니까! 카리오트 님."
    hide me
    show ka seri
    l4 "넌 누구지?"
    l4 "잠깐 신원 확인이 필요하겠는데.."
    hide ka
    show me
    c "저는.."
    hide me
    menu:
        "저는.."
        
        "슈퍼노바 소속의 단원 [name]입니다!":
            $ supernovaguild = 1
            show ka std
            l4 "..."
        
        "이클립스 소속의 단원 [name]입니다!":
            $ eclipseguild = 1
            show ka std
            l4 "..."

        "아스트라 소속의 단원 [name]입니다!":
            $ astraguild = 1
            show ka std
            l4 "..."

    l4 "그런가.."
    show ka hmm
    l4 "이 시간에 왜 이곳까지 온거지?"
    hide ka
    show me
    c "아, 혹시라도 종언서의 남은 일부가 발견될까 하고요."
    c "잠시 탐색중이였습니다."
    hide me
    show ka cham
    l4 "이 인근은 어제부로 조사가 종료됐어."
    l4 "아무것도 없는거로 결론났고."
    l4 "보고받은 게 없었나?"
    hide ka
    show me
    c "어.. 별도로 보고받은 사안은 없었습니다."
    hide me
    show ka hah
    l4 "하여간에..."
    l4 "완전 개판이구만."
    l4 "각 교단의 머리라는 세 년들이 그 지경이니.."
    hide ka
    show me
    c "저.. 카리오트 님?"
    c "혹시 교주님들은 어디에 계시죠?"
    c "보고드릴 사안이 몇개 있어서요."
    hide me
    show ka cham
    l4 "교주들?"
    l4 "아마 집무국에 모여있을 거다."
    l4 "대체 모여서 뭘 하고있는 지는 모르겠지만..."
    show ka hah
    l4 "답답한 년들."
    hide ka
    show me
    c "(이 사람, 원래부터 이렇게 교주들을 디스했었나..?)"
    c "(전에 보여준 모습이랑은 사뭇 다른데.)"
    c "감사합니다!"
    hide me
    show ka seri
    l4 "아, 가는 길에 이것도 좀 전해라."
    l4 "까먹고 그대로 들고 나와버렸네."
    hide ka
    "(문서를 건내준다.)"
    show me
    c "이건?"
    hide me
    show ka hmm
    l4 "뭐긴.. 그간 조사국에서 발견한 내용들이지."
    l4 "별 영양가 없는 내용들뿐이지만."
    hide ka
    show me
    c "!" with vpunch
    c "알겠습니다."
    c "들어가보십쇼!"
    hide me
    show ka haha
    l4 "응. 그럼 수고~"
    hide ka
    "(카리오트는 발걸음을 옮겼다.)"
    show me
    c "...."
    c "(내용을 보지 않을 수 없다.)"
    c "(한번 봐볼까?)"
    hide me
    stop music fadeout 2.0
    bogo "보고서_XXXX.XX.XX"
    bogo "예언 당일까지 6일 남았습니다."
    bogo "이하는 금일의 보고 사항입니다."
    bogo "1. 종언서 관련"
    bogo "추가적으로 발견된 문서나 특이사항 없음."
    play music "audio/what.mp3"
    bogo "2. '구원자' 관련"
    bogo "최근들어 정부 소속의 자매님들 사이에 '구원자'라는 유언비어가 퍼지고 있습니다."
    bogo "구원자는 존재하지도, 앞으로 존재하게 될 가능성조차 없습니다."
    bogo "근거 없는 정보로 내부의 질서를 혼란케 하는 행위는 엄격히 금지됩니다."
    bogo "혹시라도 본인을 구원자라고 칭하는 사람과 조우하는 경우,\n조사국 핫라인으로 연락해주시면 감사하겠습니다."
    bogo "이상."
    bogo "국가의 안녕에 힘써주시는 자매님들께 항상 감사드리며,\n함께 종말을 이겨냅시다."
    bogo "보고자 카리오트"
    nvl clear
    show me
    c "...?!" with vpunch
    c "(분명 카리오트 씨가 작성한 보고서인데..)"
    c "(구원자는 존재하지 않는다고 나와있잖아?)"
    c "(이게 대체...)"
    c "(이 보고서의 내용을 그대로 전달해주면..)"
    c "(구원자의 존재가 완전 부정당하는 거잖아.)"
    c "(그보다도.. 전후관계가 어떻게 되는거지?)"
    c "(분명 교주들과 처음 조우했고 나를 소개했을 때, \n구원자에 대한 신뢰가 있었어.)"
    c "(만약 이 보고서가 먼저 교주들에게 전달됐다면..)"
    c "(그런 반응이 나오지 않았을거고..)"
    c "(그렇다는 건.. 만약 내가 교주들을 처음으로 만났고,\n그 후 집무국으로 이동하는 수순을 밟았다면)"
    c "(이 보고서의 내용들은 교주들에게 전달되지 않았다는 거지.)"
    c "(나라는 구원자의 존재가 나타났기에, \n카리오트 씨가 문서를 전달하지 않았다는 건데.)"
    c "(의도적으로 구원자라는 존재를 부정하려고 했다고?)"
    c "(비대위원장이라는 사람이..?)"
    c "(머리속이 혼란스럽다.)"
    c "(일단 집무국으로 가자.)"
    hide me
    scene black
    ""
    show image "backgrounds/집무국.jpg"
    "잠시 후, 집무국"
    c "(도착했다.)"
    if (supernovaguild == 1):
        show me
        c "(슈퍼노바 소속이라고 둘러댔으니..\n아크룩스 님에게 가야겠군.)"
    
    elif (eclipseguild == 1):
        show me
        c "(이클립스 소속이라고 둘러댔으니..\n폴라리스에게 가야겠군.)"

    elif (astraguild == 1):
        show me
        c "(아스트라 소속이라고 둘러댔으니..\n클라우드 씨에게 가야겠군.)"
    c "(그런데.. 어느 쪽으로 가야하지?)"
    c "(내 방과 회의실 외에는 가본 적이 없어서 모르겠다.)"
    hide me
    "(그렇게 생각하던 중, 앞쪽에 세 교주들이 지나가는 모습이 보인다.)"
    show me
    c "앗!"
    c "잠..잠시만요!"
    c "(아니.. 잠깐만, 뒤에 누군가가 같이 있다.)"
    c "(저건 누구지?)"
    c "(뒤를 밟아보자.)"
    hide me
    show ak eh
    l1 "그래서.."
    l1 "이 분이 정말 구원자라고?"
    hide ak
    show po ho
    l2 "응! 그렇다니까!!"
    l2 "내가 길에서 우연히 만났는데, \n자기를 구원자라고 하더라니깐?"
    hide po
    show cl awkmoo
    l3 "하지만 정말일까~"
    l3 "구원자가 이렇게 뚝딱! 하고 내려오는 거였다니.."
    hide cl
    show ak std
    l1 "그건 뭐, 카리오트 님께서 결정해주실 사안이지."
    hide ak
    show po std
    l2 "그래~ 일단 데려가보자구!"
    hide po
    "(그렇게 넷은 회의실 안으로 들어간다.)"
    show me
    c "(.....저게.. 대체.. 무슨...)"
    c "(내가 처음 회의실에 들어갔을 때랑 \n완전히 똑같은 흐름이잖아..)"
    c "(....다른 구원자가 있었다고?)"
    c "(그러면.. 이 흐름대로라면....)"
    hide me
    "(멀리서 카리오트가 황급히 들어온다.)"
    show ka seri
    l4 "어이, [name]!!"
    hide ka
    show me
    c "앗, 네! 카리오트 님!!"
    hide me
    show ka seri
    l4 "아직 그 보고서, 전달 안했지?!"
    hide ka
    show me
    c "엇, 어.. 네!"
    c "아직 안 했습니다만.."
    hide me
    show ka deadha
    l4 "후.... 그래."
    show ka cham
    l4 "그거, 그냥 갖다 버려."
    l4 "정정 사항이 좀 많이 생겨서 말이야."
    show ka seri
    l4 "나중에 내가 수정해서 전달할 테니까."
    hide ka
    show me
    c "...네..?... 네!"
    hide me
    "(카리오트는 뒤따라 회의실로 들어간다.)"
    show me
    c "...."
    c "아하, 이제야 조금은 알겠다."
    c "내가 처음 이곳에 왔을 때에도..."
    c "이런 식으로... 버려버렸던 건가..?"
    c "내 존재를 눈치채고..?"
    c "..."
    c "대체.. 왜?"
    hide me
    scene black
    ""
    "예언 당일까지 3일 새벽"
    show image "backgrounds/조사국.jpg"
    "조사국 청사 어딘가"
    show me
    c "오늘 보고서의 내용은..."
    hide me
    bogo "예언 당일까지 3일 남았습니다."
    bogo "이하는 금일의 보고 사항입니다."
    bogo "1. 종언서 관련"
    bogo "스플릿시 유적지에서 종언서의 파편이 발견되었습니다."
    bogo "해독 결과, 전문은 다음과 같습니다."
    bogo "종언서 3장"
    bogo "1. 아버지께서 보시기에 인간 세상이 심히 혼란하여 보기에 좋지 않더라."
    bogo "2. 이에 당신께서 어리석은 자들을 심판하고자 이르셨으니"
    bogo "3. 불타는 고리와 서늘한 발톱을 가지고"
    bogo "4. 찬연히 빛나는 신의 사자들 사이로"
    bogo "5. 짐승의 모습을 한 재앙이 찾아오리라"
    bogo "6. 그 말씀에 모두가 놀라 눈물을 흘리며 잘못을 참회하였으니"
    bogo "7. 마을 하나를 거친 뒤에야 아버지께서 노여움을 거치시더라."
    nvl clear
    show me
    c "...??"
    c "이건.. 내용이 비슷하면서도 바뀌어 있잖아."
    c "의미 자체는 바뀐게 없는 듯 하지만.."
    c "더 해석하기 난해해졌어."
    hide me
    "(때마침 카리오트가 멀리서 보인다.)"
    show ka deadha
    l4 "오, [name]!"
    l4 "이름이 [name] 맞았지?"
    l4 "저번엔 고마웠다."
    l4 "보고서 원본은 읽어봤어?"
    hide ka
    show me
    c "아, 넵. 방금 읽었습니다."
    c "드디어 가장 중요한 구절을 찾아냈던데요."
    hide me
    show ka ssha
    l4 "그래. 해석하느라 애좀 먹었다."
    l4 "이제부턴 저게 구체적으로 어디인지 찾아내면 돼."
    show ka seri
    l4 "말 나온 김에 그것 좀 집무국으로 갖다줄래?"
    l4 "급하게 다녀올 곳이 있어서 말이야."
    l4 "회의실에 두면 내가 알아서 가져갈게."
    hide ka
    show me
    c "네. 알겠습니다."
    hide me
    show ka deadha
    l4 "응. 그럼 수고~"
    hide ka
    show me
    c "....."
    c "(이걸 원문으로 바꿔두면 되겠군.)"
    hide me
    $ i = 0
    while(i != 2):
        menu:
            "3번 구절의 내용이 뭐였지?"

            "해가 우울히 울고 달이 지쳐 스러져가는 날":
                pass
            "해가 서글피 울고 달이 지쳐 스러져가는 날":
                pass
            "해가 서럽게 울고 달이 지쳐 스러져가는 날":
                $ i += 1
        menu:
            "4번 구절의 내용이 뭐였지?"

            "세계를 비추는 찬연히 빛나는 별들 사이로":
                pass

            "세계를 머금은 찬연히 빛나는 별들 사이로":
                $ i += 1

            "세계를 그리는 찬연히 빛나는 별들 사이로":
                pass

        if (i != 2):
            show me
            c "(...뭔가 이상하다.)"
            c "(다시 생각해보자.)"
            hide me
            $ i = 0

    show me
    c "(...그래. 분명 원래 이런 내용이였지.)"
    c "(회의실에 가져다두자.)"
    hide me
    scene black
    stop music fadeout 2.0
    "몇 시간 뒤,"
    show image "backgrounds/조사국.jpg"
    "조사국 청사"
    "(카리오트가 잔뜩 구겨진 채로 문을 열어재끼고 나온다.)"
    play music "audio/battle.mp3"
    show ka mad
    l4 "....."
    show ka deepmad
    l4 "[name] 어딨어!!!!" with vpunch
    hide ka
    "(사무실이 술렁인다.)"
    show ka deepmad
    l4 "안 들려?! [name] 어딨냐고!!!!" with vpunch
    hide ka
    e "저.. 카리오트 님?"
    show ka hah
    l4 "뭐, 임마!!"
    hide ka
    e "그런 이름의 조사원은.. 없는데요..?"
    show ka hah
    l4 "...뭐?"
    l4 "그게 무슨 소리야?"
    l4 "그럼 나랑 얘기했던 건 누군데?"
    hide ka
    scene black
    "그 시각,"
    show image "backgrounds/forest2.jpg"
    "조사국 청사 바깥 외딴 길"
    show me
    c "..."
    c "이걸로 된걸까."
    c "나는.. 종언서의 그 구절이 발견된 시점부터는.."
    c "그럭저럭 잘 해결해나갔지."
    c "그 구원자일지 모르는 놈도.. 아마 해낼거야."
    hide me
    "(카리오트가 달려온다.)"
    show ka deepmad
    l4 "[name]...!!!" with vpunch
    l4 "너.. 너 정체가 뭐야?"
    l4 "대체 왜 보고서를 되돌려놓은 거지?"
    show ka deepdeepmad
    l4 "일개 단원인 네가 대체 어떻게 종언서의 원문을 알고있는 거냐고?!"
    l4 "아니.. 애초에.."
    l4 "너 단원이 맞기는 한거냐?"
    hide ka
    show me
    c "..."
    c "이제야 본모습을 드러내시는군요."
    c "카리오트 씨... 아니,"
    c "{color=#e71010}흑막."
    c "처음에는 긴가민가했어."
    c "내가 알던 모습과는 많이 달랐거든."
    c "입은 좀 험할지언정.. 세 교주를 챙겨주는 구석도 보였었는데."
    c "..."
    c "구원자의 존재를 은폐하려고 했었고,"
    c "종언서의 구절도 의도적으로 해석하기 모호하게끔 바꿔뒀었지?"
    hide me
    show ka ssha
    l4 "모든 걸.. 알고 있구나."
    l4 "너..."
    l4 "{color=#e71010}너...이쪽 세계 놈이 아니구나."
    hide ka
    show me
    c "이 세계를 구했을 때.."
    c "뭔가 뒷맛이 구린 부분이 여럿 있었지."
    c "종언서는 대체 왜 이제서야 발굴된거고.."
    c "에크모트와 관련조차 없었던 \n스플릿시의 악한 기운의 출처는 대체 무엇이며.."
    c "가장 중요한 건,"
    c "{color=#e71010}대체 왜 당신은 단 한번도 우리와 함께 다니지 않았으면서,\n이상하리만치 완벽한 타이밍에 도움이 되는 정보들을 들고 왔을까?"
    c "마치.. 우리를 정해진 흐름으로 이끌려고 하듯이."
    hide me
    show ka deadha
    l4 "크큭..."
    show ka ssha
    l4 "크크크크큭...."
    show ka real
    l4 "{color=#e71010}캬하하하하하하하!!!!" with vpunch
    l4 "젠장... 거의 다 된 밥이였는데.."
    show ka hah
    l4 "넌 대체 뭐야?"
    l4 "구원자는... 저쪽에 있던 녀석 아니였냐고?"
    show ka deepmad
    l4 "저놈만 방해하면 될 줄 알았는데.."
    show ka ssha
    l4 "그래.. 네 말이 맞아."
    l4 "내가 의도적으로 정보를 조작했어."
    show ka seri
    l4 "...스플릿시에서 종언서의 원문을 발견했다."
    l4 "그 당시에는 역사서에 지나지 않았지."
    show ka ssha
    l4 "하지만... 내용은 꽤 재밌는 게 있더군."
    l4 "과거에 있었던 운석 충돌을 후대에게 경고하는 내용의 역사서.."
    l4 "이건 더할나위 없이 예언서로 조작하기에 완벽했지."
    hide ka
    show me
    c "어째서..."
    c "이 정도로 정교한 선동을 강행한거지?"
    hide me
    show ka seri
    l4 "..."
    l4 "정계의 음흉한 늙은이들도,"
    l4 "종교계의 철없는 꼬맹이들도.."
    show ka hah
    l4 "이 나라는 하나같이 글러먹었으니까."
    l4 "너도 알고 있잖아? 이 나라는 서서히 썩어가고 있었어."
    l4 "정치인이라는 작자들은 국익은 뒷전이고 \n자기들끼리 세력 싸움이나 하고 앉아있고,"
    l4 "이번 대의 교주들은 어째서인지 하나같이 \n젖비린내 나는 어린애들로만 채워졌어."
    l4 "이래서는.. 과학도, 종교도...\n어느 쪽도 집중할 수 없다고."
    show ka ssha
    l4 "이 나라를 바꾸기 위해서는.. 처음부터 싸그리 뜯어 고쳐야 해."
    hide ka
    show me
    c "그걸.. 대체 왜 당신 혼자 속단하는 거지?"
    c "이 나라는 충분히 바뀔 수 있는 가능성이 열려있어."
    c "교주들도...당신이 느끼는 걸 비슷하게 느끼고 있다고."
    hide me
    show ka hah
    l4 "어디서 굴러들어온 놈인지는 몰라도.."
    show ka deepdeepmad
    l4 "나보다 내 나라의 사정을 잘 아는 척 하지 마라!!" with vpunch
    hide ka
    show me
    c "흥. 마음대로 생각해."
    c "어차피 내가 돌아가는 대로\n당신의 실체가 이제 만천하에 드러날 테니까."
    hide me
    show ka real
    l4 "{color=#e71010}누구 맘대로?"
    l4 "{color=#e71010}넌... 여기서 살아나갈 수 없을텐데."
    hide ka
    "(형용할 수 없는 사악한 기운이 카리오트로부터 뿜어져 나온다.)"
    "(그리고 이내 검은 공간을 만들어낸다.)"
    show me
    c "이 기운은...!"
    c "스플릿시에서 느꼈던 기운.....!!"
    c "당신이 그 기운의 출처였던 거야?!"
    hide me
    show ka real
    l4 "{color=#e71010}캬캬캬캬캬캬캬!!" with vpunch
    l4 "{color=#e71010}그야 그 곳에는 너무 많은 증거들이 있었거든!!!"
    l4 "{color=#e71010}그 누구라도 종언서가 위조된 거라고 알아차렸을 테니까!!!!" with vpunch
    l4 "{color=#e71010}널... 이 곳에서 흔적조차 없게 지워주마!"
    hide ka
    show me
    c "(제기랄..)"
    c "(움직일 수가.. 없어!)"
    c "(이건 대체 무슨 힘이지?)"
    c "(이건 진짜 판타지물에서나 보던 거잖아..)"
    c "(...)"
    c "(여기까진가..)"
    hide me
    show god
    g "아니요."
    hide god
    show me
    c "....!"
    c "신...!"
    hide me
    show god
    g "고생하셨습니다, [name]님."
    g "드디어 진범을 찾아내셨군요."
    hide god
    show ka deepdeepmad
    l4 "{color=#e71010}...!!!" with vpunch
    show ka ssha
    l4 "{color=#e71010}이게 누구야?!?!"
    show ka real
    l4 "{color=#e71010}나랏일은 나몰라라 하고 도망간 신 아니셔?!"
    hide ka
    show me
    c "저건.. 대체 뭐야?"
    c "인간이 아닌것만 같은데."
    hide me
    show god
    g "반은 맞고 반은 틀려요."
    g "카리오트라는 자의 몸에 들어가있는 건.."
    g "'괴이신'이라고 불리는 자들 중 '말라리'라는 존재죠."
    g "괴이신은.. 저의 실패작들입니다."
    g "세계 곳곳에 흩어져서.. 훼방을 놓고 있죠."
    g "카리오트의 이 세계를 바꾸고 싶어하는 마음.."
    g "그 마음을 양분삼아.. 그녀의 정신 속에 숨어들어간 겁니다."
    g "대체 언제부터 숨어있었는 지는 모르겠지만.."
    g "카리오트의 뒤틀린 행동들의 이유는..\n아마 저 녀석 때문일 겁니다."
    hide god
    show ka real
    l5 "{color=#e71010}캬하하하하하하!!! 눈치 하나는 더럽게 빠르구만!!!!" with vpunch
    l5 "{color=#e71010}맞아....너의 오~랜 친구이자 원수...." with vpunch
    l5 "{color=#e71010}괴이신이였습니다~~캬하하하하하하하!!!" with vpunch
    hide ka
    show god
    g "이번에야말로 널 봉인시켜주지."
    hide god
    "(엄청난 진동과 함께 눈부신 빛이 뿜어져나온다.)"
    show god
    g "[name]님..!"
    g "저녀석의 움직임을 잠깐 제한했습니다!!"
    g "저 녀석을 잡기 위해서는.. \n클린스타클의 세 구역에 표식을 새겨야 합니다..!"
    g "부디 기억해내실 수 있기를....!"
    $ i = 0
    while (i != 3):
        g "먼저...!"
        g "클린스타클에서 가장 해가 잘 드는 곳의 위치입니다..!"
        hide god

        menu:
            "클린스타클에서 가장 해가 잘 드는 곳은?"

            "해가 우는 협곡":
                pass

            "해가 우는 언덕":
                $ i += 1

            "해가 우는 마을":
                pass
        show god
        g "그 곳이군요..!"
        g "다음은.. 클린스타클에서 가장 달이 크게 보이는 곳의 위치입니다..!"
        hide god

        menu:
            "클린스타클에서 가장 달이 크게 보이는 곳은?"

            "달이 잠든 성소":
                $ i += 1

            "달이 잠든 신전":
                pass

            "달이 잠든 도시":
                pass
        
        show god
        g "..이제 마지막입니다!"
        g "클린스타클에서.. 가장 은하수가 잘 보이는 곳의 위치입니다..!"
        hide god

        menu:
            "클린스타클에서 가장 은하수가 잘 보이는 곳은?"

            "별이 웃는 꿈길":
                pass

            "별이 먹힌 꿈길":
                $ i += 1

            "별이 피는 꿈길":
                pass
        
        if (i != 3):
            show god
            g "....[name]님..!!"
            g "뭔가 이상합니다!!"
            g "봉인이 작동하지 않아요!!"
            g "무언가 잘못 알려주신 것 같습니다..!"
            g "시간이 없습니다!! 다시 제대로 알려주셔야 해요!"
            $ i = 0

    stop music fadeout 2.0
    play music "audio/realend.mp3"
    show god
    g "좋습니다!!"
    g "봉인이 작동하고 있어요!"
    hide god
    show ka deepdeepmad
    l5 "{color=#e71010}얕은 수를...!!!"
    l5 "{color=#e71010}한 걸음 남았었거늘..."
    l5 "{color=#e71010}분하다..!!!!"
    l5 "{color=#e71010}여기서 끝이라고 생각하지 마라....!!"
    l5 "{color=#e71010}넌 날 평생 잡을 수 없어!!!"
    show ka real
    l5 "{color=#e71010}다시 만나게 될 거다...."
    l5 "{color=#e71010}영원히...!!!!!"
    hide ka
    "(서서히 검은 기운이 사라진다.)"
    "(동시에 카리오트는 바닥에 쓰러졌다.)"
    show god
    g "젠장.. 또 도망을."
    g "거의 다 잡은 거였는데."
    g "정말 추잡하리만치 끈질긴 놈입니다."
    hide god
    show me
    c "...."
    c "그럼, 어떻게 되는 거야?"
    hide me
    show god
    g "그래도 당분간은 다시 모습을 드러내지는 못할 겁니다.."
    g "도망치기 직전에 제 낙인을 새겨뒀거든요."
    g "그보다도.."
    g "저기 저 숙주부터 챙기시는 편이 나을 겁니다."
    g "아마 정신을 완전히 지배당한 뒤부터의 \n기억들은 삭제됐을 거거든요."
    g "자신이 무슨 짓을 벌였는지도 모를 겁니다."
    hide god
    show me
    c "허..."
    c "카리오트 씨가.. 진짜 흑막이였다니.."
    c "아, 맞아..!"
    c "교주들의 옆에 또 다른 구원자가 보이던데?"
    c "그건 뭐지?"
    hide me
    show god
    g "음."
    g "솔직히 말씀드리자면.."
    g "저는 [name]님이 순간적인 판단 실수를 한다는 등의 이유로..\n클린스타클을 구하지 못하셨을 때"
    g "'세계선 반복'이라는 행위를 강행했습니다."
    g "세계선 반복이라 함은.."
    g "이 세계의 분신을 떼어낸 다음,\n 시간을 특정한 시점으로 다시금 되돌리는 신의 권능입니다."
    g "권능이라고는 하지만.. \n잘못 집행했다가는 온 시간선이 대혼돈에 빠질수도 있는 위험한 일이죠."
    g "하지만 이번은 상황이 상황이니만큼..\n몇 번 정도는 괜찮으리라는 자의적 판단 하에 강행했습니다."
    g "여하튼.. 세계를 되돌리고, 제가 다시 구원을 시작하려는 \n[name]님을 모니터링하다가 잠시 한눈을 판 사이,"
    g "순간적으로 [name]님의 존재가 말소되었습니다."
    g "저에게 들어오던 신호가 끊겼거든요."
    g "저조차도 이해할 수 없는 현상이였습니다."
    g "생체 신호라는 건.. 사망한 게 아닌 이상\n그렇게 한순간에 끊길 수 있는 게 아니거든요."
    g "저는 [name]님께서 사망했거나.. \n모종의 이유로 실종됐다고 생각했어요."
    g "그래서... 정말 최후의 '세계선 반복'을 강행한 거였습니다."
    g "만약 이번에도 실패했다면..\n그땐 정말 파멸뿐이 기다리고 있었을 겁니다."
    g "어쨌건.. 사라진 [name]님 대신 \n새로운 인물을 이곳으로 이끌었습니다."
    g "그가 바로.. [name]님을 이은 구원자가 된거죠."
    g "그렇게 그 구원자님을 모니터링하던 도중.."
    g "우연히 근처에 있던 [name]님을 발견하게 됐습니다!"
    g "그것도 방금의 일촉즉발의 상황에서요."
    g "정말 1초 차이로 모든 결과가 바뀔지도 모르는 상황이였습니다."
    hide god
    show me
    c "후우.."
    c "그런 거였나.."
    c "그렇다면.. 이전의 나도,"
    c "다른 시간선의 어떤 '구원자'에게 도움을 받았을지도 모르겠군."
    c "내가 겪었었던 모든 일련의 사건들이 \n내가 지금 도움을 줬던 것에 기반한 것만 같거든."
    hide me
    show god
    g "후훗."
    g "그럴 지도 모르죠."
    g "이 우주에는 수많은 시간선과 평행우주가 \n복잡하게 얽힌 채..존재하거든요."
    g "아마.. 같은 실수를 되풀이하지 않게 하기 위해 \n또다른 차원의 누군가가 [name]님을 도와줬을지도요."
    g "하여튼.. 그렇게 된 고로..."
    g "정말 감사합니다, [name]님!!"
    g "솔직히 정말로 완벽히 해내실 줄은 몰랐어요."
    g "단순히 클린스타클을 지켜내는 선에서 \n끝날 줄 알았습니다만.."
    hide god
    show me
    c "...나도 잘은 모르겠지만.."
    c "뭔가.. 나를 도와주는 의문의 힘이 느껴졌어."
    c "그 힘이.. 나에게 수많은 기억들을 불어넣어줬어."
    c "아크룩스 님과 태양을 관측하면서 \n종교와 과학 간의 괴리를 좁힌 기억.."
    c "폴라리스와 달에 소원을 빌면서 \n지도자의 자질에 대한 의미를 얘기한 기억.."
    c "클라우드 씨와 별자리를 바라보고 \n세상 만물 하나하나의 소중함에 대해 다시금 깨달은 기억."
    c "이 모두가 동시에 흘러들어왔어."
    c "그러고는..나를 다시금 이 세계로 불러들였지."
    c "내가 처음 이 곳으로 떨어졌던 시간의, 그 장소로.."
    hide me
    show god
    g "... 후훗."
    g "아무래도 저 말고 또다른 '신'이 있었나보군요."
    g "[name]님의 뒤에 말이죠."
    hide god
    scene black
    "잠시 후,"
    "카리오트는 정신을 차렸고..\n그녀의 기억은 매우 오래전부터 멈춰있었다."
    "나는 자초지종을 매우 간략하게 설명했고,\n다행히도 그녀는 전부 납득하는 분위기였다."
    "그녀는 진심으로 사죄하며,\n앞으로의 모든 과정에 적극적으로 협조하겠다고 했다."
    "천재 소리를 듣던 그녀답게..\n그녀가 협력하자 예언의 해석이 정말 빠르게 진행되었다."
    "그녀와 교주들, 그리고 다른 구원자는..\n내가 했던 것처럼 종언서의 진짜 의미를 알아내는 데에 성공했고.."
    "...그렇게 모든 사건은 마무리되었다."
    stop music fadeout 2.0
    "이것이..."
    "진정한 '에크모트' 이야기의 마무리이다."
    "...당신이 없었더라면 이뤄내지 못했을 거야."
    "고마워."
    "나를 이끌어줘서."
    "이 세계를.."
    "진정하게 구원할 수 있게 해줘서."
    ""
    "Hidden Ending : Thank You, My God"
    $ persistent.hiddenending = 1
    call credits_hidden from _call_credits_hidden
return


label credits_bad:
    $ _skipping = False
    hide screen stat_overlay
    hide screen stat_reason
    stop music fadeout 2.0
    play music "audio/badending.mp3" fadein 2.0 loop
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show title:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide title with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide theend with dissolve
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide thanks with dissolve
    show tip:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard = True)
    hide tip with dissolve
    $ persistent.clear = 1
    pause
    stop music fadeout 2.0
    menu:
        "게임을 다시 시작하시겠습니까?"

        "네":
            call start from _call_start

        "아니오":
            return


label credits_good:
    $ _skipping = False
    hide screen stat_overlay
    hide screen stat_reason
    stop music fadeout 2.0
    play music "audio/ending.mp3" fadein 1.0 loop
    $ credits_speed = 25 #scrolling speed in seconds
    scene black #replace this with a fancy background
    with dissolve
    show title:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide title with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide theend with dissolve
    show cred1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1, hard = True)
    hide cred1 with dissolve   
    show cred2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1, hard = True)
    hide cred2 with dissolve
    show cred3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1, hard = True)
    hide cred3 with dissolve
    show cred4:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide cred4 with dissolve
    show cred at Move((0.5, 3.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    $ renpy.pause(credits_speed, hard = True)    
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide thanks with dissolve
    show tip:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard = True)
    hide tip with dissolve
    $ persistent.clear = 1
    pause
    stop music fadeout 2.0
    menu:
        "게임을 다시 시작하시겠습니까?"

        "네":
            call start from _call_start_1

        "아니오":
            return

label credits_hidden:
    $ _skipping = False
    hide screen stat_overlay
    hide screen stat_reason
    stop music fadeout 2.0
    play music "audio/hidden.mp3" fadein 1.0 loop
    $ credits_speed = 25 #scrolling speed in seconds
    scene background_ending with dissolve
    with dissolve
    show title:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide title with dissolve
    show realend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide realend with dissolve
    show cred1:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1, hard = True)
    hide cred1 with dissolve   
    show cred2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1, hard = True)
    hide cred2 with dissolve
    show cred3:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(1, hard = True)
    hide cred3 with dissolve
    show cred4:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide cred4 with dissolve
    show cred at Move((0.5, 3.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    $ renpy.pause(credits_speed, hard = True)    
    show thanks2:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard = True)
    hide thanks2 with dissolve
    show tip:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(4, hard = True)
    hide tip with dissolve
    $ persistent.clear = 1
    pause
    stop music fadeout 2.0
    menu:
        "게임을 다시 시작하시겠습니까?"

        "네":
            call start from _call_start_2

        "아니오":
            return

init python:
    credits =('모티브', '니디 걸 오버도즈'), ('모티브', '너의 이름은'), ('모티브', '원샷'), ('참고','http://baekansi.dothome.co.kr/' ),('참고','https://askance.tistory.com'), ('참고','https://lemmasoft.renai.us'), ('배경', 'wallpapers.com'), ('일러스트', 'Clip Studio Paint'), ('BGM', '던전 앤 파이터'), ('BGM', '메이플스토리'), ('BGM', '크로노 트리거'), ('BGM', '붕괴: 스타레일'), ('BGM', '오리와 눈 먼 숲'), ('BGM', '포켓몬스터 B/W'), ('BGM', '그 외 다수'), ('개발기간', '약 2달'), ('Special Thanks', '정희성'), ('Special Thanks', '김용범'), ('Special Thanks', '이승찬'), ('Special Thanks', '유동호'), ('Special Thanks', '전진우')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c2 in credits:
        if not c1==c2[0]:
            credits_s += "\n{size=40}" + c2[0] + "\n"
        credits_s += "{size=60}" + c2[1] + "\n"
        c1=c2[0]
    credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n8.13.23091805" #Don't forget to set this to your Ren'py version

init:
    image cred = Text(credits_s, font="NanumBarunGothic.ttf", text_align=0.5) #use this if you want to use special fonts
    image cred = Text(credits_s, text_align=0.5)
    image title = Text("{size=80}에크모트 : 별을 먹은 괴물", text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image realend = Text("{size=80}The True End", text_align=0.5)
    image cred1 = Text("{size=80}개발\n차현준(컴퓨터공학부 20)", text_align=0.5)
    image cred2 = Text("{size=80}디자인\n차현준(컴퓨터공학부 20)", text_align=0.5)
    image cred3 = Text("{size=80}시나리오\n차현준(컴퓨터공학부 20)", text_align=0.5)
    image cred4 = Text("{size=80}지원\n건국대학교 게임개발 동아리 EDGE", text_align=0.5)
    image thanks = Text("{size=80}플레이해주셔서 감사합니다!", text_align=0.5)
    image thanks2 = Text("{size=80}완벽하게 플레이해주셔서 감사합니다!", text_align=0.5)
    image tip = Text("{size=80}모든 엔딩 관람에 도전하세요!", text_align=0.5)