@tool
class_name Agent extends CharacterBody2D

enum States {WORK, CHASE, COMEBACK, LEAVE, COLLECT}

@export var sprite_texture : Texture2D:
	set(value):
		sprite_texture = value
		if not (is_inside_tree() and is_instance_valid(value)):
			return
		sprite.texture = value

@onready var env = get_parent()
@onready var sprite : Sprite2D = $Sprite2D
@onready var shape : CollisionShape2D = $CollisionShape2D

var initial_position : Vector2i
var state : States
var speed : float 


func _ready() -> void:
	sprite_texture = sprite_texture
	print(name)
	print("-", sprite, "-")
	#sprite.texture = sprite_texture


func _process(delta: float) -> void:
	#sprite.texture = sprite_texture
	pass
	## Using move_and_collide.
	#var collision = agent.move_and_collide(agent.velocity * delta)
	#if collision:
		#print("I collided with ", collision.get_collider().name)
#
	## Using move_and_slide.
	#agent.move_and_slide()
	#for i in agent.get_slide_collision_count():
		#collision = agent.get_slide_collision(i)
		#print("I collided with ", collision.get_collider().name)

#func move_towards( _position: Vector2 ) -> void:
	#var direction = (_position - position).normalized()
	#position += direction * speed
	

func see() -> void:
	pass

func action() -> void:
	pass
