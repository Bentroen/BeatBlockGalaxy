say SWITCH

scoreboard players add state main 2
execute if score state main matches 4.. run scoreboard players set state main 0

execute if score state main matches 0 run function beatblock:states/green_active
execute if score state main matches 1 run function beatblock:states/green_flashing
execute if score state main matches 2 run function beatblock:states/yellow_active
execute if score state main matches 3 run function beatblock:states/yellow_flashing
