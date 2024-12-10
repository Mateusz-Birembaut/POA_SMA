class_name Agent extends Node

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
@onready var agent : CharacterBody2D = %Agent
@onready var mini_agent : CharacterBody2D = $mini_agent

var initial_position : Vector2
var state : States
var speed : float
const ACCEL : float = 2.0


func _ready() -> void:
	sprite_texture = sprite_texture
	state = States.WORK
	if initial_position:
		agent.position = initial_position
		mini_agent.position = initial_position
	else:
		initial_position = agent.position


func _physics_process(delta):
	agent.velocity *= speed * delta
	if agent.move_and_slide():
		mini_agent.position = agent.position
	else:
		mini_agent.velocity *= speed * delta
		mini_agent.move_and_slide()


func look_towards(p_position: Vector2 ) -> void:
	agent.velocity = (p_position - agent.position).normalized()
	mini_agent.velocity = (p_position - mini_agent.position).normalized()


func see() -> void:
	pass


func action() -> void:
	pass
