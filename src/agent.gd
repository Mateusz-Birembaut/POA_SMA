class_name Agent extends CharacterBody2D

enum States {WORK, CHASE, COMEBACK, LEAVE, COLLECT, READY}

@export var sprite_texture : Texture2D:
	set(value):
		sprite_texture = value
		if not (is_inside_tree() and is_instance_valid(value)):
			return
		sprite.texture = value

@onready var env = get_parent()
@onready var sprite : Sprite2D = $Sprite2D
@onready var shape : CollisionShape2D = $CollisionShape2D
@onready var nav : NavigationAgent2D = $NavigationAgent2D

var initial_position : Vector2
var state : States
var speed : float
const ACCEL : float = 2.0


func _ready() -> void:
	sprite_texture = sprite_texture
	initial_position = position
	state = States.WORK


func _physics_process(delta):
	velocity *= speed * delta
	#move_and_collide(velocity)
	move_and_slide()


func look_towards(p_position: Vector2 ) -> void:
	velocity = (p_position - position).normalized()


func see() -> void:
	pass


func action() -> void:
	pass
