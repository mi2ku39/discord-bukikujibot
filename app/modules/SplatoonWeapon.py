from enum import Enum
from typing import List


class MainWeapon(Enum):
    wakaba = 'わかばシューター'
    sushi = 'スプラシューター'
    garon52 = '.52ガロン'
    garon96 = '.96ガロン'
    sharp = 'シャープマーカー'
    zap = 'N-ZAP'
    prime = 'プライムシューター'
    bold = 'ボールドマーカー'
    promodeler = 'プロモデラー'
    l3_lille = 'L3リールガン'
    h3_lille = 'H3リールガン'
    jet_sweeper = 'ジェットスイーパー'
    bottle = 'ボトルガイザー'
    dual_sweeper = 'デュアルスイーパー'
    spla_maneuver = 'スプラマニューバー'
    spattary = 'スパッタリー'
    kelbin = 'ケルビン525'
    quad_hopper = 'クアッドホッパー'
    spla_charger = 'スプラチャージャー'
    sqickrin = 'スクイックリン'
    take = '14式竹筒銃'
    soi_tuber = 'ソイチューバー'
    litter = 'リッター4K'
    nova_blaster = 'ノヴァブラスター'
    long_blaster = 'ロングブラスター'
    hot_blaster = 'ホットブラスター'
    rapid_blaster = 'ラピッドブラスター'
    rapid_blaster_elite = 'Rブラスターエリート'
    clash_blaster = 'クラッシュブラスター'
    dinamo_roller = 'ダイナモローラー'
    spla_roller = 'スプラローラー'
    carbon_roller = 'カーボンローラー'
    variable_roller = 'ヴァリアブルローラー'
    hokusai = 'ホクサイ'
    pablo = 'パブロ'
    bucket_slosher = 'バケットスロッシャー'
    hissen = 'ヒッセン'
    screw_slosher = 'スクリュースロッシャー'
    explorer = 'エクスプロッシャー'
    over_frosher = 'オーバーフロッシャー'
    spla_spinner = 'スプラスピナー'
    barrel_spinner = 'バレルスピナー'
    hi_drant = 'ハイドラント'
    kugel_shuliver = 'クーゲルシュライバー'
    nautilus = 'ノーチラス'
    parashelter = 'パラシェルター'
    camping_shelter = 'キャンピングシェルター'
    spy_gadget = 'スパイガジェット'


class SubWeapon(Enum):
    splash_bomb = 'スプラッシュボム'
    quick_bomb = 'クイックボム'
    q_ban_bomb = 'キューバンボム'
    point_sensor = 'ポイントセンサー'
    trap = 'トラップ'
    sprinkler = 'スプリンクラー'
    jump_beacon = 'ジャンプビーコン'
    curling_bomb = 'カーリングボム'
    splash_shield = 'スプラッシュシールド'
    poison_mist = 'ポイズンミスト'
    robot_bomb = 'ロボットボム'
    tansan_bomb = 'タンサンボム'
    t_p_d = 'トーピード'


class SpecialWeapon(Enum):
    ink_armor = 'インクアーマー'
    multi_missile = 'マルチミサイル'
    hyper_presser = 'ハイパープレッサー'
    jetpack = 'ジェットパック'
    super_chakuchi = 'スーパーチャクチ'
    bomb_pitcher = 'ボムピッチャー'
    rain = 'アメフラシ'
    ika_sphere = 'イカスフィア'
    bubble_launcher = 'バブルランチャー'
    nice_ball = 'ナイスダマ'
    ultra_stamp = 'ウルトラハンコ'


class Category(Enum):
    shooter = 'シューター'
    charger = 'チャージャー'
    blaster = 'ブラスター'
    roller = 'ローラー'
    fude = 'フデ'
    slosher = 'スロッシャー'
    spinner = 'スピナー'
    maneuver = 'マニューバー'
    shelter = 'シェルター'


class Custom(Enum):
    original = '無印'
    deco = 'デコ'
    betchu = 'ベッチュー'
    custom = 'カスタム'
    collabo = 'コラボ'
    replica = 'レプリカ'
    neo = 'ネオ'
    bukiti = 'ブキチセレクション'
    hue = 'ヒュー'
    foil = 'フォイル'
    other = 'その他'
    solera = 'ソレーラ'


class Buki:
    def __init__(self,
                 name: str,
                 category: Category,
                 main_weapon: MainWeapon,
                 sub_weapon: SubWeapon,
                 special_weapon: SpecialWeapon,
                 custom: Custom = Custom.original,
                 replica: bool = False):
        self.name = name
        self.category = category
        self.main_weapon = main_weapon
        self.sub_weapon = sub_weapon
        self.special_weapon = special_weapon
        self.custom = custom
        self.replica = replica

    @staticmethod
    def weapons():
        return [
            Buki(
                'スプラシューターコラボ',
                Category.shooter,
                MainWeapon.sushi,
                SubWeapon.splash_bomb,
                SpecialWeapon.jetpack,
                Custom.collabo
            ),
            Buki(
                '.52ガロン',
                Category.shooter,
                MainWeapon.garon52,
                SubWeapon.point_sensor,
                SpecialWeapon.ika_sphere
            ),
            Buki(
                'わかばシューター',
                Category.shooter,
                MainWeapon.wakaba,
                SubWeapon.splash_bomb,
                SpecialWeapon.ink_armor
            ),
            Buki(
                'オクタシューターレプリカ',
                Category.shooter,
                MainWeapon.sushi,
                SubWeapon.splash_bomb,
                SpecialWeapon.jetpack,
                Custom.replica,
                True
            ),
            Buki(
                '.96ガロンデコ',
                Category.shooter,
                MainWeapon.garon96,
                SubWeapon.splash_shield,
                SpecialWeapon.super_chakuchi,
                Custom.deco
            ),
            Buki(
                'シャープマーカー',
                Category.shooter,
                MainWeapon.sharp,
                SubWeapon.poison_mist,
                SpecialWeapon.jetpack
            ),
            Buki(
                'N-ZAP89',
                Category.shooter,
                MainWeapon.zap,
                SubWeapon.robot_bomb,
                SpecialWeapon.multi_missile,
                Custom.other
            ),
            Buki(
                'N-ZAP85',
                Category.shooter,
                MainWeapon.zap,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.ink_armor
            ),
            Buki(
                'プライムシューター',
                Category.shooter,
                MainWeapon.prime,
                SubWeapon.point_sensor,
                SpecialWeapon.rain
            ),
            Buki(
                'シャープマーカーネオ',
                Category.shooter,
                MainWeapon.sharp,
                SubWeapon.quick_bomb,
                SpecialWeapon.bomb_pitcher,
                Custom.neo
            ),
            Buki(
                'ボールドマーカー',
                Category.shooter,
                MainWeapon.bold,
                SubWeapon.curling_bomb,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'ボールドマーカーネオ',
                Category.shooter,
                MainWeapon.bold,
                SubWeapon.jump_beacon,
                SpecialWeapon.multi_missile,
                Custom.neo
            ),
            Buki(
                'プロモデラーRG',
                Category.shooter,
                MainWeapon.promodeler,
                SubWeapon.sprinkler,
                SpecialWeapon.ika_sphere,
                Custom.other
            ),
            Buki(
                'スプラシューター',
                Category.shooter,
                MainWeapon.sushi,
                SubWeapon.quick_bomb,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                '.52ガロンデコ',
                Category.shooter,
                MainWeapon.garon52,
                SubWeapon.curling_bomb,
                SpecialWeapon.hyper_presser,
                Custom.deco
            ),
            Buki(
                'L3リールガンD',
                Category.shooter,
                MainWeapon.l3_lille,
                SubWeapon.quick_bomb,
                SpecialWeapon.jetpack,
                Custom.other
            ),
            Buki(
                'ジェットスイーパーカスタム',
                Category.shooter,
                MainWeapon.jet_sweeper,
                SubWeapon.quick_bomb,
                SpecialWeapon.hyper_presser,
                Custom.custom
            ),
            Buki(
                'プライムシューターコラボ',
                Category.shooter,
                MainWeapon.prime,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.bubble_launcher,
                Custom.collabo
            ),
            Buki(
                'もみじシューター',
                Category.shooter,
                MainWeapon.wakaba,
                SubWeapon.robot_bomb,
                SpecialWeapon.rain,
                Custom.other
            ),
            Buki(
                'プロモデラーMG',
                Category.shooter,
                MainWeapon.promodeler,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.bomb_pitcher
            ),
            Buki(
                'H3リールガンチェリー',
                Category.shooter,
                MainWeapon.h3_lille,
                SubWeapon.splash_shield,
                SpecialWeapon.bubble_launcher,
                Custom.bukiti
            ),
            Buki(
                '.96ガロン',
                Category.shooter,
                MainWeapon.garon96,
                SubWeapon.sprinkler,
                SpecialWeapon.ink_armor
            ),
            Buki(
                'ボールドマーカー7',
                Category.shooter,
                MainWeapon.bold,
                SubWeapon.splash_bomb,
                SpecialWeapon.ultra_stamp,
                Custom.bukiti
            ),
            Buki(
                'N-ZAP83',
                Category.shooter,
                MainWeapon.zap,
                SubWeapon.sprinkler,
                SpecialWeapon.rain,
                Custom.bukiti
            ),
            Buki(
                'ヒーローシューターレプリカ',
                Category.shooter,
                MainWeapon.sushi,
                SubWeapon.quick_bomb,
                SpecialWeapon.super_chakuchi,
                Custom.replica,
                True
            ),
            Buki(
                'L3リールガン',
                Category.shooter,
                MainWeapon.l3_lille,
                SubWeapon.curling_bomb,
                SpecialWeapon.ika_sphere
            ),
            Buki(
                'ジェットスイーパー',
                Category.shooter,
                MainWeapon.jet_sweeper,
                SubWeapon.poison_mist,
                SpecialWeapon.multi_missile
            ),
            Buki(
                'H3リールガン',
                Category.shooter,
                MainWeapon.h3_lille,
                SubWeapon.curling_bomb,
                SpecialWeapon.ika_sphere
            ),
            Buki(
                'プロモデラーPG',
                Category.shooter,
                MainWeapon.promodeler,
                SubWeapon.quick_bomb,
                SpecialWeapon.nice_ball,
                Custom.bukiti
            ),
            Buki(
                'H3リールガンD',
                Category.shooter,
                MainWeapon.h3_lille,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.ink_armor,
                Custom.other
            ),
            Buki(
                'ボトルガイザー',
                Category.shooter,
                MainWeapon.bottle,
                SubWeapon.splash_shield,
                SpecialWeapon.hyper_presser
            ),
            Buki(
                'ボトルガイザーフォイル',
                Category.shooter,
                MainWeapon.bottle,
                SubWeapon.splash_bomb,
                SpecialWeapon.bubble_launcher,
                Custom.foil
            ),
            Buki(
                'スプラシューターベッチュー',
                Category.shooter,
                MainWeapon.sushi,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.multi_missile,
                Custom.betchu
            ),
            Buki(
                'プライムシューターベッチュー',
                Category.shooter,
                MainWeapon.prime,
                SubWeapon.splash_bomb,
                SpecialWeapon.nice_ball,
                Custom.betchu
            ),
            Buki(
                'おちばシューター',
                Category.shooter,
                MainWeapon.wakaba,
                SubWeapon.t_p_d,
                SpecialWeapon.bubble_launcher,
                Custom.betchu
            ),
            Buki(
                'L3リールガンベッチュー',
                Category.shooter,
                MainWeapon.l3_lille,
                SubWeapon.splash_shield,
                SpecialWeapon.ultra_stamp,
                Custom.betchu
            ),
            Buki(
                '.52ガロンベッチュー',
                Category.shooter,
                MainWeapon.garon52,
                SubWeapon.splash_shield,
                SpecialWeapon.nice_ball,
                Custom.betchu
            ),
            Buki(
                'デュアルスイーパー',
                Category.maneuver,
                MainWeapon.dual_sweeper,
                SubWeapon.point_sensor,
                SpecialWeapon.multi_missile
            ),
            Buki(
                'デュアルスイーパーカスタム',
                Category.maneuver,
                MainWeapon.dual_sweeper,
                SubWeapon.splash_bomb,
                SpecialWeapon.rain,
                Custom.custom
            ),
            Buki(
                'スプラマニューバー',
                Category.maneuver,
                MainWeapon.spla_maneuver,
                SubWeapon.quick_bomb,
                SpecialWeapon.multi_missile
            ),
            Buki(
                'スプラマニューバーコラボ',
                Category.maneuver,
                MainWeapon.spla_maneuver,
                SubWeapon.curling_bomb,
                SpecialWeapon.jetpack,
                Custom.collabo
            ),
            Buki(
                'スパッタリー',
                Category.maneuver,
                MainWeapon.spattary,
                SubWeapon.jump_beacon,
                SpecialWeapon.bomb_pitcher
            ),
            Buki(
                'ヒーローマニューバーレプリカ',
                Category.maneuver,
                MainWeapon.spla_maneuver,
                SubWeapon.quick_bomb,
                SpecialWeapon.multi_missile,
                Custom.replica,
                True
            ),
            Buki(
                'ケルビン525',
                Category.maneuver,
                MainWeapon.kelbin,
                SubWeapon.trap,
                SpecialWeapon.jetpack
            ),
            Buki(
                'スパッタリー・ヒュー',
                Category.maneuver,
                MainWeapon.spattary,
                SubWeapon.poison_mist,
                SpecialWeapon.rain,
                Custom.hue
            ),
            Buki(
                'クアッドホッパーブラック',
                Category.maneuver,
                MainWeapon.quad_hopper,
                SubWeapon.robot_bomb,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'ケルビン525デコ',
                Category.maneuver,
                MainWeapon.kelbin,
                SubWeapon.splash_shield,
                SpecialWeapon.ika_sphere,
                Custom.deco
            ),
            Buki(
                'クアッドホッパーホワイト',
                Category.maneuver,
                MainWeapon.quad_hopper,
                SubWeapon.sprinkler,
                SpecialWeapon.bomb_pitcher,
                Custom.other
            ),
            Buki(
                'スプラマニューバーベッチュー',
                Category.maneuver,
                MainWeapon.spla_maneuver,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.ika_sphere,
                Custom.betchu
            ),
            Buki(
                'ケルビン525ベッチュー',
                Category.maneuver,
                MainWeapon.kelbin,
                SubWeapon.tansan_bomb,
                SpecialWeapon.ink_armor,
                Custom.betchu
            ),
            Buki(
                'スパッタリークリア',
                Category.maneuver,
                MainWeapon.spattary,
                SubWeapon.t_p_d,
                SpecialWeapon.super_chakuchi,
                Custom.bukiti
            ),
            Buki(
                'スプラスコープ',
                Category.charger,
                MainWeapon.spla_charger,
                SubWeapon.splash_bomb,
                SpecialWeapon.hyper_presser
            ),
            Buki(
                'スクイックリンα',
                Category.charger,
                MainWeapon.sqickrin,
                SubWeapon.point_sensor,
                SpecialWeapon.ink_armor
            ),
            Buki(
                'スプラチャージャー',
                Category.charger,
                MainWeapon.spla_charger,
                SubWeapon.splash_bomb,
                SpecialWeapon.hyper_presser
            ),
            Buki(
                '14式竹筒銃・甲',
                Category.charger,
                MainWeapon.take,
                SubWeapon.curling_bomb,
                SpecialWeapon.multi_missile
            ),
            Buki(
                'ヒーローチャージャーレプリカ',
                Category.charger,
                MainWeapon.spla_charger,
                SubWeapon.splash_bomb,
                SpecialWeapon.hyper_presser,
                Custom.replica,
                True
            ),
            Buki(
                'スクイックリンγ',
                Category.charger,
                MainWeapon.sqickrin,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.jetpack,
                Custom.bukiti
            ),
            Buki(
                '14式竹筒銃・丙',
                Category.charger,
                MainWeapon.take,
                SubWeapon.tansan_bomb,
                SpecialWeapon.bubble_launcher,
                Custom.bukiti
            ),
            Buki(
                'スクイックリンβ',
                Category.charger,
                MainWeapon.sqickrin,
                SubWeapon.robot_bomb,
                SpecialWeapon.ika_sphere,
                Custom.other
            ),
            Buki(
                '14式竹筒銃・乙',
                Category.charger,
                MainWeapon.take,
                SubWeapon.poison_mist,
                SpecialWeapon.bomb_pitcher,
                Custom.other
            ),
            Buki(
                'ソイチューバー',
                Category.charger,
                MainWeapon.soi_tuber,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'スプラチャージャーコラボ',
                Category.charger,
                MainWeapon.spla_charger,
                SubWeapon.splash_shield,
                SpecialWeapon.bomb_pitcher,
                Custom.collabo
            ),
            Buki(
                'スプラスコープコラボ',
                Category.charger,
                MainWeapon.spla_charger,
                SubWeapon.splash_shield,
                SpecialWeapon.bomb_pitcher,
                Custom.collabo
            ),
            Buki(
                'リッター4K',
                Category.charger,
                MainWeapon.litter,
                SubWeapon.trap,
                SpecialWeapon.rain
            ),
            Buki(
                '4Kスコープ',
                Category.charger,
                MainWeapon.litter,
                SubWeapon.trap,
                SpecialWeapon.rain
            ),
            Buki(
                'リッター4Kカスタム',
                Category.charger,
                MainWeapon.litter,
                SubWeapon.jump_beacon,
                SpecialWeapon.bubble_launcher,
                Custom.custom
            ),
            Buki(
                '4Kスコープカスタム',
                Category.charger,
                MainWeapon.litter,
                SubWeapon.jump_beacon,
                SpecialWeapon.bubble_launcher,
                Custom.custom
            ),
            Buki(
                'ソイチューバーカスタム',
                Category.charger,
                MainWeapon.soi_tuber,
                SubWeapon.curling_bomb,
                SpecialWeapon.jetpack,
                Custom.custom
            ),
            Buki(
                'スプラチャージャーベッチュー',
                Category.charger,
                MainWeapon.spla_charger,
                SubWeapon.sprinkler,
                SpecialWeapon.ika_sphere,
                Custom.betchu
            ),
            Buki(
                'スプラスコープベッチュー',
                Category.charger,
                MainWeapon.spla_charger,
                SubWeapon.sprinkler,
                SpecialWeapon.ika_sphere,
                Custom.betchu
            ),
            Buki(
                'ノヴァブラスターネオ',
                Category.blaster,
                MainWeapon.nova_blaster,
                SubWeapon.trap,
                SpecialWeapon.bomb_pitcher,
                Custom.neo
            ),
            Buki(
                'ロングブラスター',
                Category.blaster,
                MainWeapon.long_blaster,
                SubWeapon.curling_bomb,
                SpecialWeapon.bubble_launcher
            ),
            Buki(
                'ホットブラスターカスタム',
                Category.blaster,
                MainWeapon.hot_blaster,
                SubWeapon.robot_bomb,
                SpecialWeapon.jetpack,
                Custom.custom
            ),
            Buki(
                'ノヴァブラスター',
                Category.blaster,
                MainWeapon.nova_blaster,
                SubWeapon.splash_bomb,
                SpecialWeapon.ika_sphere
            ),
            Buki(
                'ラピッドブラスター',
                Category.blaster,
                MainWeapon.rapid_blaster,
                SubWeapon.trap,
                SpecialWeapon.bomb_pitcher
            ),
            Buki(
                'ロングブラスターネクロ',
                Category.blaster,
                MainWeapon.long_blaster,
                SubWeapon.quick_bomb,
                SpecialWeapon.multi_missile,
                Custom.bukiti
            ),
            Buki(
                'ホットブラスター',
                Category.blaster,
                MainWeapon.hot_blaster,
                SubWeapon.poison_mist,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'Rブラスターエリートデコ',
                Category.blaster,
                MainWeapon.rapid_blaster_elite,
                SubWeapon.splash_shield,
                SpecialWeapon.ink_armor,
                Custom.deco
            ),
            Buki(
                'Rブラスターエリート',
                Category.blaster,
                MainWeapon.rapid_blaster_elite,
                SubWeapon.poison_mist,
                SpecialWeapon.rain
            ),
            Buki(
                'ラピッドブラスターデコ',
                Category.blaster,
                MainWeapon.rapid_blaster,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.jetpack,
                Custom.deco
            ),
            Buki(
                'ロングブラスター',
                Category.blaster,
                MainWeapon.long_blaster,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.rain
            ),
            Buki(
                'クラッシュブラスター',
                Category.blaster,
                MainWeapon.clash_blaster,
                SubWeapon.splash_bomb,
                SpecialWeapon.hyper_presser
            ),
            Buki(
                'ヒーローブラスターレプリカ',
                Category.blaster,
                MainWeapon.hot_blaster,
                SubWeapon.poison_mist,
                SpecialWeapon.super_chakuchi,
                Custom.replica,
                True
            ),
            Buki(
                'クラッシュブラスターネオ',
                Category.blaster,
                MainWeapon.clash_blaster,
                SubWeapon.curling_bomb,
                SpecialWeapon.multi_missile,
                Custom.neo
            ),
            Buki(
                'ノヴァブラスターベッチュー',
                Category.blaster,
                MainWeapon.nova_blaster,
                SubWeapon.tansan_bomb,
                SpecialWeapon.rain,
                Custom.betchu
            ),
            Buki(
                'ラピッドブラスターベッチュー',
                Category.blaster,
                MainWeapon.rapid_blaster,
                SubWeapon.t_p_d,
                SpecialWeapon.ika_sphere
            ),
            Buki(
                'ダイナモローラー',
                Category.roller,
                MainWeapon.dinamo_roller,
                SubWeapon.trap,
                SpecialWeapon.hyper_presser
            ),
            Buki(
                'スプラローラーコラボ',
                Category.roller,
                MainWeapon.spla_roller,
                SubWeapon.jump_beacon,
                SpecialWeapon.ika_sphere,
                Custom.collabo
            ),
            Buki(
                'カーボンローラー',
                Category.roller,
                MainWeapon.carbon_roller,
                SubWeapon.robot_bomb,
                SpecialWeapon.rain
            ),
            Buki(
                'ダイナモローラーテスラ',
                Category.roller,
                MainWeapon.dinamo_roller,
                SubWeapon.splash_bomb,
                SpecialWeapon.ink_armor,
                Custom.other
            ),
            Buki(
                'スプラローラー',
                Category.roller,
                MainWeapon.spla_roller,
                SubWeapon.curling_bomb,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'カーボンローラーデコ',
                Category.roller,
                MainWeapon.carbon_roller,
                SubWeapon.quick_bomb,
                SpecialWeapon.bomb_pitcher,
                Custom.deco
            ),
            Buki(
                'ヒーローローラーレプリカ',
                Category.roller,
                MainWeapon.spla_roller,
                SubWeapon.curling_bomb,
                SpecialWeapon.super_chakuchi,
                Custom.replica,
                True
            ),
            Buki(
                'ヴァリアブルローラー',
                Category.roller,
                MainWeapon.variable_roller,
                SubWeapon.splash_shield,
                SpecialWeapon.bomb_pitcher
            ),
            Buki(
                'ヴァリアブルローラーフォイル',
                Category.roller,
                MainWeapon.variable_roller,
                SubWeapon.splash_shield,
                SpecialWeapon.bomb_pitcher,
                Custom.foil
            ),
            Buki(
                'スプラローラーベッチュー',
                Category.roller,
                MainWeapon.spla_roller,
                SubWeapon.splash_bomb,
                SpecialWeapon.bubble_launcher,
                Custom.betchu
            ),
            Buki(
                'ダイナモローラーベッチュー',
                Category.roller,
                MainWeapon.dinamo_roller,
                SubWeapon.sprinkler,
                SpecialWeapon.nice_ball,
                Custom.betchu
            ),
            Buki(
                'ホクサイ',
                Category.fude,
                MainWeapon.hokusai,
                SubWeapon.robot_bomb,
                SpecialWeapon.jetpack
            ),
            Buki(
                'パブロ',
                Category.fude,
                MainWeapon.pablo,
                SubWeapon.splash_bomb,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'ホクサイ・ヒュー',
                Category.fude,
                MainWeapon.hokusai,
                SubWeapon.jump_beacon,
                SpecialWeapon.multi_missile,
                Custom.hue
            ),
            Buki(
                'パーマネント・パブロ',
                Category.fude,
                MainWeapon.pablo,
                SubWeapon.sprinkler,
                SpecialWeapon.ink_armor,
                Custom.bukiti
            ),
            Buki(
                'パブロ・ヒュー',
                Category.fude,
                MainWeapon.pablo,
                SubWeapon.trap,
                SpecialWeapon.ika_sphere,
                Custom.hue
            ),
            Buki(
                'ヒーローブラシレプリカ',
                Category.fude,
                MainWeapon.hokusai,
                SubWeapon.robot_bomb,
                SpecialWeapon.jetpack,
                Custom.replica,
                True
            ),
            Buki(
                'ホクサイベッチュー',
                Category.fude,
                MainWeapon.hokusai,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.ultra_stamp,
                Custom.betchu
            ),
            Buki(
                'バケットスロッシャー',
                Category.slosher,
                MainWeapon.bucket_slosher,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.multi_missile
            ),
            Buki(
                'ヒッセン',
                Category.slosher,
                MainWeapon.hissen,
                SubWeapon.quick_bomb,
                SpecialWeapon.ink_armor
            ),
            Buki(
                'スクリュースロッシャー',
                Category.slosher,
                MainWeapon.screw_slosher,
                SubWeapon.robot_bomb,
                SpecialWeapon.hyper_presser
            ),
            Buki(
                'バケットスロッシャーデコ',
                Category.slosher,
                MainWeapon.bucket_slosher,
                SubWeapon.sprinkler,
                SpecialWeapon.ika_sphere,
                Custom.deco
            ),
            Buki(
                'バケットスロッシャーソーダ',
                Category.slosher,
                MainWeapon.bucket_slosher,
                SubWeapon.splash_bomb,
                SpecialWeapon.bomb_pitcher,
                Custom.bukiti
            ),
            Buki(
                'ヒッセン・ヒュー',
                Category.slosher,
                MainWeapon.hissen,
                SubWeapon.splash_bomb,
                SpecialWeapon.rain,
                Custom.hue
            ),
            Buki(
                'スクリュースロッシャーネオ',
                Category.slosher,
                MainWeapon.screw_slosher,
                SubWeapon.point_sensor,
                SpecialWeapon.bomb_pitcher,
                Custom.neo
            ),
            Buki(
                'ヒーロースロッシャーレプリカ',
                Category.slosher,
                MainWeapon.bucket_slosher,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.multi_missile,
                Custom.replica,
                True
            ),
            Buki(
                'エクスプロッシャー',
                Category.slosher,
                MainWeapon.explorer,
                SubWeapon.sprinkler,
                SpecialWeapon.bubble_launcher
            ),

            Buki(
                'オーバーフロッシャー',
                Category.slosher,
                MainWeapon.over_frosher,
                SubWeapon.splash_shield,
                SpecialWeapon.rain
            ),
            Buki(
                'スクリュースロッシャーベッチュー',
                Category.slosher,
                MainWeapon.screw_slosher,
                SubWeapon.tansan_bomb,
                SpecialWeapon.super_chakuchi,
                Custom.betchu
            ),
            Buki(
                'エクスプロッシャーカスタム',
                Category.slosher,
                MainWeapon.explorer,
                SubWeapon.point_sensor,
                SpecialWeapon.ika_sphere,
                Custom.custom
            ),
            Buki(
                'オーバーフロッシャーデコ',
                Category.slosher,
                MainWeapon.over_frosher,
                SubWeapon.sprinkler,
                SpecialWeapon.bomb_pitcher,
                Custom.deco
            ),
            Buki(
                'スプラスピナーコラボ',
                Category.spinner,
                MainWeapon.spla_spinner,
                SubWeapon.curling_bomb,
                SpecialWeapon.rain,
                Custom.collabo
            ),
            Buki(
                'バレルスピナーデコ',
                Category.spinner,
                MainWeapon.barrel_spinner,
                SubWeapon.splash_shield,
                SpecialWeapon.bubble_launcher,
                Custom.deco
            ),
            Buki(
                'ハイドラントカスタム',
                Category.spinner,
                MainWeapon.hi_drant,
                SubWeapon.trap,
                SpecialWeapon.ink_armor,
                Custom.custom
            ),
            Buki(
                'バレルスピナー',
                Category.spinner,
                MainWeapon.barrel_spinner,
                SubWeapon.sprinkler,
                SpecialWeapon.hyper_presser
            ),
            Buki(
                'バレルスピナーリミックス',
                Category.spinner,
                MainWeapon.barrel_spinner,
                SubWeapon.point_sensor,
                SpecialWeapon.nice_ball,
                Custom.bukiti
            ),
            Buki(
                'ハイドラント',
                Category.spinner,
                MainWeapon.hi_drant,
                SubWeapon.robot_bomb,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'スプラスピナー',
                Category.spinner,
                MainWeapon.spla_spinner,
                SubWeapon.quick_bomb,
                SpecialWeapon.multi_missile
            ),
            Buki(
                'ヒーロースピナーレプリカ',
                Category.spinner,
                MainWeapon.barrel_spinner,
                SubWeapon.sprinkler,
                SpecialWeapon.hyper_presser,
                Custom.replica,
                True
            ),
            Buki(
                'クーゲルシュライバー',
                Category.spinner,
                MainWeapon.kugel_shuliver,
                SubWeapon.poison_mist,
                SpecialWeapon.jetpack
            ),
            Buki(
                'ノーチラス47',
                Category.spinner,
                MainWeapon.nautilus,
                SubWeapon.point_sensor,
                SpecialWeapon.ika_sphere
            ),
            Buki(
                'クーゲルシュライバー・ヒュー',
                Category.spinner,
                MainWeapon.kugel_shuliver,
                SubWeapon.jump_beacon,
                SpecialWeapon.rain,
                Custom.hue
            ),
            Buki(
                'ノーチラス79',
                Category.spinner,
                MainWeapon.nautilus,
                SubWeapon.q_ban_bomb,
                SpecialWeapon.jetpack,
                Custom.bukiti
            ),
            Buki(
                'スプラスピナーベッチュー',
                Category.spinner,
                MainWeapon.spla_spinner,
                SubWeapon.poison_mist,
                SpecialWeapon.ultra_stamp,
                Custom.betchu
            ),
            Buki(
                'パラシェルター',
                Category.shelter,
                MainWeapon.parashelter,
                SubWeapon.sprinkler,
                SpecialWeapon.rain
            ),
            Buki(
                'ヒーローシェルターレプリカ',
                Category.shelter,
                MainWeapon.parashelter,
                SubWeapon.sprinkler,
                SpecialWeapon.rain,
                Custom.replica,
                True
            ),
            Buki(
                'キャンピングシェルター',
                Category.shelter,
                MainWeapon.camping_shelter,
                SubWeapon.jump_beacon,
                SpecialWeapon.bubble_launcher
            ),
            Buki(
                'スパイガジェット',
                Category.shelter,
                MainWeapon.spy_gadget,
                SubWeapon.trap,
                SpecialWeapon.super_chakuchi
            ),
            Buki(
                'パラシェルターソレーラ',
                Category.shelter,
                MainWeapon.parashelter,
                SubWeapon.robot_bomb,
                SpecialWeapon.bomb_pitcher,
                Custom.solera
            ),
            Buki(
                'スパイガジェットソレーラ',
                Category.shelter,
                MainWeapon.spy_gadget,
                SubWeapon.splash_bomb,
                SpecialWeapon.ika_sphere,
                Custom.solera
            ),
            Buki(
                'キャンピングシェルターソレーラ',
                Category.shelter,
                MainWeapon.camping_shelter,
                SubWeapon.splash_bomb,
                SpecialWeapon.ika_sphere,
                Custom.solera
            ),
            Buki(
                'スパイガジェットベッチュー',
                Category.shelter,
                MainWeapon.spy_gadget,
                SubWeapon.t_p_d,
                SpecialWeapon.ink_armor,
                Custom.betchu
            ),
            Buki(
                'キャンピングシェルターカーモ',
                Category.shelter,
                MainWeapon.camping_shelter,
                SubWeapon.trap,
                SpecialWeapon.ultra_stamp,
                Custom.bukiti
            )]

    @classmethod
    def get(cls,
            categories: List[Category],
            subs: List[SubWeapon],
            specials: List[SpecialWeapon],
            customs: List[Custom],
            replica: bool = False):

        filtered_weapons = []
        for weapon in cls.weapons():
            if (len(categories) <= 0 or weapon.category in categories) and \
                    (len(subs) <= 0 or weapon.sub_weapon in subs) and \
                    (len(specials) <= 0 or weapon.special_weapon in specials) and \
                    (len(customs) <= 0 or weapon.custom in customs) and \
                    (not weapon.replica or replica):
                filtered_weapons.append(weapon)

        return filtered_weapons
