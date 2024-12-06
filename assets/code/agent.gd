class_name Agent extends CharacterBody2D

enum States {WORK, CHASE, COMEBACK, LEAVE, COLLECT}

@onready var env = get_parent()
var initial_position : Vector2i
var state : States
var speed : float 


func _ready() -> void:
	pass


func _process(delta: float) -> void:
	pass

func move_towards( _position: Vector2 , delta: float) -> void:
	var direction = (_position - position).normalized()
	var velocity = direction * speed
	
	var collision = move_and_collide(velocity * delta)
	if collision:
		velocity = velocity.slide(collision.get_normal())
	

	

func see() -> void:
	pass

func action() -> void:
	pass
