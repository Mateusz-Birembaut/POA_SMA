class_name Agent extends Area2D

enum {WORK, CHASE, COMEBACK, LEAVE}

@onready var env = get_parent()

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
