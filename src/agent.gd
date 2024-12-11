class_name Agent extends CharacterBody2D

enum States {WORK, CHASE, COMEBACK, LEAVE, COLLECT, READY}

@export var sprite_texture : Texture2D:
	set(value):
		sprite_texture = value
		if not (is_inside_tree() and is_instance_valid(value)):
			return
		sprite.texture = value

@onready var env = get_parent()
@onready var sprite : Sprite2D = %Sprite2D
@onready var nav : NavigationAgent2D = %NavigationAgent2D

var initial_position : Vector2
var state : States
var speed : float
const ACCEL : float = 2.0


func _ready() -> void:
	sprite_texture = sprite_texture
	state = States.WORK
	if initial_position:
		position = initial_position
	else:
		initial_position = position


func _physics_process(delta):
	velocity *= speed * delta
	if velocity.length() > 0:
		var angle = velocity.angle() - PI/2
		sprite.set_rotation(angle)
	else:
		sprite.set_rotation(0)
	move_and_slide()


func look_towards(p_position: Vector2 ) -> void:
	velocity = (p_position - position).normalized()
