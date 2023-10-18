from get_up_data_handler import Message
from get_up_data_handler import ChainMessageReminderService
from get_up_data_handler import pretty_json_print_get_up_data


"""
Unit Tests
"""


if __name__ == '__main__':
    # test_msg_content = "wxid_9im2cf55yze722:\n<?xml version=\"1.0\"?>\n<msg>\n\t<appmsg appid=\"\" sdkver=\"0\">\n\t\t<title>#接龙\n早六点半到九点半 运动照灯学习吃饭吃药\n\n1. 清川 早六点半到九点半 运动照灯学习吃饭吃药\n2. 大螃蟹 7:20-8:35 玩手机，洗漱收拾，吃早饭，学习拍照基础知识\n3. forever 扣手机、早餐、看书\n4. 吃可爱长大的 早餐、打扫、做午饭、收拾猫砂\n5. Sheep 早餐,看spring源码视频\n6. Bean 吃早饭，看CAP Twelve Years Later\n7. 鹌鹑的乌龟 7:45-8:20 跳操拉伸 8:25-9:30 洗漱+搬砖通勤\n8. 萨小坦 6:30 洗澡吹头7:10出门打工\n9. 立夏 7-8洗漱通勤 8-9工位学习\n10. XQian 7:20-9:14洗漱，吃早饭，抖音，刷碗，磨蹭出门</title>\n\t\t<des />\n\t\t<username />\n\t\t<action>view</action>\n\t\t<type>53</type>\n\t\t<showtype>0</showtype>\n\t\t<content />\n\t\t<url />\n\t\t<lowurl />\n\t\t<forwardflag>0</forwardflag>\n\t\t<dataurl />\n\t\t<lowdataurl />\n\t\t<contentattr>0</contentattr>\n\t\t<streamvideo>\n\t\t\t<streamvideourl />\n\t\t\t<streamvideototaltime>0</streamvideototaltime>\n\t\t\t<streamvideotitle />\n\t\t\t<streamvideowording />\n\t\t\t<streamvideoweburl />\n\t\t\t<streamvideothumburl />\n\t\t\t<streamvideoaduxinfo />\n\t\t\t<streamvideopublishid />\n\t\t</streamvideo>\n\t\t<canvasPageItem>\n\t\t\t<canvasPageXml><![CDATA[]]></canvasPageXml>\n\t\t</canvasPageItem>\n\t\t<appattach>\n\t\t\t<totallen>0</totallen>\n\t\t\t<attachid />\n\t\t\t<cdnattachurl />\n\t\t\t<emoticonmd5 />\n\t\t\t<aeskey />\n\t\t\t<fileext />\n\t\t\t<islargefilemsg>0</islargefilemsg>\n\t\t</appattach>\n\t\t<extinfo>\n\t\t\t<solitaire_info><![CDATA[<solitaire><tt>0-25</tt><ex>0-0</ex><tl>0-0</tl><s>.</s><au>wxid_denb6dom19oh22</au><hrt>1</hrt><loss>0</loss><content><s>10</s><i><u>wxid_denb6dom19oh22</u><h>0</h><s>.</s><t>1667959229</t><r>30-23</r></i><i><u>wxid_35pizrahyfsb22</u><h>0</h><s>.</s><t>1667959591</t><r>57-35</r></i><i><u>wxid_u7nokk5ypg2i21</u><h>0</h><s>.</s><t>1667959659</t><r>96-17</r></i><i><u>wxid_fmtmadnn7den12</u><h>0</h><s>.</s><t>1667959717</t><r>117-23</r></i><i><u>wxid_9imslukia1pq22</u><h>0</h><s>.</s><t>1667959933</t><r>144-21</r></i><i><u>wxid_a5uazi0y0lm522</u><h>0</h><s>.</s><t>1667959976</t><r>169-32</r></i><i><u>wxid_86b4cb2pxtyd22</u><h>0</h><s>.</s><t>1667960542</t><r>205-38</r></i><i><u>wxid_07831t9zvkl922</u><h>0</h><s>.</s><t>1667960895</t><r>247-21</r></i><i><u>wxid_f9e2vdhcdr8e11</u><h>0</h><s>.</s><t>1667961001</t><r>272-18</r></i><i><u>wxid_9im2cf55yze722</u><h>0</h><s>.</s><t>1667962191</t><r>295-32</r></i></content></solitaire>]]></solitaire_info>\n\t\t</extinfo>\n\t\t<androidsource>0</androidsource>\n\t\t<thumburl />\n\t\t<mediatagname />\n\t\t<messageaction><![CDATA[]]></messageaction>\n\t\t<messageext><![CDATA[]]></messageext>\n\t\t<emoticongift>\n\t\t\t<packageflag>0</packageflag>\n\t\t\t<packageid />\n\t\t</emoticongift>\n\t\t<emoticonshared>\n\t\t\t<packageflag>0</packageflag>\n\t\t\t<packageid />\n\t\t</emoticonshared>\n\t\t<designershared>\n\t\t\t<designeruin>0</designeruin>\n\t\t\t<designername>null</designername>\n\t\t\t<designerrediretcturl>null</designerrediretcturl>\n\t\t</designershared>\n\t\t<emotionpageshared>\n\t\t\t<tid>0</tid>\n\t\t\t<title>null</title>\n\t\t\t<desc>null</desc>\n\t\t\t<iconUrl>null</iconUrl>\n\t\t\t<secondUrl>null</secondUrl>\n\t\t\t<pageType>0</pageType>\n\t\t</emotionpageshared>\n\t\t<webviewshared>\n\t\t\t<shareUrlOriginal />\n\t\t\t<shareUrlOpen />\n\t\t\t<jsAppId />\n\t\t\t<publisherId />\n\t\t</webviewshared>\n\t\t<template_id />\n\t\t<md5 />\n\t\t<weappinfo>\n\t\t\t<username />\n\t\t\t<appid />\n\t\t\t<appservicetype>0</appservicetype>\n\t\t\t<secflagforsinglepagemode>0</secflagforsinglepagemode>\n\t\t\t<videopageinfo>\n\t\t\t\t<thumbwidth>0</thumbwidth>\n\t\t\t\t<thumbheight>0</thumbheight>\n\t\t\t\t<fromopensdk>0</fromopensdk>\n\t\t\t</videopageinfo>\n\t\t</weappinfo>\n\t\t<statextstr />\n\t\t<musicShareItem>\n\t\t\t<musicDuration>0</musicDuration>\n\t\t</musicShareItem>\n\t\t<finderLiveProductShare>\n\t\t\t<finderLiveID />\n\t\t\t<finderUsername />\n\t\t\t<finderObjectID />\n\t\t\t<finderNonceID />\n\t\t\t<liveStatus />\n\t\t\t<appId />\n\t\t\t<pagePath />\n\t\t\t<productId />\n\t\t\t<coverUrl />\n\t\t\t<productTitle />\n\t\t\t<marketPrice><![CDATA[0]]></marketPrice>\n\t\t\t<sellingPrice><![CDATA[0]]></sellingPrice>\n\t\t\t<platformHeadImg />\n\t\t\t<platformName />\n\t\t\t<shopWindowId />\n\t\t\t<flashSalePrice><![CDATA[0]]></flashSalePrice>\n\t\t\t<flashSaleEndTime><![CDATA[0]]></flashSaleEndTime>\n\t\t</finderLiveProductShare>\n\t\t<finderShopWindowShare>\n\t\t\t<finderUsername />\n\t\t\t<avatar />\n\t\t\t<nickname />\n\t\t\t<commodityInStockCount />\n\t\t\t<appId />\n\t\t\t<path />\n\t\t\t<appUsername />\n\t\t\t<query />\n\t\t\t<liteAppId />\n\t\t\t<liteAppPath />\n\t\t\t<liteAppQuery />\n\t\t</finderShopWindowShare>\n\t\t<findernamecard>\n\t\t\t<username />\n\t\t\t<avatar><![CDATA[]]></avatar>\n\t\t\t<nickname />\n\t\t\t<auth_job />\n\t\t\t<auth_icon>0</auth_icon>\n\t\t\t<auth_icon_url />\n\t\t</findernamecard>\n\t\t<finderGuarantee>\n\t\t\t<scene><![CDATA[0]]></scene>\n\t\t</finderGuarantee>\n\t\t<directshare>0</directshare>\n\t\t<gamecenter>\n\t\t\t<namecard>\n\t\t\t\t<iconUrl />\n\t\t\t\t<name />\n\t\t\t\t<desc />\n\t\t\t\t<tail />\n\t\t\t\t<jumpUrl />\n\t\t\t</namecard>\n\t\t</gamecenter>\n\t\t<patMsg>\n\t\t\t<chatUser />\n\t\t\t<records>\n\t\t\t\t<recordNum>0</recordNum>\n\t\t\t</records>\n\t\t</patMsg>\n\t\t<secretmsg>\n\t\t\t<issecretmsg>0</issecretmsg>\n\t\t</secretmsg>\n\t\t<referfromscene>0</referfromscene>\n\t\t<websearch>\n\t\t\t<rec_category>0</rec_category>\n\t\t\t<channelId>0</channelId>\n\t\t</websearch>\n\t</appmsg>\n\t<fromusername>wxid_9im2cf55yze722</fromusername>\n\t<scene>0</scene>\n\t<appinfo>\n\t\t<version>1</version>\n\t\t<appname></appname>\n\t</appinfo>\n\t<commenturl></commenturl>\n</msg>\n"
    test_msg_content = "wxid_fmtmadnn7den12:\n#接龙\n\n1. 和尚 7-10，补觉咖啡修暖气收拾纸箱看后期\n2. Bean 早饭+daily plan+极客时间大数据论文\n3. forever 7.50-9.20 早餐、刷剧\n4. 大螃蟹 7:23-8:40 洗漱收拾，早餐，B站\n5. 大京 6-9：了解TODO类APP+肌肉放松核心激活+早餐+学穿搭\n6. 星航 耍手机，读书半小时\n7. Carrie🌿 7:20-8:45 起床，跳绳，洗澡，收拾通勤。\n8. 萤窗小语 7.35起床，吃早饭，化妆，听广播，结束居家隔离这周第一天去上班感觉还行\n9. 清川 7点半到九点半上厕所学习吃早饭看卿卿日常！化妆\n10. 鹌鹑的乌龟 7:30-8:20 发呆 读书 8:20-9:30 洗漱 通勤\n11. XQian 7:24-7:40赖床7:40-8:20洗漱8:20-9:00学习9:00-9:30吃饭，看剧，出门\n12. Sheep 7-8.30 爬楼,早餐,搭建环境\n13. 吃可爱长大的 6:10-8:15吃早饭做午饭，打扫卫生，运动"
    test_msg = Message(test_msg_content)

    service = ChainMessageReminderService(test_msg)

    reminded_msg = service.get_reminded_msg()
    print(reminded_msg)
    '''
    Output:
    Hi，@琴****** @大****** @影** @小******* @汤*** @小** @钱****** @e**** @利**** @FOUND40*****，记得更新今天的早起日志哦 (*^▽^*)
    '''

    parsed_content_dict, format_error_users = service.get_parsed_content_dict()
    pretty_json_print_get_up_data(parsed_content_dict)
    print(f"error user count: {len(format_error_users)}, they are: {format_error_users}")

    '''
    Output:
    {
        "大*-**": {
            "nick": "大*-**",
            "get_up_time": "04:30:00",
            "get_up_log": "-5:30阅读&筋**松\n-7:00跑***\n-8:00洗漱***路\n-9:00阅读"
        },
        "M***": {
            "nick": "M***",
            "get_up_time": "04:52:00",
            "get_up_log": "-5:10 小**\n-5:30 冥想🧘\u200d♀️\n-6:00-《也许你该找个人聊聊》\n-6:45有氧\n-7:20收拾洗漱出门"
        },
        "李***": {
            "nick": "李***",
            "get_up_time": "05:33:00",
            "get_up_log": "6:10 护肤，听课\n6:30 冥想🧘\u200d♀️，《心经》，自我肯定\n6:58 背书，蒙田的教育思想\n7:20 出门"
        },
        "和****": {
            "nick": "和****",
            "get_up_time": "06:00:00",
            "get_up_log": "-9.24\n-7.51 清理 13 个随手记正念\n-9.24 今天的依赖倒置原则终于非常快速懂了，设计原则和模式就像摄影的构图和拍人脚放在下面一样\n心智觉察解悟，原来评判也是一种情绪，评判由于有了对与错，但是实际上没有对错好坏，放下对错，对错是你五官收集起来的"
        },
        "利****": {
            "nick": "利****",
            "get_up_time": "06:10:00",
            "get_up_log": ""
        },
        "人*****": {
            "nick": "人*****",
            "get_up_time": "06:18:00",
            "get_up_log": "-6:40坐在床上清醒，最近总是睡得晚，起不来了\n-7:20听书，阅读\n-7:50早饭 洗漱出门"
        },
        "曾**": {
            "nick": "曾**",
            "get_up_time": "06:25:00",
            "get_up_log": "-7:05 早餐出门\n-7:25 遇到老同事聊天\n-7:50 国庆备考复习计划\n-8:20 学习得到课程"
        },
        "🐑*****": {
            "nick": "🐑*****",
            "get_up_time": "06:28:00",
            "get_up_log": "-7:10运动\n-7:30洗头洗澡\n-7:50吃早饭\n-8:20收拾，洗漱出门"
        },
        "琴******": {
            "nick": "琴******",
            "get_up_time": "06:30:00",
            "get_up_log": ""
        },
        "小*******": {
            "nick": "小*******",
            "get_up_time": "06:36:00",
            "get_up_log": ""
        },
        "大******": {
            "nick": "大******",
            "get_up_time": "07:00:00",
            "get_up_log": ""
        },
        "FOUND40*****": {
            "nick": "FOUND40*****",
            "get_up_time": "07:04:00",
            "get_up_log": ""
        },
        "e****": {
            "nick": "e****",
            "get_up_time": "07:04:00",
            "get_up_log": ""
        },
        "猫**": {
            "nick": "猫**",
            "get_up_time": "07:20:00",
            "get_up_log": "7.30 洗漱\n8.00 打球\n9.00 算法训练\n9.30 学习掘金小册"
        },
        "汤***": {
            "nick": "汤***",
            "get_up_time": "07:26:00",
            "get_up_log": ""
        },
        "丁****": {
            "nick": "丁****",
            "get_up_time": "07:30:00",
            "get_up_log": "-8.00 冥想\n-8.20洗漱\n-9.00 《内证****》"
        },
        "钱******": {
            "nick": "钱******",
            "get_up_time": "07:30:00",
            "get_up_log": ""
        },
        "影**": {
            "nick": "影**",
            "get_up_time": "07:50:00",
            "get_up_log": ""
        },
        "小**": {
            "nick": "小**",
            "get_up_time": "07:50:00",
            "get_up_log": ""
        }
    }
    '''
