class_name Agent extends Area2D

enum States {WORK, CHASE, COMEBACK, LEAVE, COLLECT}

@onready var env = get_parent()
var initial_position : Vector2i
var state : States
var speed : float 


func _ready() -> void:
	pass


func _process(delta: float) -> void:
	pass

func move_towards( _position ) -> void:
	# direction = _position - position . normalize
	# position = position + direction * speed
	pass

func see() -> void:
	pass

func action() -> void:
	pass
