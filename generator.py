import base64
import time
import socket

def b64(s):
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

desc_fast = b64("Самые быстрые сервера")
desc_wifi = b64("Для WIFI")
desc_lte  = b64("Для LTE")

# Список нод WIFI: (vless_ссылка_без_хэша, хост, порт, имя)
wifi_nodes = [
    ("vless://d39b5724-76a0-44f1-98d0-089f78886ad2@lllkkd.save-node.com:443?type=tcp&security=reality&sni=lllkkd.save-node.com&fp=firefox&pbk=3par0TzZau_hWBaViirT7zlEfcRv1xzOgc-gigtcFWE&sid=45ee70d182e5&spx=%2F&flow=xtls-rprx-vision", "lllkkd.save-node.com", 443, "🇺🇸 США ✨"),
    ("vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@nl.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision", "nl.tlsov.pro", 443, "🇳🇱 Нидерланды ✨"),
    ("vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@fi.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision", "fi.tlsov.pro", 443, "🇫🇮 Финляндия ✨"),
    ("vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@lat.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision", "lat.tlsov.pro", 443, "🇱🇻 Латвия ✨"),
    ("vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@de.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision", "de.tlsov.pro", 443, "🇩🇪 Германия ✨"),
    ("vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@pl.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision", "pl.tlsov.pro", 443, "🇵🇱 Польша ✨"),
]

# Список нод LTE:
lte_nodes = [
    ("vless://402ced46-cf91-41f3-87a4-0a1a9e939a35@hole-nn.datanode-internal.net:443?type=grpc&security=reality&sni=ads.x5.ru&fp=qq&pbk=r6lN34m1nN-xQZ458j5NPD5xJ3_QBF2bGzY4KJEo4ic&sid=abbcd128&spx=%2F&serviceName=ads.x5.ru", "hole-nn.datanode-internal.net", 443, "🇪🇺 Обход #1"),
    ("vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@goodwin-pro.tlsov.pro:443?type=grpc&security=reality&sni=ads.x5.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=50&spx=%2F&serviceName=ads.x5.ru", "goodwin-pro.tlsov.pro", 443, "🇪🇺 Обход #2"),
    ("vless://83ef6f40-2397-4fb1-8c03-537839c55a35@79.174.92.149:443?type=grpc&security=reality&sni=smartcaptcha.yandexcloud.net&fp=safari&pbk=YkSkOZx_fKqpdyFD_ICMEahkAgG5drRkawHC2f3xlUQ&sid=0ed41244d37d4afe&spx=%2F&serviceName=%2Fapi%2Fv1%2Fstream", "79.174.92.149", 443, "🇪🇺 Обход #3"),
    ("vless://d39b5724-76a0-44f1-98d0-089f78886ad2@90.156.218.236:443?type=grpc&security=reality&sni=360.yandex.ru&fp=firefox&pbk=VaKp9XjMqT7lA4F3b6hpdF6fmsiY4B_hz6MzT6fv938&spx=%2F", "90.156.218.236", 443, "🇪🇺 Обход #4"),
    ("vless://d39b5724-76a0-44f1-98d0-089f78886ad2@founders-blog.online:443?type=ws&security=tls&sni=founders-blog.online&fp=chrome&path=%2Fstream%2F615428%2Fsocket&host=founders-blog.online", "founders-blog.online", 443, "🇪🇺 Обход #5"),
    ("vless://d39b5724-76a0-44f1-98d0-089f78886ad2@founders-blog.online:443?type=ws&security=tls&sni=founders-blog.online&fp=chrome&path=%2Fstream%2F615428%2Fsocket&host=founders-blog.online", "founders-blog.online", 443, "🇪🇺 Обход #6"),
    ("vless://d39b5724-76a0-44f1-98d0-089f78886ad2@176.109.85.63:8444?type=grpc&security=reality&sni=360.yandex.ru&fp=firefox&pbk=VaKp9XjMqT7lA4F3b6hpdF6fmsiY4B_hz6MzT6fv938&spx=%2F", "176.109.85.63", 8444, "🇪🇺 Обход #7"),
]

def ping_tcp(host, port):
    t0 = time.time()
    try:
        s = socket.create_connection((host, int(port)), timeout=2.5)
        s.close()
        return time.time() - t0
    except Exception:
        return 999.0

def get_fastest(nodes, auto_title):
    best_item = nodes[0]
    min_lat = 999.0
    for item in nodes:
        raw_link, host, port, title = item
        latency = ping_tcp(host, port)
        print(f"[{title}] Latency: {latency*1000:.1f} ms")
        if latency < min_lat:
            min_lat = latency
            best_item = item
    return f"{best_item[0]}#{auto_title}?serverDescription={desc_fast}"

print("Проверка WIFI серверов...")
best_wifi = get_fastest(wifi_nodes, "🌐 Автоподбор WIFI")

print("Проверка LTE серверов...")
best_lte = get_fastest(lte_nodes, "🌐 Автоподбор LTE")

headers = [
    "#profile-title: 𝗣𝗵𝗹𝘂𝘅 𝘃𝗽𝗻🔥",
    "#profile-update-interval: 1",
    "#providerid: Dqb26ol8",
    "#hide-settings: 1",
    "#profile-web-page-url: https://phluxvpn.hs.vc",
    "#support-url: https://t.me/Phluxvpnbot",
    "#per-app-proxy-mode: bypass",
    "#per-app-proxy-list: ru.sberbankmobile,ru.sberbank.sbol,com.idamob.tinkoff.android,ru.vtb24.mobilebanking.android,ru.alfabank.mobile.android,ru.gazprombank.android.mobilebank.app,ru.raiffeisennews,ru.rshb.dbo.mobile,ru.sovcombank.halva,ru.mkb.mobile,ru.rosbank.android,ru.bcs.bank,ru.pochta.bank,ru.uralsib.mobile,ru.otpbank.mobile,ru.psbank.mobile,ru.akbars.mobile,ru.open.bank,ru.homecredit.mybank,ru.tcsbank.investing,ru.nspk.sbpay,ru.vtb.mobilebank,ru.ozon.app.android,com.wildberries.ru,com.magnit.express,ru.tander.magnit,com.x5retailgroup.pyaterochka,ru.perekrestok.app,ru.lentaonline.android,ru.aliexpress.buyer,ru.dns_shop.android,ru.mvideo.android,ru.eldorado.android,ru.citilink.android,com.avito.android,ru.yandex.market,ru.detmir.dmbonus,com.vkontakte.android,ru.oneme.app,com.icq.mobile,ru.ok.android,ru.mail.mailapp,ru.yandex.searchplugin,ru.yandex.taxi,ru.yandex.yandexmaps,ru.yandex.music,ru.rutube.app,ru.kinopoisk,ru.gosuslugi.mobile,ru.nalog.lk,ru.mos.polis,ru.sberbankmobile_alpha,ru.mts.mymts,ru.beeline.services,ru.megafon.mlk,ru.tele2.mytele2,ru.rt.mlk,ru.delivery.club,ru.samokat.android,ru.yandex.eda,ru.dodopizza.app,ru.kfc.mobile,ru.burgerking.mobile,ru.sportmaster.app,ru.mvm.android,ru.aptekaru.android,ru.apteka.eapteka,ru.rzd.pass,ru.aeroflot.mobile,ru.pochta.mobileapp,ru.cdek.app,ru.boxberry.app",
    "#announce: base64:8J+RqOKAjfCfkrsg0J/QvtC00LTQtdGA0LbQutCwIOKAlCBAUGhsdXh2cG5ib3QNCuKcqCDigJQg0KHRgtCw0LHQuNC70YzQvdGL0LUg0YHQtdGA0LLQtdGA0LAg0LTQu9GPIHdpZmkNCuKaoSDigJQg0JLRgdC1INGB0L3QuNC30YMg0J7QsdGF0L7QtNCwINCR0KEg0LjRgdC60LvRjtGH0LjRgtC10LvRjNC90L4g0LTQu9GPINC80L7QsdC40LvRjNC90L4g0YHQtdCy0Y/Qt9C4DQo=",
    "#sub-info-text: Phlux vpn — лучший vpn для обхода блокировок!",
    "#sub-info-color: blue",
    "#sub-info-button-text: поддержка",
    "#sub-info-button-link: https://t.me/Phluxvpnbot",
    "#subscription-userinfo: upload=0; download=0; total=0; expire=149280451200",
    '#color-profile: {"backgroundGradientRotationAngle":125,"backgroundGradientColorIntensity":1,"backgroundColors":["#0A1628FF","#0D3B2EFF","#1A0A3DFF","#0A2840FF","#1A1A0AFF"],"backgroundImageType":"dark","elipseColors":["#00FFB3AA","#B388FFCC","#00E5FF99"],"buttonColor":"#00FFB3FF","buttonTextColor":"#0A1628FF","buttonTimerColor":"#0A1628FF","buttonImageType":"dark","powerIconColor":"#00FFB3FF","additionalOptionsButtonColor":"#B388FFFF","topBarButtonsColor":"#B388FFFF","subHeaderButtonColor":"#00E5FFFF","subsHeaderColor":"#0D3B2E99","disclosureHeaderTextColor":"#E0FFF8FF","disclosureSubHeaderTextColor":"#80CBC4FF","serverRowBackgroundColor":"#0D3B2E44","selectedServerRowColor":"#00FFB344","serverRowTitleTextColor":"#E0FFF8FF","serverRowSubTitleTextColor":"#80CBC4FF","serverRowChevronColor":"#80CBC4FF","subscriptionInfoBackgroundColor":"#0A162899","subscriptionInfoTextColor":"#E0FFF8FF","subscriptionTrafficBackgroundColor":"#00FFB322","profileWebPageIconColor":"#FF80ABFF","supportIconColor":"#00E5FFFF","settingsControlsTintColor":"#00FFB3FF"}'
]

servers = [
    best_wifi,
    best_lte,
    "hysteria2://00000000-0000-0000-0000-000000000004@0.0.0.0:443?type=tcp&security=reality&sni=example.com&fp=firefox&sid=00000004&spx=%2F#─── ОСНОВНЫЕ СЕРВЕРА ───",
    f"vless://f3d4f530-ca70-4e99-b2bb-c90e63abf65e@usa.oblaco.bet:443?type=tcp&security=reality&sni=usa.oblaco.bet&fp=firefox&pbk=mJ-0fJDvKp0rhuyUvs1bw4RasRRM-BEOAl9iAZ8gXy0&spx=%2F&flow=xtls-rprx-vision#🇺🇸 США ✨?serverDescription={desc_wifi}",
    f"vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@nl.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision#🇳🇱 Нидерланды ✨?serverDescription={desc_wifi}",
    f"vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@fi.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision#🇫🇮 Финляндия ✨?serverDescription={desc_wifi}",
    f"hysteria2://d39b5724-76a0-44f1-98d0-089f78886ad2@segfddd.save-node.com:443?sni=segfddd.save-node.com#🇨🇭 Швейцария ✨?serverDescription={desc_wifi}",
    f"vless://6bef6685-e989-467c-8fea-7fa1c6a0af2c@194.156.26.16:443?type=ws&security=tls&sni=LZc2j8i5PteXj5I7Aq0hFxQadvZcq.wF99sAF201Sfs9.wOrKers.dev&fp=qq&path=%2Fvl%2FBBj8crirrHMxntD7H3o3z#🇷🇺 Россия Youtube 🎬?serverDescription={desc_wifi}",
    f"vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@lat.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision#🇱🇻 Латвия ✨?serverDescription={desc_wifi}",
    f"vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@de.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision#🇩🇪 Германия ✨?serverDescription={desc_wifi}",
    f"vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@pl.tlsov.pro:443?type=tcp&security=reality&sni=vedomosti.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=1000&spx=%2F&flow=xtls-rprx-vision#🇵🇱 Польша ✨?serverDescription={desc_wifi}",
    "hysteria2://00000000-0000-0000-0000-000000000004@0.0.0.0:443?type=tcp&security=reality&sni=example.com&fp=firefox&sid=00000004&spx=%2F#─── ОБХОД БС ───",
    f"vless://402ced46-cf91-41f3-87a4-0a1a9e939a35@hole-nn.datanode-internal.net:443?type=grpc&security=reality&sni=ads.x5.ru&fp=qq&pbk=r6lN34m1nN-xQZ458j5NPD5xJ3_QBF2bGzY4KJEo4ic&sid=abbcd128&spx=%2F&serviceName=ads.x5.ru#🇪🇺 Обход #1?serverDescription={desc_lte}",
    f"vless://38d28b1d-8675-4e4c-80bc-ad2315bfb8cc@goodwin-pro.tlsov.pro:443?type=grpc&security=reality&sni=ads.x5.ru&fp=qq&pbk=K42aHYxM9Lt1Tl4vF-OniHV5pNju-wnB_opA-hVihgs&sid=50&spx=%2F&serviceName=ads.x5.ru#🇪🇺 Обход #2?serverDescription={desc_lte}",
    f"vless://83ef6f40-2397-4fb1-8c03-537839c55a35@79.174.92.149:443?type=grpc&security=reality&sni=smartcaptcha.yandexcloud.net&fp=safari&pbk=YkSkOZx_fKqpdyFD_ICMEahkAgG5drRkawHC2f3xlUQ&sid=0ed41244d37d4afe&spx=%2F&serviceName=%2Fapi%2Fv1%2Fstream#🇪🇺 Обход #3?serverDescription={desc_lte}",
    f"vless://d39b5724-76a0-44f1-98d0-089f78886ad2@90.156.218.236:443?type=grpc&security=reality&sni=360.yandex.ru&fp=firefox&pbk=VaKp9XjMqT7lA4F3b6hpdF6fmsiY4B_hz6MzT6fv938&spx=%2F#🇪🇺 Обход #4?serverDescription={desc_lte}",
    f"vless://d39b5724-76a0-44f1-98d0-089f78886ad2@founders-blog.online:443?type=ws&security=tls&sni=founders-blog.online&fp=chrome&path=%2Fstream%2F615428%2Fsocket&host=founders-blog.online#🇪🇺 Обход #5?serverDescription={desc_lte}",
    f"vless://d39b5724-76a0-44f1-98d0-089f78886ad2@founders-blog.online:443?type=ws&security=tls&sni=founders-blog.online&fp=chrome&path=%2Fstream%2F615428%2Fsocket&host=founders-blog.online#🇪🇺 Обход #6?serverDescription={desc_lte}",
    f"vless://d39b5724-76a0-44f1-98d0-089f78886ad2@176.109.85.63:8444?type=grpc&security=reality&sni=360.yandex.ru&fp=firefox&pbk=VaKp9XjMqT7lA4F3b6hpdF6fmsiY4B_hz6MzT6fv938&spx=%2F#🇪🇺 Обход #7?serverDescription={desc_lte}"
]

full_text = "\r\n".join(headers + servers) + "\r\n"
b64_output = base64.b64encode(full_text.encode('utf-8')).decode('utf-8')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(b64_output)

with open("sub_raw.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("Файл index.html успешно обновлен!")
print("Всего серверов:", len(servers))
