from django.apps import AppConfig


class ToolsConfig(AppConfig):
    name = 'tools'

RACE_ICONS = {
    'Human': 'UI/Glues/Loading/Backgrounds/Campaigns/HumanSymbol.blp',
    'Orc': 'UI/Glues/Loading/Backgrounds/Campaigns/OrcSymbol.blp',
    'NightElf': 'UI/Glues/Loading/Backgrounds/Campaigns/NightElfSymbol.blp',
    'Undead': 'UI/Glues/Loading/Backgrounds/Campaigns/UndeadSymbol.blp',
}

REPLACEABLE_ICONS_DIR = 'ReplaceableTextures/CommandButtons'

UNITS_MAPPING = {
    'AbominationCIN': {
        'ignore': True,
        'categorization': ('campaign'),
        'replaceable_icon': 'Abomination',
    },
    'AncestralGuardian': {
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'Arthas': {
        'categorization': ('campaign', 'heroic'),
    },
    'ArthaswithSword': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'Arthas',
    },
    'AzureDragonWelp': {
        'replaceable_icon': 'AzureDragon',
    },
    'BansheeGhost': {
        'replaceable_icon': 'Ghost',
    },
    'BlackDragonWelp': {
        'replaceable_icon': 'BlackDragon',
    },
    'BlackStagMale': {
        'replaceable_icon': 'Stag',
    },
    'BristleBack': {
        'replaceable_icon': 'Razorback',
    },
    'BronzeDragonWelp': {
        'replaceable_icon': 'BronzeDragon',
    },
    'BrownWolf': {
        'replaceable_icon': 'DireWolf',
    },
    'BurningArcher': {
        'replaceable_icon': 'SkeletonArcher',
    },
    'Cairne': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroTaurenChieftain',
    },
    'ChaosGrunt': {
        'categorization': ('campaign'),
    },
    'ChaosHellscream': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'ChaosGrom',
    },
    'ChaosKotoBeast': {
        'categorization': ('campaign'),
    },
    'ChaosOrcRange': {
        'ignore': True,
        'categorization': ('campaign'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'ChaosPeon': {
        'categorization': ('campaign'),
    },
    'ChaosSpaceOrc': {
        'categorization': ('campaign'),
    },
    'ChaosWarlock': {
        'categorization': ('campaign'),
    },
    'ChaosWarlockGreen': {
        'categorization': ('campaign'),
    },
    'ChaosWarlord': {
        'categorization': ('campaign'),
    },
    'ChaosWolfrider': {
        'categorization': ('campaign'),
        'replaceable_icon': 'ChaosWolfRider',
    },
    'DoomGuard': {
        'categorization': ('campaign'),
    },
    'ElfVillagerWoman': {
        'categorization': ('campaign'),
        'replaceable_icon': 'FemaleElfVillager',
    },
    'Ent': {
        'categorization': ('special'),
    },
    'EvilArthas': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroDeathKnight',
    },
    'felhound': {
        'categorization': ('campaign'),
    },
    'FlyingSheep': {
        'categorization': ('campaign', 'special'),
    },
    'Furion': {
        'categorization': ('campaign', 'heroic'),
    },
    'FlyingSheep': {
        'replaceable_icon': 'Sheep',
    },
    'ForestTrollTrapper': {
        'replaceable_icon': 'ForestTrollTrapper',
    },
    'felhound': {
        'replaceable_icon': 'FelHound',
    },
    'GnollOverSeer': {
        'replaceable_icon': 'GnollKing',
    },
    'GoblinLandMine': {
        'categorization': ('special'),
    },
    'GolemStatue': {
        'replaceable_icon': 'ArmorGolem',
    },
    'GreenDragonWelp': {
        'replaceable_icon': 'GreenDragon',
    },
    'GyroCopter': {
        'replaceable_icon': 'Gyrocopter',
    },
    'HeadHunter': {
        'replaceable_icon': 'Headhunter',
    },
    'HealingWard': {
        'categorization': ('special'),
    },
    'Hellscream': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HellScream',
    },
    'HeroArchMage': {
        'categorization': ('heroic'),
    },
    'HeroBladeMaster': {
        'categorization': ('heroic'),
        'replaceable_icon': 'HeroBlademaster',
    },
    'HeroChaosBladeMaster': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'ChaosBlademaster',
    },
    'HeroDeathKnight': {
        'categorization': ('heroic'),
    },
    'HeroDemonHunter': {
        'categorization': ('heroic'),
    },
    'HeroDreadLord': {
        'categorization': ('heroic'),
    },
    'HeroFarseer': {
        'categorization': ('heroic'),
    },
    'HeroKeeperOfTheGrove': {
        'categorization': ('heroic'),
        'replaceable_icon': 'KeeperOfTheGrove',
    },
    'HeroKeeperoftheGroveGhost': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'KeeperGhostBlue',
    },
    'HeroLich': {
        'categorization': ('heroic'),
    },
    'HeroLichCIN': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'LichVersion2',
    },
    'HeroMoonPriestess': {
        'categorization': ('heroic'),
    },
    'HeroMountainKing': {
        'categorization': ('heroic'),
    },
    'HeroPaladin': {
        'categorization': ('heroic'),
    },
    'HeroPaladinBoss': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroPaladin',
    },
    'HeroPaladinBoss2': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroPaladin',
    },
    'HeroTaurenChieftain': {
        'categorization': ('heroic'),
    },
    'HeroTaurenChieftainCIN': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroTaurenChieftain',
    },
    'HighElfArcher': {
        'replaceable_icon': 'HighElvenArcher',
    },
    'HighElfPeasant': {
        'categorization': ('campaign'),
        'replaceable_icon': 'ElfVillager',
    },
    'HippoGryph': {
        'replaceable_icon': 'Hippogriff',
    },
    'HumanMage': {
        'replaceable_icon': 'BanditMage',
    },
    'Hydralisk': {
        'categorization': ('campaign'),
    },
    'IronGolem': {
        'replaceable_icon': 'ArmorGolem',
    },
    'Illidan': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroDemonHunter',
    },
    'Infernal': {
        'categorization': ('campaign'),
    },
    'Jaina': {
        'categorization': ('campaign', 'heroic'),
    },
    'Kelthuzad': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'KelThuzad',
    },
    'KelthuzadGhost': {
        'ignore': True,
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'GhostOfKelThuzad',
    },
    'KelThuzadLich': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'KelThuzad',
    },
    'KelThuzadNecro': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'GhostOfKelThuzad',
    },
    'KnightNoRider': {
        'categorization': ('campaign', 'special'),
        'replaceable_icon': 'RiderlessHorse',
    },
    'KotoBeastNoRider': {
        'categorization': ('campaign'),
        'replaceable_icon': 'RiderlessKodo',
    },
    'Mannoroth': {
        'categorization': ('campaign', 'heroic'),
    },
    'Marine': {
        'categorization': ('campaign'),
    },
    'Meatwagon': {
        'replaceable_icon': 'MeatWagon',
    },
    'Medivh': {
        'categorization': ('campaign', 'heroic'),
    },
    'Militia': {
        'categorization': ('special'),
    },
    'Muradin': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroMountainKing',
    },
    'MurlocWarrior': {
        'replaceable_icon': 'Murloc',
    },
    'NerubianSpiderLord': {
        'replaceable_icon': 'nerubianSpiderLord',
    },
    'OrcJuggernaught': {
        'categorization': ('campaign'),
        'replaceable_icon': 'Juggernaut',
    },
    'Owlbear': {
        'replaceable_icon': 'OwlBear',
    },
    'Owl': {
        'categorization': ('special'),
        'replaceable_icon': 'OwlBear',
    },
    'OwlSCOUT': {
        'categorization': ('special'),
        'replaceable_icon': 'Scout',
    },
    'Pitlord': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'PitLord',
    },
    'PlagueCloud': {
        'categorization': ('special'),
    },
    'Rat': {
        'replaceable_icon': 'YouDirtyRat!',
    },
    'RazorMane': {
        'replaceable_icon': 'Razorback',
    },
    'RazorManeChief': {
        'replaceable_icon': 'RazormaneChief',
    },
    'RedDragonWelp': {
        'replaceable_icon': 'RedDragon',
    },
    'RiddenHippoGryph': {
        'categorization': ('special'),
        'replaceable_icon': 'HippogriffRider',
    },
    'RiderlessWyvern': {
        'categorization': ('campaign'),
        'replaceable_icon': 'Wyvern',
    },
    'SammyCube': {
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'satyrhellcaller': {
        'replaceable_icon': 'SatyrTrickster',
    },
    'SentryWard': {
        'categorization': ('special'),
    },
    'Shandris': {
        'categorization': ('campaign', 'heroic'),
    },
    'Shoveler': {
        'categorization': ('special'),
    },
    'Skeleton': {
        'categorization': ('special'),
        'replaceable_icon': 'SkeletonWarrior',
    },
    'SludgeMonster': {
        'replaceable_icon': 'SludgeCreature',
    },
    'SpiritPig': {
        'categorization': ('special'),
        'replaceable_icon': 'Pig',
    },
    'Spiritwolf': {
        'categorization': ('special'),
        'replaceable_icon': 'SpiritWolf',
    },
    'StasisTotem': {
        'categorization': ('special'),
        'replaceable_icon': 'StasisTrap',
    },
    'SylvanusWindrunner': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'SylvanusWindRunner',
    },
    'TempArt': {
        'ignore': True,
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'TheCaptain': {
        'categorization': ('campaign'),
    },
    'Thrall': {
        'categorization': ('heroic'),
    },
    'Tichondrius': {
        'categorization': ('campaign', 'heroic'),
    },
    'Tyrande': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroMoonPriestess',
    },
    'Uther': {
        'categorization': ('campaign', 'heroic'),
        'replaceable_icon': 'HeroPaladin',
    },
    'VillagerKid': {
        'categorization': ('campaign'),
    },
    'VillagerKid1': {
        'categorization': ('campaign'),
        'replaceable_icon': 'VillagerKid2',
    },
    'VillagerMan': {
        'categorization': ('campaign'),
    },
    'VillagerMan1': {
        'categorization': ('campaign'),
    },
    'VillagerWoman': {
        'categorization': ('campaign'),
    },
    'Warlock': {
        'categorization': ('campaign'),
    },
    'WarWagon': {
        'categorization': ('campaign', 'special'),
    },
    'Warlock': {
        'replaceable_icon': 'OrcWarlockRed',
    },
    'WarWagon': {
        'replaceable_icon': 'SeigeEngine',
    },
    'Watcher': {
        'replaceable_icon': 'AvengingWatcher',
    },
    'WaterElemental': {
        'categorization': ('special'),
        'replaceable_icon': 'SummonWaterElemental',
    },
    'WendigoShaman': {
        'replaceable_icon': 'Wendigo',
    },
    'WhiteWolf': {
        'replaceable_icon': 'TimberWolf',
    },
    'WindSerpent': {
        'categorization': ('special'),
        'replaceable_icon': 'SelectHeroOn',
    },
    'Wolfrider': {
        'replaceable_icon': 'Raider',
    },
    'zergling': {  # Zergling ?
        'categorization': ('campaign'),
        'replaceable_icon': 'Zergling',
    },
}
