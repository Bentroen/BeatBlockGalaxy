execute as @e[type=armor_stand,tag=block5] run data modify entity @s HandItems[0].tag.CustomModelData set value 0
execute as @e[type=armor_stand,tag=block2] run data modify entity @s HandItems[0].tag.CustomModelData set value 2

execute as @e[type=armor_stand,tag=block5] at @s run fill ~ ~ ~ ~1 ~-1 ~1 air
execute as @e[type=armor_stand,tag=block2] at @s run fill ~ ~ ~ ~1 ~-1 ~1 barrier
