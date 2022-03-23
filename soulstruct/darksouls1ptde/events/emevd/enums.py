__all__ = [
    # Basic enums/types
    "RestartType",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
    "CLIENT_PLAYER_1",
    "CLIENT_PLAYER_2",
    "CLIENT_PLAYER_3",
    "CLIENT_PLAYER_4",
    "CLIENT_PLAYER_5",
    "PlayerEntity",
    # Enums identical in all games
    "AIStatusType",
    "BitOperation",
    "ButtonType",
    "CharacterType",
    "CharacterUpdateRate",
    "ClassType",
    "ComparisonType",
    "ChangeType",
    "CutsceneType",
    "DamageTargetType",
    "EventReturnType",
    "FlagState",
    "FlagType",
    "InterpolationState",
    "ItemType",
    "RangeState",
    "CoordEntityType",
    "NavmeshType",
    "NumberButtons",
    "OnOffChange",
    "RestartType",
    "SoundType",
    "StatueType",
    "SummonSignType",
    "TriggerAttribute",
    "WorldTendencyType",
    "UpdateAuthority",
    # Enums in Dark Souls 1 (both PTD and DSR) only
    "CalculationType",
    "ConditionGroup",
    "Covenant",
    "TeamType",
    "BannerType",
    "MultiplayerState",
    "NPCPartType",
    "PlayerStats"
]

from enum import IntEnum

from soulstruct.base.events.emevd.enums import *


class CalculationType(IntEnum):
    Add = 0
    Subtract = 1
    Multiply = 2
    Divide = 3
    Modulus = 4


class ConditionGroup(IntEnum):
    OR_7 = -7
    OR_6 = -6
    OR_5 = -5
    OR_4 = -4
    OR_3 = -3
    OR_2 = -2
    OR_1 = -1
    MAIN = 0
    AND_1 = 1
    AND_2 = 2
    AND_3 = 3
    AND_4 = 4
    AND_5 = 5
    AND_6 = 6
    AND_7 = 7


class Covenant(IntEnum):
    NoCovenant = 0
    WayOfWhite = 1
    PrincessGuard = 2
    WarriorOfSunlight = 3
    Darkwraith = 4
    PathOfTheDragon = 5
    GravelordServant = 6
    ForestHunter = 7
    DarkmoonBlade = 8
    ChaosServant = 9


class TeamType(IntEnum):
    Default = -1
    NoTeam = 0
    Human = 1
    WhitePhantom = 2
    BlackPhantom = 3
    Hollow = 4
    Vagrant = 5
    Enemy = 6
    Boss = 7
    Ally = 8  # Targets no one, targeted by Enemy/Boss. (Not sure about HostileAlly.)
    HostileAlly = 9  # Targets and targeted by everyone.
    Decoy = 10
    RedChild = 11  # Seems identical to Enemy.
    FightingAlly = 12  # Targets Enemy/Boss, targeted by Enemy/Boss.
    Intruder = 13  # Targets and targeted by Human/WhitePhantom/Hollow
    Neutral = 14
    Charm = 15  # Seems to target and hurt everyone, but can't be locked onto, and keeps attacking dead (Charm) enemies.


class BannerType(IntEnum):
    VictoryAchieved = 1
    YouDied = 2
    HumanityRestored = 3
    SoulsRetrieved = 4
    TargetDestroyed = 5
    YouDiedPhantom = 6  # Phantom version of "YOU DIED"
    BlackPhantomDestroyed = 7
    AreaName = 8  # Name determined by current floor collision.
    MagicRevival = 9
    RingRevival = 10
    RareRingRevival = 11
    Congratulations = 12  # Bugged texture.
    BonfireLit = 13
    YouWin = 15
    YouLose = 16
    Draw = 17
    BeginMatch = 18  # REMASTERED ONLY.


class MultiplayerState(IntEnum):
    Host = 0
    Client = 1
    Multiplayer = 2
    Singleplayer = 3
    UnknownPlayerType4 = 4  # REMASTERED ONLY.
    UnknownPlayerType5 = 5  # REMASTERED ONLY.


class NPCPartType(IntEnum):
    """Used in definining different behavior for parts of NPC models, e.g. tails that can be cut or Smough's invincible
    hammer."""
    Part1 = 1
    Part2 = 2
    Part3 = 3
    Part4 = 4
    Part5 = 5
    Part6 = 6
    WeakPoint = 7
    Part7 = 8
    Part8 = 9


class PlayerStats(IntEnum):
    """ used to reference player statss """
    Vitality = 0
    Attunement = 1
    Endurance = 2
    Strength = 3
    Dexterity = 4
    Intelligence = 5
    Faith = 6
    # TODO: Resistance or Luck = 7 ?
    Soul = 8
    TotalGetSoul = 9 # TODO: soul memory?
    Humanity = 10
    Covenant = 11
    Gender = 12 # TODO: which is which?
    BossKillAssists = 13
    """ number of hosts assisted through multiplayer, used to offset faith req of sunbro covenant"""
    ForestInvadersKilled = 14
    """ number of hosts killed through forest hunter covenant invasions """
    CurrentCovenantPoints = 15
    """ how many respective covenant items have been offered\n
    a soft betrayal (leaving a covenant amicably) causes this number to be halved (rounded down)\n
    a hard betrayal (getting kicked out) causes this number to be reset to 0 """
    CurrentCovenantLevel = 16
    """ the covenant level that corresponds to the respective CovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    WarriorOfSunlightCovenantPoints = 17
    """ how many sunlight medals have been offered to the Sunlight Altar """
    DarkwraithCovenantPoints = 18
    """ how many humanity have been offered to Kaathe """
    PathOfTheDragonCovenantPoints = 19
    """ how many dragon scales have been offered to the Stone Dragon """
    GravelordServantCovenantPoints = 20
    """ how many eyes of death have been offered to Nito """
    ForestHunterCovenantPoints = 21
    """ how many forest intruders have been defeated """
    DarkmoonBladeCovenantPoints = 22
    """ how many souvenirs of reprisal have been offered to Gwyndolin"""
    ChaosServantCovenantPoints = 23
    """ how many humanity have been offered to the Fair Lady"""
    WarriorOfSunlightCovenantLevel = 24
    """ the covenant level that corresponds to WarriorOfSunlightCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    DarkwraithCovenantLevel = 25
    """ the covenant level that corresponds to DarkwraithCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    PathOfTheDragonCovenantLevel = 26
    """ the covenant level that corresponds to PathOfTheDragonCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    GravelordServantCovenantLevel = 27
    """ the covenant level that corresponds to GravelordServantCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    ForestHunterCovenantLevel = 28
    """ the covenant level that corresponds to ForestHunterCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    DarkmoonBladeCovenantLevel = 29
    """ the covenant level that corresponds to DarkmoonBladeCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    ChaosServantCovenantLevel = 30
    """ the covenant level that corresponds to ChaosServantCovenantPoints:\n
        0-9:    Level 0
        10-29:  Level 1
        30-79:  Level 2
        80+:    Level 3
    """
    ReturnResultofHardcodedEventFlag = 31
