from typing import Union, Callable, Optional, TYPE_CHECKING
if TYPE_CHECKING:
    from soulstruct.emevd.game_types import *


# TYPING HINTS

CharacterInt = Union[Character, int]
FlagInt = FlagInt
HitboxInt = Union[Hitbox, int]
MapEntityInt = Union[MapEntity, int]
ObjectInt = Union[Object, int]
RegionInt = Union[Region, int]
TextInt = Union[Text, int]


# Restart decorators.
def NeverRestart(func: Callable): ...
def RestartOnRest(func: Callable): ...
def UnknownRestart(func: Callable): ...


# Dummy enum for accessing event flags defined by events.
class EVENTS(Flag): ...
# Dummy class for creating conditions.
class Condition(object):
    def __init__(self, condition: bool, hold=False): ...


# Terminators.
END = ...
RESTART = ...


# The Await function. Equivalent to using the 'await' built-in Python keyword.
def Await(condition): ...


# Boolean constants.
THIS_FLAG = ...
THIS_SLOT_FLAG = ...
ONLINE = ...
OFFLINE = ...
DLC_OWNED = ...
SKULL_LANTERN_ACTIVE = ...

# Compare these constants to numeric values.
WHITE_WORLD_TENDENCY = ...
BLACK_WORLD_TENDENCY = ...
NEW_GAME_CYCLE = ...
SOUL_LEVEL = ...

def FlagEnabled(flag: FlagInt): ...
def FlagDisabled(flag: FlagInt): ...

def SecondsElapsed(elapsed_seconds): ...
def FramesElapsed(elapsed_frames): ...

def EntityInsideRegion(entity: MapEntityInt, region: RegionInt): ...
def EntityOutsideRegion(entity: MapEntityInt, region: RegionInt): ...
def PlayerInsideRegion(region: RegionInt): ...
def PlayerOutsideRegion(region: RegionInt): ...
def AllPlayersInsideRegion(region: RegionInt): ...
def AllPlayersOutsideRegion(region: RegionInt): ...

def InsideMap(game_map: Map): ...
def OutsideMap(game_map: Map): ...

def EntityWithinDistance(first_entity: MapEntityInt, second_entity: MapEntityInt, max_distance): ...
def EntityBeyondDistance(first_entity: MapEntityInt, second_entity: MapEntityInt, min_distance): ...
def PlayerWithinDistance(entity: MapEntityInt, max_distance): ...
def PlayerBeyondDistance(entity: MapEntityInt, min_distance): ...

# These do NOT include the Bottomless Box.
def HasItem(item: ItemInt): ...  # Can be used with any subclass of Item.
def HasWeapon(weapon: WeaponInt): ...
def HasArmor(armor: ArmorInt): ...
def HasRing(ring: RingInt): ...
def HasGood(good: GoodInt): ...

# These include the Bottomless Box. (Not sure if that include general storage in other games.)
def OwnsItem(item: ItemInt): ...  # Can be used with any subclass of Item.
def OwnsWeapon(weapon: WeaponInt): ...
def OwnsArmor(armor: ArmorInt): ...
def OwnsRing(ring: RingInt): ...
def OwnsGood(good: GoodInt): ...

# This test creates a dialog prompt, and returns True when the prompt is activated (with A).
# Should only be used with Await().
def DialogPromptActivated(prompt_text: TextInt, anchor_entity: MapEntityInt, facing_angle: float=None,
                          max_distance: float = None, model_point: int=None, human_or_hollow_only=True, button=0,
                          anchor_type=None, boss_version=False, line_intersects: Optional[MapEntityInt] = None): ...

def MultiplayerEvent(multiplayer_event): ...

def EventFlagValue(left_start_flag, left_bit_count, right_start_flag, right_bit_count): ...  # Compare two flags.

def AnyItemDroppedInRegion(region: RegionInt): ...
def ItemDropped(item: Item): ...

def IsAlive(character: CharacterInt): ...
def IsDead(character: CharacterInt): ...

def IsAttacked(attacked_entity: Union[Object, CharacterInt], attacking_character: CharacterInt): ...

# The values returned by these should be compared with a number literal.
def TrueFlagCount(flag_range) -> int: ...
def EventValue(start_flag, bit_count) -> int: ...  # Use this to compare an event value to an arbitrary integer.
def HealthRatio(character: CharacterInt) -> float: ...
def HealthValue(character: CharacterInt) -> int: ...
def PartHealthValue(character: CharacterInt, part_type) -> int: ...

# Character tests.
def IsCharacterType(character: CharacterInt, character_type: CharacterType): ...
def IsHollow(character: CharacterInt): ...
def IsHuman(character: CharacterInt): ...
def IsInvader(character: CharacterInt): ...
def IsBlackPhantom(character: CharacterInt): ...
def IsWhitePhantom(character: CharacterInt): ...

def PlayerIsClass(class_type: ClassType): ...
def PlayerInCovenant(covenant_type: Covenant): ...

def IsTargeting(targeting_chr: CharacterInt, targeted_chr: CharacterInt): ...
def HasAiStatus(character: CharacterInt, ai_status): ...
def AiStatusIsNormal(character: CharacterInt): ...
def AiStatusIsRecognition(character: CharacterInt): ...
def AiStatusIsAlert(character: CharacterInt): ...
def AiStatusIsBattle(character: CharacterInt): ...

def HasTaeEvent(character: CharacterInt, tae_event_id): ...
def HasSpecialEffect(character: CharacterInt, special_effect): ...

def BackreadEnabled(character: CharacterInt): ...
def BackreadDisabled(character: CharacterInt): ...

# Objects
def IsDestroyed(obj: ObjectInt): ...
def IsActivated(obj: ObjectInt): ...

# Hitboxes
def PlayerStandingOnHitbox(hitbox: HitboxInt): ...
def PlayerMovingOnHitbox(hitbox: HitboxInt): ...
def PlayerRunningOnHitbox(hitbox: HitboxInt): ...
